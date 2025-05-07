<template>
  <div class="container mt-5">
    <!-- Page Header -->
    <div class="page-header text-center mb-4">
      <h3 class="section-title">{{ user.name }}'s Profile</h3>
    </div>
    
    <!-- User Info Section -->
    <div v-if="loading" class="alert loading-alert text-center py-3">
      <i class="bi bi-hourglass-split me-2"></i>Loading user profile...
    </div>
    <div v-else-if="error" class="alert error-alert text-center py-3">
      <i class="bi bi-exclamation-triangle me-2"></i>{{ error }}
    </div>
    <div v-else>
      <div class="user-card card mb-4 shadow">
        <div class="card-header user-header py-3">
          <h4 class="mb-0"><i class="bi bi-person-circle me-2"></i>User Profile</h4>
        </div>
        <div class="row g-0">
          <div class="col-md-4 d-flex justify-content-center align-items-center p-4 user-photo-section">
            <div class="user-photo-container">
              <img
                :src="user.photo ? `${API_BASE_URL}/uploads/${user.photo}` : `${API_BASE_URL}/uploads/defaultAvatar.png`"
                class="rounded-circle user-img"
                alt="User Photo"
              />
              <div class="member-badge">
                <i class="bi bi-calendar3 me-1"></i>Member since {{ formatDateYear(user.date_joined) }}
              </div>
            </div>
          </div>
          <div class="col-md-8">
            <div class="card-body p-4">
              <h4 class="user-name">{{ user.name }}</h4>
              
              <div class="row mb-3">
                <div class="col-md-6">
                  <div class="info-panel rounded">
                    <span class="info-label">EMAIL ADDRESS</span>
                    <div class="d-flex align-items-center mt-1">
                      <i class="bi bi-envelope me-2"></i>
                      <span>{{ user.email }}</span>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="info-panel rounded">
                    <span class="info-label">ACCOUNT STATUS</span>
                    <div class="d-flex align-items-center mt-1">
                      <i class="bi bi-check-circle-fill me-2 status-icon"></i>
                      <span>Active Member</span>
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="d-flex justify-content-end mt-3">
                <button class="btn edit-btn me-2">
                  <i class="bi bi-pencil-square me-1"></i>Edit Profile
                </button>
                <button class="btn create-btn">
                  <i class="bi bi-plus-circle me-1"></i>Create New Profile
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- All Profiles Created by This User -->
      <div class="mb-4 d-flex justify-content-between align-items-center">
        <h5 class="profile-section-title">My Profiles</h5>
        <span class="profile-count-badge">
          {{ profiles.length }} Profile(s)
        </span>
      </div>
      
      <div v-if="profiles.length === 0" class="empty-profiles-alert text-center py-4 mb-4">
        <i class="bi bi-info-circle me-2"></i>You haven't created any profiles yet.
        <div class="mt-3">
          <button class="btn primary-btn">
            <i class="bi bi-plus-circle me-1"></i>Create Your First Profile
          </button>
        </div>
      </div>
      
      <div class="row">
        <div v-for="profile in profiles" :key="profile.id" class="col-md-4 mb-4">
          <div class="profile-card card h-100 shadow-sm">
            <div class="card-header profile-header py-2">
              <div class="d-flex justify-content-between align-items-center">
                <span>{{ profile.sex }} - {{ profile.race }}</span>
                <span class="profile-id-badge">ID: {{ profile.id }}</span>
              </div>
            </div>
            <div class="card-body p-3">
              <div class="mb-3 detail-panel rounded">
                <div class="row g-2">
                  <div class="col-6">
                    <span class="detail-label">PARISH</span>
                    <div class="fw-bold">{{ profile.parish }}</div>
                  </div>
                  <div class="col-6">
                    <span class="detail-label">BIRTH YEAR</span>
                    <div class="fw-bold">{{ profile.birth_year }}</div>
                  </div>
                </div>
              </div>
              
              <div class="mb-3">
                <div class="d-flex mb-2">
                  <div class="color-dot" :style="{backgroundColor: profile.fav_colour}"></div>
                  <span class="profile-detail">
                    <span class="detail-title">Fav. Colour:</span> <span class="fav">{{ profile.fav_colour }}</span>
                  </span>
                </div>
                <div class="profile-detail">
                  <span class="detail-title">🍴 Fav. Cuisine:</span> <span class="fav">{{ profile.fav_cuisine }}</span>
                </div>
              </div>
              
              <div class="d-flex mt-3">
                <router-link 
                  :to="`/profiles/${profile.id}`" 
                  class="btn view-btn me-2 flex-grow-1"
                >
                  <i class="bi bi-eye me-1"></i>View
                </router-link>
                <router-link 
                  :to="`/match-report/${profile.id}`" 
                  class="btn match-btn flex-grow-1"
                >
                  <i class="bi bi-arrow-through-heart me-1"></i>Match
                </router-link>
              </div>
            </div>
            <div class="card-footer profile-footer text-end py-2">
              <i class="bi bi-calendar2 me-1"></i>Created: {{ formatDate(profile.created_at) }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import api from '../api'
import { API_BASE_URL } from '../config'

const route = useRoute()
const userStr = localStorage.getItem('user')
const userParse = JSON.parse(userStr)
const userId = userParse.id 

console.log('User ID:', userId)

const user = ref({})
const profiles = ref([])
const loading = ref(true)
const error = ref('')

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}

