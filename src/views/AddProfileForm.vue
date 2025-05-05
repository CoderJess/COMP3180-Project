<template>
  <div class="container">
    <h1>Create New Profile</h1>
    
    <div v-if="error" class="alert alert-error">
      {{ error }}
    </div>
    
    <div v-if="success" class="alert alert-success">
      {{ success }}
    </div>
    
    <div class="form-container">
      <form @submit.prevent="createProfile">
        <!-- Description Field -->
        <div class="form-group">
          <label for="description">Description</label>
          <input 
            type="text" 
            id="description" 
            v-model="profileData.description" 
            required
          />
        </div>
        
        <!-- Parish Field -->
        <div class="form-group">
          <label for="parish">Parish</label>
          <select 
            id="parish" 
            v-model="profileData.parish" 
            required
          >
            <option value="" disabled>Select a parish</option>
            <option v-for="parish in parishes" :key="parish" :value="parish">{{ parish }}</option>
          </select>
        </div>
        
        <!-- Biography Field -->
        <div class="form-group">
          <label for="biography">Biography</label>
          <textarea 
            id="biography" 
            v-model="profileData.biography" 
            rows="4" 
            required
          ></textarea>
        </div>
        
        <!-- Sex Field -->
        <div class="form-group">
          <label>Sex</label>
          <div class="radio-group">
            <label class="radio-option">
              <input type="radio" v-model="profileData.sex" value="Male" required> Male
            </label>
            <label class="radio-option">
              <input type="radio" v-model="profileData.sex" value="Female" required> Female
            </label>
          </div>
        </div>
        
        <!-- Race Field -->
        <div class="form-group">
          <label for="race">Race</label>
          <select 
            id="race" 
            v-model="profileData.race" 
            required
          >
            <option value="" disabled>Select race</option>
            <option v-for="race in races" :key="race" :value="race">{{ race }}</option>
          </select>
        </div>
        
        <!-- Birth Year Field -->
        <div class="form-group">
          <label for="birth_year">Birth Year</label>
          <input 
            type="number" 
            id="birth_year" 
            v-model="profileData.birth_year" 
            min="1940" 
            :max="currentYear - 18" 
            required
          />
        </div>
        
        <!-- Height Field -->
        <div class="form-group">
          <label for="height">Height (inches)</label>
          <input 
            type="number" 
            id="height" 
            v-model="profileData.height" 
            min="48" 
            max="96" 
            required
          />
        </div>
        
        <!-- Favorite Cuisine Field -->
        <div class="form-group">
          <label for="fav_cuisine">Favorite Cuisine</label>
          <select 
            id="fav_cuisine" 
            v-model="profileData.fav_cuisine" 
            required
          >
            <option value="" disabled>Select cuisine</option>
            <option v-for="cuisine in cuisines" :key="cuisine" :value="cuisine">{{ cuisine }}</option>
          </select>
        </div>
        
        <!-- Favorite Color Field -->
        <div class="form-group">
          <label for="fav_colour">Favorite Color</label>
          <select 
            id="fav_colour" 
            v-model="profileData.fav_colour" 
            required
          >
            <option value="" disabled>Select color</option>
            <option v-for="color in colors" :key="color" :value="color">{{ color }}</option>
          </select>
        </div>
        
        <!-- Favorite School Subject Field -->
        <div class="form-group">
          <label for="fav_school_subject">Favorite School Subject</label>
          <select 
            id="fav_school_subject" 
            v-model="profileData.fav_school_subject" 
            required
          >
            <option value="" disabled>Select subject</option>
            <option v-for="subject in schoolSubjects" :key="subject" :value="subject">{{ subject }}</option>
          </select>
        </div>
        
        <!-- Political Views Field -->
        <div class="form-group">
          <label for="political">Political Views</label>
          <select 
            id="political" 
            v-model="profileData.political" 
            required
          >
            <option value="" disabled>Select political view</option>
            <option v-for="view in politicalViews" :key="view" :value="view">{{ view }}</option>
          </select>
        </div>
        
        <!-- Religious Views Field -->
        <div class="form-group">
          <label for="religious">Religious Views</label>
          <select 
            id="religious" 
            v-model="profileData.religious" 
            required
          >
            <option value="" disabled>Select religious view</option>
            <option v-for="view in religiousViews" :key="view" :value="view">{{ view }}</option>
          </select>
        </div>
        
        <!-- Family Oriented Field -->
        <div class="form-group">
          <label>Family Oriented</label>
          <div class="radio-group">
            <label class="radio-option">
              <input type="radio" v-model="profileData.family_oriented" value="Yes" required> Yes
            </label>
            <label class="radio-option">
              <input type="radio" v-model="profileData.family_oriented" value="No" required> No
            </label>
          </div>
        </div>
        
        <div class="form-group">
          <button 
            type="submit" 
            class="btn-submit"
            :disabled="isSubmitting"
          >
            {{ isSubmitting ? 'Creating Profile...' : 'Create Profile' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AddProfileForm',
  data() {
    return {
      profileData: {
        description: '',
        parish: '',
        biography: '',
        sex: '',
        race: '',
        birth_year: '',
        height: '',
        fav_cuisine: '',
        fav_colour: '',
        fav_school_subject: '',
        political: '',
        religious: '',
        family_oriented: ''
      },
      isSubmitting: false,
      error: '',
      success: '',
      currentYear: new Date().getFullYear(),
      // Pre-defined options for select fields
      parishes: [
        'Kingston', 'St. Andrew', 'St. Thomas', 'Portland', 'St. Mary', 
        'St. Ann', 'Trelawny', 'St. James', 'Hanover', 'Westmoreland', 
        'St. Elizabeth', 'Manchester', 'Clarendon', 'St. Catherine'
      ],
      races: [
        'Black', 'White', 'Asian', 'Hispanic', 'Mixed', 'Other'
      ],
      cuisines: [
        'Jamaican', 'Italian', 'Chinese', 'Indian', 'Mexican', 'American', 
        'Japanese', 'Thai', 'French', 'Mediterranean', 'Other'
      ],
      colors: [
        'Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 
        'Black', 'White', 'Brown', 'Grey', 'Other'
      ],
      schoolSubjects: [
        'Mathematics', 'English', 'Science', 'History', 'Geography', 'Art', 
        'Music', 'Physical Education', 'Computer Science', 'Foreign Language', 'Other'
      ],
      politicalViews: [
        'Conservative', 'Liberal', 'Moderate', 'Progressive', 'Libertarian', 
        'Independent', 'Not Political', 'Other'
      ],
      religiousViews: [
        'Christian', 'Catholic', 'Protestant', 'Baptist', 'Methodist', 'Anglican',
        'Jewish', 'Muslim', 'Hindu', 'Buddhist', 'Atheist', 'Agnostic', 
        'Spiritual but not Religious', 'Other'
      ]
    }
  },
  methods: {
    async createProfile() {
      this.isSubmitting = true;
      this.error = '';
      this.success = '';
      
      try {
        // Get auth token from localStorage
        const token = localStorage.getItem('token');
        
        if (!token) {
          this.$router.push('/login');
          return;
        }
        
        // Convert birth_year and height to numbers
        this.profileData.birth_year = parseInt(this.profileData.birth_year);
        this.profileData.height = parseInt(this.profileData.height);
        
        const response = await fetch('http://localhost:8080/api/profiles', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify(this.profileData)
        });
        
        let data;
        try {
          const text = await response.text();
          data = text ? JSON.parse(text) : {};
        } catch (jsonError) {
          console.error('JSON parsing error:', jsonError);
          throw new Error('Invalid response from server. Please try again later.');
        }
        
        if (!response.ok) {
          throw new Error(data.message || 'Failed to create profile');
        }
        
        this.success = data.message || 'Profile created successfully!';
        
        // Reset form after successful submission
        this.profileData = {
          description: '',
          parish: '',
          biography: '',
          sex: '',
          race: '',
          birth_year: '',
          height: '',
          fav_cuisine: '',
          fav_colour: '',
          fav_school_subject: '',
          political: '',
          religious: '',
          family_oriented: ''
        };
        
        // Redirect to user profile page after short delay
        setTimeout(() => {
          this.$router.push(`/users/${this.getUserId()}`);
        }, 2000);
        
      } catch (error) {
        console.error('Profile creation error:', error);
        this.error = error.message || 'An unexpected error occurred. Please try again.';
      } finally {
        this.isSubmitting = false;
      }
    },
    
    getUserId() {
      return localStorage.getItem('userId');
    }
  }
}
</script>

