<template>
  <div>
    <div id="mod">
      <div style="background-color: rgba(0, 0, 0, 0.3);text-align: center;width: 500px;height: 100px;margin-left: auto;margin-right: auto;border-radius: 20px;">
        <h3 style="color: white;padding-top: 10px;">오늘의 User </h3>
        <h2 style="color: white;">{{ TodayUser.nickname }} 님의 Pick</h2>
      </div>
      <pre>

      </pre>
      <vue-glide
        v-if="movieToday"
        :startAt="3"
        :focusAt="2"
        :perView="5"
        :autoplay="2500"
        class="demo"
      >
        <vue-glide-slide style="width: 100%;" v-for="(movie, idx) in movieToday" :key="idx">
          <img @click="movieDetailInfo(movie.id)" style="height: 400px;" :src="movie.poster_path" />
        </vue-glide-slide>
      </vue-glide>
    </div>
  </div>
</template>

<script>
// import MovieListItem from '@/components/MovieListItem'
import { Glide, GlideSlide } from 'vue-glide-js'

export default {
  name: 'RecoToday',
  components:{
    // MovieListItem
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
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
  computed: {
    movieToday: function () {
      console.log(this.$store.state.movieToday, '오늘')
      return this.$store.state.movieToday
    },
    TodayUser: function () {
      console.log(this.$store.state.TodayUser, '유저')
      return this.$store.state.TodayUser
    }
  }
}
</script>
<style scoped lang="scss">

#mod {
  background-image: url("https://i.ytimg.com/vi/ijUsSpRVhBU/maxresdefault.jpg");
  background-size: 100% 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;  
  padding-top: 200px;
  padding-bottom: 400px;
  .demo {
    .glide {
      &__slide {
        display: flex;
        border: none;
        height: 410px;
        align-items: center;
        justify-content: center;
        color: #aaa;
        font-size: 36px;
        font-weight: 600;
        border-radius: 5px;
        transition: all .3s;
        opacity: .8;
        &--active {
          border: none;
          color: #fff;
           opacity: 1;
          background: rgba(0,0,0,0.6);
        }
      }
    }
  }
}
</style>