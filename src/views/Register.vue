<template>
  <div class="register-container">
    <div class="form-box">
      <h2 class="title">Register</h2>
      <form @submit.prevent="register">
        <div class="input-group">
          <input v-model="username" placeholder="Username" required />
        </div>
        <div class="input-group">
          <input v-model="password" type="password" placeholder="Password" required />
        </div>
        <div class="input-group">
          <input v-model="name" placeholder="Name" required />
        </div>
        <div class="input-group">
          <input v-model="email" type="email" placeholder="Email" required />
        </div>
        <div class="file-input-group">
          <label for="photo-upload" class="file-label">
            <span>Upload Profile Photo</span>
          </label>
          <input id="photo-upload" type="file" @change="handleFile" accept="image/*" class="file-input" />
        </div>
        <button type="submit" class="register-btn">Register</button>
      </form>
    </div>
  </div>
</template>

<script>
import api from '../api';

api.defaults.withCredentials = true;

export default {
  data() {
    return {
      username: '',
      password: '',
      name: '',
      email: '',
      photoFile: null,
      csrfToken: ''
    };
  },
  async mounted() {
    try {
      const { data } = await api.get('/api/csrf-token');
      this.csrfToken = data.csrf_token;
    } catch (e) {
      console.error('Could not fetch CSRF token:', e);
    }
  },
  methods: {
    handleFile(event) {
      this.photoFile = event.target.files[0];
      // Update file label to show selected file name
      const fileName = event.target.files[0]?.name || 'No file selected';
      const fileLabel = document.querySelector('.file-label span');
      if (fileLabel) {
        fileLabel.textContent = fileName;
      }
    },
    async register() {
      try {
        const formData = new FormData();
        formData.append('username', this.username);
        formData.append('password', this.password);
        formData.append('name', this.name);
        formData.append('email', this.email);

        // Use uploaded photo or fallback to default
        if (this.photoFile) {
          formData.append('photo', this.photoFile);
        } else {
          const resp = await fetch('/defaultAvatar.jpg');
          const blob = await resp.blob();
          const file = new File([blob], 'defaultAvatar.jpg', { type: blob.type });
          formData.append('photo', file);
        }

        await api.post('/api/register', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'X-CSRFToken': this.csrfToken
          }
        });

        this.$router.push('/login');
      } catch (error) {
        const data = error.response?.data;
        if (data?.errors) {
          alert(Object.values(data.errors).flat().join('\n'));
        } else {
          alert(data?.message || 'Registration failed');
        }
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
.register-container {
  background: linear-gradient(135deg, #0a0a0a 0%, #111 100%);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.form-box {
  background-color: #0c0c0c;
  padding: 40px 30px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(107, 142, 35, 0.2);
  width: 100%;
  max-width: 400px;
  text-align: center;
  border: 1px solid #1a7c2a;
  position: relative;
  overflow: hidden;
}

.form-box::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #1a7c2a, #c5a31b, #1a7c2a);
}

.title {
  color: #d4af37;
  font-size: 28px;
  margin-bottom: 30px;
  font-weight: 600;
  letter-spacing: 1px;
}

.input-group {
  margin-bottom: 20px;
  position: relative;
}

input {
  display: block;
  width: 100%;
  padding: 14px 16px;
  background-color: #131313;
  border: 1px solid #2a2a2a;
  border-radius: 8px;
  font-size: 15px;
  color: #e0e0e0;
  transition: all 0.3s ease;
}

input:focus {
  border-color: #1a7c2a;
  outline: none;
  box-shadow: 0 0 0 3px rgba(26, 124, 42, 0.2);
}

input::placeholder {
  color: #666;
}

.file-input-group {
  margin-bottom: 20px;
}

.file-label {
  display: block;
  padding: 14px 16px;
  background-color: #131313;
  border: 1px solid #2a2a2a;
  border-radius: 8px;
  color: #666;
  text-align: left;
  cursor: pointer;
  transition: all 0.3s ease;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.file-label:hover {
  border-color: #1a7c2a;
  color: #e0e0e0;
}

.file-input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.register-btn {
  width: 100%;
  padding: 14px;
  background: linear-gradient(90deg, #1a7c2a, #1f8f31);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  letter-spacing: 0.5px;
  margin-top: 10px;
  box-shadow: 0 4px 15px rgba(26, 124, 42, 0.3);
}

.register-btn:hover {
  background: linear-gradient(90deg, #1f8f31, #24a538);
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(26, 124, 42, 0.4);
}

.register-btn:active {
  transform: translateY(1px);
}

.register-btn::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(rgba(255, 255, 255, 0.2), transparent);
  transform: rotate(45deg);
  opacity: 0;
  transition: opacity 0.3s;
}

.register-btn:hover::after {
  opacity: 0.1;
}
</style>