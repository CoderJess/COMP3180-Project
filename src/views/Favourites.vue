<template>
  <div class="favorites-container">
    <h2 class="favorites-title">Favourites Report</h2>

    <!-- Section 1: Top 20 Most Favoured Users -->
    <div class="favorites-section">
      <div class="section-header">
        <h3 class="section-title">Most Popular Profiles</h3>
        <div class="section-divider"></div>
      </div>
      
      <div class="favorites-grid">
        <div
          v-for="user in topFavoured"
          :key="user.id"
          class="favorite-card"
        >
          <div class="favorite-spotlight"></div>
          <div class="card-content">
            <div class="avatar-container">
              <div class="avatar-frame">
                <img
                  :src="user.photo ? `${API_BASE_URL}/uploads/${user.photo}` : `${API_BASE_URL}/uploads/defaultAvatar.png`"
                  alt="Profile photo"
                  class="avatar-image"
                />
              </div>
              <div class="favorite-badge">{{ user.favourite_count }}</div>
            </div>
            <div class="favorite-info">
              <h4 class="favorite-name">{{ user.username }}</h4>
              <p class="favorite-meta">Favoured {{ user.favourite_count }} time{{ user.favourite_count !== 1 ? 's' : '' }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 2: Users You Have Favourited -->
    <div class="favorites-section">
      <div class="section-header">
        <h3 class="section-title">Your Favourite Profiles</h3>
        <div class="section-divider"></div>
      </div>
      
      <div class="favorites-grid">
        <div
          v-for="user in favourites"
          :key="user.id"
          class="favorite-card"
        >
          <div class="favorite-personal"></div>
          <div class="card-content">
            <div class="avatar-container">
              <div class="avatar-frame your-favorites">
                <img
                  :src="user.photo ? `${API_BASE_URL}/uploads/${user.photo}` : `${API_BASE_URL}/uploads/defaultAvatar.png`"
                  alt="Profile photo"
                  class="avatar-image"
                />
              </div>
              <div class="heart-icon">♥</div>
            </div>
            <div class="favorite-info">
              <h4 class="favorite-name">{{ user.username }}</h4>
              <p class="favorite-meta">{{ user.email }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-overlay">
      <div class="spinner">
        <div class="spinner-inner"></div>
      </div>
      <p>Loading favourites...</p>
    </div>
    
    <!-- Error Message -->
    <div v-if="error" class="error-message">
      <div class="error-icon">!</div>
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import api from '../api'
import { API_BASE_URL } from '../config';

const userStr = localStorage.getItem('user')
const user = JSON.parse(userStr)

const favourites = ref([])
const topFavoured = ref([])
const loading = ref(false)
const error = ref('')

const fetchData = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('token')
    if (!token) throw new Error('Not authenticated')

    const [topRes, myRes] = await Promise.all([
      api.get('/api/users/favourites/20', {
        headers: { Authorization: `Bearer ${token}` }
      }),
      api.get(`/api/users/${user.id}/favourites`, {
        headers: { Authorization: `Bearer ${token}` }
      })
    ])

    topFavoured.value = topRes.data
    favourites.value = myRes.data
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to load favourites'
  } finally {
    loading.value = false
  }
}

onMounted(fetchData)
</script>

<style>
/* Black, Green and Gold Theme for Favorites Report */

/* Container */
.favorites-container {
  max-width: 1200px;
  margin: 3rem auto;
  padding: 0 1rem;
  position: relative;
}

/* Page Title */
.favorites-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 3rem;
  color: #242424;
  text-transform: uppercase;
  letter-spacing: 1px;
  position: relative;
}

.favorites-title:after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 120px;
  height: 3px;
  background: linear-gradient(90deg, #1a5e20, #ffd700, #1a5e20);
}

/* Section Styling */
.favorites-section {
  margin-bottom: 4rem;
}

.section-header {
  margin-bottom: 2rem;
  position: relative;
}

.section-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: #1a5e20;
  position: relative;
  display: inline-block;
  padding-right: 1.5rem;
}

