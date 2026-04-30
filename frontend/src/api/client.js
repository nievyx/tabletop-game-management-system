const BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

export async function request(endpoint, options = {}) {
    const res = await fetch(`${BASE_URL}${endpoint}`,options);

    if (!res.ok) {
        throw Error(`HTTP Error: ${res.status}`);
    }
    return res.json();
}

export function get(endpoint) {
    return request(endpoint);
}

export function post(endpoint, data) {
    return request(endpoint, {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });

}

export function put(endpoint, data) {
    return request(endpoint, {
        method : 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
        });
}

export function del(endpoint) {
    return request(endpoint, {
        method: 'DELETE',
    });
}

export async function getPlayers() {
    return get('/players/');
}