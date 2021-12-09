<template>
  <div id="topp">
    <div style="padding-top: 60px; padding-bottom: 300px;">
      <div id="transe" style="background-color: rgba(0,0,0,0.5); text-align: center;width: 300px;height: 80px;margin-left: auto;margin-right: auto; border-radius : 20px; 
        ">
        <h1 style="color: white;display: inline-block;padding-top: auto;padding-top: 20px; opacity: 1; ">최신 영화 12선</h1>
      </div>
      <carousel-3d
        height="480"
        border="5"
        :autoplay="true"
        :count="movie13.length"
      >
        <slide style="border-color: rgb(26, 30, 35);" v-for="(movie, idx) in movie13" :index="idx" :key="idx">
          <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
            <img 
              @click="movieDetailInfo(movie.id)" :data-index="index" 
              :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="movie.poster_path">
          </template>
        </slide>
      </carousel-3d>
    </div>
  </div>
</template>

<script>
// import MovieListItem from '@/components/MovieListItem'
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'MovieList',
  components:{
    // MovieListItem
    Carousel3d,
    Slide
  },
  data: function () {
    return {
      movies: [],
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
    movie13: function () {
      return this.$store.state.movie13
    }
  }
}
</script>
<style>


@keyframes fadeInDown {
      0% {
          opacity: 0;
          transform: translate3d(0, -100%, 0);
      }
      to {
          opacity: 1;
          transform: translateZ(0);
      }
  }

  #topp::before{
  position: fixed; 
  top: 0; 
  left: 0; 
  right: 0; 
  bottom: 0;
  background-image: url("https://t1.daumcdn.net/cfile/tistory/227F0641574AB98428");
  background-size: 100% 100%;
  /* filter: blur(2px);  */
  z-index: -1; 
  content: "";
}

h1 {
  font-family: 'Black Han Sans', sans-serif;
}

#transe {
  animation : fadeInDown 2s;
}
</style>