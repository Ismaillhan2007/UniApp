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
    
class AdmissionInfo(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='admissions'
    )
    program = models.ForeignKey(
        Program,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='admissions'
    )

    requirements = models.TextField(blank=True)          # требования к поступлению
    exams = models.CharField(max_length=200, blank=True) # например: ЕНТ, IELTS
    min_score = models.CharField(max_length=100, blank=True)  # минимальный балл
    deadline = models.CharField(max_length=100, blank=True)   # сроки подачи
    scholarships = models.TextField(blank=True)          # инфо про гранты/стипендии

    def __str__(self):
        base = f"Поступление в {self.university.name}"
        if self.program:
            base += f" – {self.program.name}"
        return base


class InternationalCooperation(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='international_programs'
    )
    partner_name = models.CharField(max_length=200)      # партнёрский вуз
    country = models.CharField(max_length=100)           # страна партнёра
    program_name = models.CharField(max_length=200)      # название программы
    type = models.CharField(
        max_length=50,
        choices=[
            ('exchange', 'Обмен'),
            ('double_degree', 'Двойной диплом'),
            ('internship', 'Стажировка'),
        ]
    )
    language = models.CharField(max_length=50, blank=True)  # язык обучения
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.university.name} – {self.partner_name} ({self.country})"
