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
    
    # Contact
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.name

class Faculty(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.university.name} - {self.name}"

class Program(models.Model):
    DEGREE_CHOICES = [
        ('bachelor', 'Бакалавриат'),
        ('master', 'Магистратура'),
        ('phd', 'Докторантура'),
    ]
    
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    duration_years = models.IntegerField()
    language = models.CharField(max_length=50)  # KZ, RU, EN
    tuition_fee = models.IntegerField(null=True, blank=True)  # per year in tenge
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.degree})"