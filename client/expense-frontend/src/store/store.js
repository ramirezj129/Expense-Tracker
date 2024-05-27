import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    token: localStorage.getItem('token') || '',
    incomes: [],
    expenses: [],
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
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
    },
    clearToken(state) {
      state.token = '';
      localStorage.removeItem('token');
    },
    setIncomes(state, incomes) {
      state.incomes = incomes;
    },
    setExpenses(state, expenses) {
      state.expenses = expenses;
    },
    clearData(state) {
      state.incomes = [];
      state.expenses = [];
      state.chartData.labels = [];
      state.chartData.datasets[0].data = [];
    },
    setChartData(state, chartData) {
      state.chartData = chartData;
    },
    clearChartData(state) {
      state.chartData = {
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
      };
    },
  },
  getters: {
    isAuthenticated: state => !!state.token,
    getIncomes: state => state.incomes,
    getExpenses: state => state.expenses,
    getChartData: state => state.chartData,
  },
  actions: {
    async fetchIncomes({ commit, state }) {
      try {
        const response = await axios.get('http://127.0.0.1:8000/income/income-info/', {
          headers: {
            Authorization: `Token ${state.token}`
          }
        });
        commit('setIncomes', response.data);
      } catch (error) {
        console.error('Error fetching income data:', error);
      }
    },
    async fetchExpenses({ commit, state }) {
      try {
        const response = await axios.get('http://127.0.0.1:8000/expenses/list/', {
          headers: {
            Authorization: `Token ${state.token}`
          }
        });
        commit('setExpenses', response.data);
      } catch (error) {
        console.error('Error fetching expense data:', error);
      }
    },
    async fetchChartData({ commit, state }) {
      try {
        const response = await axios.get('http://127.0.0.1:8000/expenses/list/', {
          headers: {
            Authorization: `Token ${state.token}`
          }
        });
        const expenses = response.data;
        const chartData = this.processChartData(expenses);
        commit('setChartData', chartData);
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    },
    logout({ commit }) {
      commit('clearToken');
      commit('clearData');
      commit('clearChartData');
    }
  }
});

export default store;
