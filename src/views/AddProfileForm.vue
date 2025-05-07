<template>
  <div class="profile-container">
    <div class="profile-card">
      <div class="profile-header">
        <h4>Create New Profile</h4>
      </div>
      <div class="profile-body">
        <form @submit.prevent="submitProfile">
          <div class="form-group">
            <label>Biography</label>
            <textarea v-model="form.biography" rows="2" required></textarea>
          </div>
          
          <div class="form-group">
            <label>Description</label>
            <textarea v-model="form.description" rows="2" required></textarea>
          </div>
          
          <div class="form-group">
            <label>Parish</label>
            <input v-model="form.parish" type="text" required />
          </div>
          
          <div class="form-group">
            <label>Sex</label>
            <select v-model="form.sex" required>
              <option value="">Select</option>
              <option>Male</option>
              <option>Female</option>
            </select>
          </div>
          
          <div class="form-group">
            <label>Race</label>
            <input v-model="form.race" type="text" required />
          </div>
          
          <div class="form-group">
            <label>Birth Year</label>
            <input v-model.number="form.birth_year" type="number" required />
          </div>
          
          <div class="form-group">
            <label>Height (m)</label>
            <input v-model.number="form.height" type="number" step="0.01" required />
          </div>
          
          <div class="form-group">
            <label>Favourite Cuisine</label>
            <input v-model="form.fav_cuisine" type="text" required />
          </div>
          
          <div class="form-group">
            <label>Favourite Colour</label>
            <input v-model="form.fav_colour" type="text" required />
          </div>
          
          <div class="form-group">
            <label>Favourite School Subject</label>
            <input v-model="form.fav_school_subject" type="text" required />
          </div>
          
          <div class="form-group beliefs-group">
            <label>Beliefs</label>
            <div class="checkbox-container">
              <div class="checkbox-group">
                <input v-model="form.political" type="checkbox" id="political" />
                <label for="political">Political</label>
              </div>
              <div class="checkbox-group">
                <input v-model="form.religious" type="checkbox" id="religious" />
                <label for="religious">Religious</label>
              </div>
              <div class="checkbox-group">
                <input v-model="form.family_oriented" type="checkbox" id="family_oriented" />
                <label for="family_oriented">Family Oriented</label>
              </div>
            </div>
          </div>
  
          <div class="form-submit">
            <button type="submit">Create Profile</button>
          </div>
  
          <div v-if="message" class="form-message" :class="messageType === 'alert-success' ? 'success-message' : 'error-message'">
            {{ message }}
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue'
import api from '../api'

const userStr = localStorage.getItem('user')
const user = JSON.parse(userStr)

console.log('User ID:', user.id)

// State
const csrfToken = ref('')
const form = ref({
  description: '',
  parish: '',
  biography: '',
  sex: '',
  race: '',
  birth_year: '',
  height: '',
  fav_cuisine: '',
  fav_colour: '',
  fav_school_subject: '',
  political: false,
  religious: false,
  family_oriented: false,
  user_id: user.id,
})
const message = ref('')
const messageType = ref('')

// Fetch CSRF token on mount
const fetchCSRFToken = async () => {
  try {
    const res = await api.get('/api/csrf-token', { withCredentials: true })
    csrfToken.value = res.data.csrf_token
  } catch (err) {
    console.error('Failed to fetch CSRF token:', err)
    message.value = 'Unable to get CSRF token.'
    messageType.value = 'alert-danger'
  }
}

// Submit profile
const submitProfile = async () => {
  message.value = ''
  try {
    await api.post('/api/profiles', form.value, {
      headers: {
        'X-CSRFToken': csrfToken.value,
      },
      withCredentials: true
    })
    message.value = 'Profile created successfully!'
    messageType.value = 'alert-success'
    Object.keys(form.value).forEach(key => form.value[key] = typeof form.value[key] === 'boolean' ? false : '')
  } catch (err) {
    console.error(err)
    message.value = err.response?.data?.message || 'Failed to create profile.'
    messageType.value = 'alert-danger'
  }
}

// Fetch CSRF token once
onMounted(fetchCSRFToken)
</script>

<style>
/* Black, Green and Gold Theme */
:root {
  --black: #121212;
  --dark-black: #080808;
  --light-black: #1e1e1e;
  --green: #1a5d1a;
  --light-green: #2e8b57;
  --gold: #ffd700;
  --gold-hover: #f0c000;
  --light-gold: #ffeb99;
  --white: #ffffff;
  --light-gray: #f5f5f5;
  --gray: #cccccc;
  --error: #dc3545;
  --success: #198754;
}

/* Reset and base styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Container */
.profile-container {
  width: 100%;
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

/* Card */
.profile-card {
  background-color: var(--black);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  border: 1px solid var(--light-black);
}

/* Header */
.profile-header {
  background-color: var(--green);
  color: var(--gold);
  padding: 1.5rem;
  border-bottom: 3px solid var(--gold);
}

.profile-header h4 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
  letter-spacing: 0.5px;
}

/* Body */
.profile-body {
  padding: 2rem;
}

/* Form layout */
.form-group {
  margin-bottom: 1.5rem;
  width: 100%;
}

/* Form controls */
.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--gold);
  font-weight: 500;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  background-color: var(--light-black);
  border: 1px solid var(--gray);
  border-radius: 4px;
  color: var(--white);
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--gold);
  box-shadow: 0 0 0 2px rgba(255, 215, 0, 0.25);
}

.form-group select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' fill='%23ffd700' viewBox='0 0 16 16'%3E%3Cpath d='M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem center;
  background-size: 12px;
  padding-right: 2.5rem;
}

.form-group textarea {
  resize: vertical;
  min-height: 80px;
}

/* Checkbox styling */
.beliefs-group {
  display: flex;
  flex-direction: column;
}

.checkbox-container {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-top: 0.5rem;
}

.checkbox-group {
  display: flex;
  align-items: center;
}

.checkbox-group input[type="checkbox"] {
  width: 20px;
  height: 20px;
  margin-right: 0.5rem;
  accent-color: var(--green);
  cursor: pointer;
}

.checkbox-group label {
  margin-bottom: 0;
  cursor: pointer;
}

/* Submit button */
.form-submit {
  text-align: right;
  margin-top: 2rem;
}

.form-submit button {
  background-color: var(--green);
  color: var(--white);
  border: 2px solid var(--gold);
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.form-submit button:hover {
  background-color: var(--light-green);
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.form-submit button:active {
  transform: translateY(0);
}

/* Message styling */
.form-message {
  margin-top: 1.5rem;
  padding: 1rem;
  border-radius: 4px;
  font-weight: 500;
}

.success-message {
  background-color: rgba(25, 135, 84, 0.1);
  color: var(--success);
  border-left: 4px solid var(--success);
}

.error-message {
  background-color: rgba(220, 53, 69, 0.1);
  color: var(--error);
  border-left: 4px solid var(--error);
}

/* Media Queries */
@media (max-width: 768px) {
  .profile-body {
    padding: 1.5rem;
  }
  
  .form-submit {
    text-align: center;
  }
  
  .form-submit button {
    width: 100%;
  }
}
</style>