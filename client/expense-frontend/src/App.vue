<script setup>
import {  RouterView } from 'vue-router'
import HeaderComponent from './components/HeaderComponent.vue';
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFToken";



</script>

<template>
  <HeaderComponent/>

  <RouterView />

  <HomeView/>
</template>

<style scoped>

</style>
