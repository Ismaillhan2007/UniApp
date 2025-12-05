import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Universities from './pages/Universities';
import UniversityDetail from './pages/UniversityDetail';
function App() {
    return (
        <BrowserRouter>
            <div className="min-h-screen bg-gray-100">
                <Navbar />
                <Routes>
                    <Route path="/" element={<Home />} />
                      <Route path="/universities" element={<Universities />} />
                      <Route path="/universities/:id" element={<UniversityDetail />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;