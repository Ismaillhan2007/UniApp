from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import University, Faculty, Program
from .serializers import (
    UniversityListSerializer,
    UniversityDetailSerializer,
    ProgramSerializer,
    FacultySerializer,
    UniversityCompareSerializer,
)

# ============ UNIVERSITIES ============

@api_view(['GET'])
def university_list(request):
    """Get all universities"""
    universities = University.objects.all().order_by('ranking')
    serializer = UniversityListSerializer(universities, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def university_detail(request, pk):
    """Get single university with faculties and programs"""
    try:
        university = University.objects.get(pk=pk)
        serializer = UniversityDetailSerializer(university)
        return Response(serializer.data)
    except University.DoesNotExist:
        return Response({'error': 'University not found'}, status=status.HTTP_404_NOT_FOUND)


# ============ FACULTIES ============

@api_view(['GET'])
def faculty_list(request, uni_id):
    """Get all faculties of a university"""
    faculties = Faculty.objects.filter(university_id=uni_id)
    serializer = FacultySerializer(faculties, many=True)
    return Response(serializer.data)


# ============ PROGRAMS ============

@api_view(['GET'])
def program_list(request):
    """
    Get all programs
    Filter by: ?university=1 or ?degree=bachelor or ?language=EN
    """
    programs = Program.objects.all()
    
    uni_id = request.GET.get('university')
    degree = request.GET.get('degree')
    language = request.GET.get('language')
    
    if uni_id:
        programs = programs.filter(university_id=uni_id)
    if degree:
        programs = programs.filter(degree=degree)
    if language:
        programs = programs.filter(language__icontains=language)
    
    serializer = ProgramSerializer(programs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def university_programs(request, uni_id):
    """Get all programs of a university"""
    programs = Program.objects.filter(university_id=uni_id)
    serializer = ProgramSerializer(programs, many=True)
    return Response(serializer.data)


# ============ SEARCH ============

@api_view(['GET'])
def search(request):
    """Search universities and programs"""
    query = request.GET.get('q', '')
    
    if not query:
        return Response({'universities': [], 'programs': []})
    
    universities = University.objects.filter(name__icontains=query)
    programs = Program.objects.filter(name__icontains=query)
    
    return Response({
        'universities': UniversityListSerializer(universities, many=True).data,
        'programs': ProgramSerializer(programs, many=True).data
    })


# ============ COMPARE ============

@api_view(['GET', 'POST'])
def compare(request):
    # --- 1. IDs вузов ---
    if request.method == 'GET':
        ids_param = request.GET.get('ids', '')
        ids = [int(x) for x in ids_param.split(',') if x.strip().isdigit()]
        degree = request.GET.get('degree')
        language = request.GET.get('language')
    else:  # POST
        ids = request.data.get('ids', []) or []
        degree = request.data.get('degree')
        language = request.data.get('language')

    if len(ids) < 2:
        return Response(
            {'error': 'Need at least 2 universities'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # --- 2. Фильтры для программ ---
    program_filters = {
        'degree': degree,
        'language': language,
    }

    # --- 3. Вузы + сериализация ---
    universities = University.objects.filter(id__in=ids)

    serializer = UniversityCompareSerializer(
        universities,
        many=True,
        context={'program_filters': program_filters}
    )
    return Response(serializer.data)

