<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: null
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/')  // Replace URL with your Django backend URL
      .then(response => {
        this.data = response.data;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }
};
</script>

<template>
  <div class="container text-center mt-4">
    <h2 class="home-header mx-3 my-3">Welcome to my Expense Tracker</h2>
    <RouterLink to="/input">
      <button class="btn btn-success">Create Input</button>
    </RouterLink>
  </div>




</template>


<style scoped>

.home-header {
  color: rgb(0, 8, 255);
}



</style>