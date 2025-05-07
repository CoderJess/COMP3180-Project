import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'

// Lazy-loaded views (optimal for performance)
const About = () => import('../views/About.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Dashboard,
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/users/:userid',
      name: 'my-profile',
      component: () => import('../views/MyProfileView.vue')
    },
    {
      path: '/profiles/:id',
      name: 'ProfileDetails',
      component: () => import('@/views/ProfileDetails.vue')
    },
    {
      path: '/match-report/:profileId',
      name: 'Match Report',
      component: () => import('@/views/MatchReport.vue')
    },
    {
      path: '/profiles/new',
      name: 'CreateProfile',
      component: () => import('@/views/AddProfileForm.vue')
    },
    {
      path: '/profiles/favourites',
      name: 'Favourites',
      component: () => import('@/views/Favourites.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('@/views/NotFound.vue')
    },
    
    
    
  ]
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  const publicPages = ['/login', '/register']
  const authRequired = !publicPages.includes(to.path)

  if (authRequired && !token) {
    return next('/login')
  }

  if ((to.path === '/login' || to.path === '/register') && token) {
    return next('/')
  }

  next()
})


export default router
