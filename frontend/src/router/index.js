import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/views/Dashboard.vue';
import Clients from '@/views/Clients.vue';
import Staff from '@/views/Staff.vue';

const siteName = 'Food Bank';

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
      path: '/clients',
      name: 'clients',
      component: Clients,
      meta: {
        title: 'Clients',
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

router.beforeEach((to, from) => {
  let title = '';

  if (to.meta.title) {
    title = ` - ${to.meta.title}`
  }

  document.title = `${siteName}${title}`;
})

export default router;
