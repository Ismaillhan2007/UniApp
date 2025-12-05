from rest_framework import serializers
from .models import University, Faculty, Program

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
            'faculties',   # All faculties of this university
            'programs'     # All programs of this university
        ]
