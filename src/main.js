import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

axios.defaults.baseURL = "http://127.0.0.1:5001/api"; // Change backend port here if needed

axios.interceptors.request.use(config => {
    const token = localStorage.getItem("token");
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
});

const app = createApp(App);
app.use(router);
app.mount('#app');
