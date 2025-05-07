<template>
  <header>
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Jam + Date</a>

        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="d-flex ms-auto align-items-center gap-3">
            <RouterLink to="/about" class="nav-link">About</RouterLink>
            <RouterLink to="/profiles/new" class="nav-link">
              Create Profile
            </RouterLink>
            <RouterLink to="/profiles/favourites" class="nav-link">Favourites</RouterLink>
            <button class="nav-link" @click="logout">
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>

    <div class="subheader container-fluid px-4 py-2">
      <RouterLink :to="`/users/${user.id}`" class="subheader-link">My Profile</RouterLink>
      <span class="divider">/</span>
      <span class="current-page">{{ currentPage }}</span>
    </div>
  </header>
</template>

<script setup>
import api from '../api'
import { useRouter } from 'vue-router'

const userStr = localStorage.getItem('user')
// if (!userStr) throw new Error('user data missing')
let user = { id: null, name: null };
if (userStr) {
  user = JSON.parse(userStr)
}

// console.log('User ID:', user.id)

const router = useRouter()

async function logout() {
  try {
    const token = localStorage.getItem('token')
    if (!token) throw new Error('JWT token missing')

    await api.post('/api/auth/logout', {}, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    // Clean up and redirect
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    router.push('/login')
  } catch (err) {
    console.error('Logout failed:', err)
  }
}
</script>

<style>
/* Navbar Base */
.navbar {
  background: linear-gradient(135deg, #331f12 0%, #5a3d28 100%);
  padding: 1rem 1.5rem;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.2);
}

/* Brand Name */
.navbar-brand {
  color: #ffd700 !important;
  font-weight: 800;
  font-size: 1.7rem;
  text-decoration: none;
  letter-spacing: 1px;
  text-transform: uppercase;
  position: relative;
  padding-bottom: 3px;
}

.navbar-brand::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #ffd700 30%, #ffd700 70%, transparent);
}

/* Navigation Links */
.navbar .nav-link {
  color: #f0f0f0 !important;
  font-weight: 500;
  margin: 0 12px;
  padding: 8px 0;
  position: relative;
  transition: all 0.3s ease;
}

.navbar .nav-link::after {
  content: "";
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #ffc107;
  transition: width 0.3s ease;
}

.navbar .nav-link:hover::after {
  width: 100%;
}

.navbar .nav-link:hover {
  color: #ffffff !important;
  transform: translateY(-2px);
  text-decoration: none;
}

/* Button Styling */
/* .btn {
  border-radius: 25px;
  padding: 0.5rem 1.2rem;
  transition: all 0.3s ease;
  font-weight: 600;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
} */

/* .btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
} */

/* Create Profile Button */
/* .btn-outline-warning {
  border: 2px solid #ffc107;
  color: #ffc107;
  background: rgba(255, 193, 7, 0.05);
} */

/* .btn-outline-warning:hover {
  background: #ffc107;
  color: #2f2f2f;
} */

/* Favorites Button */
/* .btn-outline-info {
  border: 2px solid #0dcaf0;
  color: #0dcaf0;
  background: rgba(13, 202, 240, 0.05);
} */

/* .btn-outline-info:hover {
  background: #0dcaf0;
  color: #2f2f2f;
} */

/* Logout Button */
/* .btn-outline-light {
  border: 2px solid #f8f9fa;
  color: #f8f9fa;
  background: rgba(248, 249, 250, 0.05);
}

.btn-outline-light:hover {
  background: #f8f9fa;
  color: #2f2f2f;
} */

/* Navbar Toggle Button */
.navbar-toggler {
  border: none;
  padding: 0;
  width: 30px;
  height: 20px;
  position: relative;
  cursor: pointer;
  background: transparent;
}

.navbar-toggler-icon {
  background-image: none !important;
  background-color: #ffd700;
  height: 2px;
  width: 100%;
  position: absolute;
  border-radius: 1px;
  transition: all 0.3s ease;
}

.navbar-toggler-icon:before,
.navbar-toggler-icon:after {
  content: '';
  background-color: #ffd700;
  height: 2px;
  width: 100%;
  position: absolute;
  border-radius: 1px;
  transition: all 0.3s ease;
  left: 0;
}

.navbar-toggler-icon:before {
  top: -8px;
}

.navbar-toggler-icon:after {
  bottom: -8px;
}

.navbar-toggler[aria-expanded="true"] .navbar-toggler-icon {
  background-color: transparent;
}

.navbar-toggler[aria-expanded="true"] .navbar-toggler-icon:before {
  transform: rotate(45deg);
  top: 0;
}

.navbar-toggler[aria-expanded="true"] .navbar-toggler-icon:after {
  transform: rotate(-45deg);
  bottom: 0;
}

/* Subheader */
.subheader {
  background: linear-gradient(90deg, #6b5a45 0%, #8e7b67 50%, #6b5a45 100%);
  color: #f5f5f5;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  width: 90%;
  height: 48px;
  border-bottom-left-radius: 30px;
  border-bottom-right-radius: 30px;
  padding: 0 2rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  position: relative;
  z-index: 10;
  margin: 0 auto;
}

.subheader-link {
  color: #ffd700;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.3s ease;
}

.subheader-link:hover {
  text-decoration: none;
  color: #ffffff;
  transform: translateY(-1px);
  text-shadow: 0 0 5px rgba(255, 215, 0, 0.5);
}

.divider {
  color: #d4c5b3;
  font-weight: 300;
}

.current-page {
  font-weight: 500;
}

/* Button spacing in navbar */
.d-flex.ms-auto.align-items-center.gap-3 {
  gap: 12px !important;
}

/* Responsive adjustments */
@media (max-width: 991.98px) {
  .navbar {
    padding: 0.8rem 1rem;
  }
  
  .navbar-collapse {
    background: rgba(47, 47, 47, 0.95);
    margin-top: 1rem;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  }
  
  .d-flex.ms-auto.align-items-center.gap-3 {
    flex-direction: column;
    align-items: flex-start !important;
    gap: 15px !important;
  }
  
  .navbar .nav-link,
  .btn {
    width: 100%;
    text-align: left;
    margin: 5px 0;
  }
  
  .subheader {
    width: 95%;
    height: 40px;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
  }
}
</style>