<template>
  <div class="container mt-4">
    <h2 class="page-title mb-4">Latest Profiles</h2>

    <!-- Search Box -->
    <div class="search-container mb-4">
      <div class="search-row">
        <div class="search-input-container">
          <input
            v-model="searchText"
            type="text"
            placeholder="Search..."
            class="search-input"
          />
        </div>
        <div class="filter-buttons">
          <button class="filter-btn" @click="setFilter('name')">Name</button>
          <button class="filter-btn" @click="setFilter('birth_year')">Birth Year</button>
          <button class="filter-btn" @click="setFilter('sex')">Sex</button>
          <button class="filter-btn" @click="setFilter('race')">Race</button>
          <button class="clear-btn" @click="clearSearch">Clear</button>
        </div>
      </div>
    </div>

    <!-- Profiles Grid -->
    <div class="profiles-grid">
      <div v-for="profile in displayedProfiles" :key="profile.id" class="profile-col">
        <div class="profile-card">
          <div class="img-container">
            <img
              :src="profile.photo ? `${API_BASE_URL}/uploads/${profile.photo}` : `${API_BASE_URL}/uploads/defaultAvatar.png`"
              class="profile-img"
              alt="Profile photo"
            />
          </div>
          <div class="card-body">
            <h5 class="card-title">{{ profile.username }}</h5>
            <p class="card-text"><span class="text-label">Sex:</span> {{ profile.sex }}</p>
            <p class="card-text"><span class="text-label">Race:</span> {{ profile.race }}</p>
            <p class="card-text"><span class="text-label">Parish:</span> {{ profile.parish }}</p>

            <!-- View More Button -->
            <router-link 
              :to="`/profiles/${profile.id}`" 
              class="view-more-btn"
            >
              View More Details
            </router-link>
          </div>

          <div class="card-footer">
            Joined: {{ formatDate(profile.date_joined) }}
          </div>
        </div>
      </div>
    </div>

    <!-- Messages -->
    <div v-if="!loading && displayedProfiles.length === 0" class="message info-message">
      No profiles found.
    </div>
    <div v-if="loading" class="message warning-message">
      Loading profiles...
    </div>
    <div v-if="error" class="message error-message">
      {{ error }}
    </div>
  </div>
</template>



<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../api'
import { API_BASE_URL } from '../config'

// State
const allProfiles = ref([])
const profiles = ref([])
const searchText = ref('')
const filterKey = ref('')
const loading = ref(false)
const error = ref('')
const searching = ref(false)


// Computed
const displayedProfiles = computed(() => profiles.value)


// Methods
const fetchProfiles = async () => {
  loading.value = true
  error.value = ''
  searching.value = false

  try {
    const token = localStorage.getItem('token')
    if (!token) {
      error.value = 'Not authenticated. Please log in.'
      return
    }

    const res = await api.get('/api/profiles', {
      headers: { Authorization: `Bearer ${token}` }
    })

    profiles.value = res.data.slice(0, 4) // Only 4 on default load
  } catch (err) {
    console.error('Error fetching profiles:', err)
    error.value = err.response?.data?.message || 'Failed to load profiles'
  } finally {
    loading.value = false
  }
}


const setFilter = (key) => {
  filterKey.value = key
  if (searchText.value) {
    searchProfiles()
  }
}



const clearSearch = () => {
  filterKey.value = ''
  searchText.value = ''
  fetchProfiles() // goes back to 4 latest
}



function formatDate(dateStr) {
  const options = { year: 'numeric', month: 'short', day: 'numeric' }
  return new Date(dateStr).toLocaleDateString(undefined, options)
}

const searchProfiles = async () => {
  loading.value = true
  error.value = ''
  searching.value = true

  try {
    const token = localStorage.getItem('token')
    if (!token) {
      error.value = 'Not authenticated. Please log in.'
      return
    }

    const params = new URLSearchParams()
    if (filterKey.value && searchText.value) {
      params.append(filterKey.value, searchText.value)
    }

    const res = await api.get(`/api/search?${params.toString()}`, {
      headers: { Authorization: `Bearer ${token}` }
    })

    profiles.value = res.data // Full search results
  } catch (err) {
    console.error('Search failed:', err)
    error.value = err.response?.data?.message || 'Search failed'
  } finally {
    loading.value = false
  }
}




