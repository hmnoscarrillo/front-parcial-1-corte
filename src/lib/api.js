const configuredApiUrl = import.meta.env.VITE_API_URL?.trim();

export const API_BASE_URL = configuredApiUrl ||
	(import.meta.env.DEV ? 'http://127.0.0.1:8000' : 'https://parcial-1-corte-api.onrender.com');

export async function apiRequest(endpoint, options = {}) {
	const response = await fetch(`${API_BASE_URL}${endpoint.startsWith('/') ? endpoint : `/${endpoint}`}`, {
		...options,
		headers: {
			Accept: 'application/json',
			...(options.body ? { 'Content-Type': 'application/json' } : {}),
			...options.headers
		}
	});

	if (!response.ok) {
		let detail = `Error HTTP ${response.status}`;
		try {
			const body = await response.json();
			if (body.detail) detail = typeof body.detail === 'string' ? body.detail : JSON.stringify(body.detail);
		} catch {
			// Use the HTTP status when the API response is not JSON.
		}
		throw new Error(detail);
	}

	return response.status === 204 ? null : response.json();
}
