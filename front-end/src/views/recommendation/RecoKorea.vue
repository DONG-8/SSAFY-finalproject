<template>
  <div style="padding-top: 200px; padding-bottom: 220px;">
    <pre>



    </pre>
    <center><h1 style="color: white;"><bold> 오늘의 한국 영화 </bold></h1></center>
    <b-card-group deck
      class="d-flex justify-content-center"
    >
      <reco-korea-item
        v-for="(movie, idx) in ko_movies" :key="idx"
        :movie="movie"
        @like-change="getMovies"
        >
      </reco-korea-item >
    </b-card-group>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import RecoKoreaItem from '@/views/recommendation/RecoKoreaItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'RecoKorea',
  components: {
    RecoKoreaItem
  },
  data: function () {
    return {
      ko_movies : null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMovies: function () {
      axios({
        method: 'GET',
        url: `${SERVER_URL}/recommendation/recommend_by_korea/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          this.ko_movies = _.sampleSize(res.data, 20)
          console.log(res)
          console.log('성공')
        })
        .catch(err => {
          console.log(err)
        })
      },
  },
  created : function() {
    this.getMovies()
  }
}
</script>

<style>

</style>