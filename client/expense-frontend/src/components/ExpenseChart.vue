<template>
  <div v-if="isAuthenticated">
    <h2 class="chart-header mt-5">Expense Chart</h2>
    <div class="chart-container">
      <bar-chart :key="chartKey" :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Bar } from 'vue-chartjs';
import { Chart, BarController } from 'chart.js';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
import { mapGetters } from 'vuex';
Chart.register(BarController);
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  components: {
    BarChart: Bar,
  },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [{
          label: 'Expense',
          data: [],
          backgroundColor: [
            'rgba(255, 99, 132, 0.5)',
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(153, 102, 255, 0.5)',
            'rgba(255, 159, 64, 0.5)',
          ],
          borderWidth: 1,
        }],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
      chartKey: 0,
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  watch: {
    isAuthenticated(newValue) {
      if (!newValue) {
        // Clear chart data when user logs out
        this.chartData.labels = [];
        this.chartData.datasets[0].data = [];
      } else {
        // Fetch expenses when user logs in
        this.fetchExpenses();
      }
    },
  },
  methods: {
    async fetchExpenses() {
      try {
        const token = localStorage.getItem('token'); // Retrieve token from localStorage
        const response = await axios.get('http://127.0.0.1:8000/expenses/list/', {
          headers: {
            Authorization: `Token ${token}`, // Include token in request headers
          },
        });
        const expenses = response.data;
        this.processData(expenses);
      } catch (error) {
        console.error('Error fetching expense data:', error);
      }
    },
    processData(expenses) {
      if (expenses.length === 0) {
        // Clear chart data when there are no expenses
        this.chartData.labels = [];
        this.chartData.datasets[0].data = [];
      } else {
        const expenseAmounts = expenses.map(expense => parseFloat(expense.amount));
        const expenseDescriptions = expenses.map(expense => expense.description);

        this.chartData.labels = expenseDescriptions;
        this.chartData.datasets[0].data = expenseAmounts;

        // Increment the chartKey to force chart re-render
        this.chartKey++;
      }
    },
  },
  created() {
    if (this.isAuthenticated) {
      this.fetchExpenses();
    }
  },
};
</script>

<style scoped>
.chart-header {
  color: rgb(0, 8, 255);
  text-align: center;
}

.chart-container {
  margin-top: 20px;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}
</style>
