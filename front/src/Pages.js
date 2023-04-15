import "./App.css"
import DDL from "./DDL";
import DML from './DML'
import {useState, useEffect} from 'react';
import axios from "axios";

// El home va a ser el DDL porque es la primera pagina, la principal la importante
export const Home = () => {
  
  return (
    <div >
        <DDL/>
    </div>
  );
};

export const Page2 = () => {
  
  return (
    <div >
        <DML/>
    </div>
  );
};