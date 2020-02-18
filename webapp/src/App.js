import React from "react";
import logo from "./logo.svg";
import "./App.css";
import Login from "./Login";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Inital development stage.</p>
        <a
          className="App-link"
          href="https://github.com/magsouza/Weltfy"
          target="_blank"
          rel="noopener noreferrer"
        >
          Source code
        </a>
        <Login />
      </header>
    </div>
  );
}

export default App;
