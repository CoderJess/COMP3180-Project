import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

const app = createApp(App);

// Set baseURL for Axios
axios.defaults.baseURL = 'http://127.0.0.1:5000'; // or wherever your Flask backend runs

// If token already saved (like after refresh), set Authorization header
const token = localStorage.getItem('token');
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

// Make Axios available globally (optional but nice)
app.config.globalProperties.$axios = axios;

// Use router
app.use(router);

// Mount the app
app.mount('#app');
