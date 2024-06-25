import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

const Navbar = () => {
  const { isAuthenticated, logout } = useContext(AuthContext);

  return (
    <nav className="p-4 bg-gray-800 text-white">
      <ul className="flex space-x-4">
        {isAuthenticated ? (
          <>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/draw_card">Draw Card</Link></li>
            <li><Link to="/fortune_history">Fortune History</Link></li>
            <li><Link to="/about">About</Link></li>
            <li><button onClick={logout}>Logout</button></li>
          </>
        ) : (
          <li><Link to="/login">Login</Link></li>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
