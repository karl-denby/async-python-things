<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Count msg="Number of clients is: "/>
  </div>
</template>

<script>
import Count from './components/Count.vue'

export default {
  name: 'app',
  components: {
    Count
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
