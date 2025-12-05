from rest_framework import serializers
from .models import University, Faculty, Program, AdmissionInfo, InternationalCooperation

# ============ BASIC SERIALIZERS ============

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name']


class ProgramSerializer(serializers.ModelSerializer):
    faculty_name = serializers.CharField(source='faculty.name', read_only=True)
    university_name = serializers.CharField(source='university.name', read_only=True)
    
    class Meta:
        model = Program
        fields = [
            'id', 
            'name', 
            'degree', 
            'duration_years', 
            'language', 
            'tuition_fee', 
            'description',
            'faculty',
            'faculty_name',
            'university',
            'university_name'
        ]


# ============ UNIVERSITY SERIALIZERS ============

# For listing all universities (simple, less data)
class UniversityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'city', 'logo', 'ranking', 'student_count']


# For single university (detailed, includes children)
class UniversityDetailSerializer(serializers.ModelSerializer):
    # Include related children
    faculties = FacultySerializer(source='faculty_set', many=True, read_only=True)
    programs = ProgramSerializer(source='program_set', many=True, read_only=True)

    # НОВЫЕ ПОЛЯ:
    admissions = AdmissionSerializer(many=True, read_only=True)              # related_name='admissions'
    international_programs = InternationalSerializer(many=True, read_only=True)  # related_name='international_programs'
    
    class Meta:
        model = University
        fields = [
            'id',
            'name',
            'city',
            'description',
            'founded_year',
            'logo',
            'website',
            'ranking',
            'student_count',
            'address',
            'phone',
            'email',
            'faculties',
            'programs',
            'admissions',            # ← ПРИЁМ И ПОСТУПЛЕНИЕ
            'international_programs' # ← МЕЖДУНАРОДНОЕ СОТРУДНИЧЕСТВО
        ]


class UniversityCompareSerializer(serializers.ModelSerializer):
    programs = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = [
            'id',
            'name',
            'city',
            'ranking',
            'student_count',
            'website',
            'programs',
        ]

    def get_programs(self, obj):
        
        filters = self.context.get('program_filters', {})
        qs = obj.program_set.all()

        degree = filters.get('degree')
        language = filters.get('language')

        if degree:
            qs = qs.filter(degree=degree)
        if language:
            qs = qs.filter(language__icontains=language)

        return ProgramSerializer(qs, many=True).data

class AdmissionSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.name', read_only=True)

    class Meta:
        model = AdmissionInfo
        fields = [
            'id',
            'university',
            'program',
            'program_name',
            'requirements',
            'exams',
            'min_score',
            'deadline',
            'scholarships',
        ]


class InternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalCooperation
        fields = [
            'id',
            'university',
            'partner_name',
            'country',
            'program_name',
            'type',
            'language',
            'description',
        ]
