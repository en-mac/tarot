import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './components/About';
import DrawCard from './components/DrawCard';
import FortuneHistory from './components/FortuneHistory';
import Login from './components/Login';
import './App.css';

function App() {
  console.log('App component rendered');
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/draw_card" element={<DrawCard />} />
        <Route path="/fortune_history" element={<FortuneHistory />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </>
  );
}

export default App;
