from django.core.management.base import BaseCommand
from api.models import University, Faculty, Program


class Command(BaseCommand):
    help = 'Seed database with universities'

    def handle(self, *args, **options):
        University.objects.all().delete()
        
        uni1 = University.objects.create(
            name="Назарбаев Университет",
            city="Астана",
            description="Автономный исследовательский университет",
            founded_year=2010,
            website="https://nu.edu.kz",
            ranking=1,
            student_count=6000
        )

        uni2 = University.objects.create(
            name="Казахский национальный университет им. аль-Фараби",
            city="Алматы",
            description="Крупнейший университет Казахстана",
            founded_year=1934,
            website="https://www.kaznu.kz",
            ranking=2,
            student_count=20000
        )

        uni3 = University.objects.create(
            name="КБТУ",
            city="Алматы",
            description="Ведущий технический университет",
            founded_year=2001,
            website="https://kbtu.edu.kz",
            ranking=3,
            student_count=3000
        )

        uni4 = University.objects.create(
            name="КИМЭП",
            city="Алматы",
            description="Институт менеджмента и экономики",
            founded_year=1992,
            website="https://www.kimep.kz",
            ranking=4,
            student_count=3500
        )

        uni5 = University.objects.create(
            name="Satbayev University",
            city="Алматы",
            description="Технический университет",
            founded_year=1934,
            website="https://satbayev.university",
            ranking=5,
            student_count=15000
        )

        self.stdout.write(f"Created {University.objects.count()} universities")

        Faculty.objects.create(university=uni1, name="School of Engineering")
        Faculty.objects.create(university=uni1, name="School of Medicine")
        Faculty.objects.create(university=uni3, name="Факультет IT")
        Faculty.objects.create(university=uni3, name="Бизнес школа")

        self.stdout.write(f"Created {Faculty.objects.count()} faculties")

        Program.objects.create(
            university=uni1,
            name="Computer Science",
            degree="bachelor",
            duration_years=4,
            language="EN",
            tuition_fee=0
        )

        Program.objects.create(
            university=uni3,
            name="Информационные системы",
            degree="bachelor",
            duration_years=4,
            language="RU/EN",
            tuition_fee=2500000
        )

        Program.objects.create(
            university=uni4,
            name="Business Administration",
            degree="bachelor",
            duration_years=4,
            language="EN",
            tuition_fee=3200000
        )

        self.stdout.write(f"Created {Program.objects.count()} programs")
        self.stdout.write(self.style.SUCCESS("Done!"))