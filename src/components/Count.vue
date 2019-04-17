<template>
  <div class="count">
    <h1 v-on:click="fetchCount()">{{ msg }}{{ count }}</h1>
  </div>
</template>

<script>
export default {
  name: 'Count',
  data () {
    return { 
      count: null
    }
  },
  mounted () {
    this.fetchCount()
  },
  props: {
    msg: String
  },
  methods: {
    fetchCount() {
      this.axios
        .get('/client-count')
        .then(response => this.count = response.data.count)
        .catch(error => {
          console.log(error)
          this.errored = true
        })
    }
  }
}
</script>

<style scoped>
h1 {
  margin: 40px 0 0;
}
</style>
