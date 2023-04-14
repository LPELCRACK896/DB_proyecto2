import { render } from "react-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import React from 'react';
import { BrowserRouter, Routes, Route} from "react-router-dom"
import { Home } from './Pages';

const rootElement = document.getElementById("root");
const NotFound = () => <h1>404: Page Not Found</h1>;

function App() {
  render(
    
    <BrowserRouter>
      <Routes>
        {/* Pagina principal */}
        <Route path="/" element={<Home />} />
        
      </Routes>
    </BrowserRouter>,
  rootElement
  );
  
  
}

export default App;

