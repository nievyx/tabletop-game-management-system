 // Profiles
 function Profiles({ profiles, loadingProfiles }) {
    return (
        <section className="card">
            <h2>Profiles</h2>
            {profiles.length === 0 ? (
                <p>No users found</p>
            ) : (
                <table>
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Username</th>
                    </tr>
                    </thead>
                    <tbody>
                    {profiles.map((profile) => (
                        <tr key={profile.id}>
                            <td>{profile.id}</td>
                            <td>{profile.display_name}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            )}
        </section>
    )
 }

 export default Profiles;