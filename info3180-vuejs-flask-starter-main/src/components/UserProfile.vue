<template>
  <div class="container mt-5">
    <h2>My Profile</h2>
    <div v-if="user">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>

      <h4>My Profiles</h4>
      <ul>
        <li v-for="profile in userProfiles" :key="profile.id">
          <router-link :to="`/profiles/${profile.id}`">{{ profile.description }}</router-link>
        </li>
      </ul>

      <h4>Favourites</h4>
      <ul>
        <li v-for="fav in favourites" :key="fav.id">{{ fav.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'UserProfile',
  data() {
    return {
      user: null,
      userProfiles: [],
      favourites: []
    };
  },
  mounted() {
    this.fetchUserInfo();
  },
  methods: {
    fetchUserInfo() {
      const userId = this.$route.params.user_id;
      axios.get(`/api/users/${userId}`)
        .then(response => {
          this.user = response.data.user;
          this.userProfiles = response.data.profiles;
        })
        .catch(error => {
          console.error(error);
        });

      axios.get(`/api/users/${userId}/favourites`)
        .then(response => {
          this.favourites = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
