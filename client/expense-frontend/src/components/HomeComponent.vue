<template>
  <div>
    <h2 class="home-header">Expenses Overview</h2>

    <div class="row">
      <div class="col-sm-6">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title text-success">Income Info:</h5>
            <p class="card-text">This is the Income you submitted.</p>
            <p class="text-center text-success" v-for="income in incomes" :key="income.id">
              Amount: $ {{ income.amount }}
            </p>
          </div>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title text-danger">Expense Info:</h5>
            <p class="card-text">This is the Expense you submitted</p>
            <p class="text-center text-danger">Total Expenses: $ {{ totalExpenses }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- New row for the difference card -->
    <div class="row justify-content-center mt-4">
      <div class="col-sm-6">
        <div class="card text-center">
          <div class="card-body">
            <h5 class="card-title">Difference of Income and Expenses</h5>
            <p class="card-text text-info" v-for="income in incomes" :key="income.id">$ {{ income.amount - totalExpenses }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Add the ExpenseChart component here -->
    <ExpenseChart :expenses="expenses" />
  </div>
</template>


<script>
import axios from 'axios';
import ExpenseChart from './ExpenseChart.vue'; // Import the ExpenseChart component

export default {
  data() {
    return {
      incomes: [],
      expenses: [],
    };
  },
  created() {
    this.fetchIncomes();
    this.fetchExpenses();
  },
  methods: {
    async fetchIncomes() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/income/income-info/');
        this.incomes = response.data;
      } catch (error) {
        console.error('Error fetching income data:', error);
      }
    },
    async fetchExpenses() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/expenses/list/');
        this.expenses = response.data;
      } catch (error) {
        console.error('Error fetching expense data:', error);
      }
    },
  },
  computed: {
    totalExpenses() {
      return this.expenses.reduce((total, expense) => total + parseFloat(expense.amount), 0);
    },
  },
  components: {
    ExpenseChart, // Register the ExpenseChart component
  },
};
</script>

<style scoped>
.home-header {
  color: rgb(0, 8, 255);
}
</style>
