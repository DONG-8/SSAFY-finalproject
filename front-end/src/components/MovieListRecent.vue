<template>
  <div style="background-color: #1a1e23; padding-top: 60px;">
    <h3 style="color:white">장르별</h3>
    <div style="
    padding-top: 0px;">
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="최신">최신</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="horrorMovies">공포</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="sfMovies">SF</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="criminalMovies">범죄</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="mysteryMovies">미스터리</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="thrillerMovies">스릴러</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="romanceMovies">멜로/로맨스</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="fantasyMovies">판타지</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="warMovies">전쟁</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="animationMovies">애니메이션</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="adventureMovies">모험</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="documentaryMovies">다큐멘터리</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="actionMovies">액션</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="dramaMovies">드라마</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="suspenseMovies">서스펜스</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="comedyMovies">코미디</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="familyMovies">가족</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="concertMovies">콘서트</b-button>
      <b-button pill variant="secondary" class="mx-2 my-2" @click="valueChange" value="musicalMovies">뮤지컬</b-button>
    </div>
    <div>
      <h3 style="color:white">연령별</h3>
      <hr>  
      <b-button pill variant="secondary" class="mx-2"  @click="ageChange" value="모든연령">ALL</b-button>
      <b-button pill variant="secondary" class="mx-2"  @click="ageChange" value="전체">전체관람가능</b-button>
      <b-button pill variant="secondary" class="mx-2"  @click="ageChange" value="12세">12세이상 관람가능</b-button>
      <b-button pill variant="secondary" class="mx-2"  @click="ageChange" value="15세">15세이상 관람가능</b-button>
      <b-button pill variant="secondary" class="mx-2"  @click="ageChange" value="19세">19세이상 관람가능</b-button>

    </div>

    <br>
    <hr>
    <h2 style="color: white">{{genreName}} 영화 목록</h2>
    <br>
    <br>
      <div v-if="genreId==='최신'">
        <b-card-group deck
          class="d-flex justify-content-center"
        >
          <movie-list-recent-item-copy
            v-for="(movie, idx) in movies" :key="idx"
            :movie="movie"
            @like-change="getMovies"
            >
          </movie-list-recent-item-copy >
        </b-card-group>
      </div>
      <div v-else>
        <div v-if="age==='모든연령'">
          <b-card-group deck
            class="d-flex justify-content-center"
          >
            <movie-genre-list
              v-for="gmovie in changeList"
              :key="gmovie.idx"
              :gmovie="gmovie"
              :genreName="genreName"
              @change="getGenre">    
            </movie-genre-list>
          </b-card-group>
        </div>
        <div v-else>
          <b-card-group deck
            class="d-flex justify-content-center"
          >
            <movie-genre-list
              v-for="gmovie in ageList"
              :key="gmovie.idx"
              :gmovie="gmovie"
              :genreName="genreName"
              @change="getGenre">
            </movie-genre-list>
          </b-card-group>
        </div>
      </div>



    <br>
    
  </div>
</template>

<script>
// import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'
// import jwtDecode from "jwt-decode"

import MovieListRecentItemCopy from '@/components/MovieListRecentItemCopy.vue'
import MovieGenreList from '@/components/MovieGenreList.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieList',
  components:{
    MovieListRecentItemCopy,
    MovieGenreList
  },
  data: function () {
    return {
      movies: [],
      genreMovie: null,
      genreId : "최신",
      changeList: null,
      genreName: "최신 ",
      age: "모든연령",
      ageList : null
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
      // const token = localStorage.getItem('jwt')
      // const user_id = jwtDecode(token).user_id
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/recent/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          console.log(res.data,"여기에용")
          this.movies = res.data
          // if (this.movies.like_users.includes(user_id)) {

          // }
        })
        .catch(err => {
          console.log(err)
        })
      },
      getGenre : function () {
        axios({
        method: 'get',
        url: `${SERVER_URL}/movies/movie_by_genre/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res.data)
          // console.log(res.data)
          // this.movies = res.data
          // console.log('앙 기모띵')
          this.genreMovie = res.data
        })
        .catch(err => {
          console.log(err)
        })
      },
      valueChange : function (event) {
        // console.log(event.target.innerText)
        this.age = "모든연령"
        this.genreName = event.target.innerText
        this.genreId = event.target.value
        const genreId = this.genreId
        //  const age = this.age
        
        for (const genre in this.genreMovie) {
          if (genre === genreId) {
            this.changeList = this.genreMovie[genre]
          }
        }
        // } else {
      
        //   console.log(age)
        //   for (const genre in this.genreMovie) {
        //     if (genre === genreId) {
        //       this.changeList = this.genreMovie[genre]
        //     }
          
        //   for (const ageGenre in this.changeList) {
        //     console.log(ageGenre)
        //   }
        //   }
        // }
        // console.log(this.changeList)
      },
      ageChange : function (event) {
        console.log(event.target.value)
        this.age = event.target.value
        const age = this.age
   
         if (age==="모든연령") {
            // console.log(ageList.grade[0].rating)
            console.log('앙')
          }
          else if (age==="전체") {
            console.log(this.changeList)
            this.ageList = this.changeList.filter(list =>
                list.grade[0].rating === "전체 관람가"
              )
          }
          else if (age==="12세") {
            console.log(this.changeList)
            this.ageList = this.changeList.filter(list =>
                list.grade[0].rating === "12세 관람가"
              )
          }
          else if (age==="15세") {
            console.log(this.changeList)
            this.ageList = this.changeList.filter(list =>
                list.grade[0].rating === "15세 관람가"
              )
          }
          else {
            this.ageList = this.changeList.filter(list =>
                list.grade[0].rating === "청소년 관람불가"
              )
          }
      }
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
      this.getGenre()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style>

</style>