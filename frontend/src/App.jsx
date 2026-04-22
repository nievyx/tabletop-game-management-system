import { useEffect, useState } from 'react';
import './App.css';

function App () {
    const BASE_URL = 'http://127.0.0.1.8000';
//     const BASE_URL = import.meta.env.VITE_API_URL;
    const [status, setStatus] = useState('Loading...');
    const [error, setError] = useState('');
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/db-check')
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
        fetch(`${BASE_URL}/users`)
        .then(res => res.json())
        .then(data => setUsers(data))
        .catch(err => console.error(err));
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

            <section className="card">
              <h2>Users</h2>

              {users.length === 0 ? (
                  <p>No users found</p>
              ) : (
                  <ul>
                      {users.map((user) => (
                          <li key={user.id}>
                              {user.username} ({user.email})
                          </li>
                      ))}
                  </ul>
              )}
            </section>

            <section className="card">
              <h2>Profiles</h2>
              <p>Later this will display profile or character data.</p>
            </section>
          </main>
        </div>
    );
}

export default App;