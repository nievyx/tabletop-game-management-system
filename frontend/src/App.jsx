import { useEffect, useState } from 'react';
import './App.css';
import Users from './components/Users';
import Characters from "./components/Characters.jsx";
import GalaxyBackground from "./components/backgrounds/GalaxyBackground";
import './styles/tables.css'
import './styles/buttons.css';

const BASE_URL = 'http://127.0.0.1:8000';


function App () {
//     const BASE_URL = import.meta.env.VITE_API_URL;
    const [status, setStatus] = useState('Loading...');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(true);
    // Toggle Galaxy Background
    const [showGalaxy, setShowGalaxy] = useState(true);


    useEffect(() => {
        // Database Health Check
        fetch(`${BASE_URL}/db-check`)
          .then((res) => {
            if (!res.ok) {
                throw new Error(`HTTP error: ${res.status}`);
            }
            return res.json();
          })
          .then((data) => {
              setStatus(`Connection: ok = ${data.ok}`);
          })
          .catch((err) => {
             setError(err.message);
             setStatus('Connection Failed');
          });

  }, []);

    return (
        // Galaxy Background
        <div className="app-shell">
            {showGalaxy && <GalaxyBackground />}

        {/* === DASHBOARD === */}
        <div className= 'app'>
            <header className="topbar">
                <h1>Nova Systems Dashboard</h1>
                <p>Database API demo frontend</p>

                {/* Toggle galaxy button */}
                <button onClick={() => {
                    console.log('Click toggle button');
                    setShowGalaxy(!showGalaxy);}}>
                    {showGalaxy ? 'Hide Galaxy' : 'Show Galaxy'}
                </button>
            </header>

          {/* Backend Status Block */}
          <main className="content">
            <section className="card">
              <h2>Backend Status</h2>
              <p>{status}</p>
              {error && <p> Error: {error}</p>}
            </section>

            {/* Users Block */}
            <Users />

          {/* Characters Block */}
          <Characters />


          </main>
        </div>
        </div>
    );
}

export default App;