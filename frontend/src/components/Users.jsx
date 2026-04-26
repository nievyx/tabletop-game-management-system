// USER CRUDs

import { get } from '../api/client';
import { useEffect, useState} from "react";


// USERS
function Users() {
    const [users, setUsers] = useState([]);
    const [editingUser, setEditingUser] = useState(null);
    const [form, setForm] = useState({ username: '', email: ''});

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
        setForm({ username: user.username, email: user.email });
    }

    // SUBMIT (Add + update)
    async function handleSubmit(e) {
        e.preventDefault();

        const method = editingUser ? 'PUT' : 'POST';
        const url = editingUser
            ? `${API_URL}${editingUser}`
            : API_URL;

        await fetch(url, {
            method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({form})
        });

        setForm({ username: '', email: ''});
        setEditingUser(null);

        await loadUsers();
    }

    // DELETE
    async function handleDelete(userId) {
        const confirmed = window.confirm(`Are you sure you want to delete ${userId}`);

        if (!confirmed) return;

        await del(`${BASE_URL}/${userId}`, {
            method: 'DELETE',
        });
        loadUsers().catch(console.error)
    }



    return (
        <section className="card">
            <h2>Users</h2>
            {users.length === 0 ? (
                <p>No users found</p>
            ) : (

                // Table Headers
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
                                <button onClick={() => handleEdit(user)}>Edit</button>
                                <button onClick={() => handleDelete(user.user_id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            )}
        </section>
    )
}

export default Users;