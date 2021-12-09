<template>
  <div>
    <br>
    <center><h1 style="color: white">Movie List</h1></center>
    <br>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="2000"
      controls
      indicators
      background="black"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;
       width: 60%;
       height: 150%;
       margin: 0 auto;
       z-index: auto;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <movie-list-item
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
      >
      </movie-list-item>
    </b-carousel>
    <pre>


    </pre>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components:{
    MovieListItem
  },
  data: function () {
    return {
      movies: [],
      slide:0,
      sliding: null,
      backgroundImg: 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20160918_202%2Feunvely27_14741711286530YRhy_JPEG%2Fse3_image_3991052682.jpg&type=sc960_832'
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
        method: 'get',
        url: `${SERVER_URL}/movies/movie_list/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data)
          this.movies = res.data
          
        })
        .catch(err => {
          console.log(err)
        })
    },
    onSlideStart() {
    this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>
<style scoped>
.bestMovie {
  float: left
}

</style>