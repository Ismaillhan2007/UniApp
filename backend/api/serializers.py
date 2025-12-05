from rest_framework import serializers
from .models import University, Faculty, Program, AdmissionInfo, InternationalCooperation

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name']

class ProgramSerializer(serializers.ModelSerializer):
    faculty_name = serializers.CharField(source='faculty.name', read_only=True)
    
    class Meta:
        model = Program
        fields = [
            'id', 'name', 'degree', 'duration_years', 
            'language', 'tuition_fee', 'description', 
            'faculty', 'faculty_name'
        ]

# === NEW SERIALIZERS ===
class AdmissionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionInfo
        fields = ['id', 'requirements', 'exams', 'min_score', 'deadline', 'scholarships']

class InternationalCooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalCooperation
        fields = ['id', 'partner_name', 'country', 'program_name', 'type', 'language', 'description']

class UniversityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'city', 'logo', 'ranking', 'student_count']

class UniversityDetailSerializer(serializers.ModelSerializer):
    # Include all related data
    faculties = FacultySerializer(many=True, read_only=True)
    programs = ProgramSerializer(many=True, read_only=True)
    admissions = AdmissionInfoSerializer(many=True, read_only=True) # New
    international_programs = InternationalCooperationSerializer(many=True, read_only=True) # New
    
    class Meta:
        model = University
        fields = [
            'id', 'name', 'city', 'description', 'founded_year',
            'logo', 'website', 'ranking', 'student_count',
            'address', 'phone', 'email', # Added these contact fields
            'faculties', 'programs', 
            'admissions', 'international_programs' # Added these sections
        ]

class UniversityCompareSerializer(serializers.ModelSerializer):
    programs = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = ['id', 'name', 'city', 'ranking', 'student_count', 'website', 'programs']

    def get_programs(self, obj):
        filters = self.context.get('program_filters', {})
        qs = obj.programs.all() # Changed from program_set to programs (related_name)
        
        degree = filters.get('degree')
        language = filters.get('language')

        if degree:
            qs = qs.filter(degree=degree)
        if language:
            qs = qs.filter(language__icontains=language)

        return ProgramSerializer(qs, many=True).data