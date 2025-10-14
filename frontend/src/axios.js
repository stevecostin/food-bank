import axios from 'axios';
import { useAuthStore } from '@/stores/auth.js';

const api = axios.create({
  baseURL: '',
});

// Attach token to every request safely
api.interceptors.request.use((config) => {
    const store = useAuthStore();

    if (store.token) {
        config.headers['Authorization'] = `Token ${store.token}`;
    }

    return config;
});

export default api;