<style>
/* Color Variables */
:root {
  --main-green: #007c3e;
  --dark-green: #005d2f;
  --gold: #ffd700;
  --light-gold: #fff2b3;
  --black: #000000;
  --white: #ffffff;
  --error: #8b0000;
  --success: #006400;
  --gray: #eaeaea;
  --dark-gray: #333333;
}

/* Base Styles */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  color: var(--white);
}

/* Header */
h1 {
  color: var(--gold);
  text-align: center;
  font-size: 2rem;
  margin-bottom: 30px;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-bottom: 2px solid var(--gold);
  padding-bottom: 10px;
}

/* Form Styling */
.form-container {
  background-color: var(--white);
  border: 2px solid var(--gold);
  border-radius: 8px;
  padding: 25px;
  max-width: 600px;
  margin: 0 auto;
  box-shadow: 0 4px 12px rgba(255, 215, 0, 0.15);
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 8px;
  color: var(--gold);
}

input[type="text"],
input[type="number"],
select,
textarea {
  width: 100%;
  padding: 12px;
  border: 2px solid var(--main-green);
  border-radius: 4px;
  background-color: var(--dark-gray);
  color: var(--white);
  font-size: 1rem;
  box-sizing: border-box;
}

input[type="text"]:focus,
input[type="number"]:focus,
select:focus,
textarea:focus {
  border-color: var(--gold);
  outline: none;
  box-shadow: 0 0 5px rgba(255, 215, 0, 0.5);
}

