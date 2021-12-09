<template>
  <div class="topp">
    <reco-today :movie="movieToday"></reco-today>
    <reco-week :movie="movieWeek"></reco-week>
    <reco-korea style="background-color: #1a1e23;" :movie="movieKorea"></reco-korea>
  </div>
</template>

<script>
import RecoToday from '@/views/recommendation/RecoToday'
import RecoWeek from '@/views/recommendation/RecoWeek'
import RecoKorea from '@/views/recommendation/RecoKorea'

export default {
  name: 'Recommendation',
  components: {
    RecoToday,
    RecoWeek,
    RecoKorea
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
  computed: {
    movieToday: function () {
      return this.$store.state.movieToday
    },
    movieWeek: function () {
      return this.$store.state.movieWeek
    },
    movieKorea: function () {
      return this.$store.state.movieKorea
    }
  },
  created () {
    this.$store.dispatch("movieToday", this.setToken())
    this.$store.dispatch("movieWeek", this.setToken())
    this.$store.dispatch("movieKorea", this.setToken())
  }
}
</script>

<style lang="scss" scoped>
.topp{
  margin-top: 0px!important;
}
</style>