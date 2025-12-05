from django.core.management.base import BaseCommand
from api.models import University, Faculty, Program

class Command(BaseCommand):
    help = 'Seed database with universities'

    def handle(self, *args, **options):
        # Очистка старых данных перед заливкой
        self.stdout.write('Очистка базы данных...')
        Program.objects.all().delete()
        Faculty.objects.all().delete()
        University.objects.all().delete()
        
        # ==========================================
        # 1. NAZARBAYEV UNIVERSITY
        # ==========================================
        uni1 = University.objects.create(
            name="Назарбаев Университет",
            city="Астана",
            description="Автономный исследовательский университет международного уровня.",
            founded_year=2010,
            website="https://nu.edu.kz",
            ranking=1,
            student_count=7000,
            logo="https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Nazarbayev_University_Logo.png/220px-Nazarbayev_University_Logo.png"
        )
        # Факультеты NU
        f1_eng = Faculty.objects.create(university=uni1, name="School of Engineering")
        f1_med = Faculty.objects.create(university=uni1, name="School of Medicine")
        f1_hum = Faculty.objects.create(university=uni1, name="School of Sciences and Humanities")

        # Программы NU
        self.create_programs(uni1, [
            (f1_eng, "Computer Science", "bachelor", 4, "EN", 0), # Грант
            (f1_eng, "Robotics", "bachelor", 4, "EN", 0),
            (f1_eng, "Data Science", "master", 2, "EN", 4500000),
            (f1_med, "Medicine", "bachelor", 5, "EN", 3500000),
            (f1_hum, "Economics", "bachelor", 4, "EN", 0),
        ])

        # ==========================================
        # 2. KAZNU (КазНУ)
        # ==========================================
        uni2 = University.objects.create(
            name="Казахский национальный университет им. аль-Фараби",
            city="Алматы",
            description="Крупнейший многопрофильный университет страны.",
            founded_year=1934,
            website="https://www.kaznu.kz",
            ranking=2,
            student_count=20000,
            logo="https://upload.wikimedia.org/wikipedia/ru/thumb/9/9c/KazNU_Logo.png/200px-KazNU_Logo.png"
        )
        # Факультеты KazNU
        f2_mech = Faculty.objects.create(university=uni2, name="Механико-математический")
        f2_bio = Faculty.objects.create(university=uni2, name="Биологии и биотехнологии")
        f2_jur = Faculty.objects.create(university=uni2, name="Юридический")

        # Программы KazNU
        self.create_programs(uni2, [
            (f2_mech, "Математика", "bachelor", 4, "KZ/RU", 1000000),
            (f2_mech, "Информационные системы", "bachelor", 4, "KZ/RU", 1100000),
            (f2_bio, "Биотехнология", "bachelor", 4, "KZ/RU", 1200000),
            (f2_jur, "Юриспруденция", "bachelor", 4, "KZ/RU", 1300000),
            (f2_jur, "Международное право", "master", 2, "EN", 1800000),
        ])

        # ==========================================
        # 3. KBTU (КБТУ)
        # ==========================================
        uni3 = University.objects.create(
            name="КБТУ",
            city="Алматы",
            description="Ведущий технический вуз, лидер в IT и нефтегазовом секторе.",
            founded_year=2001,
            website="https://kbtu.edu.kz",
            ranking=3,
            student_count=3000,
            logo="https://kbtu.edu.kz/images/logo_kbtu_new.png"
        )
        # Факультеты KBTU
        f3_it = Faculty.objects.create(university=uni3, name="Факультет информационных технологий")
        f3_bs = Faculty.objects.create(university=uni3, name="Бизнес школа")
        f3_oil = Faculty.objects.create(university=uni3, name="Факультет энергетики")

        # Программы KBTU
        self.create_programs(uni3, [
            (f3_it, "Information Systems", "bachelor", 4, "EN", 2600000),
            (f3_it, "Cybersecurity", "bachelor", 4, "EN", 2600000),
            (f3_it, "Artificial Intelligence", "master", 2, "EN", 3200000),
            (f3_bs, "Finance", "bachelor", 4, "EN", 2400000),
            (f3_oil, "Petroleum Engineering", "bachelor", 4, "EN", 2800000),
        ])

        # ==========================================
        # 4. KIMEP (КИМЭП)
        # ==========================================
        uni4 = University.objects.create(
            name="КИМЭП",
            city="Алматы",
            description="Ведущий университет в области бизнеса и социальных наук.",
            founded_year=1992,
            website="https://www.kimep.kz",
            ranking=4,
            student_count=3500,
            logo="https://www.kimep.kz/wp-content/uploads/2019/02/KIMEP_Logo_RGB_ENG.png"
        )
        # Факультеты KIMEP
        f4_bcb = Faculty.objects.create(university=uni4, name="Banga College of Business")
        f4_css = Faculty.objects.create(university=uni4, name="College of Social Sciences")
        f4_law = Faculty.objects.create(university=uni4, name="School of Law")

        # Программы KIMEP
        self.create_programs(uni4, [
            (f4_bcb, "Accounting and Audit", "bachelor", 4, "EN", 3200000),
            (f4_bcb, "Marketing", "bachelor", 4, "EN", 3200000),
            (f4_css, "International Relations", "bachelor", 4, "EN", 3000000),
            (f4_law, "International Law", "master", 2, "EN", 3500000),
        ])

        # ==========================================
        # 5. SATBAYEV UNIVERSITY
        # ==========================================
        uni5 = University.objects.create(
            name="Satbayev University",
            city="Алматы",
            description="Старейший технический университет Казахстана.",
            founded_year=1934,
            website="https://satbayev.university",
            ranking=5,
            student_count=15000,
            logo="https://satbayev.university/resources/img/logo_satbayev_university.png"
        )
        # Факультеты Satbayev
        f5_arch = Faculty.objects.create(university=uni5, name="Институт архитектуры и строительства")
        f5_geo = Faculty.objects.create(university=uni5, name="Горно-металлургический институт")
        f5_cyber = Faculty.objects.create(university=uni5, name="Институт кибернетики")

        # Программы Satbayev
        self.create_programs(uni5, [
            (f5_arch, "Архитектура", "bachelor", 5, "KZ/RU", 1200000),
            (f5_geo, "Геология", "bachelor", 4, "KZ/RU", 1100000),
            (f5_cyber, "Робототехника", "bachelor", 4, "KZ/RU", 1150000),
            (f5_cyber, "Automation", "master", 2, "EN", 1500000),
        ])

        self.stdout.write(self.style.SUCCESS(f"Готово! Создано {University.objects.count()} университетов с факультетами и программами."))

    # Вспомогательная функция для быстрого создания программ
    def create_programs(self, uni, programs_data):
        for faculty, name, degree, duration, lang, fee in programs_data:
            Program.objects.create(
                university=uni,
                faculty=faculty,
                name=name,
                degree=degree,
                duration_years=duration,
                language=lang,
                tuition_fee=fee,
                description=f"Программа {name} ({degree}) на факультете {faculty.name}."
            )