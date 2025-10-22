import axios from 'axios';
import { useUtils } from "@/composables/utils.js";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    withCredentials: true,
});

api.interceptors.request.use(
    (config) => {
        config.headers['X-CSRFToken'] = useUtils().getCookie('csrftoken');
        config.headers['Content-Type'] = 'application/json';

        return config;
    }
);

export default api;