.section-title:before {
  content: '★';
  color: #ffd700;
  margin-right: 0.75rem;
}

.section-divider {
  height: 2px;
  background: linear-gradient(90deg, #000 0%, rgba(0,0,0,0.1) 100%);
  margin-top: 0.5rem;
}

/* Grid Layout */
.favorites-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1.5rem;
}

/* Card Styling */
.favorite-card {
  position: relative;
  background-color: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #e6e6e6;
  height: 100%;
  min-height: 260px;
}

.favorite-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
}

/* Top section accent colors */
.favorite-spotlight {
  height: 8px;
  background: linear-gradient(90deg, #000000, #1a5e20);
}

.favorite-personal {
  height: 8px;
  background: linear-gradient(90deg, #1a5e20, #ffd700);
}

/* Card Content */
.card-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  text-align: center;
}

/* Avatar Styling */
.avatar-container {
  position: relative;
  margin-bottom: 1rem;
}

.avatar-frame {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: linear-gradient(135deg, #000000, #1a5e20);
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.avatar-frame.your-favorites {
  background: linear-gradient(135deg, #1a5e20, #ffd700);
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

/* Favorite Count Badge */
.favorite-badge {
  position: absolute;
  bottom: 5px;
  right: 0;
  background-color: #ffd700;
  color: #000;
  border: 2px solid #1a5e20;
  border-radius: 50%;
  width: 35px;
  height: 35px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

/* Heart Icon */
.heart-icon {
  position: absolute;
  bottom: 5px;
  right: 0;
  background-color: #ffd700;
  color: #1a5e20;
  border: 2px solid #1a5e20;
  border-radius: 50%;
  width: 35px;
  height: 35px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.2rem;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

/* Info Section */
.favorite-info {
  width: 100%;
}

.favorite-name {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #333;
}

.favorite-meta {
  font-size: 0.85rem;
  color: #666;
  margin: 0;
}

/* Loading Spinner */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255, 255, 255, 0.8);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.spinner {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: conic-gradient(#1a5e20 0%, #ffd700);
  animation: spin 1.5s linear infinite;
  display: flex;
  align-items: center;
  justify-content: center;
}

.spinner-inner {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: white;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loading-overlay p {
  margin-top: 1rem;
  font-weight: 500;
  color: #1a5e20;
}

/* Error Message */
.error-message {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 1rem;
  background-color: #ffe6e6;
  border-left: 5px solid #ff3333;
  border-radius: 8px;
  margin: 2rem 0;
}

.error-icon {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #ff3333;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.2rem;
}

.error-message p {
  margin: 0;
  font-weight: 500;
}

/* Responsive Adjustments */
@media (max-width: 991px) {
  .favorites-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

@media (max-width: 767px) {
  .favorites-grid {
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  }
  
  .favorites-title {
    font-size: 2rem;
  }
  
  .section-title {
    font-size: 1.5rem;
  }
  
  .avatar-frame {
    width: 100px;
    height: 100px;
  }
}

@media (max-width: 480px) {
  .favorites-grid {
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  }
  
  .avatar-frame {
    width: 80px;
    height: 80px;
  }
  
  .favorite-badge, .heart-icon {
    width: 28px;
    height: 28px;
    font-size: 0.8rem;
  }
  
  .favorite-name {
    font-size: 1rem;
  }
}

/* Dark Mode Support */
@media (prefers-color-scheme: dark) {
  .favorites-title {
    color: #e0e0e0;
  }
  
  .favorite-card {
    background-color: #1e1e1e;
    border-color: #333;
  }
  
  .favorite-name {
    color: #e0e0e0;
  }
  
  .favorite-meta {
    color: #aaa;
  }
  
  .loading-overlay {
    background-color: rgba(0, 0, 0, 0.7);
  }
  
  .spinner-inner {
    background: #1e1e1e;
  }
  
  .loading-overlay p {
    color: #fff;
  }
  
  .section-divider {
    background: linear-gradient(90deg, #ffd700 0%, rgba(255, 215, 0, 0.1) 100%);
  }
}
</style>