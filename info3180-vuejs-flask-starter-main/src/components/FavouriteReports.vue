<template>
  <div class="container mt-5">
    <h2>Favourite Reports</h2>

    <h4>Top 20 Favourite Users</h4>
    <ul>
      <li v-for="user in topFavs" :key="user.id">{{ user.name }}</li>
    </ul>

    <h4>Users I Favourited</h4>
    <ul>
      <li v-for="fav in myFavourites" :key="fav.id">{{ fav.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'FavouriteReports',
  data() {
    return {
      topFavs: [],
      myFavourites: []
    };
  },
  mounted() {
    this.fetchFavourites();
  },
  methods: {
    fetchFavourites() {
      axios.get('/api/users/favourites/20')
        .then(response => {
          this.topFavs = response.data;
        })
        .catch(error => {
          console.error(error);
        });

      const userId = 1; // Ideally get logged-in user's ID
      axios.get(`/api/users/${userId}/favourites`)
        .then(response => {
          this.myFavourites = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
