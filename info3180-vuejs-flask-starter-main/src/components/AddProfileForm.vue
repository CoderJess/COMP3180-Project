<template>
  <div class="container mt-5">
    <h2>Add New Profile</h2>
    <form @submit.prevent="addProfile">
      <input v-model="description" placeholder="Description" class="form-control mb-2" required />
      <input v-model="parish" placeholder="Parish" class="form-control mb-2" required />
      <textarea v-model="biography" placeholder="Biography" class="form-control mb-2"></textarea>
      <!-- Add all other fields similarly -->
      <button type="submit" class="btn btn-primary">Add Profile</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'AddProfileForm',
  data() {
    return {
      description: '',
      parish: '',
      biography: '',
      // Add other fields here
    };
  },
  methods: {
    addProfile() {
      axios.post('/api/profiles', {
        description: this.description,
        parish: this.parish,
        biography: this.biography
      })
      .then(response => {
        this.$router.push('/');
      })
      .catch(error => {
        console.error(error);
      });
    }
  }
};
</script>
