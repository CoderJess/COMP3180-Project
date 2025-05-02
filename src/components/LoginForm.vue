<template>
  <div class="container mt-5">
    <h2>Login</h2>

    <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>

    <form @submit.prevent="loginUser">
      <input v-model="username" placeholder="Username" class="form-control mb-2" required />
      <input v-model="password" type="password" placeholder="Password" class="form-control mb-2" required />
      <button type="submit" class="btn btn-primary" :disabled="loading">
        {{ loading ? 'Logging in...' : 'Login' }}
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      errorMessage: ''
    };
  },
  methods: {
    loginUser() {
      this.loading = true;
      this.errorMessage = '';

      axios.post('/api/auth/login', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        const token = response.data.token;
        localStorage.setItem('token', token);
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        this.$router.push('/');
      })
      .catch(error => {
        console.error(error);
        this.errorMessage = error.response?.data?.message || 'Login failed. Please check your username and password.';
      })
      .finally(() => {
        this.loading = false;
      });
    }
  }
};
</script>
