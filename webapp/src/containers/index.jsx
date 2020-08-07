import React, { Component } from "react";
import logo from "../logo.svg";
import "./App.css";
import Login from "./Login";

class App extends Component {
  
  render () {
    const desc = "Weltfy is an app where you can find the most played songs from a selected country by local artists only. Log in Spotify in the button bellow, choose one country and then enjoy the trending local songs from there! :)"
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="title">Weltfy</h1>
          <div className="description">{desc}</div>
          <Login />
          <p>Inital development stage.</p>
          <a
            className="App-link"
            href="https://github.com/magsouza/Weltfy"
            target="_blank"
            rel="noopener noreferrer"
          >
            Source code
          </a>
        </header>
      </div>
    );
  }
}

export default App;
