import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const Navbar = () => {
  const { isAuthenticated, isAdmin, logout } = useAuth();

  return (
    <nav className="bg-white shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center py-4">
          <Link to="/" className="text-xl font-bold text-gray-800">
            Portfolio
          </Link>
          <div className="flex space-x-4">
            <Link to="/" className="text-gray-600 hover:text-gray-800">Home</Link>
            <Link to="/projects" className="text-gray-600 hover:text-gray-800">Projects</Link>
            {isAuthenticated && (
              <Link to="/blogs" className="text-gray-600 hover:text-gray-800">Blogs</Link>
            )}
            <Link to="/contact" className="text-gray-600 hover:text-gray-800">Contact</Link>
            {isAdmin && (
              <Link to="/admin" className="text-gray-600 hover:text-gray-800">Admin</Link>
            )}
            {isAuthenticated ? (
              <button onClick={logout} className="text-gray-600 hover:text-gray-800">
                Logout
              </button>
            ) : (
              <>
                <Link to="/login" className="text-gray-600 hover:text-gray-800">Login</Link>
                <Link to="/register" className="text-gray-600 hover:text-gray-800">Register</Link>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;