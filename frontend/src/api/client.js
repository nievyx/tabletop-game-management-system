const BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

export async function get(endpoint) {
    const res = await fetch(`${BASE_URL}${endpoint}`);

    if (!res.ok) {
        throw Error(`HTTP Error: ${res.status}`);
    }
    return res.json();
}
