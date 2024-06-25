import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  console.log('Navbar component rendered');
  return (
    <nav className="bg-gray-800 p-4">
      <ul className="flex space-x-4">
        <li>
          <Link to="/" className="text-white">Home</Link>
        </li>
        <li>
          <Link to="/draw_card" className="text-white">Draw Card</Link>
        </li>
        <li>
          <Link to="/fortune_history" className="text-white">Fortune History</Link>
        </li>
        <li>
          <Link to="/about" className="text-white">About</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
