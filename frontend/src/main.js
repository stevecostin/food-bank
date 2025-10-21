import './assets/main.css';
import 'primeicons/primeicons.css'
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import ToastService from 'primevue/toastservice';
import { enUK } from './locales';
import { useAuth } from "@/composables/auth.js";

const app = createApp(App);
const pinia = createPinia();

pinia.use(piniaPluginPersistedstate);

app.use(pinia);
app.use(router);
app.use(PrimeVue, {
    theme: {
        preset: Aura,
    },
    locale: enUK,
});
app.use(ToastService);

try {
  const token = await useAuth().getCSFRToken();

  if (!token.success) {
    console.error('Failed to get CSRF token');
  }
} catch (e) {
  console.error('Failed to get CSRF token', e);
}

app.mount('#app');
