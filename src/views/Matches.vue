<template>
  <div class="container">
    <h1>Match Results</h1>

    <div v-if="matches.length">
      <div v-for="match in matches" :key="match.id" class="match-card">
        <h3>{{ match.description }}</h3>
        <p><strong>Parish:</strong> {{ match.parish }}</p>
        <p><strong>Sex:</strong> {{ match.sex }}</p>
        <p><strong>Race:</strong> {{ match.race }}</p>
        <router-link :to="'/profiles/' + match.id">View Profile</router-link>
      </div>
    </div>
    <p v-else>No matches found for this profile.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      matches: []
    };
  },
  mounted() {
    const profileId = this.$route.params.id;
    axios.get(`/profiles/matches/${profileId}`).then(res => {
      this.matches = res.data;
    });
  }
};
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}

.match-card {
  background-color: #f9f9f9;
  border-radius: 10px;
  padding: 15px;
  margin-bottom: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.match-card h3 {
  color: #333;
}

.match-card p {
  color: #666;
}

.match-card a {
  display: inline-block;
  margin-top: 10px;
  color: #407BFF;
  text-decoration: none;
}

.match-card a:hover {
  text-decoration: underline;
}
</style>
