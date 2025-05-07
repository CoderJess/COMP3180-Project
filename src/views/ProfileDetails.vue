<template>
  <div class="container mt-5">
    <div v-if="loading" class="alert text-center py-3" style="background-color: #f0e6c8; color: #1a1a1a;">
      <i class="bi bi-hourglass-split me-2"></i>Loading profile...
    </div>
    <div v-else-if="error" class="alert text-center py-3" style="background-color: #f7e9c3; color: #8b0000;">
      {{ error }}
    </div>
    <div v-else class="card shadow-lg mx-auto" style="max-width: 600px; border: none;">
      <div class="card-header text-center py-3" style="background-color: #1a1a1a; color: #d4af37;">
        <h3 class="mb-0">User Profile</h3>
      </div>
      <div class="row g-0">
        <div class="col-md-5 position-relative">
          <div style="background-color: #1a1a1a; height: 100%;">
            <img
              :src="profile.photo ? `${API_BASE_URL}/uploads/${profile.photo}` : `${API_BASE_URL}/uploads/defaultAvatar.png`"
              class="img-fluid h-100 w-100"
              alt="Profile Picture"
              style="object-fit: cover; opacity: 0.9;"
            />
            <div class="position-absolute bottom-0 start-0 w-100 p-2 text-center" 
                 style="background-color: rgba(26, 26, 26, 0.7); color: #d4af37;">
              <h5 class="mb-0">{{ profile.username }}</h5>
              <small>Member since {{ formatDate(profile.date_joined) }}</small>
            </div>
          </div>
        </div>
        <div class="col-md-7">
          <div class="card-body" style="background-color: #f8f9fa;">
            <div class="mb-4 p-3" style="background-color: #f0f5f1; border-left: 4px solid #2e8b57;">
              <h6 class="text-muted mb-1" style="color: #2e8b57;">Bio</h6>
              <p class="mb-0">{{ profile.biography || 'No biography available' }}</p>
            </div>
            
            <div class="row g-2">
              <div class="col-6">
                <div class="p-2 rounded" style="background-color: #f0f5f1;">
                  <span class="d-block" style="color: #2e8b57; font-size: 0.8rem;">PARISH</span>
                  <span class="fw-bold">{{ profile.parish }}</span>
                </div>
              </div>
              <div class="col-6">
                <div class="p-2 rounded" style="background-color: #f0f5f1;">
                  <span class="d-block" style="color: #2e8b57; font-size: 0.8rem;">SEX</span>
                  <span class="fw-bold">{{ profile.sex }}</span>
                </div>
              </div>
              <div class="col-6">
                <div class="p-2 rounded" style="background-color: #f0f5f1;">
                  <span class="d-block" style="color: #2e8b57; font-size: 0.8rem;">RACE</span>
                  <span class="fw-bold">{{ profile.race }}</span>
                </div>
              </div>
              <div class="col-6">
                <div class="p-2 rounded" style="background-color: #f0f5f1;">
                  <span class="d-block" style="color: #2e8b57; font-size: 0.8rem;">BIRTH YEAR</span>
                  <span class="fw-bold">{{ profile.birth_year }}</span>
                </div>
              </div>
              <div class="col-6">
                <div class="p-2 rounded" style="background-color: #f0f5f1;">
                  <span class="d-block" style="color: #2e8b57; font-size: 0.8rem;">HEIGHT</span>
                  <span class="fw-bold">{{ profile.height }} in</span>
                </div>
              </div>
              <div class="col-6">
                <div class="p-2 rounded" style="background-color: #f0f5f1;">
                  <span class="d-block" style="color: #2e8b57; font-size: 0.8rem;">FAV CUISINE</span>
                  <span class="fw-bold">{{ profile.fav_cuisine }}</span>
                </div>
              </div>
            </div>
            
            <div class="row g-2 mt-2">
              <div class="col-6">
                <div class="p-2 rounded" style="background-color: #f0f5f1;">
                  <span class="d-block" style="color: #2e8b57; font-size: 0.8rem;">FAV COLOR</span>
                  <span class="fw-bold">{{ profile.fav_colour }}</span>
                </div>
              </div>
              <div class="col-6">
                <div class="p-2 rounded" style="background-color: #f0f5f1;">
                  <span class="d-block" style="color: #2e8b57; font-size: 0.8rem;">SUBJECT</span>
                  <span class="fw-bold">{{ profile.fav_school_sibject }}</span>
                </div>
              </div>
            </div>
            
            <div class="d-flex gap-2 mt-3 mb-2">
              <div class="badge" :style="`background-color: ${profile.political ? '#2e8b57' : '#e9ecef'}; color: ${profile.political ? 'white' : '#6c757d'};`">
                Political
              </div>
              <div class="badge" :style="`background-color: ${profile.religious ? '#2e8b57' : '#e9ecef'}; color: ${profile.religious ? 'white' : '#6c757d'};`">
                Religious
              </div>
              <div class="badge" :style="`background-color: ${profile.family_oriented ? '#2e8b57' : '#e9ecef'}; color: ${profile.family_oriented ? 'white' : '#6c757d'};`">
                Family Oriented
              </div>
            </div>
           
            <div class="d-flex justify-content-between mt-4">
              <button @click="favouriteUser" class="btn" style="background-color: #1a1a1a; color: #d4af37; border: 1px solid #d4af37;">
                <i class="bi bi-heart-fill me-1"></i> Favourite
              </button>
              <button class="btn" style="background-color: #2e8b57; color: white;" disabled>
                <i class="bi bi-envelope-fill me-1"></i> Contact
              </button>
            </div>
            <p v-if="favMessage" class="mt-2 p-2 rounded" style="background-color: #d4f1d9; color: #2e8b57;">
              <i class="bi bi-check-circle me-1"></i>{{ favMessage }}
            </p>
            <p v-if="favError" class="mt-2 p-2 rounded" style="background-color: #f7e9c3; color: #8b0000;">
              <i class="bi bi-exclamation-triangle me-1"></i>{{ favError }}
            </p>
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
import { API_BASE_URL } from '../config'

const route = useRoute()
const profile = ref({})
const loading = ref(true)
const error = ref('')

const formatDate = (dateStr) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateStr).toLocaleDateString(undefined, options)
}

const fetchProfile = async () => {
  loading.value = true
  try {
    const token = localStorage.getItem('token')
    const id = route.params.id

    const res = await api.get(`/api/profiles/${id}`, {
      headers: { Authorization: `Bearer ${token}` }
    })

    profile.value = res.data
  } catch (err) {
    error.value = err.response?.data?.message || 'Profile not found.'
  } finally {
    loading.value = false
  }
}

const favMessage = ref('')
const favError = ref('')

const favouriteUser = async () => {
  favMessage.value = ''
  favError.value = ''
  try {
    const token = localStorage.getItem('token')
    const id = profile.value.user_id // Use user_id, not profile.id

    const res = await api.post(`/api/profiles/${id}/favourite`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    })

    favMessage.value = res.data.message || 'Added to favourites.'
  } catch (err) {
    favError.value = err.response?.data?.error || err.response?.data?.message || 'Could not add to favourites.'
  }
}

onMounted(fetchProfile)
</script>