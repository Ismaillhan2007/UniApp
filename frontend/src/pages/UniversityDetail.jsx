import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import apiClient from '../services/api'; // Убедитесь, что импорт правильный

export default function UniversityDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [university, setUniversity] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Состояния фильтров
  const [selectedDegree, setSelectedDegree] = useState('all');
  const [selectedLanguage, setSelectedLanguage] = useState('all');
  const [selectedFaculty, setSelectedFaculty] = useState('all');

  useEffect(() => {
    const fetchUniversityData = async () => {
      try {
        setLoading(true);
        // Запрашиваем детали университета (API уже возвращает programs и faculties внутри)
        const response = await apiClient.get(`/universities/${id}/`);
        setUniversity(response.data);
        setLoading(false);
      } catch (err) {
        console.error(err);
        setError('Не удалось загрузить данные университета');
        setLoading(false);
      }
    };

    fetchUniversityData();
  }, [id]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Загрузка данных...</p>
        </div>
      </div>
    );
  }

  if (error || !university) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 text-xl mb-4">{error || "Университет не найден"}</p>
          <button 
            onClick={() => navigate('/')}
            className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            На главную
          </button>
        </div>
      </div>
    );
  }

  // === ИСПРАВЛЕННАЯ ЛОГИКА ФИЛЬТРАЦИИ ===
  const filteredPrograms = university.programs.filter(program => {
    // 1. Фильтр по степени
    if (selectedDegree !== 'all' && program.degree !== selectedDegree) return false;
    
    // 2. Фильтр по языку (используем includes, так как бывает "RU/EN")
    if (selectedLanguage !== 'all' && !program.language.includes(selectedLanguage)) return false;
    
    // 3. Фильтр по факультету (ИСПРАВЛЕНО)
    // program.faculty - это ID (число) из API
    // selectedFaculty - это строка из select
    // Сравниваем их как строки
    if (selectedFaculty !== 'all' && String(program.faculty) !== String(selectedFaculty)) return false;
    
    return true;
  });

  return (
    <div className="min-h-screen bg-gray-50 pb-10">
      {/* Шапка */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <button 
            onClick={() => navigate(-1)}
            className="flex items-center text-gray-600 hover:text-gray-900 mb-4 transition"
          >
            ← Назад
          </button>
          
          <div className="flex flex-col md:flex-row items-start gap-6">
            {university.logo && (
              <img 
                src={university.logo} 
                alt={university.name}
                className="w-24 h-24 object-contain rounded-lg border p-1 bg-white"
              />
            )}
            <div className="flex-1">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">{university.name}</h1>
              <p className="text-gray-600 mb-3">{university.city} • Основан в {university.founded_year}</p>
              <div className="flex flex-wrap gap-3 text-sm">
                <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full font-medium">
                  Рейтинг: #{university.ranking}
                </span>
                <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full font-medium">
                  Студентов: {university.student_count?.toLocaleString()}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* Левая колонка - Инфо */}
          <div className="lg:col-span-1 space-y-6">
            <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
              <h2 className="text-xl font-bold mb-4 text-gray-800">О университете</h2>
              <p className="text-gray-600 leading-relaxed text-sm">{university.description}</p>
            </div>

            <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
              <h2 className="text-xl font-bold mb-4 text-gray-800">Факультеты</h2>
              {university.faculties && university.faculties.length > 0 ? (
                <ul className="space-y-3">
                  {university.faculties.map((faculty) => (
                    <li key={faculty.id} className="text-gray-700 text-sm pl-4 border-l-2 border-blue-500">
                      {faculty.name}
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-gray-400 text-sm">Список факультетов пуст</p>
              )}
            </div>
          </div>

          {/* Правая колонка - Программы */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-gray-900">
                  Программы обучения
                  <span className="ml-2 text-sm font-normal text-gray-500 bg-gray-100 px-2 py-1 rounded-full">
                    {filteredPrograms.length}
                  </span>
                </h2>
              </div>

              {/* Фильтры */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8 p-5 bg-gray-50 rounded-xl border border-gray-200">
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Степень</label>
                  <select 
                    value={selectedDegree}
                    onChange={(e) => setSelectedDegree(e.target.value)}
                    className="w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
                  >
                    <option value="all">Все степени</option>
                    <option value="bachelor">Бакалавриат</option>
                    <option value="master">Магистратура</option>
                    <option value="phd">PhD</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Язык</label>
                  <select 
                    value={selectedLanguage}
                    onChange={(e) => setSelectedLanguage(e.target.value)}
                    className="w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
                  >
                    <option value="all">Любой язык</option>
                    <option value="KZ">Казахский</option>
                    <option value="RU">Русский</option>
                    <option value="EN">Английский</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Факультет</label>
                  <select 
                    value={selectedFaculty}
                    onChange={(e) => setSelectedFaculty(e.target.value)}
                    className="w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
                  >
                    <option value="all">Все факультеты</option>
                    {university.faculties?.map((faculty) => (
                      <option key={faculty.id} value={faculty.id}>
                        {faculty.name}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Список программ */}
              <div className="space-y-4">
                {filteredPrograms.length === 0 ? (
                  <div className="text-center py-12">
                    <span className="text-4xl">🔍</span>
                    <p className="text-gray-500 mt-2 font-medium">Программы не найдены</p>
                    <p className="text-gray-400 text-sm">Попробуйте изменить параметры фильтрации</p>
                  </div>
                ) : (
                  filteredPrograms.map((program) => (
                    <div key={program.id} className="group border border-gray-200 rounded-xl p-5 hover:border-blue-400 hover:shadow-md transition cursor-pointer bg-white">
                      <div className="flex justify-between items-start mb-2">
                        <div>
                          <h3 className="text-lg font-bold text-gray-900 group-hover:text-blue-600 transition">
                            {program.name}
                          </h3>
                          <p className="text-sm text-gray-500 mt-1">
                            {program.faculty_name}
                          </p>
                        </div>
                        <div className="text-right">
                          <div className="text-lg font-bold text-blue-600 whitespace-nowrap">
                            {program.tuition_fee === 0 ? 'Грант' : `${program.tuition_fee.toLocaleString()} ₸`}
                          </div>
                          <div className="text-xs text-gray-400">в год</div>
                        </div>
                      </div>

                      <div className="flex flex-wrap gap-2 mt-4 pt-3 border-t border-gray-100">
                        <span className={`px-2.5 py-0.5 text-xs font-medium rounded-full ${
                          program.degree === 'bachelor' ? 'bg-purple-50 text-purple-700' : 
                          program.degree === 'master' ? 'bg-indigo-50 text-indigo-700' : 'bg-gray-100 text-gray-700'
                        }`}>
                          {program.degree === 'bachelor' ? 'Бакалавриат' : 
                           program.degree === 'master' ? 'Магистратура' : 'PhD'}
                        </span>
                        
                        <span className="px-2.5 py-0.5 text-xs font-medium bg-blue-50 text-blue-700 rounded-full">
                          {program.duration_years} {program.duration_years === 1 ? 'год' : 'года'}
                        </span>
                        
                        <span className="px-2.5 py-0.5 text-xs font-medium bg-emerald-50 text-emerald-700 rounded-full flex items-center gap-1">
                          {program.language.includes('EN') ? '🇬🇧' : program.language.includes('KZ') ? '🇰🇿' : '🇷🇺'} 
                          {program.language}
                        </span>
                      </div>
                    </div>
                  ))
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}