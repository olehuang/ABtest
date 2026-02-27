import React from 'react';

import './App.css';
import { Routes,Route,BrowserRouter,createBrowserRouter,createRoutesFromElements } from 'react-router-dom';
import ComparPage from "./page/ComparPage";
import Laderboard from "./page/Leaderboard"
function App() {
  return (
    <div className="App">
        <BrowserRouter>
            <Routes>
                <Route element={<Laderboard/>} path="/" />{/*Laderboard*/}
             <Route element={<ComparPage/>} path="/comparpage" />{/*Comparpage*/}
            </Routes>
        </BrowserRouter>

      {/*<ComparPage/>*/}
      {/*<Laderboard/>*/}
    </div>
  );
}

export default App;