// Lifecycle
onMounted(fetchProfiles)
</script>

<style>
/* Global Styles */
body {
  background-color: #121212;
  color: #e0e0e0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

/* Page Title */
.page-title {
  color: #d4af37; /* Gold */
  font-size: 32px;
  font-weight: 600;
  letter-spacing: 1px;
  border-bottom: 2px solid #1db954; /* Green */
  padding-bottom: 10px;
  margin-bottom: 25px;
}

/* Search Container */
.search-container {
  background-color: #1a1a1a;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 1px solid #333;
  margin-bottom: 30px;
}

.search-row {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  align-items: center;
}

.search-input-container {
  flex: 1;
  min-width: 250px;
}

.search-input {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #333;
  border-radius: 6px;
  background-color: #242424;
  color: white;
  font-size: 14px;
  transition: all 0.3s ease;
}

.search-input:focus {
  border-color: #1db954; /* Green */
  outline: none;
  box-shadow: 0 0 0 2px rgba(29, 185, 84, 0.3);
}

.search-input::placeholder {
  color: #888;
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-btn {
  padding: 10px 15px;
  background-color: #333;
  color: #d4af37; /* Gold */
  border: 1px solid #d4af37; /* Gold */
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.filter-btn:hover {
  background-color: #444;
  transform: translateY(-2px);
}

.clear-btn {
  padding: 10px 15px;
  background-color: rgba(169, 68, 66, 0.2);
  color: #d4af37; /* Gold */
  border: 1px solid #d4af37; /* Gold */
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.clear-btn:hover {
  background-color: rgba(169, 68, 66, 0.3);
  transform: translateY(-2px);
}

/* Profiles Grid */
.profiles-grid {
  display: flex;
  flex-wrap: wrap;
  margin: -10px;
}

.profile-col {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
}

@media (min-width: 576px) {
  .profile-col {
    width: 50%;
  }
}

@media (min-width: 992px) {
  .profile-col {
    width: 25%;
  }
}

.profile-card {
  background-color: #1a1a1a;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
  border: 1px solid #333;
  position: relative;
}

.profile-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  border-color: #1db954; /* Green border on hover */
}

.profile-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, #1db954, #d4af37); /* Green to gold gradient */
}

.img-container {
  width: 100%;
  aspect-ratio: 1 / 1; /* Square image container */
  overflow: hidden;
}

.profile-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.profile-card:hover .profile-img {
  transform: scale(1.05);
}

.card-body {
  padding: 15px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-title {
  color: #d4af37; /* Gold */
  font-size: 18px;
  margin-bottom: 12px;
  font-weight: 600;
}

.card-text {
  margin-bottom: 8px;
  font-size: 14px;
  color: #e0e0e0;
}

.text-label {
  color: #1db954; /* Green */
  font-weight: 600;
}

.view-more-btn {
  display: inline-block;
  background: transparent;
  color: #1db954; /* Green */
  border: 1px solid #1db954; /* Green */
  padding: 8px 15px;
  border-radius: 6px;
  margin-top: auto;
  text-align: center;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
  cursor: pointer;
}

.view-more-btn:hover {
  background-color: #1db954; /* Green */
  color: #fff;
}

.card-footer {
  background-color: #242424;
  padding: 10px 15px;
  text-align: right;
  font-size: 12px;
  color: #888;
  border-top: 1px solid #333;
}

/* Messages */
.message {
  padding: 15px;
  border-radius: 8px;
  margin: 20px 0;
  text-align: center;
  font-size: 16px;
}

.info-message {
  background-color: rgba(51, 102, 153, 0.2);
  color: #d4af37; /* Gold */
  border: 1px solid #d4af37; /* Gold */
}

.warning-message {
  background-color: rgba(204, 153, 0, 0.2);
  color: #d4af37; /* Gold */
  border: 1px solid #d4af37; /* Gold */
}

.error-message {
  background-color: rgba(169, 68, 66, 0.2);
  color: #d4af37; /* Gold */
  border: 1px solid #d4af37; /* Gold */
}
</style>