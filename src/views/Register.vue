<template>
    <div class="register-page">
      <div class="register-card">
        <h2>Create Account</h2>
        <p>Join Jam-Date today!</p>
  
        <form @submit.prevent="register">
          <input v-model="username" type="text" placeholder="Username" required />
          <input v-model="password" type="password" placeholder="Password" required />
          <input v-model="name" type="text" placeholder="Full Name" required />
          <input v-model="email" type="email" placeholder="Email" required />
  
          <button type="submit">Register</button>
        </form>
  
        <p class="login-link">
          Already have an account? 
          <router-link to="/login">Login</router-link>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        name: '',
        email: ''
      }
    },
    methods: {
      async register() {
        try {
          await axios.post('/register', {
            username: this.username,
            password: this.password,
            name: this.name,
            email: this.email
          });
          alert("Registration successful!");
          this.$router.push('/login');
        } catch (err) {
          alert("Registration failed. Username may already exist.");
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .register-page {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #ffecd2, #fcb69f);
    font-family: 'Segoe UI', Tahoma, sans-serif;
  }
  
  .register-card {
    background-color: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 350px;
  }
  
  .register-card h2 {
    margin-bottom: 10px;
    color: #333;
  }
  
  .register-card p {
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
    border-color: #fc8a5e;
    outline: none;
  }
  
  button {
    width: 100%;
    padding: 12px;
    background-color: #fc8a5e;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #e07046;
  }
  
  .login-link {
    margin-top: 20px;
    font-size: 13px;
  }
  
  .login-link a {
    color: #fc8a5e;
    font-weight: bold;
    text-decoration: none;
  }
  
  .login-link a:hover {
    text-decoration: underline;
  }
  </style>
  