<template>
  <div>
    <p>{{review.rank}}</p>
    <!-- <p>{{review}}</p> -->
    <!-- <p>{{review.content}}</p> -->
    <p v-if="update">{{review.content}}</p>
    <input v-else type="text" value="#" v-model="newReview">
    <button @click="updateReview" v-if="update">수정</button>
    <button @click="pushReview" v-else>업데이트</button>

    <button @click="deleteReview(review)">삭제</button>

    <button @click="reviewLikeClick" v-if="!like">좋아요</button>
    <button @click="reviewLikeClick" v-else>좋아요취소</button>
    <p>좋아요 갯수 {{this.likeCount}}</p>
    <button @click="reviewHateClick" v-if="!hate">싫어요</button>
    <button @click="reviewHateClick" v-else>싫어요취소</button>
    <p>싫어요 갯수 {{this.hateCount}}</p>
    <!-- <button>싫어요</button> -->
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"

const SERVER_URL = process.env.VUE_APP_SERVER_URL


export default {
  name: 'ReviewList',
  props: {
    review: Object,
    movie: Object
  },
  data: function () {
    return {
      update : true,
      content : this.review.content,
      newReview : null,
      reviewLike : null,
      reviewLikeCount: null,
      like: false,
      likeCount : 0,
      hate: false,
      hateCount : 0
    }
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteReview: function (review) {
      const movieId = this.movie.id
      // console.log(this.review.id)
       axios({
        method: 'delete',
        url: `${SERVER_URL}/movies/${movieId}/review/${review.id}/delete`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          console.log('성공했다요')
          this.$emit('update-review')
        })
        .catch(err => {
          console.log(err)
          console.log('실패했다요')
        })
    },
    updateReview: function () {
      this.update = false
    },
    pushReview: function() {
      this.review.content = this.newReview
      this.update = true
    },
    reviewLikeClick : function () { 
      const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      const reviewId = this.review.id
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/review/${reviewId}/like/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            this.like = res.data.like
            this.likeCount = res.data.count
            this.$emit('like-update')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    reviewHateClick : function () { 
      const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      const reviewId = this.review.id
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${movieId}/review/${reviewId}/hate/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            this.hate = res.data.hate
            this.hateCount = res.data.count
            this.$emit('hate-update')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    checkStatus : function () {
      const token = localStorage.getItem('jwt')
      const userpk = jwtDecode(token).user_id
      if (this.review.like_users.includes(userpk)) {
        this.like = true
      } else {
        this.like = false
      }
      if (this.review.hate_users.includes(userpk)) {
        this.hate = true
      } else {
        this.hate = false
      }
      // console.log(this.review.like_users.length)
      this.likeCount =this.review.like_users.length
      this.hateCount= this.review.hate_users.length
    }
  },
  created : function() {
    this.checkStatus()
  }
}
</script>

<style>

</style>