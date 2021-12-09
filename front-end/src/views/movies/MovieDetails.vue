<template>
  <div class="topp">
    <div class="is-full featured_wrapper p-0">
      <img id="topId" :src="imgsrc" class="featured">
      <div class="title_wrapper">
          <h1 class="has-text-white">{{ movieTitle }}</h1>
          <div style="float: right; padding-right: 100px; padding-bottom: 100px;">
            <img style="width: 280px;" :src="imgsrc" alt="">
          </div>
          <br>
          <div class="d-flex justify-content-start">
            <div style="margin-right: 30px;">
              <b-icon icon="star" font-scale="2" @click="movieFavorit" v-if="!favorite" v-b-popover.hover.top="'내가 찜한 콘텐츠에 추가'"></b-icon>
              <b-icon icon="star-fill" font-scale="2" @click="movieFavorit" v-else v-b-popover.hover.top="'내가 찜한 콘텐츠에서 제거'"></b-icon>
            </div>
            <div style="margin-right: 30px;">
              <span>
                <b-icon icon="emoji-smile" font-scale="2" @click="movieLike" v-if="!like" v-b-popover.hover.top="'이 영화가 마음에 듭니다.'"></b-icon>
                <b-icon icon="emoji-smile-fill" font-scale="2" @click="movieLike" v-else v-b-popover.hover.top="`${likeCount}명이 좋아합니다.`"></b-icon>
              </span>
            </div>
            <div>
              <span>
                <b-icon icon="emoji-frown" font-scale="2" @click="movieHate" v-if="!hate" v-b-popover.hover.top="'이 영화가 마음에 들지 않습니다.'"></b-icon>
                <b-icon icon="emoji-frown-fill" font-scale="2" @click="movieHate" v-else v-b-popover.hover.top="`${hateCount}명이 싫어합니다.`"></b-icon>
              </span>
            </div>
          </div>
          <br>
          <span style="font-size: 1.3rem;">관람객 평점: <b-icon icon="star-fill" style="color : yellow;"></b-icon> {{ vote }}점</span>
          <br><br>
          <div>출연: {{ actors }}</div>
          <div>장르: {{ genres }}</div>
          <br>
          <div>{{ openDate }}  |  {{ runTime }}</div>
          <div>{{ grade }}</div>
          <div>국가: {{ country }}</div>
          <br>
          <div style="width: 50%"><span class="title is-1 has-text-white">{{ content }}</span></div>
          <br>
          <b-icon v-b-modal.modal-1 icon="youtube" font-scale="5" style="color: #d03939;"></b-icon>
          <b-modal id="modal-1" title="Youtube 관련 영상">
            <div>
              <b-embed
                type="iframe"
                aspect="16by9"
                :src="youtubeList"
                allowfullscreen
              ></b-embed>
            </div>
          </b-modal>
      </div>
    </div>
    <div>
      <br>
      <h2 style="color: white;text-align: center;margin-left: 0px;margin-bottom: 20px;">추천 영화 리스트</h2>
      <b-container class="bv-example-row">
        <b-row class="text-center">
          <b-col v-for="(smovie, idx) in simmilarMovie" :key="idx">
            <img @click="movieDetailInfo(smovie.id)" style="margin-bottom: 100px;" :src="smovie.poster_path" alt="" />
          </b-col>
        </b-row>
      </b-container>
      
      


    </div>
  </div>

</template>