const formatDateYear = (dateStr) => {
  return new Date(dateStr).getFullYear()
}

const fetchUserAndProfiles = async () => {
  try {
    const token = localStorage.getItem('token')
    if (!token) throw new Error('Not authenticated')

    const userRes = await api.get(`/api/users/${userId}`, {
      headers: { Authorization: `Bearer ${token}` }
    })

    const profileRes = await api.get(`/api/users/${userId}/profiles`, {
      headers: { Authorization: `Bearer ${token}` }
    })

    user.value = userRes.data
    profiles.value = profileRes.data
  } catch (err) {
    error.value = err.response?.data?.message || 'Could not load profile data.'
  } finally {
    loading.value = false
  }
}

onMounted(fetchUserAndProfiles)
</script>

<style>
/* Theme Colors */
:root {
  --theme-black: #1a1a1a;
  --theme-green: #2e8b57;
  --theme-gold: #d4af37;
  --theme-pale-green: #f0f5f1;
  --theme-pale-gold: #f0e6c8;
  --theme-error: #8b0000;
  --theme-light-text: #6c757d;
}

/* Page Header */
.section-title {
  color: var(--theme-green);
  border-bottom: 2px solid var(--theme-gold);
  display: inline-block;
  padding-bottom: 8px;
}

/* Alerts */
.loading-alert {
  background-color: var(--theme-pale-gold);
  color: var(--theme-black);
}

.error-alert {
  background-color: #f7e9c3;
  color: var(--theme-error);
}

.fav{
  color: var(--theme-gold);
}

/* User Card */
.user-card {
  border: none;
  overflow: hidden;
}

.user-header {
  background-color: var(--theme-black);
  color: var(--theme-gold);
}

.user-photo-section {
  background-color: var(--theme-pale-green);
}

.user-photo-container {
  position: relative;
  width: 150px;
  height: 150px;
}

.user-img {
  border: 4px solid var(--theme-green);
  width: 150px;
  height: 150px;
  object-fit: cover;
}

.member-badge {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  padding: 4px 12px;
  border-radius: 20px;
  background-color: var(--theme-black);
  color: var(--theme-gold);
  font-size: 0.8rem;
  white-space: nowrap;
}

.user-name {
  color: var(--theme-green);
  border-bottom: 1px solid #e9ecef;
  padding-bottom: 10px;
  margin-bottom: 16px;
}

.info-panel {
  padding: 12px;
  background-color: var(--theme-pale-green);
}

.info-label {
  color: var(--theme-green);
  font-size: 0.8rem;
}

.status-icon {
  color: var(--theme-green);
}

/* Buttons */
.edit-btn {
  background-color: var(--theme-green);
  color: white;
}

.create-btn {
  background-color: var(--theme-black);
  color: var(--theme-gold);
  border: 1px solid var(--theme-gold);
}

.primary-btn {
  background-color: var(--theme-green);
  color: white;
}

.btn:hover {
  opacity: 0.9;
  transform: translateY(-2px);
  transition: all 0.2s;
}

/* Profile Section */
.profile-section-title {
  color: var(--theme-green);
  border-left: 4px solid var(--theme-gold);
  padding-left: 10px;
}

.profile-count-badge {
  background-color: var(--theme-black);
  color: var(--theme-gold);
  padding: 4px 8px;
  border-radius: 4px;
}

.empty-profiles-alert {
  background-color: var(--theme-pale-gold);
  color: var(--theme-black);
  border-left: 4px solid var(--theme-gold);
}

/* Profile Cards */
.profile-card {
  border: none;
  overflow: hidden;
}

.profile-header {
  background-color: var(--theme-black);
  color: var(--theme-gold);
}

.profile-id-badge {
  background-color: var(--theme-green);
  color: white;
  padding: 2px 6px;
  border-radius: 20px;
  font-size: 0.75rem;
}

.detail-panel {
  padding: 8px;
  background-color: var(--theme-pale-green);
  margin-bottom: 12px;
}

.detail-label {
  color: var(--theme-green);
  font-size: 0.75rem;
}

.color-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  margin-right: 8px;
}

.profile-detail {
  font-size: 0.85rem;
}

.detail-title {
  color: var(--theme-green);
}

.view-btn {
  background-color: var(--theme-black);
  color: var(--theme-gold);
  border: 1px solid var(--theme-gold);
}

.match-btn {
  background-color: var(--theme-green);
  color: white;
}

.profile-footer {
  background-color: var(--theme-pale-green);
  color: var(--theme-light-text);
  font-size: 0.75rem;
}
</style>