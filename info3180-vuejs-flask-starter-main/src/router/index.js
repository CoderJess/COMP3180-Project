import { createRouter, createWebHistory } from 'vue-router';

// Import your components
import HomePage from '../components/HomePage.vue';
import RegisterForm from '../components/RegisterForm.vue';
import LoginForm from '../components/LoginForm.vue';
import UserProfile from '../components/UserProfile.vue';
import AddProfileForm from '../components/AddProfileForm.vue';
import ProfileDetails from '../components/ProfileDetails.vue';
import FavouriteReports from '../components/FavouriteReports.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterForm
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginForm
  },
  {
    path: '/users/:user_id',
    name: 'UserProfile',
    component: UserProfile
  },
  {
    path: '/profiles/new',
    name: 'AddProfile',
    component: AddProfileForm
  },
  {
    path: '/profiles/:profile_id',
    name: 'ProfileDetails',
    component: ProfileDetails
  },
  {
    path: '/profiles/favourites',
    name: 'FavouriteReports',
    component: FavouriteReports
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
