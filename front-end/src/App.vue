<template>
  <div id="app" >
    <div id="navbar">
      <b-navbar style="background-color: rgba(0,0,0,0.3)!important;" class="fixed-top" toggleable="lg" type="dark">
       <b-navbar-brand :to='{name:"Home"}'>JayPark</b-navbar-brand>


        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav  v-if="isLogin">
            <b-nav-item :to="{ name: 'Movie' }">MOVIE</b-nav-item>
            <b-nav-item :to="{ name: 'Community' }">Community</b-nav-item>
            <b-nav-item :to="{ name:'Recommendation'}">Recommend</b-nav-item>
            <!-- <b-nav-item href="#" disabled>Disabled</b-nav-item> -->
          </b-navbar-nav>

          <b-navbar-nav class="ml-auto">
            
            <b-nav-item-dropdown right v-if="isLogin">
              <!-- Using 'button-content' slot -->
              <template #button-content>
                <em>User</em>
              </template>
              <b-dropdown-item @click="myProfile">Profile</b-dropdown-item>
              <b-dropdown-item  @click.native="logout" to="#">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>

          <!-- <b-nav-form style="display: inline-block" v-if="isLogin">
              <b-form-input  class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button  class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form> -->

        </b-collapse>
      </b-navbar>
    </div>

  <router-view style="margin-top: 56px;" @login="isLogin=true" :key="$route.fullPath"/>
  
  
  </div>
</template>

<script>
import jwtDecode from "jwt-decode"
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      useridid : null
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          // console.log(res.data,'영화스통')
          this.$store.state.communityMovie = res.data
          // console.log( this.$store.state.communityMovie)
        })
        .catch(err => {
          console.log(err)
        })
      },
      getCommunity: function () {
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/`,
        headers: this.setToken()  // 'JWT token~~~'
        .then(res => {
          console.log(res,"스토어")
          // console.log(res.data)
          this.$store.state.communityList = res.data
          // console.log( this.$store.state.communityMovie)
        })
        .catch(err => {
          console.log(err)
          })
        })
        
      },
      myProfile : function() {
        const token = localStorage.getItem('jwt')
        const user_id = jwtDecode(token).user_id
        // this.$store.state.loginUserID = user_id//
      
        // const path = `/accounts/profile/${user_id}`
          // console.log(this.$route.path)
          this.$router.push({name: "profile", params: {user_id:user_id }}).catch(()=>{})
          // if (this.$route.path !== path){
          //   this.$router.push({name: "profile", params: {user_id:user_id }})
          // }
        // this.$router.push({name: "profile", params: {user_id:user_id }})
      },
      otherProfile : function() {
        this.$router.push({name: "profile", params: {user_id: 5}})
      }
    },
  created: function () {
    // 1. Vue Instance가 생성된 직후에 호출되어 jwt를 가져오기
    const token = localStorage.getItem('jwt')
    // 2. 토큰이 있으면
    if (token) {
      // 3. true로 변경하고 없으면 유지
      const user_id = jwtDecode(token).user_id
      this.isLogin = true
      this.useridid = user_id

    
      if (localStorage.getItem('jwt')) {
        this.getMovies()
        this.getCommunity()
        var d = new Date();
        var week= new Array('일','월','화','수','목','금','토');
        this.$store.state.day = week[d.getDay()]
      
      } else {
        this.$router.push({ name: 'Login' })
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  z-index: 1;
}


#navbar {
  position: fixed-top;
}


body {
	height: 100vh;
	margin: 0;
	/* display: flex; */
	justify-content: center;
}
.menu-bar {
	border-radius: 25px;
	height: fit-content;
	display: inline-flex;
	background-color: rgba(0, 0, 0, 0.5);
	-webkit-backdrop-filter: blur(10px);
	backdrop-filter: blur(10px);
	align-items: center;
	padding: 0 10px;
	margin: 10px 0 10px 0;
}
.menu-bar li {
	list-style: none;
	color: white;
	font-family: sans-serif;
	font-weight: bold;
	padding: 12px 16px;
	margin: 0 8px;
	position: relative;
	cursor: pointer;
	white-space: nowrap;
}
.menu-bar li::before {
	content: " ";
  position: absolute;
	top: 0;
	left: 0;
	height: 100%;
	width: 100%;
	z-index: -1;
	transition: 0.2s;
	border-radius: 25px;
}
.menu-bar li:hover {
	color: black;
}
.menu-bar li:hover::before {
	background: linear-gradient(to bottom, #e8edec, #554564);
	box-shadow: 0px 3px 20px 0px black;
	transform: scale(1.2);
}

p {
  margin-bottom: 0;
} 


</style>
