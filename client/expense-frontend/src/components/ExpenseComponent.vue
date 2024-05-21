<template>
  <div class="container">

    <form class="mt-5" @submit.prevent="submitData">
      <div class="form-group row">
        <label for="category-input" class="col-form-label col-3 text-center">Category</label>
        <div class="col-8">
          <select v-model="category" id="category" class="form-select" required>
            <option selected disabled>Choose...</option>
            <option value="Food">Food</option>
            <option value="Utilities">Utilities</option>
            <option value="Personal">Personal</option>
            <option value="Other">Other</option>

          </select>

        </div>
      </div>


      <div class="form-group row mt-2">
        
          <label for="date-input" class="col-form-label col-3 text-center">Date</label>
      
        <div class="col-8">
          <input v-model="date" type="date" id="date" class="form-control" placeholder="Enter Date">
        </div>
      </div>



      <div class="form-group row mt-2">
        <label for="expense-input" class="col-form-label col-3 text-center">Expense</label>
        <div class="col-8">
          <input v-model="amount" type="number" id="expense" class="form-control" placeholder="Enter Amount" required>
        </div>
      </div>

      <div class="form-group row mt-2">
        <label for="description-input" class="col-form-label col-3 text-center">Description</label>
        <div class="col-8">
          <input v-model="description" type="text" id="description" class="form-control" placeholder="Enter Expenses Description">
        </div>
      </div>






      <div class="form-group row">
        <div class="d-flex justify-content-start offset-3 mt-3">
          <button type="submit" class="btnIncome btn btn-primary">Submit Expense</button>
        </div>
      </div>
    </form>

    <div >


    </div>

  </div>
</template>

<script>
import axios from 'axios';
import store from '../store/store'; // Import your Vuex store



export default {
  data() {
    return {
      category: '',
      date: '',
      amount: '',
      description: '',
    };
  },
  methods: {
    async submitData() {
      try {
        // Get the token from the Vuex store
        const token = store.state.token;

        // Set the headers to include the authentication token
        const config = {
          headers: {
            Authorization: `Token ${token}`,
          },
        };

        // Make the POST request with the configured headers
        const response = await axios.post('http://127.0.0.1:8000/expense/', {
          category: this.category,
          date: this.date,
          amount: this.amount,
          description: this.description,
        }, config);

        // Handle the response as before
        if (response.status === 201) {
          // Expense submitted successfully
          alert('Expense submitted successfully');
          // You can optionally reset the form fields here
          this.resetForm();
        } else {
          // Handle other response statuses if needed
          console.error('Failed to submit expense:', response.data);
        }
      } catch (error) {
        console.error('Error submitting expense:', error);
      }
    },
    resetForm() {
      // Reset form fields after successful submission
      this.category = '';
      this.date = '';
      this.amount = '';
      this.description = '';
    }
  }
};

</script>


<style scoped>

</style>

