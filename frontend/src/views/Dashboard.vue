<template>
  <div class="dashboard-container">
    <div class="header">
      <h1>Welcome to Jam-Date</h1>
      <p>See the latest connections and find your match!</p>
    </div>

    <div class="search-bar">
      <input
        v-model="search"
        placeholder="Search by name, birth year, sex or race..."
      />
    </div>

    <div v-if="filteredProfiles.length === 0" class="no-profiles">
      No profiles found yet. Add some friends!
    </div>

    <div class="profiles-grid">
      <div v-for="profile in filteredProfiles" :key="profile.id" class="profile-card">
        <h3>{{ profile.name }}</h3>

        <div class="tags">
          <span class="tag sex">{{ profile.sex }}</span>
          <span class="tag year">{{ profile.birth_year }}</span>
          <span class="tag race">{{ profile.race }}</span>
        </div>

        <div class="card-buttons">
          <router-link :to="'/profiles/' + profile.id" class="view-button">View More</router-link>
          <button @click="favourite(profile.id)">Favourite</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      profiles: [],
      search: ""
    };
  },
  computed: {
    filteredProfiles() {
      if (!this.search) return this.profiles;
      return this.profiles.filter(profile =>
        (profile.name?.toLowerCase() ?? "").includes(this.search.toLowerCase()) ||
        (profile.sex?.toLowerCase() ?? "").includes(this.search.toLowerCase()) ||
        (profile.race?.toLowerCase() ?? "").includes(this.search.toLowerCase()) ||
        (profile.birth_year + "").includes(this.search)
      );
    }
  },
  methods: {
    async getProfiles() {
      try {
        const res = await axios.get("/profiles");
        this.profiles = res.data;
      } catch (err) {
        console.error(err);
      }
    },
    async favourite(id) {
      try {
        await axios.post(`/profiles/${id}/favourite`);
        alert("Added to favourites!");
      } catch (err) {
        console.error(err);
      }
    }
  },
  mounted() {
    this.getProfiles();
  }
};
</script>

<style>
.dashboard-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Segoe UI', sans-serif;
}

.header {
  background: linear-gradient(90deg, #FFB100, #FF6B00);
  color: white;
  padding: 20px;
  border-radius: 12px;
  text-align: center;
  margin-bottom: 30px;
}

.search-bar {
  text-align: center;
  margin-bottom: 30px;
}

.search-bar input {
  width: 350px;
  padding: 12px;
  border-radius: 25px;
  border: none;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.1);
}

.no-profiles {
  text-align: center;
  font-size: 18px;
  color: #888;
}

.profiles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 25px;
}

.profile-card {
  background-color: #fff9e6;
  border-radius: 16px;
  padding: 20px;
  border: 2px solid #FFD700;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  text-align: center;
}

.profile-card h3 {
  margin-bottom: 15px;
  color: #333;
}

.tags {
  margin-bottom: 15px;
}

.tag {
  display: inline-block;
  background-color: #FFB100;
  color: white;
  padding: 6px 12px;
  margin: 5px;
  border-radius: 20px;
  font-size: 12px;
}

.tag.year {
  background-color: #FF6B00;
}

.tag.sex {
  background-color: #00BFFF;
}

.tag.race {
  background-color: #9C27B0;
}

.card-buttons {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.view-button, button {
  background-color: #FF6B00;
  color: white;
  padding: 8px 14px;
  border: none;
  border-radius: 20px;
  text-decoration: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

.view-button:hover,
button:hover {
  background-color: #e35500;
}
</style>
