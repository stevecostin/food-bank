import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    isAuthenticated: !!localStorage.getItem('token'),
  }),
  getters: {
    isLoggedIn: (state) => state.isAuthenticated,
  },
  actions: {
    setToken(token) {
      this.token = token;
      this.isAuthenticated = true;
      localStorage.setItem('token', token);
    },
    removeToken() {
      this.token = '';
      this.isAuthenticated = false;
      localStorage.removeItem('token');
    },
  },
});