import './App.css';
import DDL from './DDL';

function DML() {
  return (
    // NAVBAR A LA IZQUIERDA
    <div className="App">
      <header className="App-header">
        <p className='CR'>HBASE by RS_LP_JG</p>
      </header>

      <div className="container m-0">
      <div className="nav-bar">
        <ul>
        <button className='botonp' onClick={DDL}>
          DDL
        </button>
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
      <button className='pagDML'>
        put
      </button>
      <button className='pagDML'>
        get
      </button>
      <button className='pagDML'>
        scan
      </button>
      <button className='pagDML'>
        delete
      </button>
      <button className='pagDML'>
        deleteall
      </button>
      <button className='pagDML'>
        count
      </button>
      <button className='pagDML'>
        truncate
      </button>
      <button className='pagDML'>
        updateMany
      </button>
      <button className='pagDML'>
        insertMany
      </button>
      <p className='parapapa'>Descripcion de parametros</p>
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
