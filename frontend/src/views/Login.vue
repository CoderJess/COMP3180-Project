<template>
    <div class="login-page">
      <div class="login-card">
        <h2>Welcome Back</h2>
        <p>Please login to continue</p>
  
        <form @submit.prevent="login">
          <input v-model="username" type="text" placeholder="Username" required />
          <input v-model="password" type="password" placeholder="Password" required />
  
          <button type="submit">Login</button>
        </form>
  
        <p class="register-link">
          Don't have an account? 
          <router-link to="/register">Register</router-link>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return { username: '', password: '' }
    },
    methods: {
      async login() {
        try {
          const res = await axios.post('/auth/login', { username: this.username, password: this.password });
          localStorage.setItem('token', res.data.token);
          this.$router.push('/dashboard');
        } catch (err) {
          alert("Login failed. Please check your credentials.");
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #74ebd5, #acb6e5);
    font-family: 'Segoe UI', Tahoma, sans-serif;
  }
  
  .login-card {
    background-color: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 320px;
  }
  
  .login-card h2 {
    margin-bottom: 10px;
    color: #333;
  }
  
  .login-card p {
    color: #666;
    font-size: 14px;
    margin-bottom: 20px;
  }
  
  form input {
    display: block;
    width: 100%;
    padding: 12px;
    margin-bottom: 15px;
    border-radius: 6px;
    border: 1px solid #ccc;
    transition: border-color 0.3s;
  }
  
  form input:focus {
    border-color: #3a8bd5;
    outline: none;
  }
  
  button {
    width: 100%;
    padding: 12px;
    background-color: #3a8bd5;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #2a6bb5;
  }
  
  .register-link {
    margin-top: 20px;
    font-size: 13px;
  }
  
  .register-link a {
    color: #3a8bd5;
    font-weight: bold;
    text-decoration: none;
  }
  
  .register-link a:hover {
    text-decoration: underline;
  }
  </style>
  