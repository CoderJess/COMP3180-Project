<template>
  <div class="container mt-5">
    <h2>Register</h2>

    <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
    <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>

    <form @submit.prevent="registerUser">
      <input v-model="username" placeholder="Username" class="form-control mb-2" required />
      <input v-model="password" type="password" placeholder="Password" class="form-control mb-2" required />
      <input v-model="name" placeholder="Name" class="form-control mb-2" required />
      <input v-model="email" type="email" placeholder="Email" class="form-control mb-2" required />
      <button type="submit" class="btn btn-primary" :disabled="loading">
        {{ loading ? 'Registering...' : 'Register' }}
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterForm',
  data() {
    return {
      username: '',
      password: '',
      name: '',
      email: '',
      loading: false,
      successMessage: '',
      errorMessage: ''
    };
  },
  methods: {
    registerUser() {
      this.loading = true;
      this.successMessage = '';
      this.errorMessage = '';

      axios.post('/api/register', {
        username: this.username,
        password: this.password,
        name: this.name,
        email: this.email
      })
      .then(response => {
        this.successMessage = 'Registration successful! Redirecting to login...';
        setTimeout(() => {
          this.$router.push('/login');
        }, 1500);
      })
      .catch(error => {
        console.error(error);
        this.errorMessage = error.response?.data?.message || 'Registration failed. Please try again.';
      })
      .finally(() => {
        this.loading = false;
      });
    }
  }
};
</script>
