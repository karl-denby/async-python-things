<template>
  <div class="count">
    <h1 v-on:click="fetchcount()">{{ msg }}{{ count }}</h1>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'Count',
  data () {
    return { 
      count: null
    }
  },
  mounted () {
    this.fetchcount()
  },
  props: {
    msg: String
  },
  methods: {
    fetchcount: _.debounce(function () {
      this.$http.get('/client-count')
        .then(response => this.count = response.data.count)
        .catch(err => this.count = 'N/A')
    })
  }
}
</script>
  
<style scoped>
h1 {
  margin: 40px 0 0;
}
</style>
