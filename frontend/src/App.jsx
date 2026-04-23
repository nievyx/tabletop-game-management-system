import { useEffect, useState } from 'react';
import './App.css';
import Users from './components/Users';
import Characters from "./components/Characters.jsx";

const BASE_URL = 'http://127.0.0.1:8000';

function App () {
//     const BASE_URL = import.meta.env.VITE_API_URL;
    const [status, setStatus] = useState('Loading...');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(true);
    // Users
    const [users, setUsers] = useState([]);
    const [loadingUsers, setLoadingUsers] = useState(true);
    // Characters
    const [loadingCharacters, setLoadingCharacters] = useState(true);
    const [characters, setCharacters] = useState(true);


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

        // Fetch Users
        fetch(`${BASE_URL}/users`)
        .then((res) => res.json())
        .then((data) => {
            setUsers(data);
            setLoadingUsers(false);
        })
        .catch((err) => {
            console.error(err);
            setLoadingUsers(false);
            console.log(users);
        });

        // Fetch Characters
        fetch(`${BASE_URL}/characters`)
            .then((res) => res.json())
            .then((data) => {
                console.log("characters data:", data);
                setCharacters(data);
                setLoadingCharacters(false);
            })
            .catch((err) => {
                console.error(err);
                setLoadingCharacters(false);
            });

  }, []);

    return (
        <div className= 'app'>
            <header className="topbar">
                <h1>Nova Systems Dashboard</h1>
                <p>Database API demo frontend</p>
            </header>

          <main className="content">
            <section className="card">
              <h2>Backend Status</h2>
              <p>{status}</p>
              {error && <p> Error: {error}</p>}
            </section>

            {/* Users*/}
            <Users users={users} loadingUsers={loadingUsers} />

          {/* Characters */}
          <Characters characters={characters} loadingCharacters={loadingCharacters} />


          </main>
        </div>
    );
}

export default App;