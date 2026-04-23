// Users
function Users({ users, loadingUsers }) {
    return (
        <section className="card">
            <h2>Users</h2>
            {users.length === 0 ? (
                <p>No users found</p>
            ) : (
                <table>
                    <thead>
                    <tr>
                        <th>Username</th>
                        <th>Email Address</th>
                    </tr>
                    </thead>
                    <tbody>
                    {users.map((user) => (
                        <tr key={user.username}>
                            <td>{user.username}</td>
                            <td>{user.email}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            )}
        </section>
    )
}

export default Users;