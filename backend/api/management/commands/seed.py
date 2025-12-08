from django.core.management.base import BaseCommand
from api.models import University, Faculty, Program, AdmissionInfo, InternationalCooperation

class Command(BaseCommand):
    help = 'Seed database with comprehensive data: Bachelors, Masters, PhDs'

    def handle(self, *args, **options):
        self.stdout.write('Очистка базы данных...')
        AdmissionInfo.objects.all().delete()
        InternationalCooperation.objects.all().delete()
        Program.objects.all().delete()
        Faculty.objects.all().delete()
        University.objects.all().delete()
        
        # ==========================================
        # 1. NAZARBAYEV UNIVERSITY (Research Focus)
        # ==========================================
        uni1 = University.objects.create(
            name="Назарбаев Университет",
            city="Астана",
            description="Автономный исследовательский университет международного уровня.",
            founded_year=2010,
            website="https://nu.edu.kz",
            ranking=1,
            student_count=7000,
            address="пр. Кабанбай батыра, 53",
            phone="+7 (7172) 70 66 88",
            email="info_admissions@nu.edu.kz",
            logo="/logos/nu.png"
        )
        
        AdmissionInfo.objects.create(
            university=uni1,
            requirements="SAT (1200+), IELTS 6.5 (не менее 6.0)",
            exams="NUET, IELTS/TOEFL, SAT Subject",
            min_score="IELTS 6.5",
            deadline="30 апреля",
            scholarships="Abay Kunanbayev Grant, Государственный грант"
        )

        InternationalCooperation.objects.create(
            university=uni1,
            partner_name="Duke University",
            country="USA",
            program_name="Medical Research",
            type="internship",
            language="English",
            description="Летняя стажировка для студентов школы медицины."
        )

        # Faculties
        nu_eng = Faculty.objects.create(university=uni1, name="School of Engineering and Digital Sciences")
        nu_med = Faculty.objects.create(university=uni1, name="School of Medicine")
        nu_sci = Faculty.objects.create(university=uni1, name="School of Sciences and Humanities")
        
        # Programs (Bachelor, Master, PhD)
        self.create_programs(uni1, [
            # Bachelor
            (nu_eng, "Computer Science", "bachelor", 4, "EN", 5300000, "ABET accredited program in CS."),
            (nu_eng, "Robotics and Mechatronics", "bachelor", 4, "EN", 5300000, "Focus on AI and automation."),
            (nu_sci, "Mathematics", "bachelor", 4, "EN", 5000000, "Pure and applied mathematics."),
            # Master
            (nu_eng, "Data Science", "master", 2, "EN", 6000000, "Advanced big data analytics."),
            (nu_med, "Public Health", "master", 2, "EN", 7500000, "MPH program for health professionals."),
            # PhD
            (nu_eng, "Science, Engineering and Technology", "phd", 4, "EN", 8000000, "Research intensive PhD program."),
        ])

        # ==========================================
        # 2. KAZNU (Classical University)
        # ==========================================
        uni2 = University.objects.create(
            name="КазНУ им. аль-Фараби",
            city="Алматы",
            description="Ведущий многопрофильный университет страны.",
            founded_year=1934,
            website="https://www.kaznu.kz",
            ranking=2,
            student_count=25000,
            address="пр. аль-Фараби, 71",
            phone="+7 (727) 377 33 33",
            email="info@kaznu.kz",
            logo="/logos/kaznu.png"
        )

        AdmissionInfo.objects.create(
            university=uni2,
            requirements="Аттестат, ЕНТ",
            exams="ЕНТ (Единое Национальное Тестирование)",
            min_score="70 баллов (для платного), 100+ (грант)",
            deadline="25 августа",
            scholarships="Государственные гранты РК"
        )

        InternationalCooperation.objects.create(
            university=uni2,
            partner_name="Peoples' Friendship University of Russia",
            country="Russia",
            program_name="Dual Degree Law",
            type="double_degree",
            language="Russian",
            description="Магистратура по международному праву."
        )

        # Faculties
        kaznu_mech = Faculty.objects.create(university=uni2, name="Механико-математический факультет")
        kaznu_bio = Faculty.objects.create(university=uni2, name="Факультет биологии")
        kaznu_law = Faculty.objects.create(university=uni2, name="Юридический факультет")

        # Programs
        self.create_programs(uni2, [
            # Bachelor
            (kaznu_mech, "Математика", "bachelor", 4, "KZ/RU", 1000000, "Классическое математическое образование."),
            (kaznu_bio, "Биотехнология", "bachelor", 4, "KZ/RU", 1100000, "Лабораторные исследования."),
            (kaznu_law, "Юриспруденция", "bachelor", 4, "KZ/RU", 1200000, "Гражданское и уголовное право."),
            # Master
            (kaznu_mech, "Информационные системы", "master", 2, "KZ/RU", 1500000, "Управление IT-проектами."),
            (kaznu_law, "Международное право", "master", 2, "EN", 1800000, "International trade law."),
            # PhD
            (kaznu_bio, "Биология", "phd", 3, "KZ/RU/EN", 2500000, "Научная степень в биологии."),
        ])

        # ==========================================
        # 3. KBTU (Technical/Business)
        # ==========================================
        uni3 = University.objects.create(
            name="КБТУ",
            city="Алматы",
            description="Лидер в области IT и нефтегазового сектора.",
            founded_year=2001,
            website="https://kbtu.edu.kz",
            ranking=3,
            student_count=4000,
            address="ул. Толе би, 59",
            phone="+7 (727) 357 42 42",
            email="info@kbtu.kz",
            logo="/logos/kbtu.png"
        )

        AdmissionInfo.objects.create(
            university=uni3,
            requirements="ЕНТ, KEPT (English Test)",
            exams="ЕНТ, KEPT, Математика (профильный)",
            min_score="ЕНТ 50+, Английский B1",
            deadline="20 августа",
            scholarships="Гранты КБТУ, Стипендии КазМунайГаз"
        )
        
        InternationalCooperation.objects.create(
            university=uni3,
            partner_name="University of London",
            country="UK",
            program_name="LSE Double Degree",
            type="double_degree",
            language="English",
            description="Двойной диплом с Лондонской школой экономики."
        )

        # Faculties
        kbtu_fit = Faculty.objects.create(university=uni3, name="Факультет информационных технологий")
        kbtu_oil = Faculty.objects.create(university=uni3, name="Факультет энергетики и нефтегаза")
        kbtu_bs = Faculty.objects.create(university=uni3, name="Бизнес школа")
        
        # Programs
        self.create_programs(uni3, [
            # Bachelor
            (kbtu_fit, "Information Systems", "bachelor", 4, "EN", 2600000, "Software engineering focus."),
            (kbtu_oil, "Petroleum Engineering", "bachelor", 4, "EN", 2800000, "Oil and gas exploration."),
            (kbtu_bs, "Finance", "bachelor", 4, "EN", 2600000, "CFA affiliated program."),
            # Master
            (kbtu_fit, "Artificial Intelligence", "master", 2, "EN", 3200000, "Machine learning and data mining."),
            (kbtu_bs, "Project Management", "master", 1, "EN", 3500000, "Executive MBA style program."),
            # PhD
            (kbtu_oil, "Petroleum Geosciences", "phd", 3, "EN", 4000000, "Advanced geological research."),
        ])

        # ==========================================
        # 4. KIMEP (Business/Social Sciences)
        # ==========================================
        uni4 = University.objects.create(
            name="КИМЭП",
            city="Алматы",
            description="Ведущий вуз в сфере бизнеса и права североамериканского образца.",
            founded_year=1992,
            website="https://www.kimep.kz",
            ranking=4,
            student_count=3500,
            address="пр. Абая, 2",
            phone="+7 (727) 270 43 14",
            email="admissions@kimep.kz",
            logo="/logos/kimep.png"
        )

        AdmissionInfo.objects.create(
            university=uni4,
            requirements="IELTS 5.0+, Аттестат",
            exams="KIMEP Entrance Exam / IELTS",
            min_score="IELTS 4.5 (Foundation)",
            deadline="15 августа",
            scholarships="Altyn Belgi Scholarship, Dean's List"
        )

        InternationalCooperation.objects.create(
            university=uni4,
            partner_name="Yonsei University",
            country="South Korea",
            program_name="Student Exchange",
            type="exchange",
            language="English",
            description="Семестр по обмену в Сеуле."
        )

        # Faculties
        kimep_bcb = Faculty.objects.create(university=uni4, name="Bang College of Business")
        kimep_css = Faculty.objects.create(university=uni4, name="College of Social Sciences")
        kimep_law = Faculty.objects.create(university=uni4, name="School of Law")
        
        # Programs
        self.create_programs(uni4, [
            # Bachelor
            (kimep_bcb, "Accounting and Audit", "bachelor", 4, "EN", 3200000, "ACCA certified."),
            (kimep_bcb, "Marketing", "bachelor", 4, "EN", 3200000, "Digital marketing focus."),
            (kimep_css, "International Relations", "bachelor", 4, "EN", 3000000, "Diplomacy and politics."),
            # Master
            (kimep_bcb, "MBA", "master", 1, "EN", 4500000, "Master of Business Administration."),
            (kimep_law, "International Law", "master", 2, "EN", 3500000, "LLM degree."),
            # PhD
            (kimep_bcb, "Business Administration", "phd", 3, "EN", 5000000, "Doctor of Business Administration."),
        ])

        # ==========================================
        # 5. SATBAYEV UNIVERSITY (Engineering)
        # ==========================================
        uni5 = University.objects.create(
            name="Satbayev University",
            city="Алматы",
            description="Старейший технический вуз, центр инженерного образования.",
            founded_year=1934,
            website="https://satbayev.university",
            ranking=5,
            student_count=15000,
            address="ул. Сатпаева, 22а",
            phone="+7 (727) 292 60 25",
            email="info@satbayev.university",
            logo="/logos/satbayev.png"
        )

        AdmissionInfo.objects.create(
            university=uni5,
            requirements="ЕНТ (Физика/Математика)",
            exams="ЕНТ, Творческий экзамен (для архитекторов)",
            min_score="65 баллов",
            deadline="25 августа",
            scholarships="Государственные гранты, Стипендии KazMinerals"
        )

        InternationalCooperation.objects.create(
            university=uni5,
            partner_name="Politecnico di Torino",
            country="Italy",
            program_name="Architecture Dual Degree",
            type="double_degree",
            language="English",
            description="Двойной диплом по архитектуре и дизайну."
        )

        # Faculties
        sat_cyber = Faculty.objects.create(university=uni5, name="Институт кибернетики")
        sat_arch = Faculty.objects.create(university=uni5, name="Институт архитектуры")
        sat_geo = Faculty.objects.create(university=uni5, name="Горно-металлургический институт")
        
        # Programs
        self.create_programs(uni5, [
            # Bachelor
            (sat_cyber, "Робототехника", "bachelor", 4, "KZ/RU", 1150000, "Мехатроника и схемотехника."),
            (sat_arch, "Архитектура", "bachelor", 5, "KZ/RU", 1200000, "Градостроительство."),
            (sat_geo, "Геология", "bachelor", 4, "KZ/RU", 1100000, "Разведка полезных ископаемых."),
            # Master
            (sat_cyber, "Automation and Control", "master", 2, "EN", 1500000, "Industrial automation systems."),
            # PhD
            (sat_geo, "Metallurgy", "phd", 3, "KZ/RU", 2000000, "Advanced metallurgy research."),
        ])
        # ==========================================
        # 6. NARXOZ UNIVERSITY (Business/Economics)
        # ==========================================
        uni6 = University.objects.create(
            name="Нархоз Университет",
            city="Алматы",
            description="Ведущий бизнес-университет с сильной экономической школой.",
            founded_year=1963,
            website="https://narxoz.kz",
            ranking=6,
            student_count=8000,
            address="ул. Жандосова, 55",
            phone="+7 (727) 356 25 25",
            email="info@narxoz.kz",
            logo="/logos/narxoz.png"
        )

        AdmissionInfo.objects.create(
            university=uni6,
            requirements="ЕНТ, IELTS 5.0+ (для англоязычных программ)",
            exams="ЕНТ, IELTS/TOEFL (для международных программ)",
            min_score="65 баллов (ЕНТ), IELTS 5.0",
            deadline="20 августа",
            scholarships="Гранты Narxoz, Стипендии от партнеров"
        )

        InternationalCooperation.objects.create(
            university=uni6,
            partner_name="University of Westminster",
            country="UK",
            program_name="Business Administration",
            type="double_degree",
            language="English",
            description="Двойной диплом в области бизнес-администрирования."
        )

        # Faculties
        narxoz_econ = Faculty.objects.create(university=uni6, name="Высшая школа экономики")
        narxoz_business = Faculty.objects.create(university=uni6, name="Высшая школа бизнеса")
        narxoz_law = Faculty.objects.create(university=uni6, name="Высшая школа права")

        # Programs
        self.create_programs(uni6, [
            # Bachelor
            (narxoz_econ, "Экономика", "bachelor", 4, "KZ/RU", 1800000, "Микро и макроэкономика."),
            (narxoz_business, "Менеджмент", "bachelor", 4, "EN", 2000000, "Управление бизнес-процессами."),
            (narxoz_business, "Финансы", "bachelor", 4, "KZ/RU/EN", 1900000, "Финансовый анализ и инвестиции."),
            (narxoz_law, "Право", "bachelor", 4, "KZ/RU", 1700000, "Корпоративное право."),
            # Master
            (narxoz_business, "MBA", "master", 1, "EN", 4000000, "Executive MBA программа."),
            (narxoz_econ, "Экономическая аналитика", "master", 2, "EN", 2500000, "Data-driven economics."),
            # PhD
            (narxoz_econ, "Экономические науки", "phd", 3, "KZ/RU/EN", 3000000, "Докторантура по экономике."),
        ])

        self.stdout.write(self.style.SUCCESS(f"База данных успешно обновлена! Добавлено 6 вузов с бакалавриатом, магистратурой и PhD."))

    def create_programs(self, uni, programs_data):
        for faculty, name, degree, duration, lang, fee, desc in programs_data:
            Program.objects.create(
                university=uni,
                faculty=faculty,
                name=name,
                degree=degree,
                duration_years=duration,
                language=lang,
                tuition_fee=fee,
                description=desc
            )