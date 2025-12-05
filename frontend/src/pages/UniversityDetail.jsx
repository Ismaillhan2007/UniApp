import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

export default function UniversityDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [university, setUniversity] = useState(null);
  const [programs, setPrograms] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Filters
  const [selectedDegree, setSelectedDegree] = useState('all');
  const [selectedLanguage, setSelectedLanguage] = useState('all');
  const [selectedFaculty, setSelectedFaculty] = useState('all');

  useEffect(() => {
    const fetchUniversityData = async () => {
      try {
        setLoading(true);
        
        // Fetch university details
        const uniResponse = await fetch(`http://127.0.0.1:8000/api/universities/${id}/`);
        if (!uniResponse.ok) throw new Error('University not found');
        const uniData = await uniResponse.json();
        setUniversity(uniData);
        
        // Fetch programs
        const programsResponse = await fetch(`http://127.0.0.1:8000/api/universities/${id}/programs/`);
        if (!programsResponse.ok) throw new Error('Failed to fetch programs');
        const programsData = await programsResponse.json();
        setPrograms(programsData);
        
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchUniversityData();
  }, [id]);

  // Filter programs
  const filteredPrograms = programs.filter(program => {
    if (selectedDegree !== 'all' && program.degree !== selectedDegree) return false;
    if (selectedLanguage !== 'all' && program.language !== selectedLanguage) return false;
    if (selectedFaculty !== 'all' && program.faculty?.id !== parseInt(selectedFaculty)) return false;
    return true;
  });

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

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600 text-xl mb-4">Ошибка: {error}</p>
          <button 
            onClick={() => navigate('/')}
            className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Вернуться назад
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <button 
            onClick={() => navigate(-1)}
            className="flex items-center text-gray-600 hover:text-gray-900 mb-4"
          >
            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
            </svg>
            Назад
          </button>
          
          <div className="flex items-start gap-6">
            {university.logo && (
              <img 
                src={university.logo} 
                alt={university.name}
                className="w-24 h-24 object-contain rounded-lg border"
              />
            )}
            <div className="flex-1">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">{university.name}</h1>
              <p className="text-gray-600 mb-3">{university.city} • Основан в {university.founded_year}</p>
              <div className="flex gap-3 text-sm">
                <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full">
                  Рейтинг: #{university.ranking}
                </span>
                <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full">
                  {university.student_count?.toLocaleString()} студентов
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Left column - Info */}
          <div className="lg:col-span-1 space-y-6">
            {/* About */}
            <div className="bg-white rounded-lg shadow-sm p-6">
              <h2 className="text-xl font-semibold mb-4">О университете</h2>
              <p className="text-gray-700 leading-relaxed">{university.description}</p>
            </div>

            {/* Contact Info */}
            <div className="bg-white rounded-lg shadow-sm p-6">
              <h2 className="text-xl font-semibold mb-4">Контактная информация</h2>
              <div className="space-y-3 text-sm">
                <div className="flex items-start gap-3">
                  <svg className="w-5 h-5 text-gray-400 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                  <span className="text-gray-700">{university.address}</span>
                </div>
                <div className="flex items-center gap-3">
                  <svg className="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                  <span className="text-gray-700">{university.phone}</span>
                </div>
                <div className="flex items-center gap-3">
                  <svg className="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                  <a href={`mailto:${university.email}`} className="text-blue-600 hover:underline">
                    {university.email}
                  </a>
                </div>
                {university.website && (
                  <div className="flex items-center gap-3">
                    <svg className="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
                    </svg>
                    <a href={university.website} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                      Веб-сайт
                    </a>
                  </div>
                )}
              </div>
            </div>

            {/* Faculties */}
            {university.faculties && university.faculties.length > 0 && (
              <div className="bg-white rounded-lg shadow-sm p-6">
                <h2 className="text-xl font-semibold mb-4">Факультеты</h2>
                <ul className="space-y-2">
                  {university.faculties.map((faculty) => (
                    <li key={faculty.id} className="text-gray-700 pl-4 border-l-2 border-blue-500">
                      {faculty.name}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          {/* Right column - Programs */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-lg shadow-sm p-6">
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-semibold">
                  Программы обучения
                  <span className="ml-2 text-sm font-normal text-gray-500">
                    ({filteredPrograms.length})
                  </span>
                </h2>
              </div>

              {/* Filters */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6 p-4 bg-gray-50 rounded-lg">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Степень</label>
                  <select 
                    value={selectedDegree}
                    onChange={(e) => setSelectedDegree(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="all">Все</option>
                    <option value="bachelor">Бакалавриат</option>
                    <option value="master">Магистратура</option>
                    <option value="phd">PhD</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Язык обучения</label>
                  <select 
                    value={selectedLanguage}
                    onChange={(e) => setSelectedLanguage(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="all">Все</option>
                    <option value="KZ">Казахский</option>
                    <option value="RU">Русский</option>
                    <option value="EN">Английский</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Факультет</label>
                  <select 
                    value={selectedFaculty}
                    onChange={(e) => setSelectedFaculty(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="all">Все</option>
                    {university.faculties?.map((faculty) => (
                      <option key={faculty.id} value={faculty.id}>
                        {faculty.name}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Programs List */}
              <div className="space-y-4">
                {filteredPrograms.length === 0 ? (
                  <p className="text-center text-gray-500 py-8">Программы не найдены</p>
                ) : (
                  filteredPrograms.map((program) => (
                    <div key={program.id} className="border border-gray-200 rounded-lg p-5 hover:shadow-md transition-shadow">
                      <div className="flex justify-between items-start mb-3">
                        <div className="flex-1">
                          <h3 className="text-lg font-semibold text-gray-900 mb-1">
                            {program.name}
                          </h3>
                          {program.faculty && (
                            <p className="text-sm text-gray-600">{program.faculty.name}</p>
                          )}
                        </div>
                        <div className="text-right">
                          <div className="text-xl font-bold text-blue-600">
                            {program.tuition_fee?.toLocaleString()} ₸
                          </div>
                          <div className="text-xs text-gray-500">в год</div>
                        </div>
                      </div>

                      {program.description && (
                        <p className="text-sm text-gray-700 mb-3 line-clamp-2">
                          {program.description}
                        </p>
                      )}

                      <div className="flex flex-wrap gap-2">
                        <span className="px-3 py-1 text-xs bg-purple-100 text-purple-700 rounded-full">
                          {program.degree === 'bachelor' ? 'Бакалавриат' : 
                           program.degree === 'master' ? 'Магистратура' : 'PhD'}
                        </span>
                        <span className="px-3 py-1 text-xs bg-blue-100 text-blue-700 rounded-full">
                          {program.duration_years} {program.duration_years === 1 ? 'год' : 'года'}
                        </span>
                        <span className="px-3 py-1 text-xs bg-green-100 text-green-700 rounded-full">
                          {program.language === 'KZ' ? '🇰🇿 Казахский' : 
                           program.language === 'RU' ? '🇷🇺 Русский' : '🇬🇧 Английский'}
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