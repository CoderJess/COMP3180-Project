<!-- views/Home.vue -->
<template>
  <div class="home-container">
    <div class="header">
      <h1>Welcome to Jam-Date</h1>
      <p>See the latest connections and find your match!</p>
    </div>

    <div class="my-profile-container">
      <div class="my-profile-banner">
        <h1>
          <router-link class="my-profile-link" to="/myprofiles">My Profiles</router-link>
        </h1>
        <ul class="my-profile-btns">
          <li>
            <router-link to="#report" class="btn show-report-btn">Show Report</router-link>
          </li>
          <li>
            <router-link class="btn add-profile-btn" to="/add-profile">Add Profile</router-link>
          </li>
        </ul>
      </div>
    </div>
    
     <div class="profile-info">
      <!-- Search Section -->
      <div class="search-card">
        <div class="search-header">
          <h4>Search Profiles</h4>
        </div>
        <div class="search-body">
          <div class="search-grid">
            <div class="form-group">
              <label for="search-name">Name</label>
              <input
                type="text"
                id="search-name"
                v-model="searchParams.name"
              />
            </div>
            <div class="form-group">
              <label for="search-birth-year">Birth Year</label>
              <input
                type="number"
                id="search-birth-year"
                v-model="searchParams.birth_year"
              />
            </div>
            <div class="form-group">
              <label for="search-sex">Sex</label>
              <select id="search-sex" v-model="searchParams.sex">
                <option value="">Any</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
              </select>
            </div>
            <div class="form-group">
              <label for="search-race">Race</label>
              <input
                type="text"
                id="search-race"
                v-model="searchParams.race"
              />
            </div>
          </div>
          <div class="search-actions">
            <button class="btn primary" @click="searchProfiles">Search</button>
            <button class="btn secondary" @click="resetSearch">Reset</button>
          </div>
        </div>
      </div>
      
      <!-- Profiles Section -->
      <div v-if="loading" class="loading-spinner">
        <div class="spinner"></div>
      </div>
      
      <div v-else class="profiles-section">
        <h2>{{ searchActive ? 'Search Results' : 'Recent Profiles' }}</h2>
        
        <div v-if="profiles.length === 0" class="empty-state">
          No profiles found.
        </div>
        
        <div class="profiles-grid">
          <div class="profile-card" v-for="profile in profiles" :key="profile.id">
            <div class="profile-image">
              <img 
                v-if="profile.user && profile.user.photo" 
                :src="profile.user.photo" 
                alt="Profile photo"
              >
              <div v-else class="profile-placeholder">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
            </div>
            
            <div class="profile-body">
              <h5>{{ profile.user ? profile.user.name : 'User' }}</h5>
              <p class="profile-age">
                {{ profile.age || (profile.birth_year ? (new Date().getFullYear() - profile.birth_year) : 'Unknown') }} years old
              </p>
              <p class="profile-description">{{ truncate(profile.description || 'No description available', 100) }}</p>
            </div>
            
            <div class="profile-footer">
              <router-link :to="`/profiles/${profile.id}`" class="btn primary">
                View more details
              </router-link>
            </div>
          </div>
        </div>
      </div>
     </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      profiles: [],
      loading: true,
      error: null,
      searchParams: {
        name: '',
        birth_year: '',
        sex: '',
        race: ''
      },
      searchActive: false
    }
  },
  created() {
    this.fetchRecentProfiles();
  },
  methods: {
    async fetchRecentProfiles() {
      this.loading = true;
      try {
        // Fetch the 4 most recent profiles
        const response = await this.$http.get('/api/profiles');
        this.profiles = response.data;
        this.searchActive = false;
      } catch (err) {
        console.error('Error fetching recent profiles:', err);
        this.error = 'Failed to load recent profiles';
      } finally {
        this.loading = false;
      }
    },
    
    async searchProfiles() {
      this.loading = true;
      
      // Build query parameters
      const params = {};
      if (this.searchParams.name) params.name = this.searchParams.name;
      if (this.searchParams.birth_year) params.birth_year = this.searchParams.birth_year;
      if (this.searchParams.sex) params.sex = this.searchParams.sex;
      if (this.searchParams.race) params.race = this.searchParams.race;
      
      try {
        const response = await this.$http.get('/api/search', { params });
        this.profiles = response.data;
        this.searchActive = true;
      } catch (err) {
        console.error('Error searching profiles:', err);
        this.error = 'Failed to search profiles';
      } finally {
        this.loading = false;
      }
    },
    
    resetSearch() {
      this.searchParams = {
        name: '',
        birth_year: '',
        sex: '',
        race: ''
      };
      this.fetchRecentProfiles();
    },
    
    truncate(text, length) {
      if (!text) return '';
      return text.length > length ? text.substring(0, length) + '...' : text;
    }
  }
}
</script>

