<template>
  <div>
    <div class="d-flex justify-content-center" style="margin-bottom: 10px;">
      <div class="mx-3">
        작성자ID : {{ review.user }}
      </div>
      <div>
        별점 : {{ review.rank }}점
      </div>
      <div v-if="update">
        <div class="mx-3">
          <span>리뷰 : {{review.content}}</span>
        </div>
      </div>
      <input v-else type="text" value="#" v-model="newReview">
    </div>
    <div class="d-flex justify-content-center">
      <div class="mx-3">
        <span>
          <b-icon icon="emoji-heart-eyes" font-scale="2" @click="reviewLikeClick" v-if="!like" v-b-popover.hover.top="'이 리뷰가 마음에 듭니다.'"></b-icon>
          <b-icon icon="emoji-heart-eyes-fill" font-scale="2" @click="reviewLikeClick" v-else></b-icon>
          <span style="margin-left: 10px;" v-if="!like">좋아요 {{ likeCount }}명</span>
          <span style="margin-left: 10px;" v-else>좋아요 {{ likeCount }}명</span>
        </span>
      </div>
      <div class="mx-3">
        <span>
          <b-icon icon="emoji-angry" font-scale="2" @click="reviewHateClick" v-if="!hate" v-b-popover.hover.top="'이 리뷰가 마음에 들지 않습니다.'"></b-icon>
          <b-icon icon="emoji-angry-fill" font-scale="2" @click="reviewHateClick" v-else></b-icon>
          <span style="margin-left: 10px;" v-if="!hate">싫어요 {{ hateCount }}명</span>
          <span style="margin-left: 10px;" v-else>싫어요 {{ hateCount }}명</span>
        </span>
      </div>
      <div v-if="reviewerId === userId">
        <b-button class="mx-3" @click="updateReview" v-if="update">수정</b-button>
        <b-button class="mx-3"  variant="success" @click="pushReview" v-else>업데이트</b-button>
        <b-button class="mx-3"  variant="danger" @click="deleteReview(review)">삭제</b-button>
      </div>
    </div>
    <hr>
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
    community: Object
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
      hateCount : 0,
      reviewerId: this.review.user,
      userId : null
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
      // const movieId = this.movie.id
      console.log(review.id)
       axios({
        method: 'delete',
        url: `${SERVER_URL}/community/${this.community.id}/review/${review.id}/delete`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          console.log('성공했다요')
          this.$emit('update')
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
      // const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      this.userId = user_id
    
      const likeItem = {
        user: user_id
      }
      const reviewId = this.review.id
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/community/${this.community.id}/review/${reviewId}/like`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            this.like = res.data.like
            this.likeCount = res.data.count
            this.$emit('update')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    reviewHateClick : function () { 
      // const movieId = this.movie.id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      const reviewId = this.review.id
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/community/${this.community.id}/review/${reviewId}/hate`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            this.hate = res.data.hate
            this.hateCount = res.data.count
            this.$emit('update')
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    checkStatus : function () {
      const token = localStorage.getItem('jwt')
      const userpk = jwtDecode(token).user_id
      this.userId = userpk
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
    console.log(this.userId)
    console.log(this.review.user)
  }
}
</script>

<style>

</style>