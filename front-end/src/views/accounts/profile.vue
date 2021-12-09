<template>
  <div id="topp">
    <div class="container">
      <header>
        <i class="fa fa-bars" aria-hidden="true"></i>
      </header>
      <main>
        <div class="row">
          <div class="left col-lg-4">
            <div class="photo-left">
              <img class="photo" src="https://mblogthumb-phinf.pstatic.net/MjAyMTAzMjVfMjQ1/MDAxNjE2NjczNDM4MjY1.jjotNR5RgwVQwtsRltMqI3cCv_wdGKURL1bbPVmNoIgg.J0M7ucbY-PsGmAP5YWBoCNmkXkqlVYW7kKZ9sbgyFeUg.JPEG.aas0728/1616663255.jpg?type=w800"/>
              <div class="active"></div>
            </div>
            <h4 class="name">{{ nickname }}</h4>
            <p class="info">Movie Exper</p>
            <p class="info">{{ username }}</p>
            <div class="stats row">
              <div class="stat col-xs-4" style="padding-right: 50px;">
                <p class="number-stat">{{ follower }}</p>
                <p class="desc-stat">Followers</p>
                <!-- <b-icon id="dropdown-1" icon="card-list"> -->
                  <b-dropdown size="sm" text="List..." variant="secondary" class="m-2">
                    <div v-for="(list, idx) in followerList" :key="idx">
                      <b-dropdown-item>
                        {{ list.nickname }}
                      </b-dropdown-item>
                    </div>
                  </b-dropdown>
                <!-- </b-icon> -->
              </div>
              <div class="stat col-xs-4">
                <p class="number-stat">{{ following }}</p>
                <p class="desc-stat">Following</p>
                <b-dropdown size="sm" text="List..." variant="secondary" class="m-2">
                    <div v-for="(list, idx) in followingList" :key="idx">
                      <b-dropdown-item>
                        {{ list.nickname }}
                      </b-dropdown-item>
                    </div>
                  </b-dropdown>
              </div>
              <div class="stat col-xs-4" style="padding-left: 50px;">
                <p class="number-stat">{{ userCreateCommunity.length }}</p>
                <p class="desc-stat">Uploads</p>
              </div>
            </div>
            <p class="desc">Hi ! My nickname is {{ nickname }}. <br> Nice to Meet you <br> Let me introduce my profile page</p>
          </div>
          <div class="right col-lg-8">
            <ul class="nav mb-3">
              <li @click="selectProfile" value="LikeMovies">LikeMovies</li>
              <li @click="selectProfile" value="Communities">Communities</li>
              <li @click="selectProfile" value="Favorites">Favorites</li>
            </ul>
            <div v-if="itsME">
              <span class="follow">Me</span>
            </div>
            <div v-else>
              <div v-if="followBoolen">
                <span @click="follow" class="follow">Follow</span>
              </div>
              <div v-else>
                <span @click="follow" class="follow">Unfollow</span>
              </div>
            </div>
            
            <div v-if="select==='LikeMovies'">
              <profile-item :list-array="userLikeMovies" :select="select"></profile-item>
            </div>
            <div v-else-if="select==='Communities'">
              <profile-item :list-array="userCreateCommunity" :select="select"></profile-item>
            </div>
            <div v-else>
              <profile-item :list-array="userFavoriteMovies" :select="select"></profile-item>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>


