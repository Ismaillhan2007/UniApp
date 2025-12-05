from django.db import models

class University(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    description = models.TextField()
    founded_year = models.IntegerField()
    logo = models.URLField(blank=True)
    website = models.URLField(blank=True)
    ranking = models.IntegerField(null=True, blank=True)
    student_count = models.IntegerField(null=True, blank=True)
    
    # Contact Info
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class AdmissionInfo(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='admissions')
    requirements = models.TextField()
    exams = models.CharField(max_length=200)
    min_score = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    scholarships = models.TextField(blank=True)

class InternationalCooperation(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='international_programs')
    partner_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    program_name = models.CharField(max_length=200)
    type = models.CharField(max_length=100) # Exchange, Double Degree, etc.
    language = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class Faculty(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='faculties')
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.university.name} - {self.name}"

class Program(models.Model):
    DEGREE_CHOICES = [
        ('bachelor', 'Бакалавриат'),
        ('master', 'Магистратура'),
        ('phd', 'Докторантура'),
    ]
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='programs')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    duration_years = models.IntegerField()
    language = models.CharField(max_length=50)
    tuition_fee = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.degree})"