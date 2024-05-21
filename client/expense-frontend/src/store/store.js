import { createStore } from 'vuex';

const store = createStore({
  state: {
    token: localStorage.getItem('token') || ''
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
    },
    clearToken(state) {
      state.token = '';
      localStorage.removeItem('token');
    }
  },
  getters: {
    isAuthenticated: state => !!state.token
  }
});

export default store;