<script>
// import MovieListItem from '@/views/movies/MovieListItem'
import axios from 'axios'
import jwtDecode from "jwt-decode"
import ProfileItem from '@/views/accounts/ProfileItem'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'profile',
  data: function () {
    return {
      userData : null,
      itsMe : '',
      userId : null,
      nickname : null,
      username: null,
      followBoolen: false,
      follower: 0,
      following: 0,
      allData : null,
      followerList : null,
      followingList : null,
      owList : false,
      ingList : false,
      userLikeMovies : [],
      reviewInMovies : [],
      userCreateCommunity : [],
      userLikeCommunity : [],
      userFavoriteMovies: [],
      select: 'LikeMovies',
      pageNum: 0,
    }
  },
  components: {
    ProfileItem,
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },

    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getUserProfile: function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const userId = this.$route.params.user_id
      console.log(user_id,'로그인한유저')
      const userpk = parseInt(userId)
      console.log(userpk,'프로필의 유저')
      if (userpk === user_id) {
        this.itsMe = true
        console.log('같은유저네요')
      } else {
        this.itsMe = false
      }
      axios({
          method: 'GET',
          url: `${SERVER_URL}/accounts/profile/${userId}/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res.data, '성공이여')
            // console.log('성공이여')
            // console.log(res.data,'여기염')
            this.allData = res.data
            this.userData = res.data.userInfo
            this.nickname = res.data.userInfo.nickname
            this.username = res.data.userInfo.username
            this.userLikeMovies = res.data.userLikeMovies
            this.reviewInMovies = res.data.reviewInMovies
            this.userCreateCommunity = res.data.userCreateCommunity
            this.userFavoriteMovies = res.data.userFavoriteMovies
            
            // console.log(res.data,'유저데이터')
           
              
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })

    },
    goToSetting: function() {
      this.$router.push({name:'Setting'})
    },
    follow : function() {
      const profile_id = this.$route.params.user_id
      console.log(profile_id)
      const movieItem = {
        user : profile_id,
        }
        axios({
          method: 'post',
          url: `${SERVER_URL}/accounts/${profile_id}/follow/`,
          data: movieItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log(res.data, '성공했슴다팔로우')
            this.followBoolen= res.data.follow
            // console.log(res.data.followers)
            this.follower= res.data.followers
            this.following= res.data.followings
            this.getData()
            // this.$route.push({name:"profile",params: {user_id:profile_id}})
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })

    },
    getData : function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const profile_id = this.$route.params.user_id
      // console.log(profile_id)
      axios({
        method: 'get',
        url: `${SERVER_URL}/accounts/${profile_id}/follow_list/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          console.log('성공했슴다1')
          const list = res.data.followers.filter(user =>
              user.pk === user_id
              )
          // console.log(list.length)
          if (list.length) {
            this.followBoolen = false
            console.log('팔로우하고있음',this.followBoolen)
          } else {
            this.followBoolen = true
            console.log('팔로우취소',this.followBoolen)
          }
          console.log(this.followBoolen)
          console.log(res.data.followers.length)
          this.follower = res.data.followers.length
          this.following = res.data.followings.length
          this.followerList = res.data.followers
          this.followingList = res.data.followings
          console.log(this.followerList)
          console.log(this.followingList, '팔로잉리스트')
        })
        .catch(err => {
          console.log(err)
          console.log('실패')
        })
      },
    owChange : function () {
      if (this.owList === true) {
        console.log('떠라')
        this.owList = false
      } else {
        this.owList = true
      }
      // this.getData()
    },
    ingChanges : function () {
      if (this.ingList === true) {
        console.log('왔다')
        this.ingList = false
      } else {
        this.ingList = true
      }
      // this.getData()
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
    selectProfile: function (event) {
      this.select = event.target.textContent
      console.log(this.select)
    }
  },

  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getUserProfile()
      this.getData()
      console.log(this.itsMe,'생성')
      // this.getData()
      // console.log('로그인은됨')
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
  // computed: function() {
  //     // this.getData()
  // }
  
}
</script>

<style scoped>

#app {
  z-index: auto;
}

#topp::before {
  position: fixed; 
  top: 0; 
  left: 0; 
  right: 0; 
  bottom: 0;
  background-image: url("https://t1.daumcdn.net/cfile/tistory/99AB80505BFC000121");
  background-size: 100% 100%;
  filter: blur(2px); 
  z-index: -1; 
  content: "";
}

.container {
  max-width: 1500px;
  margin: 100px auto 30px;
  padding: 0px!important;
  width: 90%;
  background-color: #fff;
  box-shadow: 0 3px 6px rgba(0,0,0,0.10), 0 3px 6px rgba(0,0,0,0.10);
}

