<template>
  <div v-if="user" class="container">
    <pre>

    </pre>
    <div class="jumbotron">
      <h1>{{ user.nickname }}'s Favorite Movies</h1>
      <br>
      <br>
      <h4>나만의 보고싶은 영화 목록을 만들어봐요!!</h4>
    </div>
    
    <div class="row">
      <div v-for="(movie, idx) in favorite_movies"
        :key="idx"
        class="col-sm-6 col-md-3 mb-5"
      >
        <img @click="movieDetailInfo(movie.id)" :src="movie.poster_path" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Favorite',
  data: function () {
    return {
      favorite_movies : null,
      user: null,
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
    getFavorites: function () {
      const token = localStorage.getItem('jwt')
      const userId = jwtDecode(token).user_id
      console.log(this.userId)

      axios({
        method: 'GET',
        url: `${SERVER_URL}/accounts/favorite/${userId}/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          this.favorite_movies = res.data.movies
          this.user = res.data.user

          console.log(res)
          console.log('성공')
        })
        .catch(err => {
          console.log(err)
        })
      },
    movieDetailInfo: function(movie_id) {
      window.scrollTo(0,0)
      this.$router.push(
        { name : 'MovieDetails', 
          params: {
            movieId : movie_id,
          }
      })
    }
  },
  created : function() {
    this.getFavorites()
  }
}
</script>

<style scoped>
body {
  font-family: 'Raleway', sans-serif;
}

h1 {
  color: #105469;
  font-weight: 700;
  text-align: left;
}

h4 {
  text-align: left;
}

</style>