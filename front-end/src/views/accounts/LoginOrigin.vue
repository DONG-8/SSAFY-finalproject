<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이메일: </label>
      <input
        type="text"
        id="username"
        v-model="credentials.username"
      >
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input
        type="password"
        id="password"
        v-model="credentials.password"
        @keyup.enter="login"
      >
    </div>
    <!-- 비밀번호가 일치하지 않는 경우가 발생할 때 에러메세지 생성 -->
    <div v-if = 'passwordToggle === true'>
      비밀번호가 일치하지 않습니다!!!
    </div>

    <button @click="login">로그인</button>
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
        password: null,
      },
      passwordToggle: false
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          localStorage.setItem('userpk',res.data )
          // this.$router.push({ name: 'TodoList' })
          // App 컴포넌트는 login data가 변경된 사실을 알 수 없기 때문에 emit login 이벤트 호출
          this.$emit('login')
          // this.$store.state.myuserId
          this.$router.push({ name : 'Movie'})
        })
        .catch(err => {
          console.log(err)
          // console.log(this.passwordToggle)
          this.passwordToggle = true
        })
    }
  }
}
</script>

<style scoped>

</style>
