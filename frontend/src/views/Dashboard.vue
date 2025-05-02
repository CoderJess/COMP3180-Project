<template>
    <div class="container">
      <h2>Dashboard (Recent Profiles)</h2>
  
      <input type="text" v-model="search" placeholder="Search name, birth year, sex, race">
  
      <div v-if="profiles.length">
        <div v-for="p in filteredProfiles" :key="p.id" class="profile-card">
          <h4>{{ p.description }}</h4>
          <p>Parish: {{ p.parish }}</p>
          <p>Sex: {{ p.sex }}</p>
          <p>Race: {{ p.race }}</p>
          <router-link :to="'/profiles/' + p.id">View More</router-link>
        </div>
      </div>
      <p v-else>No profiles found.</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        profiles: [],
        search: ''
      };
    },
    mounted() {
      axios.get('/profiles').then(res => {
        this.profiles = res.data.slice(-4).reverse();
      });
    },
    computed: {
      filteredProfiles() {
        return this.profiles.filter(p =>
          (p.description && p.description.toLowerCase().includes(this.search.toLowerCase())) ||
          (p.sex && p.sex.toLowerCase().includes(this.search.toLowerCase())) ||
          (p.race && p.race.toLowerCase().includes(this.search.toLowerCase())) ||
          (p.birth_year && String(p.birth_year).includes(this.search))
        );
      }
    }
  };
  </script>
  
  <style>
  .container {
    max-width: 700px;
    margin: auto;
  }
  .profile-card {
    padding: 15px;
    background: #f5f5f5;
    border-radius: 8px;
    margin-bottom: 15px;
  }
  </style>
  