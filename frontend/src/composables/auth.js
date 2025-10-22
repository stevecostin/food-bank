import api from "@/components/api.js";

export function useAuth() {
    function getCSFRToken() {
        let response = api.get('accounts/csrf_token');

        return response.data;
    }

    return {
        getCSFRToken,
    }
}