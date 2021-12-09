<template>
  <div>
    <b-card
      :img-src="imgSrc"
      img-alt="Image"
      img-top 
      img-width="280px"
      img-height="450px"
      style="width: 290px; height: 528px;"
      class="my-5"
    >
      <b-button @click="modalShow = !modalShow">Go to Detail</b-button>

      <b-modal v-model="modalShow" :title="movie.title" ok-only button-size="ml">
        <br>
        <center>
          <img @click="movieDetailInfo(movie.id)" :src="imgSrc" alt="" style="width: 300px">
        </center>
          <br><br><hr><br>
        <span>출연  :  {{ movie.actor_1 }}, {{movie.actor_2}}, {{ movie.actor_3 }}</span>
        <br><br>
        <span>장르  :  </span>
        <span v-for="(genre, idx) in movie.genre" :key="idx">
          {{ genre.name }}
        </span>
        <br><br>
        <span>평점  :  {{ movie.vote }}</span>
        <pre>

        </pre>
        <b-container fluid class="bv-example-row">
          <b-row>
            <b-col offset-md="1">
              <b-icon icon="star" font-scale="2" @click="movieFavorit" v-if="!favorite" v-b-popover.hover.top="'내가 찜한 콘텐츠에 추가'"></b-icon>
              <b-icon icon="star-fill" font-scale="2" @click="movieFavorit" v-else v-b-popover.hover.top="'내가 찜한 콘텐츠에서 제거'"></b-icon>
            </b-col>
            <b-col offset-md="4">
              <span>
                <b-icon icon="emoji-smile" font-scale="2" @click="movieLike" v-if="!like" v-b-popover.hover.top="'이 영화가 마음에 듭니다.'"></b-icon>
                <b-icon icon="emoji-smile-fill" font-scale="2" @click="movieLike" v-else v-b-popover.hover.top="`${likeCount}명이 좋아합니다.`"></b-icon>
              </span>
            </b-col>
            <b-col>
              <span>
                <b-icon icon="emoji-frown" font-scale="2" @click="movieHate" v-if="!hate" v-b-popover.hover.top="'이 영화가 마음에 들지 않습니다.'"></b-icon>
                <b-icon icon="emoji-frown-fill" font-scale="2" @click="movieHate" v-else v-b-popover.hover.top="`${hateCount}명이 싫어합니다.`"></b-icon>
              </span>
            </b-col>
          </b-row>
          <br>
        </b-container>

      </b-modal>
    </b-card>
  </div>
  
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name : 'MovieListRecentItem',
  props: {
    movie: Object
  },
  data : function () {
    return {
      likeCount : null,
      like : null,
      hateCount : 0,
      hate : null,
      favorite : null,
      modalShow: false
      // itemData : this.movie
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
    movieLike : function () { 
      const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/like/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.like = res.data.like
            this.likeCount  = res.data.count
            this.$emit('like-change')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    movieHate : function () { 
      const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/hate/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.hate = res.data.hate
            this.hateCount  = res.data.count
            this.$emit('like-change')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    movieFavorit : function () { 
      const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/favorite/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.favorite = res.data.favorite
            this.$emit('like-change')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    getData : function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      if (this.movie.like_users.includes(user_id)) { 
        this.like = true
      } else {
        this.like = false
      }
      if (this.movie.hate_users.includes(user_id)) { 
        this.hate = true
      } else {
        this.hate = false
      }
      if (this.movie.favorite_users.includes(user_id)) { 
        this.favorite = true
      } else {
        this.favorite = false
      }
      this.likeCount = this.movie.like_users.length
      this.hateCount = this.movie.hate_users.length
      
    },
    movieDetailInfo: function() {
      window.scrollTo(0,0)
      this.$router.push(
        { name : 'MovieDetails', 
          params: {
            movieId : this.movie.id,
          }
      })
    }
  },
  computed: {
    imgSrc : function() {
      const imgsrc = this.movie.poster_path
      return imgsrc
    },
  },
  created: function () {
    this.getData()
  }
  // watch : {
  //   movieLike : function () {
  //     this.movie = this.getMovies()
  //   }
  // }
  
}
</script>

<style>

</style>