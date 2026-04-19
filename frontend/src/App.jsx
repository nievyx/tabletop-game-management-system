import './App.css';

function App () {
    return (
        <div className= 'app'>
            <header className="topbar">
                <h1>Nova Systems Dashboard</h1>
                <p>Database API demo frontend</p>
            </header>

          <main className="content">
            <section className="card">
              <h2>Backend Status</h2>
              <p>This section will show data from the API.</p>
            </section>

            <section className="card">
              <h2>Users</h2>
              <p>Later this will display user records from the backend.</p>
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