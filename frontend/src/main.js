import './assets/main.css';
import 'primeicons/primeicons.css'
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import ToastService from 'primevue/toastservice';
import {enUK} from './locales';

const app = createApp(App);

app.use(router);
app.use(PrimeVue, {
    theme: {
        preset: Aura,
    },
    locale: enUK,
});
app.use(ToastService);

app.mount('#app');
