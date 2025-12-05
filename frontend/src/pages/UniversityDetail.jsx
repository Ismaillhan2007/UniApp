import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import apiClient from '../services/api';

export default function UniversityDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [university, setUniversity] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // States for filters
  const [selectedDegree, setSelectedDegree] = useState('all');
  const [selectedLanguage, setSelectedLanguage] = useState('all');
  const [selectedFaculty, setSelectedFaculty] = useState('all');

  useEffect(() => {
    const fetchUniversityData = async () => {
      try {
        setLoading(true);
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

  if (loading) return <div className="min-h-screen flex items-center justify-center">Загрузка...</div>;
  if (error || !university) return <div className="min-h-screen flex items-center justify-center text-red-600">{error}</div>;

  // Filter Logic
  const filteredPrograms = university.programs.filter(program => {
    if (selectedDegree !== 'all' && program.degree !== selectedDegree) return false;
    if (selectedLanguage !== 'all' && !program.language.includes(selectedLanguage)) return false;
    if (selectedFaculty !== 'all' && String(program.faculty) !== String(selectedFaculty)) return false;
    return true;
  });

  return (
    <div className="min-h-screen bg-gray-50 pb-10">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <button onClick={() => navigate(-1)} className="text-gray-600 hover:text-gray-900 mb-4">← Назад</button>
          <div className="flex flex-col md:flex-row items-start gap-6">
            {university.logo && <img src={university.logo} alt={university.name} className="w-24 h-24 object-contain rounded-lg border p-1 bg-white" />}
            <div className="flex-1">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">{university.name}</h1>
              <p className="text-gray-600 mb-3">{university.city} • Основан в {university.founded_year}</p>
              <div className="flex gap-3">
                <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">Рейтинг: #{university.ranking}</span>
                <span className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm">Студентов: {university.student_count}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* LEFT COLUMN */}
          <div className="lg:col-span-1 space-y-6">
            {/* Info */}
            <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
              <h2 className="text-xl font-bold mb-4">О университете</h2>
              <p className="text-gray-600 text-sm leading-relaxed">{university.description}</p>
            </div>

            {/* Contact Info (Fixed) */}
            <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
              <h2 className="text-xl font-bold mb-4">Контакты</h2>
              <ul className="space-y-3 text-sm text-gray-600">
                <li className="flex items-start gap-2">
                    <span>📍</span> {university.address || "Адрес не указан"}
                </li>
                <li className="flex items-center gap-2">
                    <span>📞</span> {university.phone || "Нет телефона"}
                </li>
                <li className="flex items-center gap-2">
                    <span>✉️</span> 
                    <a href={`mailto:${university.email}`} className="text-blue-600 hover:underline">
                        {university.email || "Нет email"}
                    </a>
                </li>
                <li className="flex items-center gap-2">
                    <span>🌐</span> 
                    <a href={university.website} target="_blank" rel="noreferrer" className="text-blue-600 hover:underline">
                        Перейти на сайт
                    </a>
                </li>
              </ul>
            </div>

            {/* Admissions Section (New) */}
            {university.admissions && university.admissions.length > 0 && (
                <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
                    <h2 className="text-xl font-bold mb-4">Поступление</h2>
                    {university.admissions.map((adm) => (
                        <div key={adm.id} className="text-sm space-y-3">
                            <div><span className="font-semibold">Экзамены:</span> {adm.exams}</div>
                            <div><span className="font-semibold">Мин. балл:</span> {adm.min_score}</div>
                            <div><span className="font-semibold">Дедлайн:</span> <span className="text-red-500">{adm.deadline}</span></div>
                            <div className="text-xs bg-yellow-50 p-2 rounded border border-yellow-100 mt-2">
                                💡 {adm.scholarships}
                            </div>
                        </div>
                    ))}
                </div>
            )}
          </div>

          {/* RIGHT COLUMN */}
          <div className="lg:col-span-2 space-y-6">
             
             {/* International Cooperation (New) */}
             {university.international_programs && university.international_programs.length > 0 && (
                <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
                    <h2 className="text-xl font-bold mb-4">Международное сотрудничество</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {university.international_programs.map((prog) => (
                            <div key={prog.id} className="border rounded-lg p-4 bg-gray-50">
                                <div className="flex justify-between items-start mb-2">
                                    <h4 className="font-bold text-gray-800">{prog.partner_name}</h4>
                                    <span className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded-full">{prog.country}</span>
                                </div>
                                <p className="text-sm text-blue-600 font-medium mb-1">{prog.program_name}</p>
                                <p className="text-xs text-gray-500">{prog.description}</p>
                                <div className="mt-2 text-xs text-gray-400">Тип: {prog.type} • Язык: {prog.language}</div>
                            </div>
                        ))}
                    </div>
                </div>
             )}

             {/* Programs Section */}
            <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
              <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-bold">Программы ({filteredPrograms.length})</h2>
              </div>
              
              {/* Filters */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6 p-4 bg-gray-50 rounded-lg">
                 <select className="p-2 border rounded" value={selectedDegree} onChange={e => setSelectedDegree(e.target.value)}>
                    <option value="all">Все степени</option>
                    <option value="bachelor">Бакалавриат</option>
                    <option value="master">Магистратура</option>
                    <option value="phd">PhD</option>
                 </select>
                 <select className="p-2 border rounded" value={selectedLanguage} onChange={e => setSelectedLanguage(e.target.value)}>
                    <option value="all">Любой язык</option>
                    <option value="KZ">Казахский</option>
                    <option value="RU">Русский</option>
                    <option value="EN">Английский</option>
                 </select>
                 <select className="p-2 border rounded" value={selectedFaculty} onChange={e => setSelectedFaculty(e.target.value)}>
                    <option value="all">Все факультеты</option>
                    {university.faculties?.map(f => <option key={f.id} value={f.id}>{f.name}</option>)}
                 </select>
              </div>

              {/* List */}
              <div className="space-y-4">
                {filteredPrograms.map(program => (
                  <div key={program.id} className="border rounded-lg p-4 hover:border-blue-500 transition cursor-pointer">
                    <div className="flex justify-between">
                        <div>
                            <h3 className="font-bold text-lg">{program.name}</h3>
                            <p className="text-sm text-gray-500">{program.faculty_name}</p>
                        </div>
                        <div className="text-right">
                            <div className="text-lg font-bold text-blue-600">{program.tuition_fee ? `${program.tuition_fee} ₸` : "Грант"}</div>
                            <div className="text-xs text-gray-400">в год</div>
                        </div>
                    </div>
                    <div className="flex gap-2 mt-3">
                        <span className="bg-purple-100 text-purple-700 px-2 py-1 rounded text-xs">{program.degree}</span>
                        <span className="bg-blue-100 text-blue-700 px-2 py-1 rounded text-xs">{program.duration_years} года</span>
                        <span className="bg-green-100 text-green-700 px-2 py-1 rounded text-xs">{program.language}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}