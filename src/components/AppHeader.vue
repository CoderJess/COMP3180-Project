<template>
  <header>
    <nav class="navbar">
      <div class="container-fluid">
        <a class="navbar-brand" href="/dashboard">Jam + Date</a>
        <div class="nav-routes" id="navbarSupportedContent">
            <!-- <li class="nav-item">
              <RouterLink to="/" class="nav-link" active-class="active">Home</RouterLink>
            </li> -->
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about" active-class="active">About</RouterLink>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" @click.prevent="logout">Logout</a>
            </li>
            <!-- <li class="nav-item">
              <RouterLink to="/register" class="nav-link btn-primary" active-class="active">Register</RouterLink>
            </li> -->
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  data() {
    return {
      userId: null
    }
  },
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem('token');
    }
  },
  created() {
    // Get user ID from stored JWT
    const token = localStorage.getItem('token');
    if (token) {
      try {
        const payload = JSON.parse(atob(token.split('.')[1]));
        this.userId = payload.sub || payload.user_id;
      } catch (e) {
        console.error('Error parsing JWT', e);
      }
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/');
    }
  }
}
</script>

<!-- <script setup>
import { RouterLink } from "vue-router";
</script> -->

<style>
/* Header and Navbar Styles */
header {
  margin: 0; /* Space for fixed navbar */
}

.navbar {
  background-color: #343a40;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  padding: 12px 16px;
  transition: all 0.3s ease;
}

.navbar-brand {
  color: #ffffff;
  font-weight: 700;
  font-size: 1.4rem;
  letter-spacing: 0.5px;
  text-decoration: none;
}

.navbar-brand:hover {
  color: #e8eaf6;
  transform: scale(1.02);
  transition: all 0.2s ease;
}

.navbar-nav {
  list-style-type: none;
  padding-left: 0;
  margin-left: 20px;
}

.nav-item {
  margin: 0 8px;
}

.nav-link {
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 4px;
  transition: all 0.2s ease;
  text-decoration: none;
}

.nav-link:hover {
  color: #ffffff;
  background-color: rgba(255, 255, 255, 0.1);
}

.nav-link.active {
  color: #ffffff;
  background-color: rgba(255, 255, 255, 0.15);
  font-weight: 600;
}

.nav-link.btn-primary {
  background-color: #3949ab;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  margin-left: 8px;
  transition: all 0.3s ease;
}

.nav-link.btn-primary:hover {
  background-color: #303f9f;
  transform: translateY(-2px);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.navbar-toggler {
  border-color: rgba(255, 255, 255, 0.2);
  padding: 6px 10px;
}

.navbar-toggler:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.25); /* Focus ring */
}

.navbar-toggler-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3E%3Cpath stroke='rgba(255, 255, 255, 0.7)' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}

.container-fluid{
  display: flex;
  justify-content: space-between;
}

.nav-routes{
  display: flex;
  justify-content: space-around;
  text-decoration: none;
  list-style-type: none;
}

/* Add responsive adjustments */
@media (max-width: 992px) {
  .navbar-nav {
    margin-top: 15px;
    margin-left: 0;
  }
  
  .nav-item {
    margin: 5px 0;
  }
  
  .nav-link {
    padding: 10px 15px;
    display: block;
  }
}
</style>