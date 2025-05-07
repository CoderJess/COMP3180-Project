<template>
  <div class="login-container">
    <div class="form-box">
      <h2 class="title">Login</h2>
      <form @submit.prevent="login">
        <div class="input-group">
          <input v-model="username" placeholder="Username" required />
        </div>
        <div class="input-group">
          <input v-model="password" type="password" placeholder="Password" required />
        </div>
        <button type="submit">Login</button>
      </form>

      <!-- Registration Link -->
      <p class="register-link">
        Don't have an account?
        <router-link to="/register" class="register-btn">Register Here</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import api from '../api';  // Adjust the path as necessary
import { API_BASE_URL } from '../config';

// Ensure cookies (for CSRF) are always sent
api.defaults.withCredentials = true;

export default {
  data() {
    return {
      username: '',
      password: '',
      csrfToken: ''
    };
  },

  async mounted() {
    try {
      console.log("VITE_API_URL =", API_BASE_URL);
      console.log("mounted hook running...");
      const { data } = await api.get('/api/csrf-token');
      console.log("CSRF token fetched:", data.csrf_token);
      this.csrfToken = data.csrf_token;
    } catch (e) {
      console.error('Could not fetch CSRF token:', e);
    }
  },

  methods: {
    async login() {
      try {
        console.log("Login button clicked");

        // Format request correctly for Flask-WTF
        const formData = new URLSearchParams();
        formData.append("username", this.username);
        formData.append("password", this.password);

        console.log("Attempting login with URL encoded format:", formData.toString());

        const response = await api.post("/api/auth/login", formData, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",  // Flask-WTF expects this format
            "X-CSRFToken": this.csrfToken  // Include CSRF token
          }
        });

        const token = response.data.token;
        console.log("Token received:", token);
        localStorage.setItem("token", token);
        localStorage.setItem("user", JSON.stringify(response.data.user));
        api.defaults.headers.common["Authorization"] = `Bearer ${token}`;

        console.log("Login successful, redirecting...");
        this.$router.push("/");
      }
      catch (error) {
        console.error("Login error:", error.response?.data || error);
        alert(error.response?.data?.message || "Login failed");
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background-color: #121212; /* Dark background */
  color: white;
}

.form-box {
  background-color: #1a1a1a; /* Slightly lighter black for contrast */
  padding: 40px 25px;
  border-radius: 12px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  width: 100%;
  max-width: 320px;
  text-align: center;
  border: 1px solid #2d2d2d;
  position: relative;
  overflow: hidden;
}

.form-box::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #1db954, #d4af37); /* Green to gold gradient accent */
}

.title {
  color: #d4af37; /* Gold color for the title */
  font-size: 28px;
  margin-bottom: 25px;
  font-weight: 600;
  letter-spacing: 1px;
}

.input-group {
  position: relative;
  margin-bottom: 20px;
}

input {
  display: block;
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #333;
  border-radius: 8px;
  font-size: 14px;
  background-color: #242424;
  color: white;
  transition: all 0.3s ease;
}

input:focus {
  border-color: #1db954; /* Green border on focus */
  outline: none;
  box-shadow: 0 0 0 2px rgba(29, 185, 84, 0.3);
}

input::placeholder {
  color: #888;
}

button {
  width: 100%;
  padding: 12px;
  background-color: #1db954; /* Green button */
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 10px;
}

button:hover {
  background-color: #19a349; /* Slightly darker green on hover */
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(29, 185, 84, 0.2);
}

button:active {
  transform: translateY(0);
}

.register-link {
  margin-top: 25px;
  text-align: center;
  font-size: 14px;
  color: #aaa;
}

.register-btn {
  color: #d4af37; /* Gold color for the register link */
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s;
}

.register-btn:hover {
  color: #f5d76e; /* Lighter gold on hover */
  text-decoration: underline;
}
</style>