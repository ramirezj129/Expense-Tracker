<template>
  <div class="container">
    <form class="mt-5" @submit.prevent="loginUser">
      <!-- Username Input -->
      <div class="form-group row mt-2">
        <label for="username-input" class="col-form-label col-4 text-center">Username</label>
        <div class="col-7">
          <input v-model="login_username" type="text" id="login_username" class="form-control" placeholder="Enter Username or Email" required>
        </div>
      </div>

      <!-- Password Input -->
      <div class="form-group row mt-2">
        <label for="password-input" class="col-form-label col-4 text-center">Password</label>
        <div class="col-7">
          <input v-model="login_password" type="password" id="login_password" class="form-control" placeholder="Enter Password" required>
        </div>
      </div>

      <!-- Submit Button -->
      <div class="form-group row mt-3">
        <div class="col-7 offset-4 text-end">
          <button type="submit" class="btn btn-primary me-2">Login</button>
          <router-link to="/register" class="btn btn-primary ml-2">Register</router-link>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { mapMutations } from 'vuex';

export default {
  data() {
    return {
      login_username: '',
      login_password: ''
    };
  },
  methods: {
    ...mapMutations(['setToken']),
    async loginUser() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/users/login/', {
          username_or_email: this.login_username,
          password: this.login_password
        });

        if (response.status === 200) {
          const token = response.data.token;
          this.setToken(token); // Store token in Vuex

          // Redirect to home page or any other authenticated route
          this.$router.push({ name: 'Home' });
        } else {
          console.error('Login failed:', response.data);
        }
      } catch (error) {
        console.error('Error: Unable to Login User', error);
      }
    }
  },
  created() {
    // Check authentication status when the component is created
    if (this.$store.getters.isAuthenticated) {
      this.$router.push({ name: 'Home' }); // Redirect to home page if authenticated
    }
  }
};
</script>
