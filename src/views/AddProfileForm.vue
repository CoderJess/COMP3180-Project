<template>
    <div>
      <h2>Add Profile</h2>
      <form @submit.prevent="submitProfile">
        <input v-model="profile.name" placeholder="Name" required><br>
        <input v-model="profile.description" placeholder="Description" required><br>
        <input v-model="profile.parish" placeholder="Parish" required><br>
        <textarea v-model="profile.biography" placeholder="Biography" required></textarea><br>
        <input v-model="profile.sex" placeholder="Sex" required><br>
        <input v-model="profile.race" placeholder="Race" required><br>
        <input v-model.number="profile.birth_year" placeholder="Birth Year" required><br>
        <input v-model.number="profile.height" placeholder="Height" required><br>
        <input v-model="profile.fav_cuisine" placeholder="Favourite Cuisine" required><br>
        <input v-model="profile.fav_colour" placeholder="Favourite Colour" required><br>
        <input v-model="profile.fav_school_subject" placeholder="Favourite School Subject" required><br>
  
        <label><input type="checkbox" v-model="profile.political"> Political</label><br>
        <label><input type="checkbox" v-model="profile.religious"> Religious</label><br>
        <label><input type="checkbox" v-model="profile.family_oriented"> Family Oriented</label><br>
  
        <button type="submit">Add Profile</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        profile: {
          name: "",
          description: "",
          parish: "",
          biography: "",
          sex: "",
          race: "",
          birth_year: null,
          height: null,
          fav_cuisine: "",
          fav_colour: "",
          fav_school_subject: "",
          political: false,
          religious: false,
          family_oriented: false
        }
      };
    },
    methods: {
      async submitProfile() {
        try {
          const token = localStorage.getItem("token");
          const res = await axios.post('/profiles', this.profile, {
            headers: {
              Authorization: `Bearer ${token}`
            }
          });
          alert("Profile Added Successfully!");
          this.$router.push("/dashboard");
        } catch (err) {
          console.error(err.response?.data);
          alert("Error adding profile.");
        }
      }
    }
  };
  </script>
  