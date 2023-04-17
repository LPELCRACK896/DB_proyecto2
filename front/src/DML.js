import './App.css';
import { Link} from "react-router-dom";
import React, { useState } from "react";
import axios from "axios";

function DML() {
  const [selectedButton, setSelectedButton] = useState("");
  const [inputValue, setInputValue] = useState("");
  const [responseMessage, setResponseMessage] = useState("");
  const apiUrl = "http://127.0.0.1:5000/";
  const command_message = {
    "put": "Parametros para put",
    "get": "Parametros para get",
    "scan": "Parametros para scan",
    "delete": "Parametros para delete",
    "deleteall": "Parametros para delete all",
    "count": "Parametros para count",
    "truncate": "Parametros para truncate",
    "updateMany": "Parametros para update many",
    "insertMany": "Parametros para insert many",
  };
  const selectCommand = (buttonText) => {
    setSelectedButton(buttonText);
  };

  // const runCommand = async () => {
  //   if (!selectedButton) {
  //     console.error("No command selected");
  //     return;
  //   }
  //   console.log("a")
  //   try {
  //     const response = await axios.post(`${apiUrl}${selectedButton}`, { query: inputValue });
  //     setResponseMessage(JSON.stringify(response.data));
  //     console.log(response)
  //   } catch (error) {
  //     console.error("Error making API request:", error);
  //     setResponseMessage("Error making API request");
  //   }
  // };
  const runCommand = async () => {
    if (!selectedButton) {
      console.error("No command selected");
      return;
    }
    try {
      const response = await axios.post(`${apiUrl}${selectedButton}`, { query: inputValue });
      setResponseMessage(JSON.stringify(response.data.message, null, 2));
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
        <Link to='/#'>
            <button className='botonp'>
          DDL
        </button>
        </Link>
        <button className='DDL'>
          DML
        </button>
        <button className='botonp'>
          Extra
        </button>
        </ul>
      </div>


    {/* CONTENIDOOOO */}
      <div className='contenido'>
        <h1 className='titulo'>DML</h1>
      <button className='pagDML' onClick={() => selectCommand("put")}>
        put
      </button>
      <button className='pagDML'onClick={() => selectCommand("get")}>
        get
      </button>
      <button className='pagDML'onClick={() => selectCommand("scan")}>
        scan
      </button>
      <button className='pagDML'onClick={() => selectCommand("delete")}>
        delete
      </button>
      <button className='pagDML'onClick={() => selectCommand("delete_all")}>
        deleteall
      </button>
      <button className='pagDML'onClick={() => selectCommand("count")}>
        count
      </button>
      <button className='pagDML'onClick={() => selectCommand("truncate")}>
        truncate
      </button>
      <button className='pagDML'onClick={() => selectCommand("update_many")}>
        updateMany
      </button>
      <button className='pagDML'onClick={() => selectCommand("insert_many")}>
        insertMany
      </button>
      <p className='parapapa'>{command_message[selectedButton]}</p>
      <input className='parametroinput' onChange={handleInputChange} value={inputValue}></input>
      <button className='correr' onClick={runCommand}>
        RUN
      </button>
      <pre className='response-message'>{responseMessage}</pre>
      </div>
    </div>
      
    </div>
  );
}

export default DML;
