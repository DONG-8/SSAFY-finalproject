<template>
  <div>
    <button @click="changePasswordForm" v-if="!changeWant">password-change want</button>
    <div v-else>
      <div v-if="!passwordsame">
        <p>현재 비밀번호</p>
        <!-- <input type="text" v-moodel="this.context.old_password"> -->
        <label for="password">비밀번호: </label>
        <input type="password" id="password">
      </div>
      <div v-else>
        <p>변경을 원하는 비밀번호</p>
          <label for="password">비밀번호: </label>
          <input type="password" id="password">

        <p>비밀번호 확인</p>
          <label for="password">비밀번호: </label>
          <input type="password" id="password">
      </div>
  
      <button @click="changePasswordForm">back</button>
    </div>
    <br>
    <hr>
      <button @click="deleteReview">delete</button>
      <!-- <button @click="findInfo">정보확인</button> -->
  </div>
</template>

<script>
import axios from 'axios'
// import jwtDecode from "jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'statusSetting.vue',
  data: function() {
    return {
      changeWant : false,
      passwordsame: false,
      context : {
        old_password :null,
        password: null,
        pssword_confirmation: null
        }
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
    deleteReview: function () {
      // const movieId = this.movie.id
      // console.log(this.review.id)
       axios({
        method: 'delete',
        url: `${SERVER_URL}/accounts/delete/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          console.log('성공했다요')
          this.$router.push({name:'Signup'})
        })
        .catch(err => {
          console.log(err)
          console.log('실패했다요')
        })
    },
    changePasswordForm: function() {
      if (this.changeWant) {
        this.changeWant=false
      } else {
      this.changeWant = true
      }
    },

  }


}
</script>

<style>

</style>