import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ExpenseView from '@/views/ExpenseView.vue'
import IncomeView from '@/views/IncomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import AboutView from '@/views/AboutView.vue'
import store from '@/store/store'; // Import the Vuex store




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/expense',
      name: 'Expense',
      component: ExpenseView,
      meta: { requiresAuth: true } // Add meta field for authentication

    },
    {
      path: '/income',
      name: 'Income',
      component: IncomeView,
      meta: { requiresAuth: true } // Add meta field for authentication

    },
    {
      path: '/about',
      name: 'About',
      component: AboutView,

    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterView
    }

  ]
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated;
  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;