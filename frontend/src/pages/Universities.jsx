import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import apiClient from '../services/api';

function Universities() {
    const [universities, setUniversities] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        apiClient.get('/universities/')
            .then(response => {
                setUniversities(response.data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error:', error);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <p className="p-8">Loading...</p>;
    }

    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-6">Университеты Казахстана</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {universities.map(uni => (
                    <Link to={`/universities/${uni.id}`} key={uni.id}>
                        <div className="bg-white p-6 rounded-lg shadow hover:shadow-lg transition">
                            <h2 className="text-xl font-semibold">{uni.name}</h2>
                            <p className="text-gray-600">{uni.city}</p>
                            <p className="text-sm text-gray-500">Рейтинг: {uni.ranking}</p>
                            <p className="text-sm text-gray-500">Студентов: {uni.student_count}</p>
                        </div>
                    </Link>
                ))}
            </div>
        </div>
    );
}

export default Universities;