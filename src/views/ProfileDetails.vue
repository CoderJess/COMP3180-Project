<template>
    <div class="container">
      <h1>Profile Details</h1>
      <div v-if="profile">
        <p><strong>Description:</strong> {{ profile.description }}</p>
        <p><strong>Parish:</strong> {{ profile.parish }}</p>
        <p><strong>Sex:</strong> {{ profile.sex }}</p>
        <p><strong>Race:</strong> {{ profile.race }}</p>
        <p><strong>Biography:</strong> {{ profile.biography }}</p>
        <p><strong>Favorite Colour:</strong> {{ profile.fav_colour }}</p>
        <p><strong>Favorite Cuisine:</strong> {{ profile.fav_cuisine }}</p>
        
        <button>Email Profile</button>
        <button @click="favourite(profile.user_id_fk)">❤️ Favourite</button>
      </div>
      <p v-else>Loading...</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        profile: null
      };
    },
    mounted() {
      const id = this.$route.params.id;
      axios.get(`/profiles/${id}`).then(res => {
        this.profile = res.data;
      });
    },
    methods: {
      favourite(userId) {
        axios.post(`/profiles/${userId}/favourite`).then(() => {
          alert('Added to favourites!');
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
  button {
    margin: 10px 10px 0 0;
    padding: 10px 20px;
    background: #f76c6c;
    color: white;
    border: none;
    border-radius: 5px;
  }
  </style>
  