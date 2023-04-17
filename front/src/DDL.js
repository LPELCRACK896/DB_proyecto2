import './App.css';
import { Link, useParams } from "react-router-dom";
import React, { useState } from "react";
import axios from "axios";

function DDL() {

  const [selectedButton, setSelectedButton] = useState("");
  const [inputValue, setInputValue] = useState("");
  const apiUrl = "http://127.0.0.1:5000/";
  const [responseMessage, setResponseMessage] = useState("");
  const  command_message = {
    "create": "create params",
    "list": "list params",
    "disable": "disable params",
    "enable": "enable paramas",
    "is_enable": "is_enable params",
    "alter": "alter params",
    "drop": "drop params",
    "dropall": "dropall params",
    "describe": "describe params",
  };
  const selectCommand = (buttonText) => {
    setSelectedButton(command_message[buttonText]);
  };

  const runCommand = async () => {
    if (!selectedButton) {
      console.error("No command selected");
      return;
    }

    const command = Object.keys(command_message).find(key => command_message[key] === selectedButton);
    try {
      const response = await axios.post(`${apiUrl}${command}`, { query: inputValue });
      setResponseMessage(JSON.stringify(response.data));
    } catch (error) {
      console.error("Error making API request:", error);
      setResponseMessage("Error making API request");
    }
  };

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };
  return (
    // NAVBAR A LA IZQUIERDA
    <div className="App">
      <header className="App-header">
        <p className='CR'>HBASE by RS_LP_JG</p>
      </header>

      <div className="container m-0">
      <div className="nav-bar">
        <ul>
        <button className='DDL'>
          DDL
        </button>
        <Link to='/DML'>
        <button className='botonp'>
        DML
        </button>
        </Link>
        <button className='botonp'>
          Extra
        </button>
        </ul>
      </div>


    {/* CONTENIDOOOO */}
      <div className='contenido'>
        <h1 className='titulo'>DDL</h1>
      <button className='pagDDL'onClick={() => selectCommand("create")}>
        create
      </button>
      <button className='pagDDL'onClick={() => selectCommand("list")}>
        list
      </button>
      <button className='pagDDL'onClick={() => selectCommand("disable")}>
        disable
      </button>
      <button className='pagDDL'onClick={() => selectCommand("enable")}>
        enable
      </button>
      <button className='pagDDL'onClick={() => selectCommand("is_enable")}>
        is_enable
      </button>
      <button className='pagDDL'onClick={() => selectCommand("alter")}>
        alter
      </button>
      <button className='pagDDL'onClick={() => selectCommand("drop")}>
        drop
      </button>
      <button className='pagDDL'onClick={() => selectCommand("dropall")}>
        dropall
      </button>
      <button className='pagDDL'onClick={() => selectCommand("describe")}>
        describe
      </button>
      <p className='parapapa'>{selectedButton}</p>
      <input className='parametroinput' onChange={handleInputChange} value={inputValue}></input>
      <button className='correr' onClick={runCommand}>
        RUN
      </button>
      <p className='response-message'>{responseMessage}</p>
      </div>
    </div>
      
    </div>
  );
}

export default DDL;
