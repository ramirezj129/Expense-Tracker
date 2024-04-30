<template>      
    <div class="container">
      <h2 class="text-center mt-4">Input Income</h2>
  
      <form class="mt-5">
        <div class="form-group row">
          <label for="income-input" class="col-form-label col-4 text-end">Income 1</label>
          <div class="col-8">
            <input type="text" id="income1" class="form-control" placeholder="Enter Annual Income">
          </div>
        </div>
  
        <div class="form-group row">
          <div class="col-4 offset-4"> <!-- Adjust the offset value to align the button properly -->
            <button type="submit" class="btn btn-primary">Create</button> <!-- Added Bootstrap button styling -->
          </div>
        </div>
      </form>
    </div>
  </template>
  
  
  <script>
  export default {
    methods: {
      submitData() {
        // Handle form submission and send data to backend
        // Example: make HTTP request using Axios
      }
    }
  };
  </script>
  