header {
  background: #eee;
  background-image: url("https://t1.daumcdn.net/cfile/tistory/99AB80505BFC000121");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  /* background-color: gold; */
  height: 250px;
}

header i {
  position: relative;
  cursor: pointer;
  right: -96%;
  top: 25px;
  font-size: 18px !important;
  color: #fff;
}

@media (max-width:800px) {
  header {
    height: 150px;
  } 
  
  header i {
    right: -90%;
  }
}

main {
      padding: 20px 20px 0px 20px;
}

.left {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.photo {
  width: 200px;
  height: 200px;
  margin-top: -120px;
  border-radius: 100px;
  border: 4px solid #fff;
}

.active {
  width: 20px;
  height: 20px;
  border-radius: 20px;
  position: absolute;
  right: calc(50% - 70px);
  top: 75px;
  background-color: #FFC107;
  border: 3px solid #fff;
}

@media (max-width:990px) {
  .active {
    right: calc(50% - 60px);
    top: 50px;
  } 
}

.name {
  margin-top: 20px;
  font-family: "Open Sans";
  font-weight: 600;
  font-size: 18pt;
  color: #777;
}

.info {
  margin-top: -5px;
  margin-bottom: 5px;
  font-family: 'Montserrat', sans-serif;
  font-size: 11pt;
  color: #aaa;
}

.stats {
  margin-top: 25px;
  text-align: center;
  padding-bottom: 20px;
  border-bottom: 1px solid #ededed;
  font-family: 'Montserrat', sans-serif;
}


.number-stat {
  padding: 0px;
  font-size: 14pt;
  font-weight: bold;
  font-family: 'Montserrat', sans-serif;
  color: #aaa;
}

.desc-stat {
  margin-top: -15px;
  font-size: 10pt;
  color: #bbb;
}

.desc {
  text-align: center;
  margin-top: 25px;
  margin: 25px 40px;
  color: #999;
  font-size: 11pt;
  font-family: "Open Sans";
  padding-bottom: 25px;
  border-bottom: 1px solid #ededed;
}

.social {
  margin: 5px 0 12px 0;
  text-align: center;
  display: inline-block;
  font-size: 20pt;
}

.social i {
  cursor: pointer;
  margin: 0 15px;
}

.social i:nth-child(1)  { color: #4267b2; }
.social i:nth-child(2)  { color: #1da1f2; }
.social i:nth-child(3)  { color: #bd081c; }
.social i:nth-child(4)  { color: #36465d; }

.right {
  padding: 0 25px 0 25px !important;
}

.nav {
  display: inline-flex;
}

.nav li {
  margin: 40px 30px 0 10px;
  cursor: pointer;
  font-size: 13pt;
  text-transform: uppercase;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  color: #888;
}

.nav li:hover  { 
  color: #999;
  border-bottom: 2px solid #999;
}

.follow {
  position: absolute;
  right: 8%;
  top: 35px;
  font-size: 11pt;
  background-color: #42b1fa;
  color: #fff;
  padding: 8px 15px;
  cursor: pointer;
  transition: all .4s;
  font-family: 'Montserrat', sans-serif;
  font-weight: 400;
}

.follow:hover {
  box-shadow: 0 0 15px rgba(0,0,0,0.2), 0 0 15px rgba(0,0,0,0.2);
}

@media (max-width:990px) {
  .nav {
    display: none;
  }
  
  .follow {
    width: 50%;
    margin-left: 25%;
    display: block;
    position: unset;
    text-align: center;
  }
}
.gallery  {
  margin-top: 35px;
}

.gallery div {
  margin-bottom: 30px;
}

.gallery img {
  box-shadow: 0 3px 6px rgba(0,0,0,0.10), 0 3px 6px rgba(0,0,0,0.10);
  width: auto; 
  height: auto;
  cursor: pointer;
  max-width: 100%;
}
</style>