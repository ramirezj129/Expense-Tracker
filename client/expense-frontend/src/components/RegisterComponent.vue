<template>
    <div class="container">
      <form class="mt-5" @submit.prevent="registerUser">
        <!-- Username Input -->
        <div class="form-group row mt-2">
          <label for="username-input" class="col-form-label col-4 text-end">Username</label>
          <div class="col-7">
            <input v-model="register_username" type="text" id="register-username" class="form-control" placeholder="Enter Username" required>
          </div>
        </div>
  
        <!-- Email Input -->
        <div class="form-group row mt-2">
          <label for="email-input" class="col-form-label col-4 text-end">Email</label>
          <div class="col-7">
            <input v-model="register_email" type="email" id="register-email" class="form-control" placeholder="Enter Email" required>
          </div>
        </div>
  
        <!-- Password Input -->
        <div class="form-group row mt-2">
          <label for="password-input" class="col-form-label col-4 text-end">Password</label>
          <div class="col-7">
            <input v-model="register_password" type="password" id="register-password" class="form-control" placeholder="Enter Password" required>
          </div>
        </div>
  
        <!-- Submit Button -->
        <div class="form-group row mt-3">
        <div class="col-7 offset-4 text-end"> 
            <button type="submit" class="btn btn-primary">Register</button>
          </div>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';


  export default {
    data() {
      return {
        register_username: '',
        register_email: '',
        register_password: ''
      };
    },
    methods: {
      async registerUser() {
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/users/register/', {
              username: this.register_username,
              email: this.register_email,
              password: this.register_password
            });

        if (response.status === 201) {
            // Registration successful, display success message to the user
            alert('User registered successfully');

            this.$router.push({ name: 'Login' });

            // Optionally, you can redirect the user to another page
            // after successful registration
        } else {
            // Registration failed, display error message to the user
            console.error('Registration failed:', response.data);
            // Optionally, you can display the error message to the user
        }
        } catch (error) {
          console.error('Error: Unable to Register User', error);

          
        }

      }
    }
  };
  </script>
  