<style>
/* Custom CSS Variables */
:root {
  --primary-color: #4863A0;
  --primary-light: #6983c0;
  --primary-dark: #3a4f80;
  --secondary-color: #f0f2f5;
  --text-color: #333333;
  --light-text: #666666;
  --border-color: #e1e4e8;
  --success-color: #28a745;
  --warning-color: #ffc107;
  --danger-color: #dc3545;
  --info-color: #17a2b8;
  --radius: 8px;
  --shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  --transition: all 0.3s ease;
}

/* Base Styles */
.home-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
  color: var(--text-color);
}

.header {
  background: linear-gradient(90deg, #FFB100, #FF6B00);
  color: white;
  padding: 20px;
  border-radius: 12px;
  text-align: center;
  margin-bottom: 0;
}

.profile-info{
  max-width: 1200px;
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-top: 0;
}

.page-title {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: var(--primary-dark);
}

.my-profile-container{
  max-width: 1200px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.my-profile-banner {
  background-color: #343a40;
  color: #ffffff;
  padding: 20px;
  padding-top: 2px;
  padding-bottom: 2px;
  text-align: center;
  width: 945px;
  border-radius: 0 0 10px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.my-profile-link {
  text-decoration: none;
  color: white;
}

.my-profile-btns{
  display: flex;
  justify-content: space-around;
  list-style-type: none;
}

.add-profile-btn{
  background: linear-gradient(90deg, #FFB100, #FF6B00);
  color: #ffffff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  text-decoration: none;
}

.add-profile-btn:hover {
  background: linear-gradient(90deg, #8c6813, #f76802);
}

.show-report-btn {
  background-color: #28a745;
  color: #ffffff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  text-decoration: none;
}

.show-report-btn:hover {
  background-color: #218838;
}


/* Search Card */
.search-card {
  background-color: white;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  margin-bottom: 2rem;
  overflow: hidden;
}

.search-header {
  background: linear-gradient(90deg, #FFB100, #FF6B00);
  color: white;
  padding: 1rem 1.5rem;
}

.search-header h4 {
  margin: 0;
  font-weight: 600;
}

.search-body {
  padding: 1.5rem;
}

.search-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

@media (max-width: 768px) {
  .search-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .search-grid {
    grid-template-columns: 1fr;
  }
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: var(--text-color);
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  font-size: 1rem;
  transition: var(--transition);
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(72, 99, 160, 0.2);
}

.search-actions {
  display: flex;
  gap: 0.75rem;
  margin-top: 1rem;
}

/* Buttons */
.btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: var(--radius);
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
  text-decoration: none;
  display: inline-block;
}

.btn.primary {
  background: linear-gradient(90deg, #FFB100, #FF6B00);
  color: white;
}

.btn.primary:hover {
  background-color: var(--primary-dark);
}

.btn.secondary {
  background-color: var(--secondary-color);
  color: var(--text-color);
}

.btn.secondary:hover {
  background-color: #e0e0e0;
}

/* Profile Cards */
.profiles-section h2 {
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  color: var(--primary-dark);
}

.empty-state {
  background-color: rgba(23, 162, 184, 0.1);
  color: var(--info-color);
  padding: 1rem;
  border-radius: var(--radius);
  text-align: center;
}

.profiles-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

@media (max-width: 1024px) {
  .profiles-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .profiles-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 576px) {
  .profiles-grid {
    grid-template-columns: 1fr;
  }
}

.profile-card {
  background-color: white;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  overflow: hidden;
  transition: var(--transition);
  display: flex;
  flex-direction: column;
  height: 100%;
}

.profile-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.profile-image {
  height: 180px;
  background-color: #f8f9fa;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.profile-image img {
  max-height: 180px;
  max-width: 100%;
  object-fit: cover;
}

.profile-placeholder {
  width: 80px;
  height: 80px;
  color: #adb5bd;
}

.profile-body {
  padding: 1.25rem;
  flex-grow: 1;
}

.profile-body h5 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
  color: var(--primary-dark);
}

.profile-age {
  color: var(--light-text);
  font-size: 0.9rem;
  margin-bottom: 0.75rem;
}

.profile-description {
  color: var(--text-color);
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 0;
}

.profile-footer {
  padding: 1rem;
  border-top: 1px solid var(--border-color);
  text-align: center;
}

.profile-footer .btn {
  width: 100%;
  padding: 0.6rem;
  font-size: 0.9rem;
}

/* Loading Spinner */
.loading-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 3rem 0;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(72, 99, 160, 0.3);
  border-radius: 50%;
  border-top-color: var(--primary-color);
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>