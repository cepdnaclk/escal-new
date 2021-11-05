import React from 'react';
import { BrowserRouter as Router, Route} from 'react-router-dom';


// import './App.css';
import HomePage from './components/HomePage/HomePage';

function App() {
  return (
      <Router>
        <Route path="/home" component={HomePage}/>
      </Router>
  );
}

export default App;
