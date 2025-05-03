import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import Register from '../views/Register.vue';
import Login from '../views/Login.vue';
import Dashboard from '../views/Dashboard.vue';
import ProfileDetails from '../views/ProfileDetails.vue';
import MyProfiles from '../views/MyProfiles.vue';
import FavouritesReport from '../views/FavouritesReport.vue';
import AddProfileForm from '../views/AddProfileForm.vue';
import Matches from '../views/Matches.vue'; // ✅ ADD THIS

const routes = [
  { path: '/', component: HomePage },
  { path: '/register', component: Register },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/profiles/:id', component: ProfileDetails },
  { path: '/myprofiles', component: MyProfiles },
  { path: '/favourites', component: FavouritesReport },
  { path: '/add-profile', component: AddProfileForm },
  { path: '/matches/:id', component: Matches } // ✅ ADD THIS ROUTE
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
