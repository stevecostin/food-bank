import api from "@/components/api.js";

export function useAuth() {
    async function getCSFRToken() {
        let response = await api.get('accounts/csrf_token');

        return response.data;
    }

    return {
        getCSFRToken,
    }
}