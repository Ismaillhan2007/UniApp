import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const [universities, setUniversities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  // --- compare state ---
  const [compareA, setCompareA] = useState('');
  const [compareB, setCompareB] = useState('');
  const [compareResult, setCompareResult] = useState(null);
  const [compareLoading, setCompareLoading] = useState(false);
  const [compareError, setCompareError] = useState(null);

  useEffect(() => {
    const fetchUniversities = async () => {
      try {
        setLoading(true);
        const response = await fetch('http://127.0.0.1:8000/api/universities/');
        if (!response.ok) throw new Error('Failed to fetch universities');
        const data = await response.json();
        setUniversities(data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchUniversities();
  }, []);

  const handleViewDetails = (universityId) => {
    navigate(`/universities/${universityId}`);
  };

  const handleCompare = async () => {
    if (!compareA || !compareB) {
      setCompareError('Выберите два университета');
      return;
    }
    if (compareA === compareB) {
      setCompareError('Выберите два разных университета');
      return;
    }

    setCompareError(null);
    setCompareLoading(true);
    setCompareResult(null);

    try {
      const resp = await fetch('http://127.0.0.1:8000/api/compare/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          ids: [Number(compareA), Number(compareB)],
        }),
      });

      if (!resp.ok) {
        const text = await resp.text();
        throw new Error(text || 'Compare request failed');
      }

      const data = await resp.json(); // массив из 2 универов
      setCompareResult(data);
    } catch (e) {
      setCompareError(e.message || 'Ошибка сравнения');
    } finally {
      setCompareLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-20 w-20 border-4 border-blue-600 border-t-transparent mx-auto"></div>
          <p className="mt-6 text-gray-700 text-xl font-semibold">Загрузка университетов...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-red-50 to-orange-100 flex items-center justify-center">
        <div className="text-center p-8 bg-white rounded-2xl shadow-xl max-w-md">
          <div className="text-red-500 text-7xl mb-6">⚠️</div>
          <h2 className="text-2xl font-bold text-gray-900 mb-3">Ошибка загрузки</h2>
          <p className="text-red-600 text-lg mb-4">{error}</p>
          <p className="text-gray-600 mb-6">
            Убедитесь, что Django сервер запущен на<br />
            <code className="bg-gray-100 px-2 py-1 rounded">http://127.0.0.1:8000</code>
          </p>
          <button
            onClick={() => window.location.reload()}
            className="px-6 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 font-medium transition-colors"
          >
            🔄 Попробовать снова
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
      {/* Hero Section */}
      <div className="relative min-h-screen flex flex-col items-center justify-center px-4 py-20">
        {/* Decorative circles */}
        <div className="absolute top-20 left-10 w-72 h-72 bg-blue-200 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob"></div>
        <div className="absolute top-40 right-10 w-72 h-72 bg-purple-200 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob animation-delay-2000"></div>
        <div className="absolute bottom-20 left-1/2 w-72 h-72 bg-pink-200 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob animation-delay-4000"></div>

        <div className="relative z-10 text-center max-w-5xl mx-auto">
          {/* Main Title */}
          <h1 className="text-6xl md:text-7xl lg:text-8xl font-black text-gray-900 mb-8 leading-tight">
            DataHub
            <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600">
              Вузов Казахстана
            </span>
          </h1>

          {/* Subtitle */}
          <p className="text-xl md:text-2xl text-gray-600 mb-12 font-medium">
            Выбери свой университет
          </p>

          {/* Stats */}
          <div className="flex flex-wrap justify-center gap-6 mb-16">
            <div className="bg-white/80 backdrop-blur-sm rounded-2xl px-8 py-4 shadow-lg border border-gray-200">
              <div className="text-4xl font-bold text-blue-600">{universities.length}</div>
              <div className="text-sm text-gray-600 font-medium">университетов</div>
            </div>
            <div className="bg-white/80 backdrop-blur-sm rounded-2xl px-8 py-4 shadow-lg border border-gray-200">
              <div className="text-4xl font-bold text-indigo-600">10</div>
              <div className="text-sm text-gray-600 font-medium">факультетов</div>
            </div>
            <div className="bg-white/80 backdrop-blur-sm rounded-2xl px-8 py-4 shadow-lg border border-gray-200">
              <div className="text-4xl font-bold text-purple-600">50+</div>
              <div className="text-sm text-gray-600 font-medium">программ</div>
            </div>
          </div>

          {/* Scroll Indicator */}
          <div className="animate-bounce">
            <svg className="w-8 h-8 mx-auto text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
            </svg>
          </div>
        </div>
      </div>

      {/* Universities Grid */}
      <div className="relative py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              Топ университеты
            </h2>
            <p className="text-lg text-gray-600">
              Выберите университет для подробной информации
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {universities.map((university) => (
              <div
                key={university.id}
                className="group relative bg-white rounded-3xl shadow-xl hover:shadow-2xl transition-all duration-300 overflow-hidden border-2 border-gray-100 hover:border-blue-300 transform hover:-translate-y-2"
              >
                {/* Background Logo (Transparent) */}
                {university.logo && (
                  <div
                    className="absolute inset-0 opacity-5 group-hover:opacity-10 transition-opacity duration-300"
                    style={{
                      backgroundImage: `url(${university.logo})`,
                      backgroundSize: 'cover',
                      backgroundPosition: 'center',
                      backgroundRepeat: 'no-repeat',
                    }}
                  />
                )}

                {/* Content */}
                <div className="relative p-8">
                  {/* Logo */}
                  <div className="flex justify-center mb-6">
                    <div className="w-28 h-28 bg-white rounded-2xl shadow-lg p-4 border-2 border-gray-100 group-hover:border-blue-300 transition-colors">
                      {university.logo ? (
                        <img
                          src={university.logo}
                          alt={university.name}
                          className="w-full h-full object-contain"
                        />
                      ) : (
                        <div className="w-full h-full flex items-center justify-center text-4xl">
                          🎓
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Ranking Badge */}
                  <div className="absolute top-6 right-6">
                    <div className="bg-gradient-to-r from-yellow-400 to-orange-500 text-white px-4 py-2 rounded-full text-sm font-bold shadow-lg">
                      #{university.ranking}
                    </div>
                  </div>

                  {/* University Name */}
                  <h3 className="text-2xl font-bold text-gray-900 mb-4 text-center min-h-[4rem] flex items-center justify-center">
                    {university.name}
                  </h3>

                  {/* Info */}
                  <div className="space-y-3 mb-6">
                    <div className="flex items-center justify-center gap-2 text-gray-600">
                      <span className="text-xl">📍</span>
                      <span className="font-medium">{university.city}</span>
                    </div>
                    <div className="flex items-center justify-center gap-2 text-gray-600">
                      <span className="text-xl">👥</span>
                      <span className="font-medium">
                        {university.student_count?.toLocaleString()} студентов
                      </span>
                    </div>
                  </div>

                  {/* Description */}
                  <p className="text-gray-600 text-sm text-center mb-6 line-clamp-3 leading-relaxed">
                    {university.description}
                  </p>

                  {/* Stats */}
                  <div className="flex gap-2 mb-6 flex-wrap justify-center">
                    <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-semibold">
                      🎓 15 факультетов
                    </span>
                    <span className="px-3 py-1 bg-purple-100 text-purple-700 rounded-full text-xs font-semibold">
                      📚 15+ программ
                    </span>
                  </div>

                  {/* Button */}
                  <button
                    onClick={() => handleViewDetails(university.id)}
                    className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-bold py-4 rounded-xl transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105 flex items-center justify-center gap-2"
                  >
                    <span>Подробнее</span>
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                    </svg>
                  </button>
                </div>
              </div>
            ))}
          </div>

          {/* Блок сравнения */}
          <div className="mt-20 relative">
            <div className="pointer-events-none absolute -top-10 -left-6 w-40 h-40 bg-blue-200/40 rounded-full blur-3xl" />
            <div className="pointer-events-none absolute -bottom-16 -right-8 w-52 h-52 bg-purple-200/40 rounded-full blur-3xl" />

            <div className="relative bg-white/80 backdrop-blur-sm rounded-3xl shadow-2xl border border-indigo-100/70 px-6 py-8 md:px-10 md:py-10 overflow-hidden">
              <div className="absolute inset-x-0 top-0 h-1 bg-gradient-to-r from-blue-500 via-indigo-500 to-purple-500" />

              <div className="relative z-10">
                <h3 className="text-2xl md:text-3xl font-bold text-gray-900 mb-3 text-center">
                  Сравнить университеты
                </h3>
                <p className="text-gray-600 text-center mb-8 max-w-2xl mx-auto">
                  Выберите два университета и нажмите{' '}
                  <span className="font-semibold text-blue-600">Compare</span>,
                  чтобы увидеть сравнение по ключевым параметрам.
                </p>

                <div className="flex flex-col md:flex-row gap-6 mb-6 justify-center items-stretch">
                  <div className="w-full md:w-1/3">
                    <div className="bg-gray-50/80 rounded-2xl border border-gray-200/80 hover:border-blue-300 hover:bg-white transition-all shadow-sm hover:shadow-md p-4 md:p-5 h-full">
                      <label className="flex items-center gap-2 text-sm font-semibold text-gray-700 mb-2">
                        <span className="flex h-6 w-6 items-center justify-center rounded-full bg-blue-100 text-xs text-blue-700 font-bold">
                          1
                        </span>
                        <span>Университет 1</span>
                      </label>
                      <p className="text-xs text-gray-500 mb-3">
                        Основной вариант, который вы рассматриваете.
                      </p>
                      <select
                        value={compareA}
                        onChange={(e) => setCompareA(e.target.value)}
                        className="w-full px-3 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-sm"
                      >
                        <option value="">— Выберите университет —</option>
                        {universities.map((u) => (
                          <option key={u.id} value={u.id}>
                            {u.name}
                          </option>
                        ))}
                      </select>
                    </div>
                  </div>

                  <div className="w-full md:w-1/3">
                    <div className="bg-gray-50/80 rounded-2xl border border-gray-200/80 hover:border-indigo-400 hover:bg-white transition-all shadow-sm hover:shadow-md p-4 md:p-5 h-full">
                      <label className="flex items-center gap-2 text-sm font-semibold text-gray-700 mb-2">
                        <span className="flex h-6 w-6 items-center justify-center rounded-full bg-purple-100 text-xs text-purple-700 font-bold">
                          2
                        </span>
                        <span>Университет 2</span>
                      </label>
                      <p className="text-xs text-gray-500 mb-3">
                        Альтернатива для сравнения с первым вариантом.
                      </p>
                      <select
                        value={compareB}
                        onChange={(e) => setCompareB(e.target.value)}
                        className="w-full px-3 py-2.5 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white text-sm"
                      >
                        <option value="">— Выберите университет —</option>
                        {universities.map((u) => (
                          <option key={u.id} value={u.id}>
                            {u.name}
                          </option>
                        ))}
                      </select>
                    </div>
                  </div>
                </div>

                {compareError && (
                  <p className="text-center text-red-600 mb-4 text-sm">{compareError}</p>
                )}

                <div className="flex justify-center mb-2">
                  <button
                    onClick={handleCompare}
                    disabled={compareLoading}
                    className="px-8 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl shadow-md hover:shadow-lg disabled:opacity-60 disabled:cursor-not-allowed flex items-center gap-2 transition-all hover:scale-[1.02]"
                  >
                    {compareLoading ? 'Сравниваем...' : 'Compare'}
                    {!compareLoading && (
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                      </svg>
                    )}
                  </button>
                </div>

                {/* Результат сравнения */}
                {compareResult && Array.isArray(compareResult) && compareResult.length > 0 && (
                  <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
                    {compareResult.map((uni) => (
                      <div
                        key={uni.id}
                        className="border border-indigo-100 rounded-2xl p-6 bg-white/90 shadow-sm hover:shadow-xl transition-all"
                      >
                        <div className="flex items-center gap-3 mb-4">
                          {uni.logo && (
                            <img
                              src={uni.logo}
                              alt={uni.name}
                              className="w-12 h-12 object-contain rounded-lg bg-white border"
                            />
                          )}
                          <div>
                            <h4 className="text-lg font-bold text-gray-900">{uni.name}</h4>
                            <p className="text-sm text-gray-600">{uni.city}</p>
                          </div>
                          <div className="ml-auto">
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-yellow-400 to-orange-500 text-white shadow">
                              #{uni.ranking} в рейтинге
                            </span>
                          </div>
                        </div>

                        <div className="grid grid-cols-2 gap-4 text-sm mb-4">
                          <div className="bg-gray-50 rounded-xl p-3">
                            <div className="text-gray-500 text-xs">Рейтинг</div>
                            <div className="font-semibold text-gray-900 text-lg">
                              #{uni.ranking}
                            </div>
                          </div>
                          <div className="bg-gray-50 rounded-xl p-3">
                            <div className="text-gray-500 text-xs">Студентов</div>
                            <div className="font-semibold text-gray-900">
                              {uni.student_count?.toLocaleString()}
                            </div>
                          </div>
                        </div>

                        <div className="mb-4">
                          <div className="text-gray-500 text-xs mb-1">Сайт</div>
                          <a
                            href={uni.website}
                            className="text-blue-600 hover:underline break-all text-sm font-medium"
                          >
                            {uni.website}
                          </a>
                        </div>

                        {Array.isArray(uni.programs) && (
                          <div className="mt-2 pt-3 border-t border-gray-100">
                            <div className="flex items-center justify-between text-sm mb-1">
                              <span className="text-gray-500 text-xs">Количество программ</span>
                              <span className="font-semibold text-gray-900">
                                {uni.programs.length}
                              </span>
                            </div>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="relative py-12 px-4 border-t border-gray-200 bg-white/50 backdrop-blur-sm mt-12">
        <div className="max-w-7xl mx-auto text-center">
          <p className="text-gray-600 mb-2">
            <span className="font-bold text-gray-900">DataHub Вузов Казахстана</span>
          </p>
          <p className="text-sm text-gray-500">
            Полная информация о программах обучения в ведущих университетах Казахстана
          </p>
        </div>
      </footer>

      {/* Custom Animations */}
      <style jsx>{`
        @keyframes blob {
          0% { transform: translate(0px, 0px) scale(1); }
          33% { transform: translate(30px, -50px) scale(1.1); }
          66% { transform: translate(-20px, 20px) scale(0.9); }
          100% { transform: translate(0px, 0px) scale(1); }
        }
        .animate-blob {
          animation: blob 7s infinite;
        }
        .animation-delay-2000 {
          animation-delay: 2s;
        }
        .animation-delay-4000 {
          animation-delay: 4s;
        }
        .line-clamp-3 {
          display: -webkit-box;
          -webkit-line-clamp: 3;
          -webkit-box-orient: vertical;
          overflow: hidden;
        }
      `}</style>
    </div>
  );
}
