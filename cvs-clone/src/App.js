import React from 'react';
import Form from './form.js';
import Success from './Success.js';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
    <Router>
      <Switch>
        <Route path="/success">
          <Success />
        </Route>
        <Route path="/">
          <Form/>
        </Route>
      </Switch>
    </Router>
    </div>
  );
}

export default App;
