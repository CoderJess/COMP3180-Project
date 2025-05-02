
<template>
  <div class="container mt-5">
    <h1>Welcome to Jam-Date!</h1>
    <p>Search for new profiles or view the latest added profiles.</p>

    <!-- Search Form -->
    <div class="mb-4">
      <input type="text" v-model="searchTerm" placeholder="Search..." class="form-control" />
      <button @click="searchProfiles" class="btn btn-primary mt-2">Search</button>
    </div>

    <!-- Latest Profiles -->
    <div v-if="profiles.length">
      <h3>Latest Profiles</h3>
      <div v-for="profile in profiles" :key="profile.id" class="card my-3">
        <div class="card-body">
          <h5 class="card-title">{{ profile.description }}</h5>
          <p class="card-text">{{ profile.parish }}</p>
          <router-link :to="`/profiles/${profile.id}`" class="btn btn-secondary">View Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HomePage',
  data() {
    return {
      searchTerm: '',
      profiles: []
    };
  },
  mounted() {
    this.fetchLatestProfiles();
  },
  methods: {
    fetchLatestProfiles() {
      axios.get('/api/profiles')
        .then(response => {
          // Show only the last 4 profiles
          this.profiles = response.data.reverse().slice(0, 4);
        })
        .catch(error => {
          console.error(error);
        });
    },
    searchProfiles() {
      axios.get(`/api/search?query=${this.searchTerm}`)
        .then(response => {
          this.profiles = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

