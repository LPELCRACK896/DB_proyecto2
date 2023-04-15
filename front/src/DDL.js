import './App.css';

function DDL() {
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
        <button className='botonp'>
          DML
        </button>
        <button className='botonp'>
          Extra
        </button>
        </ul>
      </div>


    {/* CONTENIDOOOO */}
      <div className='contenido'>
        <h1 className='titulo'>DDL</h1>
      <button className='pagDDL'>
        create
      </button>
      <button className='pagDDL'>
        list
      </button>
      <button className='pagDDL'>
        disable
      </button>
      <button className='pagDDL'>
        enable
      </button>
      <button className='pagDDL'>
        is_enable
      </button>
      <button className='pagDDL'>
        alter
      </button>
      <button className='pagDDL'>
        drop
      </button>
      <button className='pagDDL'>
        drop all
      </button>
      <button className='pagDDL'>
        Describe
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

export default DDL;
