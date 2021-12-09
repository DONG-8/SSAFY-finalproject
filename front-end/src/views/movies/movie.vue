<template>
  <div>
    <movie-li></movie-li>
    <movie-list-recent></movie-list-recent>
  </div>
</template>

<script>
import MovieLi from '@/components/MovieLi.vue'
import MovieListRecent from '@/components/MovieListRecent.vue'
export default {
  name: 'Movie',
  components: {
    MovieLi,
    MovieListRecent,
  },
  methods: {
  setToken: function () {
    const token = localStorage.getItem('jwt')
    const config = {
      Authorization: `JWT ${token}`
    }
    return config
    },
  },
  created () {
    this.$store.dispatch("movie13", this.setToken())
  }
}
</script>

<style scoped>

</style>