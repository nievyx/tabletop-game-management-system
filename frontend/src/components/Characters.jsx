// Characters
function Characters({ characters, loadingCharacters }) {
    return (<section className="card">
        <h2>Characters</h2>

        {loadingCharacters ? (
            <p>Loading characters...</p>
        ) : characters.length === 0 ? (
            <p>No characters found</p>
        ) : (
            <table>
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Level</th>
                    <th>Class</th>
                </tr>
                </thead>
                <tbody>
                {characters.map((character) => (
                    <tr key={character.id}>
                        <td>{character.id}</td>
                        <td>{character.display_name}</td>
                        <td>{character.level}</td>
                        <td>{character.class_name}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        )}
    </section>)
}

export default Characters;