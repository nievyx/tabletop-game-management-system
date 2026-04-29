// CHARACTER CRUDs

import {  get, post, put, del, getUsers } from '../api/client';
import { useEffect, useState} from "react";


const PREFIX = '/characters/'

// CHARACTERS
function Characters() {
    const [characters, setCharacters] = useState([]);
    const [editingCharacter, setEditingCharacter] = useState(null);
    const [players, setPlayers] = useState([]);

    const [form, setForm] = useState({
        player_id: 1,
        character_name: '',
        character_type: 'Player',
        class_id: 1,
        species_id: 1,
        alignment_id: 1,
        level: 1,
    });

    // LOAD CHARACTERS
    async function loadCharacters() {
        const data = await get(PREFIX);
        setCharacters(data);
    }
    // LOAD PLAYERS ACCOUNTS (NOTE: NAMED USERS IN BACKEND)
    async function loadUsers() {
        const data = await getUsers();
        setPlayers(data);
    }

    useEffect(() => {
        loadCharacters().catch(console.error)
        loadUsers().catch(console.error);
    }, []);

    function resetForm() {
        setForm({
            player_id: 1,
            character_name: '',
            character_type: 'Player',
            class_id: 1,
            species_id: 1,
            alignment_id: 1,
            level: 1,
        });
    }

    // EDIT
    function handleEdit(character) {
        setEditingCharacter(character.id);
        console.log('Editing character', character);  //DEBUG


        setForm({
            player_id: character.player_id ?? 1,
            character_name: character.character_name ?? '',
            character_type: character.character_type ?? 'Player',
            class_id: character.class_id ?? 1,
            species_id: character.species_id ?? 1,
            alignment_id: character.alignment_id ?? 1,
            level: character.level ?? 1,
        });
    }

    // SUBMIT (Add + update)
    async function handleSubmit(e) {
        e.preventDefault();
        console.log('Adding character');  //TODO : DEBUG

        const payload = {
            player_id: Number(form.player_id),
            character_name: form.character_name,
            character_type: form.character_type,
            class_id: Number(form.class_id),
            species_id: Number(form.species_id),
            alignment_id: Number(form.alignment_id),
            level: Number(form.level),
        };

        try {
            if (editingCharacter) {
                await put(`${PREFIX}${editingCharacter}`, payload);
            } else {
                await post(PREFIX, payload);
            }

            resetForm();
            setEditingCharacter(null);
            await loadCharacters();

        } catch (err) {
            console.log(err);
            alert('Something went wrong!');
        }

    }


    // DELETE
    async function handleDelete(character) {
        if (!window.confirm(`Are you sure you want to delete character: ${character.character_name}?`)) return;


        try {
            await del(`${PREFIX}${character.id}`);
            loadCharacters().catch(console.error);
        } catch (err) {
            alert('Cannot delete this character because they are linked to other records.');
        }
    }

    return (
        // === CHARACTER TABLE ===
        <section className="card">
            <h2>Characters</h2>

            {characters.length === 0 && <p>No characters found</p>}

            {/* Table Headers */}
            <div className="table-container">
                <table>
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Character Name</th>
                        <th>Type</th>
                        <th>Class</th>
                        <th>Species</th>
                        <th>Alignment</th>
                        <th>Level</th>
                        <th>Action</th>
                    </tr>
                    </thead>
                    <tbody>

                    {/* Table Contents */}
                    {characters.map((character) => (
                        <tr key={character.id}>
                            <td>{character.id}</td>
                            <td>{character.character_name}</td>
                            <td>{character.character_type}</td>
                            <td>{character.class_name}</td>
                            <td>{character.species_name}</td>
                            <td>{character.alignment_name}</td>
                            <td>{character.level}</td>
                            <td>
                                <button className='edit' onClick={() => handleEdit(character)}>Edit</button>
                                <button className='delete' onClick={() => handleDelete(character)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>

            {/* FORM */}
            <div className="glass">
                <form onSubmit={handleSubmit}>
                    { editingCharacter ? 'Update Character : ' : 'Add character : ' }

                    {/* Character Name */}
                    <input
                        value={form.character_name}
                        onChange={(e) =>
                            setForm({ ...form, character_name: e.target.value })
                        }
                        placeholder="Character Name"
                    />

                    {/* Character Type */}
                    <select
                        value={form.character_type}
                            onChange={(e) =>
                                setForm({ ...form, character_type: e.target.value })}
                            >
                        <option value="Player">Player</option>
                        <option value="NPC">NPC</option>
                    </select>

                    {/* Player ID Non-dynamic */}
                    {/*<input*/}
                    {/*    type="number"*/}
                    {/*    value={form.player_id}*/}
                    {/*    onChange={(e) => setForm({ ...form, player_id: e.target.value })}*/}
                    {/*    placeholder="Player ID"*/}
                    {/*    min="1"*/}
                    {/*    required*/}
                    {/*/>*/}

                    {/* Player Account */}
                    <select
                        value={form.player_id}
                        onChange={(e) =>
                            setForm({ ...form, player_id: e.target.value })}
                        required
                    >
                        <option value="">Select Player account</option>

                        {players.map((player) => (
                            <option key={player.user_id} value={player.user_id}>
                                {player.username ?? player.email}
                            </option>
                        ))}
                    </select>

                    {/* Class ID */}
                    <input
                        value={form.class_id}
                        onChange={(e) =>
                            setForm({ ...form, class_id: e.target.value })}
                        placeholder="Class ID"
                        type='number'
                        min = '1'
                        required
                    />

                    {/* Species ID */}
                    <input
                        value={form.species_id}
                        onChange={(e) =>
                            setForm({ ...form, species_id: e.target.value })}
                        placeholder="Species ID"
                        type="number"
                        min = '1'
                        required
                    />

                    {/* Alignment ID */}
                    <input
                        value={form.alignment_id}
                        onChange={(e) =>
                            setForm({ ...form, alignment_id: e.target.value })}
                        placeholder="Alignment ID"
                        type="number"
                        min="1"
                        required
                    />

                   {/* Level */}
                    <input
                        type="number"
                        value={form.level}
                        onChange={(e) =>
                            setForm({ ...form, level: e.target.value })
                        }
                        placeholder="Level"
                        min='1'
                        required
                    />


                    <button className='update' type='submit'>
                        { editingCharacter ? 'Save' : 'Add character' }
                    </button>
                </form>
            </div>
        </section>
    )
}

export default Characters;

// Old character table

// Characters
// function Characters({ characters, loadingCharacters }) {
//     return (<section className="card">
//         <h2>Characters</h2>

//         {loadingCharacters ? (
//             <p>Loading characters...</p>
//         ) : characters.length === 0 ? (
//             <p>No characters found</p>
//         ) : (
//             <table>
//                 <thead>
//                 <tr>
//                     <th>ID</th>
//                     <th>Name</th>
//                     <th>Level</th>
//                     <th>Class</th>
//                 </tr>
//                 </thead>
//                 <tbody>
//                 {characters.map((character) => (
//                     <tr key={character.id}>
//                         <td>{character.id}</td>
//                         <td>{character.display_name}</td>
//                         <td>{character.level}</td>
//                         <td>{character.class_name}</td>
//                     </tr>
//                 ))}
//                 </tbody>
//             </table>
//         )}
//     </section>)
// }

// export default Characters;