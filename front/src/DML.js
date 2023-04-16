import './App.css';
import { Link, useParams } from "react-router-dom";
import React, { useState } from "react";

function DML() {
  const [selectedButton, setSelectedButton] = useState("");

  const handleClick = (buttonText) => {
    setSelectedButton(buttonText);
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
      <button className='pagDML' onClick={() => handleClick("Parametros para put")}>
        put
      </button>
      <button className='pagDML'onClick={() => handleClick("Parametros para get")}>
        get
      </button>
      <button className='pagDML'onClick={() => handleClick("Parametros para scan")}>
        scan
      </button>
      <button className='pagDML'onClick={() => handleClick("Parametros para delete")}>
        delete
      </button>
      <button className='pagDML'onClick={() => handleClick("Parametros para delete all")}>
        deleteall
      </button>
      <button className='pagDML'onClick={() => handleClick("Parametros para count")}>
        count
      </button>
      <button className='pagDML'onClick={() => handleClick("Parametros para truncate")}>
        truncate
      </button>
      <button className='pagDML'onClick={() => handleClick("Parametros para update many")}>
        updateMany
      </button>
      <button className='pagDML'onClick={() => handleClick("Parametros para insert many")}>
        insertMany
      </button>
      <p className='parapapa'>{selectedButton}</p>
      <input className='parametroinput'></input>
      <button className='correr'>
        RUN
      </button>
      </div>
    </div>
      
    </div>
  );
}

export default DML;
