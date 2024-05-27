<template>
  <div>
    <h2 class="home-header">Expenses Overview</h2>
    <div class="row">
      <div class="col-sm-6">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title text-success">Income Info:</h5>
            <p class="card-text" v-if="!isAuthenticated">Log in to add Income Info.</p>
            <p class="text-center text-success" v-else-if="incomes.length === 0">No Income Info To Display.</p>
            <p class="text-center text-success" v-else v-for="income in incomes" :key="income.id">
              Total Income: $ {{ income.amount }}
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

    <div class="row justify-content-center mt-4">
      <div class="col-sm-6">
        <div class="card text-center">
          <div class="card-body">
            <h5 class="card-title">Difference of Income and Expenses</h5>
            <p class="card-text text-info" v-if="!isAuthenticated">Log in to see the difference.</p>
            <p class="card-text text-info" v-else-if="incomes.length === 0">No Income Info To Display.</p>
            <p class="card-text text-info" v-else>$ {{ incomes[0].amount - totalExpenses }}</p>
          </div>
        </div>
      </div>
    </div>

    <ExpenseChart v-if="isAuthenticated" :expenses="expenses" />
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import ExpenseChart from './ExpenseChart.vue';

export default {
  data() {
    return {};
  },
  created() {
    if (this.isAuthenticated) {
      this.fetchIncomes();
      this.fetchExpenses();
    }
  },
  computed: {
    ...mapGetters(['getIncomes', 'getExpenses', 'isAuthenticated']),
    incomes() {
      return this.getIncomes;
    },
    expenses() {
      return this.getExpenses;
    },
    totalExpenses() {
      return this.expenses.reduce((total, expense) => total + parseFloat(expense.amount), 0);
    }
  },
  methods: {
    ...mapActions(['fetchIncomes', 'fetchExpenses']),
  },
  components: {
    ExpenseChart,
  },
  watch: {
    isAuthenticated(newVal) {
      if (newVal) {
        this.fetchIncomes();
        this.fetchExpenses();
      } else {
        this.$store.commit('clearData');
      }
    }
  }
};
</script>
<style scoped>
.home-header {
  color: rgb(0, 8, 255);
}
</style>