select {
  appearance: none;
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23FFD700%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
  background-repeat: no-repeat;
  background-position: right 12px top 50%;
  background-size: 12px auto;
  padding-right: 30px;
}

.radio-group {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.radio-option {
  display: flex;
  align-items: center;
  cursor: pointer;
  color: var(--white);
}

input[type="radio"] {
  margin-right: 8px;
  cursor: pointer;
  accent-color: var(--gold);
}

/* Button */
.btn-submit {
  background-color: var(--main-green);
  color: var(--white);
  border: 2px solid var(--gold);
  padding: 12px 24px;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
  text-transform: uppercase;
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.btn-submit:hover {
  background-color: var(--gold);
  color: var(--black);
  border-color: var(--main-green);
  transform: translateY(-2px);
}

.btn-submit:disabled {
  background-color: var(--dark-gray);
  border-color: var(--gray);
  color: var(--gray);
  cursor: not-allowed;
}

/* Alerts */
.alert {
  padding: 12px;
  margin-bottom: 20px;
  border-radius: 4px;
  font-weight: bold;
}

.alert-error {
  background-color: var(--error);
  color: var(--white);
  border: 1px solid #620000;
}

.alert-success {
  background-color: var(--success);
  color: var(--white);
  border: 1px solid #004200;
}

/* Responsive Design */
@media screen and (max-width: 768px) {
  .form-container {
    padding: 15px;
  }
  
  input[type="text"],
  input[type="number"],
  select,
  textarea {
    padding: 10px;
  }
}
</style>