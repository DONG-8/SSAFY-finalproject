<template>
  <div>
    <div class="container">
      <div class="movie">
        <div class="movie-image">
          <img style="width: 100%;" :src="gmovie.poster_path" alt="" />
          <span><i class="fa fa-align-lef"></i></span>
        </div>
        <div class="movie-info">
          <p class="title">{{ gmovie.title }}</p>
          <p class="genres">
            <span v-for="(genre, idx) in gmovie.genre" :key="idx">
              {{ genre.name }}
            </span>
          </p>
          <div class="movie-text">
            <div class="likes">
              <b-container fluid class="bv-example-row">
                <b-row>
                  <b-col>
                    <b-icon icon="star" font-scale="2" @click="movieFavorit" v-if="!favorite" v-b-popover.hover.top="'내가 찜한 콘텐츠에 추가'"></b-icon>
                    <b-icon icon="star-fill" font-scale="2" @click="movieFavorit" v-else v-b-popover.hover.top="'내가 찜한 콘텐츠에서 제거'"></b-icon>
                  </b-col>
                  <b-col>
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
            </div>
            <div class="actions">
              <button @click="movieDetailInfo(gmovie.id)">Go to Detail</button>
              <div class="actions-more">
                <i class="fa fa-save"></i>
                <i class="fa fa-bookmark"></i>
                <i class="fa fa-share-alt"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "MovieGenreList",
  props: {
    gmovie : Object,
    genreName : String,
  },
  data: function () {
    return {
      likeCount : null,
      like : null,
      hateCount : 0,
      hate : null,
      favorite : null,
      modalShow: false
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
      const movieId = this.gmovie.id
      console.log(this.gmovie.id)
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
            console.log('리센트무비')
            this.like = res.data.like
            this.likeCount  = res.data.count
            this.$emit('change')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    movieHate : function () { 
      const movieId = this.gmovie.id
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
            this.$emit('change')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    movieFavorit : function () { 
      const movieId = this.gmovie.id
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
  
            this.$emit('change')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    getData : function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      if (this.gmovie.like_users.includes(user_id)) { 
        this.like = true
      } else {
        this.like = false
      }
      if (this.gmovie.hate_users.includes(user_id)) { 
        this.hate = true
      } else {
        this.hate = false
      }
      if (this.gmovie.favorite_users.includes(user_id)) { 
        this.favorite = true
      } else {
        this.favorite = false
      }
      this.likeCount = this.gmovie.like_users.length
      this.hateCount = this.gmovie.hate_users.length
      
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
    imgSrc : function() {
      const imgsrc = this.gmovie.poster_path
      return imgsrc
    },
  },
  created: function () {
    this.getData()
  }
}
</script>


<style scoped lang="scss">
*,
*::after,
*::before{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body{
  height: 100%;
  background: url("https://i.pinimg.com/originals/af/8d/63/af8d63a477078732b79ff9d9fc60873f.jpg");
  background-size: cover;
  background-attachment: fixed;
  background-repeat: no-repeat;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  padding: 60px 0;
}

.movie{
  width: 300px;
  height: 660px;
  background: #1e1b26;
  display: flex;
  flex-direction: column;
  border-radius: 3px;
  margin: 0 20px 0 20px;
  box-shadow: 0 0 20px;
  -webkit-transition: all 0.5s ease;
	-o-transition: all 0.5s ease;
	transition: all 0.5s ease;
}

.movie:hover {
    -webkit-transform: scale(1.1);
    -ms-transform: scale(1.1);
    transform: scale(1.1);
}

.movie-image-1{
  background: url("https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201703/07/7696c9d8-f8bd-4604-b481-fa2402786d14.jpg"), rgb(30, 27, 38);
}

.movie-image{
  // max-height: 350px;
  // height: 55%;
  width: 100%;
  position: relative;
  background-size: cover;
  background-blend-mode: screen;
  -webkit-mask-image: -webkit-gradient(linear, left top, left bottom, 
			color-stop(0.00,  rgba(0,0,0,1)),
			color-stop(0.35,  rgba(0,0,0,1)),
			color-stop(0.50,  rgba(0,0,0,1)),
			color-stop(0.65,  rgba(0,0,0,1)),
			color-stop(0.85,  rgba(0,0,0,0.6)),
      color-stop(1.00,  rgba(0,0,0,0)));
}

// img{
//   -webkit-transition: all 0.5s ease;
// 	-o-transition: all 0.5s ease;
// 	transition: all 0.5s ease;
// }

// .movie-image img:hover {
//     -webkit-transform: scale(1.1);
//     -ms-transform: scale(1.1);
//     transform: scale(1.1);
// }

.movie-image span{
  position: absolute;
  top: 0;
  right: 0;
  margin: 10px;
  font-size: 1.5rem;
}

.movie-info{
  color: #bbb;
  font-family: "Open Sans", sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 15px;
}

.title {
  font-size: 1.3rem;
  margin-bottom: 5px;
}

.genres {
  font-size: 0.8rem;
  color: gray;
  margin-top: -2px;
}

.movie-text {
  // display: flex;
  // justify-content: space-between;
  margin-top: 10px;
}

.movie-text p:nth-child(1){
  font-size: 0.8rem;;
}

.likes {
  color: #f44336;
  font-size: 0.8rem;
}

.likes span{
  margin-left: 10px;
}

.summary {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: justify;
  margin: 5px 0;
}

.text {
  font-size: 0.7rem;
  color: gray;
  margin-bottom: 5px;
}

.cast {
  font-size: 0.7rem;
  font-style: italic;
  color: #bbb;
}

.actions {
  margin: 10px 0;
  display: flex;
  justify-content: space-between;
}

button {
  padding: 3px 8px;
  background: transparent;
  border: 1px solid #f44336;
  color: #f44336;
  font-size: 1rem;
  letter-spacing: 1px;
  border-radius: 3px;
  cursor: pointer;
}

button:hover i{
  color: #eee;
}

button:hover {
  color: #eee;
  background-color: #f44336;
}

button .fa{
  font-size: 0.8rem;
}

.fa{
  color:#f44336;
  margin-right: 5px;
}

.actions-more .fa{
  margin-right: 10px;
  font-size: 1.5rem;
}

</style>