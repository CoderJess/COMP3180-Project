<template>
  <div class="container mt-5">
    <h2>Profile Details</h2>
    <div v-if="profile">
      <h3>{{ profile.description }}</h3>
      <p>{{ profile.biography }}</p>
      <p>Parish: {{ profile.parish }}</p>
      <button @click="addToFavourites" class="btn btn-outline-danger">❤️ Add to Favourites</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ProfileDetails',
  data() {
    return {
      profile: null
    };
  },
  mounted() {
    this.fetchProfileDetails();
  },
  methods: {
    fetchProfileDetails() {
      const id = this.$route.params.profile_id;
      axios.get(`/api/profiles/${id}`)
        .then(response => {
          this.profile = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    addToFavourites() {
      const userId = this.profile.user_id_fk;
      axios.post(`/api/profiles/${userId}/favourite`)
        .then(response => {
          alert('Added to favourites!');
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
