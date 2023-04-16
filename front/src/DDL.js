import './App.css';
import { Link, useParams } from "react-router-dom";
import React, { useState } from "react";

function DDL() {

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
      <button className='pagDDL'onClick={() => handleClick("Parametros para create")}>
        create
      </button>
      <button className='pagDDL'onClick={() => handleClick("Parametros para list")}>
        list
      </button>
      <button className='pagDDL'onClick={() => handleClick("Parametros para disable")}>
        disable
      </button>
      <button className='pagDDL'onClick={() => handleClick("Parametros para enable")}>
        enable
      </button>
      <button className='pagDDL'onClick={() => handleClick("Parametros para is_enable")}>
        is_enable
      </button>
      <button className='pagDDL'onClick={() => handleClick("Parametros para alter")}>
        alter
      </button>
      <button className='pagDDL'onClick={() => handleClick("Parametros para drop")}>
        drop
      </button>
      <button className='pagDDL'onClick={() => handleClick("Parametros para drop all")}>
        dropall
      </button>
      <button className='pagDDL'onClick={() => handleClick("Parametros para describe")}>
        describe
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

export default DDL;
