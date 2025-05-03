<template>
    <div class="homepage">
      <div class="hero">
        <h1>Welcome to <span>Jam-Date</span></h1>
        <p>Find your perfect match. Simple, fun and secure.</p>
      </div>
      
      <div class="links">
        <router-link to="/login" class="btn">Login</router-link>
        <router-link to="/register" class="btn">Register</router-link>
        <router-link to="/favourites" class="btn">Reports</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "HomePage"
  };
  </script>
  
  <style scoped>
  .homepage {
    text-align: center;
    background: linear-gradient(135deg, #d0e0f0, #f0f0f0);
    min-height: 100vh;
    padding-top: 80px;
    font-family: "Segoe UI", Tahoma, sans-serif;
  }
  
  .hero h1 {
    font-size: 3rem;
    color: #333;
  }
  
  .hero span {
    color: #3a8bd5;
  }
  
  .hero p {
    color: #666;
    font-size: 1.2rem;
    margin-top: 10px;
  }
  
  .links {
    margin-top: 40px;
  }
  
  .btn {
    display: inline-block;
    background-color: #3a8bd5;
    color: white;
    padding: 12px 24px;
    margin: 10px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: bold;
    transition: background-color 0.3s ease;
  }
  
  .btn:hover {
    background-color: #2a6bb5;
  }
  </style>
  