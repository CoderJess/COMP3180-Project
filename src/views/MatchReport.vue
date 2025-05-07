<template>
  <div class="match-container">
    <h2 class="match-title">Match Results</h2>
    
    <!-- Status messages -->
    <div v-if="loading" class="match-alert match-alert-info">
      <div class="spinner"></div>
      <span>Finding your matches...</span>
    </div>
    <div v-else-if="error" class="match-alert match-alert-danger">{{ error }}</div>
    <div v-else-if="matches.length === 0" class="match-alert match-alert-warning">No matches found.</div>
    
    <!-- Match Cards -->
    <div class="match-grid">
      <div
        v-for="match in matches"
        :key="match.id"
        class="match-card"
      >
        <div class="match-card-header">
          <h5>{{ match.sex }} - {{ match.race }}</h5>
          <span class="match-name">{{ match.name }}</span>
        </div>
        <div class="match-card-body">
          <div class="match-info-grid">
            <div class="match-info-item">
              <span class="match-label">Parish</span>
              <span class="match-value">{{ match.parish }}</span>
            </div>
            <div class="match-info-item">
              <span class="match-label">Birth Year</span>
              <span class="match-value">{{ match.birth_year }}</span>
            </div>
            <div class="match-info-item">
              <span class="match-label">Cuisine</span>
              <span class="match-value">{{ match.fav_cuisine }}</span>
            </div>
            <div class="match-info-item">
              <span class="match-label">Colour</span>
              <span class="match-value">{{ match.fav_colour }}</span>
            </div>
            <div class="match-info-item">
              <span class="match-label">Subject</span>
              <span class="match-value">{{ match.fav_school_subject }}</span>
            </div>
          </div>
          
          <div class="match-preferences">
            <div class="preference-item" :class="{ 'active': match.political }">
              <span class="preference-icon">{{ match.political ? '✓' : '✗' }}</span>
              <span>Political</span>
            </div>
            <div class="preference-item" :class="{ 'active': match.religious }">
              <span class="preference-icon">{{ match.religious ? '✓' : '✗' }}</span>
              <span>Religious</span>
            </div>
            <div class="preference-item" :class="{ 'active': match.family_oriented }">
              <span class="preference-icon">{{ match.family_oriented ? '✓' : '✗' }}</span>
              <span>Family Oriented</span>
            </div>
          </div>

          <div class="match-fields">
            <span class="match-fields-title">Matched Fields</span>
            <ul class="match-fields-list">
              <li v-for="field in match.matched_fields" :key="field">
                <span class="match-check-icon">✓</span>
                {{ formatField(field) }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '../api'

const route = useRoute()
const matches = ref([])
const loading = ref(false)
const error = ref('')

const profileId = route.params.profileId // passed in URL like /match-report/3

const formatField = (field) => {
  const fieldMap = {
    fav_cuisine: 'Favourite Cuisine',
    fav_colour: 'Favourite Colour',
    fav_school_subject: 'Favourite Subject',
    political: 'Political',
    religious: 'Religious',
    family_oriented: 'Family Oriented',
  }
  return fieldMap[field] || field
}

const fetchMatches = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('token')
    const res = await api.get(`/api/profiles/matches/${profileId}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    matches.value = res.data
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to fetch matches.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchMatches)
</script>

<style>
/* Black, Green and Gold Theme */

/* Container */
.match-container {
  max-width: 1200px;
  margin: 3rem auto;
  padding: 0 1rem;
}

/* Title */
.match-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 2rem;
  color: #242424;
  text-transform: uppercase;
  letter-spacing: 1px;
  position: relative;
}

.match-title:after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 120px;
  height: 3px;
  background: linear-gradient(90deg, #1a5e20, #ffd700, #1a5e20);
}

/* Alerts */
.match-alert {
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
  margin-bottom: 2rem;
  font-weight: 500;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
}

.match-alert-info {
  background-color: #e8f5e9;
  color: #2e7d32;
  border-left: 5px solid #2e7d32;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.match-alert-danger {
  background-color: #ffebee;
  color: #c62828;
  border-left: 5px solid #c62828;
}

.match-alert-warning {
  background-color: #fff8e1;
  color: #ff8f00;
  border-left: 5px solid #ff8f00;
}

/* Spinner */
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid rgba(42, 125, 50, 0.3);
  border-radius: 50%;
  border-top-color: #2a7d32;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Card Grid */
.match-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

/* Cards */
.match-card {
  background-color: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #e6e6e6;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.match-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
}

/* Card Header */
.match-card-header {
  background: linear-gradient(135deg, #000000, #1a5e20);
  color: #fff;
  padding: 1.2rem;
  position: relative;
}

.match-card-header h5 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #ffd700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.match-name {
  display: block;
  font-size: 1.3rem;
  font-weight: 700;
  margin-top: 0.5rem;
}

/* Card Body */
.match-card-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  flex-grow: 1;
}

/* Info Grid */
.match-info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.8rem;
}

.match-info-item {
  display: flex;
  flex-direction: column;
}

.match-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: #666;
  margin-bottom: 0.2rem;
}

.match-value {
  font-weight: 600;
  color: #333;
}

/* Preferences */
.match-preferences {
  display: flex;
  justify-content: space-between;
  margin-top: 0.5rem;
  padding-top: 1rem;
  border-top: 1px solid #e6e6e6;
}

.preference-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.85rem;
  opacity: 0.6;
  transition: opacity 0.3s ease;
}

.preference-item.active {
  opacity: 1;
}

.preference-icon {
  width: 24px;
  height: 24px;
  background-color: #f5f5f5;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #333;
  font-weight: bold;
}

.preference-item.active .preference-icon {
  background-color: #2e7d32;
  color: white;
}

/* Matched Fields */
.match-fields {
  margin-top: 0.5rem;
  padding-top: 1rem;
  border-top: 1px solid #e6e6e6;
}

.match-fields-title {
  font-weight: 600;
  font-size: 0.95rem;
  color: #333;
  display: block;
  margin-bottom: 0.6rem;
}

.match-fields-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.match-fields-list li {
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.match-check-icon {
  color: #ffd700;
  background-color: #1a5e20;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: bold;
}

/* Responsive */
@media (max-width: 768px) {
  .match-grid {
    grid-template-columns: 1fr;
  }
  
  .match-preferences {
    padding: 1rem 0;
  }
}

/* Dark Mode Support */
@media (prefers-color-scheme: dark) {
  .match-card {
    background-color: #1e1e1e;
    border-color: #333;
  }
  
  .match-value {
    color: #e0e0e0;
  }
  
  .match-label {
    color: #aaa;
  }
  
  .match-title {
    color: #e0e0e0;
  }
  
  .preference-icon {
    background-color: #333;
    color: #e0e0e0;
  }
  
  .match-fields-title {
    color: #e0e0e0;
  }
  
  .match-fields-list li {
    color: #d0d0d0;
  }
}
</style>