// PLAYER CRUDs

import {  get, post, put, del } from '../api/client';
import { useEffect, useState} from "react";

// PLAYERS
function Players() {
    const [players, setPlayers] = useState([]);
    const [editingPlayer, setEditingPlayer] = useState(null);
    const [form, setForm] = useState({display_name: '', email: ''});

    // LOAD PLAYERS #NOTE: this is also in api/client.js now
    async function loadPlayers() {
        const data = await get('/players/');
        setPlayers(data);
    }

    useEffect(() => {
        loadPlayers().catch(console.error)
    }, []);

    // EDIT
    function handleEdit(player) {
        console.log('Editing Player', player);  //DEBUG

        setEditingPlayer(player.player_id);

        setForm({
            display_name: player.display_name,
            email: player.email
        });
    }

    // SUBMIT (Add + update)
    async function handleSubmit(e) {
        e.preventDefault();
        console.log('Adding Player');

        const payload = {
            ...form,
            password_hash: 'demo_hash'
        };

        try {
            if (editingPlayer) {
                await put(`/players/${editingPlayer}`, payload);
            } else {
                await post(`/players/`, payload);
            }

            setForm({display_name: '', email: ''});
            setEditingPlayer(null);
            await loadPlayers();

        } catch (err) {
            alert('Something went wrong!');
        }

    }


    // DELETE
    async function handleDelete(player) {
        if (!window.confirm(`Are you sure you want to delete player: ${player.display_name}`)) return;


        try {
            await del(`/players/${player.player_id}`);
            loadPlayers().catch(console.error);
        } catch (err) {
            alert('Cannot delete this player because they are linked to other records.');
        }
    }

    return (
        // === PLAYER TABLE ===
        <section className="card">
            <h2>Players</h2>

            {players.length === 0 && <p>No players found</p>}

                {/* Table Headers*/}
                <div className="table-container">
                <table>
                    <thead>
                    <tr>
                        <th>Display Name</th>
                        <th>Email Address</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>

                    {/* Table Contents */}
                    {players.map((player) => (
                        <tr key={player.player_id}>
                            <td>{player.display_name}</td>
                            <td>{player.email}</td>
                            <td>
                                <button className='edit' onClick={() => handleEdit(player)}>Edit</button>
                                <button className='delete' onClick={() => handleDelete(player)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
                </div>

            {/* FORM */}
            <div className="glass">
            <form onSubmit={handleSubmit}>
                { editingPlayer ? 'Update Player : ' : 'Add Player : ' }
                <input
                    value={form.display_name}
                    onChange={(e) =>
                        setForm({ ...form, display_name: e.target.value })
                    }
                    placeholder="Display Name"
                />

                <input
                    value={form.email}
                    onChange={(e) =>
                        setForm({ ...form, email: e.target.value })
                    }
                    placeholder="Email"
                />
                <button className='update' type='submit'>
                    { editingPlayer ? 'Save' : 'Add player' }
                </button>
            </form>
            </div>
        </section>
    )
}

export default Players;