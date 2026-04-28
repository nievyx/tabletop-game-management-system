// CHARACTER CRUDs

import {  get, post, put, del } from '../api/client';
import { useEffect, useState} from "react";

const PREFIX = '/characters/'

// CHARACTERS
function Characters() {
    const [characters, setCharacters] = useState([]);
    const [editingCharacter, setEditingCharacter] = useState(null);
    const [form, setForm] = useState({
        display_name:'',
        level: '',
        class_name:'',
    });

    // LOAD CHARACTERS
    async function loadCharacters() {
        const data = await get(PREFIX);
        setCharacters(data);
    }

    useEffect(() => {
        loadCharacters().catch(console.error)
    }, []);

    // EDIT
    function handleEdit(character) {
        console.log('Editing character', character);  //DEBUG
        setEditingCharacter(character.id);
        setForm({
            display_name: character.display_name,
            level: character.level,
            class_name: character.class_name,
        });
    }

    // SUBMIT (Add + update)
    async function handleSubmit(e) {
        e.preventDefault();
        console.log('Adding character');  //TODO : DEBUG

        const payload = {
            ...form,
            password_hash: 'demo_hash'
        };

        try {
            if (editingCharacter) {
                await put(`${PREFIX}${editingCharacter}`, payload);
            } else {
                await post(PREFIX, payload);
            }

            setForm({display_name: '', level: ''});
            setEditingCharacter(null);
            loadCharacters();

        } catch (err) {
            alert('Something went wrong!');
        }

    }


    // DELETE
    async function handleDelete(character) {
        if (!window.confirm(`Are you sure you want to delete character: ${character.display_name}`)) return;


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
                        <th>Display Name</th>
                        <th>Level</th>
                        <th>Class</th>
                        <th>Action</th>
                    </tr>
                    </thead>
                    <tbody>

                    {/* Table Contents */}
                    {characters.map((character) => (
                        <tr key={character.id}>
                            <td>{character.id}</td>
                            <td>{character.display_name}</td>
                            <td>{character.level}</td>
                            <td>{character.class_name}</td>
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
                    <input
                        value={form.display_name}
                        onChange={(e) =>
                            setForm({ ...form, display_name: e.target.value })
                        }
                        placeholder="Display Name"
                    />

                    <input
                        value={form.level}
                        onChange={(e) =>
                            setForm({ ...form, level: e.target.value })
                        }
                        placeholder="Level"
                    />

                    <input
                        value={form.class_name}
                        onChange={(e) => setForm({ ...form, class_name: e.target.value })}
                        placeholder="Class"
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