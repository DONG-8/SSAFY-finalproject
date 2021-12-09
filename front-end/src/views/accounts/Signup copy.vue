<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이메일: </label>
      <input
        type="text"
        id="username"
        v-model="credentials.username"
      >
      <button>중복확인</button>
    </div>
    <div>
      <label for="nickname">닉네임: </label>
      <input
        type="text"
        id="nickname"
        v-model="credentials.nickname"
      >
      <button>중복확인</button>
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input
        type="password"
        id="password"
        v-model="credentials.password"
      >
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input
        type="password"
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
        @keyup.enter="signup"
      >
      <div v-if = 'credentials.password === credentials.passwordConfirmation'>
        비밀번호가 일치합니다!
      </div>
      <div v-else>
        비밀번호가 일치하지 않습니다
      </div>
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        nickname: null,
        password: null, 
        passwordConfirmation: null,
      },
      passwordToggle: false
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
          this.passwordToggle = true
        })
    }
  }
}
</script>

<style scoped>

</style>