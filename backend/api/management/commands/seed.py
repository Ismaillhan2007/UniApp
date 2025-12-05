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
            description="Автономный исследовательский университет международного уровня с англоязычной средой обучения. Университет создан по инициативе Первого Президента РК и является флагманом казахстанской высшей школы. Обучение ведется полностью на английском языке по лучшим международным стандартам.",
            founded_year=2010,
            website="https://nu.edu.kz",
            ranking=1,
            student_count=7000,
            address="53 Қабанбай батыр проспект, Астана 010000",
            phone="+7 (7172) 70-93-33",
            email="info@nu.edu.kz",
            logo="https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Nazarbayev_University_Logo.png/220px-Nazarbayev_University_Logo.png"
        )
        # Факультеты NU
        f1_eng = Faculty.objects.create(university=uni1, name="School of Engineering and Digital Sciences")
        f1_med = Faculty.objects.create(university=uni1, name="School of Medicine")
        f1_hum = Faculty.objects.create(university=uni1, name="School of Sciences and Humanities")
        f1_gspp = Faculty.objects.create(university=uni1, name="Graduate School of Public Policy")
        f1_gsbusiness = Faculty.objects.create(university=uni1, name="Graduate School of Business")

        # Программы NU
        self.create_programs(uni1, [
            # Engineering
            (f1_eng, "Computer Science", "bachelor", 4, "EN", 0, "Передовая программа по CS с акцентом на искусственный интеллект, машинное обучение и разработку ПО. Полностью грантовое обучение для всех студентов."),
            (f1_eng, "Robotics and Mechatronics", "bachelor", 4, "EN", 0, "Междисциплинарная программа, объединяющая механику, электронику и программирование для создания робототехнических систем."),
            (f1_eng, "Chemical Engineering", "bachelor", 4, "EN", 0, "Программа по химической инженерии с фокусом на устойчивые технологии и инновации."),
            (f1_eng, "Data Science", "master", 2, "EN", 4500000, "Магистерская программа по анализу данных, машинному обучению и большим данным для цифровой экономики."),
            (f1_eng, "Computer Science (PhD)", "phd", 4, "EN", 0, "Докторская программа для подготовки исследователей в области компьютерных наук и искусственного интеллекта."),
            (f1_eng, "Engineering (PhD)", "phd", 4, "EN", 0, "PhD программа по инженерным наукам с возможностью специализации в различных направлениях."),
            
            # Medicine
            (f1_med, "Medicine", "bachelor", 6, "EN", 3500000, "Шестилетняя программа подготовки врачей международного уровня. Включает клиническую практику в лучших медицинских центрах."),
            (f1_med, "Public Health", "master", 2, "EN", 4000000, "Магистратура по общественному здравоохранению для подготовки специалистов в области здравоохранения."),
            
            # Humanities
            (f1_hum, "Economics", "bachelor", 4, "EN", 0, "Программа по экономике с акцентом на аналитические методы и экономическую политику."),
            (f1_hum, "Political Science and International Relations", "bachelor", 4, "EN", 0, "Изучение политических систем, международных отношений и глобальных процессов."),
            (f1_hum, "Chemistry", "bachelor", 4, "EN", 0, "Фундаментальная программа по химии для подготовки исследователей."),
            
            # Graduate Schools
            (f1_gspp, "Public Policy", "master", 2, "EN", 4200000, "Магистерская программа для подготовки специалистов в области государственной политики и управления."),
            (f1_gsbusiness, "Master of Business Administration (MBA)", "master", 2, "EN", 9000000, "Престижная MBA программа для топ-менеджеров и предпринимателей."),
        ])

        # ==========================================
        # 2. KAZNU (КазНУ им. аль-Фараби)
        # ==========================================
        uni2 = University.objects.create(
            name="Казахский национальный университет им. аль-Фараби",
            city="Алматы",
            description="Крупнейший классический университет Казахстана, основанный в 1934 году. Ведущий научно-образовательный центр страны с богатыми традициями и современными программами. Входит в топ-300 университетов мира по версии QS World University Rankings.",
            founded_year=1934,
            website="https://www.kaznu.kz",
            ranking=2,
            student_count=20000,
            address="проспект аль-Фараби 71, Алматы 050040",
            phone="+7 (727) 377-33-30",
            email="info@kaznu.kz",
            logo="https://upload.wikimedia.org/wikipedia/ru/thumb/9/9c/KazNU_Logo.png/200px-KazNU_Logo.png"
        )
        # Факультеты KazNU
        f2_mech = Faculty.objects.create(university=uni2, name="Механико-математический факультет")
        f2_bio = Faculty.objects.create(university=uni2, name="Факультет биологии и биотехнологии")
        f2_jur = Faculty.objects.create(university=uni2, name="Юридический факультет")
        f2_phil = Faculty.objects.create(university=uni2, name="Факультет философии и политологии")
        f2_econ = Faculty.objects.create(university=uni2, name="Высшая школа экономики и бизнеса")

        # Программы KazNU
        self.create_programs(uni2, [
            # Механико-математический
            (f2_mech, "Математика", "bachelor", 4, "KZ", 1000000, "Фундаментальная подготовка математиков-исследователей и преподавателей математики."),
            (f2_mech, "Прикладная математика", "bachelor", 4, "RU", 1050000, "Программа по применению математических методов в экономике, физике и IT."),
            (f2_mech, "Информационные системы", "bachelor", 4, "RU", 1100000, "Разработка информационных систем для бизнеса и государственных организаций."),
            (f2_mech, "Математика и компьютерные науки", "master", 2, "RU", 1400000, "Магистратура для углубленного изучения математики и программирования."),
            (f2_mech, "Математика (PhD)", "phd", 3, "RU", 800000, "Докторантура по математике для подготовки научных кадров высшей квалификации."),
            
            # Биология
            (f2_bio, "Биология", "bachelor", 4, "KZ", 1150000, "Классическая биологическая программа с изучением всех разделов биологии."),
            (f2_bio, "Биотехнология", "bachelor", 4, "RU", 1200000, "Современная программа по биотехнологиям с практикой в лабораториях."),
            (f2_bio, "Экология", "bachelor", 4, "KZ", 1100000, "Программа по изучению экосистем и охране окружающей среды."),
            (f2_bio, "Биотехнология", "master", 2, "EN", 1600000, "Магистратура по биотехнологиям с исследовательской компонентой."),
            
            # Юридический
            (f2_jur, "Юриспруденция", "bachelor", 4, "KZ", 1300000, "Подготовка юристов широкого профиля для работы в различных отраслях права."),
            (f2_jur, "Международное право", "bachelor", 4, "RU", 1350000, "Специализация в области международного права и международных отношений."),
            (f2_jur, "Международное право", "master", 2, "EN", 1800000, "Магистерская программа по международному праву с возможностью стажировок за рубежом."),
            (f2_jur, "Юриспруденция (PhD)", "phd", 3, "RU", 850000, "Научно-исследовательская программа для подготовки докторов юридических наук."),
            
            # Философия и политология
            (f2_phil, "Философия", "bachelor", 4, "KZ", 950000, "Изучение философских систем и развитие критического мышления."),
            (f2_phil, "Политология", "bachelor", 4, "RU", 1000000, "Анализ политических процессов и систем управления."),
            
            # Экономика и бизнес
            (f2_econ, "Экономика", "bachelor", 4, "RU", 1400000, "Фундаментальная экономическая подготовка с акцентом на аналитику."),
            (f2_econ, "Финансы", "bachelor", 4, "RU", 1450000, "Программа по финансовым рынкам, инвестициям и банковскому делу."),
            (f2_econ, "Маркетинг", "bachelor", 4, "RU", 1400000, "Современный маркетинг в эпоху цифровизации и социальных сетей."),
        ])

        # ==========================================
        # 3. KBTU (КБТУ)
        # ==========================================
        uni3 = University.objects.create(
            name="КБТУ (Казахстанско-Британский Технический Университет)",
            city="Алматы",
            description="Ведущий технический вуз Казахстана, основанный совместно с Абердинским университетом (Великобритания). Специализируется на IT, энергетике и бизнесе. Выпускники КБТУ высоко ценятся работодателями за практические навыки и знание английского языка. Университет является лидером по трудоустройству выпускников.",
            founded_year=2001,
            website="https://kbtu.edu.kz",
            ranking=3,
            student_count=3000,
            address="проспект Толе би 59, Алматы 050000",
            phone="+7 (727) 320-77-77",
            email="info@kbtu.kz",
            logo="https://kbtu.edu.kz/images/logo_kbtu_new.png"
        )
        # Факультеты KBTU
        f3_it = Faculty.objects.create(university=uni3, name="Факультет информационных технологий")
        f3_bs = Faculty.objects.create(university=uni3, name="Бизнес школа")
        f3_oil = Faculty.objects.create(university=uni3, name="Факультет энергетики и нефтегазового дела")
        f3_eng = Faculty.objects.create(university=uni3, name="Инженерный факультет")

        # Программы KBTU
        self.create_programs(uni3, [
            # IT
            (f3_it, "Information Systems", "bachelor", 4, "EN", 2600000, "Разработка и управление информационными системами для бизнеса. Включает изучение баз данных, веб-технологий и управления проектами."),
            (f3_it, "Cybersecurity", "bachelor", 4, "EN", 2600000, "Защита информации и кибербезопасность в эпоху цифровизации. Практика в реальных компаниях."),
            (f3_it, "Software Engineering", "bachelor", 4, "EN", 2600000, "Разработка программного обеспечения по международным стандартам. Агильные методологии и DevOps."),
            (f3_it, "Data Science", "bachelor", 4, "EN", 2700000, "Анализ больших данных, машинное обучение и визуализация данных для принятия бизнес-решений."),
            (f3_it, "Artificial Intelligence", "master", 2, "EN", 3200000, "Магистратура по искусственному интеллекту и глубокому обучению. Исследовательские проекты с индустрией."),
            (f3_it, "Computer Science (PhD)", "phd", 3, "EN", 1500000, "PhD программа для исследователей в области компьютерных наук и AI."),
            
            # Business School
            (f3_bs, "Finance", "bachelor", 4, "EN", 2400000, "Корпоративные финансы, инвестиционный анализ и риск-менеджмент. Подготовка к международным сертификациям CFA."),
            (f3_bs, "Accounting and Audit", "bachelor", 4, "EN", 2400000, "Бухгалтерский учет и аудит по международным стандартам ACCA и CIMA."),
            (f3_bs, "Management", "bachelor", 4, "EN", 2350000, "Стратегический менеджмент, управление персоналом и бизнес-планирование."),
            (f3_bs, "MBA", "master", 1.5, "EN", 7500000, "Программа MBA для действующих менеджеров. Вечернее и weekend обучение."),
            
            # Энергетика
            (f3_oil, "Petroleum Engineering", "bachelor", 4, "EN", 2800000, "Нефтегазовая инженерия с упором на разведку и добычу углеводородов."),
            (f3_oil, "Energy Engineering", "bachelor", 4, "EN", 2700000, "Альтернативная энергетика, энергоэффективность и зеленые технологии."),
            (f3_oil, "Oil and Gas Management", "master", 2, "EN", 3400000, "Магистратура по управлению в нефтегазовой отрасли."),
            
            # Engineering
            (f3_eng, "Industrial Engineering", "bachelor", 4, "EN", 2500000, "Оптимизация производственных процессов и управление операциями."),
        ])

        # ==========================================
        # 4. KIMEP (КИМЭП)
        # ==========================================
        uni4 = University.objects.create(
            name="КИМЭП (Казахстанский институт менеджмента, экономики и прогнозирования)",
            city="Алматы",
            description="Первый международный университет в Центральной Азии, основанный в 1992 году по американской модели образования. КИМЭП специализируется на бизнесе, юриспруденции и социальных науках. Университет аккредитован AACSB - высшим мировым стандартом для бизнес-школ. 100% англоязычное обучение.",
            founded_year=1992,
            website="https://www.kimep.kz",
            ranking=4,
            student_count=3500,
            address="улица Абая 4, Алматы 050010",
            phone="+7 (727) 270-44-44",
            email="admission@kimep.kz",
            logo="https://www.kimep.kz/wp-content/uploads/2019/02/KIMEP_Logo_RGB_ENG.png"
        )
        # Факультеты KIMEP
        f4_bcb = Faculty.objects.create(university=uni4, name="Bang College of Business")
        f4_css = Faculty.objects.create(university=uni4, name="College of Social Sciences")
        f4_law = Faculty.objects.create(university=uni4, name="School of Law")

        # Программы KIMEP
        self.create_programs(uni4, [
            # Business
            (f4_bcb, "Accounting and Audit", "bachelor", 4, "EN", 3200000, "ACCA-аккредитованная программа по бухучету и аудиту. Выпускники получают освобождение от 9 экзаменов ACCA."),
            (f4_bcb, "Finance", "bachelor", 4, "EN", 3200000, "Финансовый анализ, корпоративные финансы и инвестиционный банкинг."),
            (f4_bcb, "Marketing", "bachelor", 4, "EN", 3200000, "Современный маркетинг: брендинг, цифровой маркетинг, исследования потребителей."),
            (f4_bcb, "Management", "bachelor", 4, "EN", 3100000, "Стратегический менеджмент, предпринимательство и управление проектами."),
            (f4_bcb, "International Business", "bachelor", 4, "EN", 3250000, "Международная торговля, глобальные цепочки поставок и кросс-культурный менеджмент."),
            (f4_bcb, "MBA", "master", 2, "EN", 8500000, "Престижная MBA программа с возможностью международного обмена."),
            (f4_bcb, "Master in Finance", "master", 1.5, "EN", 4200000, "Специализированная магистратура по финансам для карьеры в инвестбанкинге."),
            
            # Social Sciences
            (f4_css, "International Relations", "bachelor", 4, "EN", 3000000, "Международные отношения, дипломатия и геополитика. Программа с обменом в университеты США и Европы."),
            (f4_css, "Public Administration", "bachelor", 4, "EN", 2900000, "Государственное управление и публичная политика."),
            (f4_css, "Journalism and Mass Communication", "bachelor", 4, "EN", 2950000, "Журналистика, PR и медиа-коммуникации в цифровую эпоху."),
            (f4_css, "International Relations", "master", 2, "EN", 3600000, "Магистратура по международным отношениям с фокусом на Центральную Азию."),
            
            # Law
            (f4_law, "Law", "bachelor", 4, "EN", 3100000, "Юриспруденция по англо-американской системе права."),
            (f4_law, "International Law", "master", 2, "EN", 3500000, "Магистратура по международному праву с возможностью двойного диплома."),
            (f4_law, "Law (PhD)", "phd", 3, "EN", 2000000, "PhD программа по юриспруденции для научной карьеры."),
        ])

        # ==========================================
        # 5. SATBAYEV UNIVERSITY (КазНИТУ)
        # ==========================================
        uni5 = University.objects.create(
            name="Satbayev University (КазНИТУ им. К.И. Сатпаева)",
            city="Алматы",
            description="Старейший и крупнейший технический университет Казахстана, основанный в 1934 году. Ведущий научный центр в области горного дела, металлургии, геологии и нефтегазового дела. Университет носит имя выдающегося ученого-геолога Каныша Сатпаева. Сильная научная школа и современная материальная база.",
            founded_year=1934,
            website="https://satbayev.university",
            ranking=5,
            student_count=15000,
            address="улица Сатпаева 22а, Алматы 050013",
            phone="+7 (727) 292-67-71",
            email="rector@satbayev.university",
            logo="https://satbayev.university/resources/img/logo_satbayev_university.png"
        )
        # Факультеты Satbayev
        f5_arch = Faculty.objects.create(university=uni5, name="Институт архитектуры и строительства")
        f5_geo = Faculty.objects.create(university=uni5, name="Горно-металлургический институт")
        f5_cyber = Faculty.objects.create(university=uni5, name="Институт кибернетики и информационных технологий")
        f5_oil = Faculty.objects.create(university=uni5, name="Институт геологии и нефтегазового дела")
        f5_energy = Faculty.objects.create(university=uni5, name="Институт энергетики и машиностроения")

        # Программы Satbayev
        self.create_programs(uni5, [
            # Архитектура и строительство
            (f5_arch, "Архитектура", "bachelor", 5, "KZ", 1200000, "Проектирование зданий и градостроительство. Программа включает практику в ведущих архитектурных бюро."),
            (f5_arch, "Строительство", "bachelor", 4, "RU", 1150000, "Промышленное и гражданское строительство с изучением современных технологий."),
            (f5_arch, "Урбанистика", "master", 2, "RU", 1400000, "Городское планирование и развитие городской среды."),
            
            # Горное дело и металлургия
            (f5_geo, "Горное дело", "bachelor", 4, "RU", 1150000, "Разработка месторождений полезных ископаемых открытым и подземным способом."),
            (f5_geo, "Геология", "bachelor", 4, "KZ", 1100000, "Поиски и разведка месторождений. Полевые практики в различных регионах Казахстана."),
            (f5_geo, "Металлургия", "bachelor", 4, "RU", 1200000, "Технологии получения и обработки металлов и сплавов."),
            (f5_geo, "Mining Engineering", "master", 2, "EN", 1500000, "Магистратура по горному делу с международными стандартами."),
            (f5_geo, "Mining Engineering (PhD)", "phd", 3, "RU", 900000, "Докторантура для научных исследований в горном деле."),
            
            # Кибернетика и IT
            (f5_cyber, "Робототехника и мехатроника", "bachelor", 4, "RU", 1150000, "Проектирование и программирование роботов и автоматизированных систем."),
            (f5_cyber, "Информационные системы", "bachelor", 4, "RU", 1100000, "Разработка корпоративных информационных систем."),
            (f5_cyber, "Кибербезопасность", "bachelor", 4, "RU", 1200000, "Защита информации в компьютерных системах и сетях."),
            (f5_cyber, "Automation and Control", "master", 2, "EN", 1500000, "Магистратура по автоматизации производственных процессов."),
            
            # Нефтегаз
            (f5_oil, "Нефтегазовое дело", "bachelor", 4, "RU", 1300000, "Бурение, добыча и транспортировка нефти и газа."),
            (f5_oil, "Геофизика", "bachelor", 4, "RU", 1150000, "Геофизические методы разведки полезных ископаемых."),
            (f5_oil, "Petroleum Engineering", "master", 2, "EN", 1800000, "Международная магистратура по нефтегазовой инженерии."),
            
            # Энергетика и машиностроение
            (f5_energy, "Энергетика", "bachelor", 4, "RU", 1150000, "Электроэнергетические системы и тепловые электростанции."),
            (f5_energy, "Машиностроение", "bachelor", 4, "KZ", 1100000, "Проектирование и производство машин и механизмов."),
            (f5_energy, "Возобновляемая энергетика", "master", 2, "EN", 1600000, "Солнечная, ветровая и другие виды альтернативной энергии."),
        ])

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ Готово! Создано:\n"
            f"   • {University.objects.count()} университетов\n"
            f"   • {Faculty.objects.count()} факультетов\n"
            f"   • {Program.objects.count()} программ\n"
            f"     - Bachelor: {Program.objects.filter(degree='bachelor').count()}\n"
            f"     - Master: {Program.objects.filter(degree='master').count()}\n"
            f"     - PhD: {Program.objects.filter(degree='phd').count()}\n"
        ))

    # Вспомогательная функция для быстрого создания программ
    def create_programs(self, uni, programs_data):
        for faculty, name, degree, duration, lang, fee, description in programs_data:
            Program.objects.create(
                university=uni,
                faculty=faculty,
                name=name,
                degree=degree,
                duration_years=duration,
                language=lang,
                tuition_fee=fee,
                description=description
            )