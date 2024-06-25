import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './components/About';
import DrawCard from './components/DrawCard';
import FortuneHistory from './components/FortuneHistory';
import Login from './components/Login';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" component={About} />
        <Route path="/draw_card" component={DrawCard} />
        <Route path="/fortune_history" component={FortuneHistory} />
        <Route path="/login" component={Login} />
      </Switch>
    </Router>
  );
};

export default App;
