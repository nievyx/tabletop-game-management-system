// USER CRUDs

import { get, post, put, del } from '../api/client';
import { useEffect, useState} from "react";

const API_URL = 'http://127.0.0.1:8000/users/';

// USERS
function Users() {
    const [users, setUsers] = useState([]);
    const [editingUser, setEditingUser] = useState(null);
    const [form, setForm] = useState({username: '', email: ''});

    // LOAD USERS
    async function loadUsers() {
        const data = await get('/users/');
        setUsers(data);
    }

    useEffect(() => {
        loadUsers().catch(console.error)
    }, []);

    // EDIT
    function handleEdit(user) {
        console.log('Editing user', user);  //DEBUG
        setEditingUser(user.user_id);
        setForm({
            username: user.username,
            email: user.email
        });
    }

    // SUBMIT (Add + update)
    async function handleSubmit(e) {
        e.preventDefault();
        console.log('Adding user');  //TODO : DEBUG

        const payload = {
            ...form,
            password_hash: 'demo_hash'
        };

        try {
            if (editingUser) {
                await put(`/users/${editingUser}`, payload);
            } else {
                await post(`/users/`, payload);
            }

            setForm({username: '', email: ''});
            setEditingUser(null);
            loadUsers();

        } catch (err) {
            alert('Something went wrong!');
        }

    }


    // DELETE
    async function handleDelete(user) {
        if (!window.confirm(`Are you sure you want to delete user: ${user.username}`)) return;


        try {
            await del(`/users/${user.user_id}`);
            loadUsers().catch(console.error);
        } catch (err) {
            alert('Cannot delete this user because they are linked to other records.');
        }
    }

    return (
        // === USER TABLE ===
        <section className="card">
            <h2>Users</h2>

            {users.length === 0 && <p>No users found</p>}

                {/* Table Headers*/}
                <div className="table-container">
                <table>
                    <thead>
                    <tr>
                        <th>Username</th>
                        <th>Email Address</th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>

                    {/* Table Contents */}
                    {users.map((user) => (
                        <tr key={user.user_id}>
                            <td>{user.username}</td>
                            <td>{user.email}</td>
                            <td>
                                <button className='edit' onClick={() => handleEdit(user)}>Edit</button>
                                <button className='delete' onClick={() => handleDelete(user)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
                </div>

            {/* FORM */}
            <div className="glass">
            <form onSubmit={handleSubmit}>
                { editingUser ? 'Update User : ' : 'Add user : ' }
                <input
                    value={form.username}
                    onChange={(e) =>
                        setForm({ ...form, username: e.target.value })
                    }
                    placeholder="Username"
                />

                <input
                    value={form.email}
                    onChange={(e) =>
                        setForm({ ...form, email: e.target.value })
                    }
                    placeholder="Email"
                />
                <button className='update' type='submit'>
                    { editingUser ? 'Save' : 'Add user' }
                </button>
            </form>
            </div>
        </section>
    )
}

export default Users;