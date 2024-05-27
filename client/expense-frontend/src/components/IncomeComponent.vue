<template>
  <div class="container">
    <form class="mt-5" @submit.prevent="submitData">
      <div class="form-group row">
        <label for="income-input" class="col-form-label col-3 text-center">Income</label>
        <div class="col-8">
          <input v-model="amount" type="number" id="income" class="form-control" placeholder="Enter Income" required>
        </div>
      </div>
      <div class="form-group row mt-2">
        <label for="description-input" class="col-form-label col-3 text-center">Description</label>
        <div class="col-8">
          <input v-model="description" type="text" id="description" class="form-control" placeholder="Enter Description">
        </div>
      </div>
      <div class="form-group row">
        <div class="d-flex justify-content-start offset-3 mt-3">
          <button type="submit" class="btn btn-primary">Submit Income</button>
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
      amount: '',
      description: '',
    };
  },
  methods: {
    async submitData() {
      try {
        const token = localStorage.getItem('token'); // Retrieve token from localStorage
        const response = await axios.post('http://127.0.0.1:8000/income/add-income/', {
          amount: this.amount,
          description: this.description,
        }, {
          headers: {
            Authorization: `Token ${token}`, // Include token in request headers
          },
        });

        if (response.status === 201) {
          alert('Income submitted successfully');
          this.resetForm();
        } else {
          console.error('Failed to submit income:', response.data);
        }
      } catch (error) {
        console.error('Error submitting income:', error);
      }
    },
    resetForm() {
      this.amount = '';
      this.description = '';
    }
  }
};
</script>
