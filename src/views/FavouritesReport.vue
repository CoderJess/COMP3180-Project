<template>
    <div class="container">
      <h1>Favourites Report</h1>
  
      <h2>Top 20 Most Favourited Users</h2>
      <ul>
        <li v-for="fav in topFavourites" :key="fav.user_id">
          User ID: {{ fav.user_id }} - Favourites: {{ fav.total }}
        </li>
      </ul>
  
      <h2>Users You Have Favourited</h2>
      <ul>
        <li v-for="fav in myFavourites" :key="fav">
          User ID: {{ fav }}
        </li>
      </ul>
  
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        topFavourites: [],
        myFavourites: []
      };
    },
    mounted() {
      axios.get("/users/favourites/20").then(res => {
        this.topFavourites = res.data;
      });
      axios.get(`/users/${localStorage.getItem("user_id")}/favourites`).then(res => {
        this.myFavourites = res.data;
      });
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 700px;
    margin: auto;
  }
  ul {
    background-color: #f7f7f7;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
  }
  li {
    padding: 8px 0;
    border-bottom: 1px solid #ddd;
  }
  </style>
  