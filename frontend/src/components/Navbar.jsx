import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="bg-blue-600 p-4">
            <div className="flex gap-6">
                <Link to="/" className="text-white font-bold">Главная</Link>
                <Link to="/universities" className="text-white font-bold">Университеты</Link>
            </div>
        </nav>
    );
}

export default Navbar;