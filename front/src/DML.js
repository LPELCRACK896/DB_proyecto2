import './App.css';

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
      <button className='pagDML'>
        create
      </button>
      <button className='pagDML'>
        list
      </button>
      <button className='pagDML'>
        disable
      </button>
      <button className='pagDML'>
        enable
      </button>
      <button className='pagDML'>
        is_enable
      </button>
      <button className='pagDML'>
        alter
      </button>
      <button className='pagDML'>
        drop
      </button>
      <button className='pagDML'>
        drop all
      </button>
      <button className='pagDML'>
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

export default DML;
