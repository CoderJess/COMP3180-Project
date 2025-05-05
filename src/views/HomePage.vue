<template>
  <div class="homepage">
    <div class="hero">
      <h1>Welcome to <span>Jam-Date</span></h1>
      <p>Find your perfect match. Simple, fun and secure.</p>
    </div>
    
    <div class="links">
      <router-link to="/login" class="btn">Login</router-link>
      <router-link to="/register" class="btn">Register</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage"
};
</script>

<style>
:root {
  --black: #121212;
  --green: #1e8f4e;
  --gold: #d4af37;
  --light-gold: #f5e7b8;
  --dark-green: #146b3a;
}

.homepage {
  text-align: center;
  background: linear-gradient(135deg, var(--black), #1a1a1a);
  min-height: 100vh;
  padding-top: 80px;
  font-family: "Segoe UI", Tahoma, sans-serif;
  color: var(--light-gold);
}

.hero h1 {
  font-size: 3.5rem;
  color: var(--light-gold);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  margin-bottom: 0.5rem;
}

.hero span {
  color: var(--gold);
  font-weight: bold;
}

.hero p {
  color: white;
  font-size: 1.3rem;
  margin-top: 10px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.links {
  margin-top: 60px;
}

.btn {
  display: inline-block;
  background-color: var(--green);
  color: white;
  padding: 14px 30px;
  margin: 10px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
  border: 2px solid transparent;
  font-size: 1.1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.btn:hover {
  background-color: var(--dark-green);
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  border: 2px solid var(--gold);
}

.btn:active {
  transform: translateY(1px);
}
</style>