import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/views/Dashboard.vue';
import Login from '@/views/Login.vue';
import Client from '@/views/client/Client.vue';
import Staff from '@/views/staff/Staff.vue';
import { useAuthStore } from "@/stores/auth.js";

const SITE_NAME = 'Food Bank';
const LOGIN_ROUTE = '/login';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard,
      meta: {
        title: 'Dashboard',
      },
    },
    {
      path: LOGIN_ROUTE,
      name: 'login',
      component: Login,
      meta: {
        title: 'Login',
      },
    },
    {
      path: '/client',
      name: 'client',
      component: Client,
      meta: {
        title: 'Client',
      },
    },
    {
      path: '/staff',
      name: 'staff',
      component: Staff,
      meta: {
        title: 'Staff',
      },
    },
  ],
});

router.beforeEach((to, from, next) => {
  // If user is not authorised to access the page that they're being routed to, re-route them to the login page
  const auth = useAuthStore();

  if (!useAuthStore().isLoggedIn) {
    if (to.path !== LOGIN_ROUTE) {
        next(LOGIN_ROUTE);
    } else {
        next();
    }
  } else if (to.path === LOGIN_ROUTE) {
    next('/');
  } else {
      next();
  }

  let title = '';

  if (to.meta.title) {
    title = `${to.meta.title} - `
  }

  document.title = `${title}${SITE_NAME}`;
})

export default router;