<script>
import axios from 'axios'
// import ReviewForm from './ReviewForm.vue'
// import ReviewList from './ReviewList.vue'
// import youtubeList from './youtubeList.vue'
// import simmilar from '@/views/movies/simmilar.vue'
// import ReviewForm from './ReviewForm.vue'
// import Review from '@/views/movies/Review.vue'
// import Review from './Review.vue'
import _ from 'lodash'
import jwtDecode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetails',
  components:{
    // ReviewList,
    // ReviewForm,
    // youtubeList,
    // simmilar
    },
    data: function () {
      return {
        movie: null,
        movieId: "",
        update : true,
        content : null,
        movieTitle : "",
        youtubeList : [],
        simmilarMovie: [],
        imgsrc: "",
        actors: "",
        genres: "",
        openDate: "",
        runTime: "",
        country: "",
        grade: "",
        vote: "",
        likeCount : null,
        like : null,
        hateCount : 0,
        hate : null,
        favorite : null,
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
      const movieId = this.$route.params.movieId

      axios({
        method: 'GET',
        url: `${SERVER_URL}/movies/${movieId}`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          console.log(res)
          this.movie = res.data
          this.movieId = res.data.movie.id
          // console.log(this.movie,'여기')
          this.movieTitle =res.data.movie.title
          this.simmilarMovie = res.data.similar_movies
          this.content = _.replace(res.data.movie.content, "[", "")
          this.content = _.replace(this.content, "]", "")
          this.imgsrc = res.data.movie.poster_path
          this.actors = res.data.movie.actor_1 + ',' + res.data.movie.actor_2 + ',' + res.data.movie.actor_3
          for (var genre of res.data.movie.genre) {
            this.genres = this.genres + genre.name + ','
          }
          this.openDate = res.data.movie.year + '년 ' + res.data.movie.month + '월 '
          this.runTime = res.data.movie.time
          this.country = res.data.movie.country
          this.grade = res.data.movie.grade[0].rating
          this.vote = res.data.movie.vote
        })
        .catch(err => {
          console.log(err)
        })
      },
    getYoutubeList : function() {
      const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
      const YOUTUBE_KEY = "AIzaSyAl95MuzIshQD-mpyN5iNvM6oRcOE154Ag"
      let movie = this.$route.params.movieId
      let movieId = parseInt(movie)
      this.movieTitle = this.$store.state.communityMovie[movieId].title
      const params = {
        q: this.movieTitle,
        key: YOUTUBE_KEY,
        part: 'snippet',
        type: 'video',
        maxResults : 1
      }
        axios({
          method: 'get',
          url: YOUTUBE_URL,
          params,
        })
        .then(res => {
          console.log(res,'youtube')
          const videoId = res.data.items[0].id.videoId
          console.log(videoId)
          this.youtubeList = `https://www.youtube.com/embed/${videoId}`
        })
        .catch(err => console.log(err))
      },
    movieDetailInfo: function(movie_id) {
      window.scrollTo(0,0)
      this.$router.push(
        { name : 'MovieDetails', 
          params: {
            movieId : movie_id,
          }
        })
      },
    movieLike : function () { 
      console.log(this.movieId)
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${this.movieId}/like/`,
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
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${this.movieId}/hate/`,
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
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${this.movieId}/favorite/`,
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
  },

  created: function () {
    if (localStorage.getItem('jwt')) {
      let movie = this.$route.params.movieId
      let movieId = parseInt(movie)
      console.log(movieId)
      this.movieTitle = this.$store.state.communityMovie[movieId].title
      this.movie = this.$store.state.communityMovie[movieId]
      this.getYoutubeList()
      this.setToken()
      this.getMovies()
    } else {
      this.$router.push({ name: 'Login' })
    }

  },
  watch :{
    getYoutubeList : function() {
      this.youtubeList = this.getYoutubeList()
    }
  },
  computed: {

  }
}
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400;800&display=swap");

body,
html {
	background: #000000;
	padding: 0;
	margin: 0;
	// padding-bottom: 6rem;
	font-family: "Montserrat", sans-serif;
	width: 100%;
}

.topp {
   background-color: #1a1e23;
   margin-top: 0px!important;
}

img {
	-webkit-box-reflect: below 5px
		linear-gradient(transparent, transparent, rgba(0, 0, 0, 0.4));
	-webkit-transition: all 0.5s ease;
	-o-transition: all 0.5s ease;
	transition: all 0.5s ease;
}

.container img:hover {
	-webkit-transform: scale(1.1);
	-ms-transform: scale(1.1);
	transform: scale(1.1);
}

.featured_wrapper {
	position: relative;
}

#topId {
	width: 100%;
	width: 90%;
	height: 800px;
	-o-object-fit: cover;
	object-fit: cover;
	-o-object-position: top;
	object-position: top;
  padding-left: 600px;
  opacity: 0.2;
}


.title_wrapper {
  font-weight: bold;
	position: absolute;
	width: 100%;
	left: 2rem;
	bottom: 5rem;
	padding: 20px 40px;
	-webkit-box-sizing: border-box;
	box-sizing: border-box;
  text-align: left;
  color: white;
}
.title_wrapper h1 {
  font-size: 3rem;
	width: 70%;
}

@media (max-width: 768px) {
	.title_wrapper {
		text-align: center;
		left: 0;
	}
	.title_wrapper h1 {
		font-size: 32px !important;
		width: 100%;
	}
}

</style>