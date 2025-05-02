<template>
    <div class="container">
      <h1>My Profiles</h1>
      
      <div v-if="profiles.length">
        <div v-for="profile in profiles" :key="profile.id" class="profile-card">
          <p><strong>Description:</strong> {{ profile.description }}</p>
          <p><strong>Parish:</strong> {{ profile.parish }}</p>
          <p><strong>Sex:</strong> {{ profile.sex }}</p>
          <p><strong>Race:</strong> {{ profile.race }}</p>
  
          <button @click="match(profile.id)">Match Me</button>
  
          <div v-if="matches.length && activeProfile === profile.id">
            <h4>Matches:</h4>
            <ul>
              <li v-for="m in matches" :key="m.id">{{ m.description }} - {{ m.parish }}</li>
            </ul>
          </div>
        </div>
      </div>
  
      <h3>My Favourited Users</h3>
      <ul>
        <li v-for="f in favourites" :key="f">{{ f }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        profiles: [],
        favourites: [],
        matches: [],
        activeProfile: null
      };
    },
    mounted() {
      axios.get("/profiles").then(res => {
        this.profiles = res.data.filter(p => p.user_id_fk == localStorage.getItem("user_id"));
      });
      axios.get(`/users/${localStorage.getItem("user_id")}/favourites`).then(res => {
        this.favourites = res.data;
      });
    },
    methods: {
      match(profileId) {
        axios.get(`/profiles/matches/${profileId}`).then(res => {
          this.matches = res.data;
          this.activeProfile = profileId;
        });
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
    background: #eee;
    border-radius: 8px;
    margin-bottom: 15px;
  }
  button {
    background: #407BFF;
    color: white;
    padding: 8px 15px;
    border: none;
    border-radius: 5px;
  }
  </style>
  