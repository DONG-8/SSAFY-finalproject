<template>
<div class="html" style="background: #1a1e23">
  <div class="body"> 
    <section class="product" style="width:800px; margin-top: 100px;">
      <div class="product__photo" style="width: 300px; height: 435px;">
        <div class="photo-container">
          <div class="photo-main">
            <div class="controls">
              <img :src="imgSrc" alt="" style="width: 300px; height: 435px;">

              
            </div>
          </div>
        </div>
       
      </div>
      <div class="product__info" style="margin-right: 20px;">
        <div class="title" v-if="update">
          <h1 >게시글 제목</h1> 
          <hr>
            <h5>{{this.communityInfo.community_title}}</h5>
          <hr>
          <span>username: {{communityInfo.user.nickname}}</span>
          <br>
          <span>작성일 : {{ create }}</span>
          <br>
        </div>
        <div v-else>
           <b-form-textarea
            id="textarea-state"
            
            placeholder="Enter at least 10 characters"
            
            v-model = "newtitle"
          ></b-form-textarea>
        </div>
   
        <h4>게시글 내용</h4>
        <div class="description" style="height: 300px; overflow: auto" v-if="update">
          <div style="height: 300px;">
             {{this.communityInfo.content}}
            
          </div>
        </div>
        <div v-else>
         <b-form-textarea
            id="textarea-rows"
            placeholder="Tall textarea"
            rows="20"
            v-model="newcontent"
          ></b-form-textarea>
        </div>
        <!-- <button class="buy--btn">ADD TO CART</button> -->
         <div class="d-flex justify-content-space-around;">
            <div style="margin-right: 30px;">
              <span>
                <b-icon icon="emoji-smile" font-scale="2" @click="movieLike" v-if="!like" v-b-popover.hover.top="'이 글이 마음에 듭니다.'"></b-icon>
                <b-icon icon="emoji-smile-fill" font-scale="2" @click="movieLike" v-else v-b-popover.hover.top="`${likeCount}명이 좋아합니다.`"></b-icon>
              </span>
            </div>
            <div>
              <span>
                <b-icon icon="emoji-frown" font-scale="2" @click="movieHate" v-if="!hate" v-b-popover.hover.top="'이 글이 마음에 들지 않습니다.'"></b-icon>
                <b-icon icon="emoji-frown-fill" font-scale="2" @click="movieHate" v-else v-b-popover.hover.top="`${hateCount}명이 싫어합니다.`"></b-icon>
              </span>
            </div>

            
            <b-button @click="updateReview" v-if="update">수정</b-button>
            <b-button variant="success" @click="pushReview" v-else>업데이트</b-button>
            <b-button variant="danger"  @click="deleteDetail">삭제</b-button>
            
          
          </div>
          <p v-if="!check" style="margin-top: 10px;">본인의 게시글이 아닙니다!</p>
          <p v-if="!deletecheck">삐빅 삭제불가입니다!</p>
      </div>
    </section>
    </div>

    <div class="product2" style="width:800px; margin-top: 100px;"> 
      
      <h1>리뷰</h1>
      <hr>
      <community-review
        v-for="review in review_list" :key="review.pk"
        :community="communityInfo" :review="review"
        @update="getCommunityDetail(community_id)"
        >
      </community-review>

      <community-reivew-form
      :community_id="community_id"
      @update-reviews="getReviews"
      />
    </div>
</div>
  
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
// import _ from 'lodash'
import CommunityReivewForm from './CommunityReivewForm.vue'
import CommunityReview from '@/views/community/CommunityReview'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  components: { CommunityReivewForm, CommunityReview },
  name:"communityDetail",
  data: function() {
    return {
      community_id: null,
      communityInfo: {},
      likeCount : 0,
      like : null,
      hateCount : 0,
      hate : null,
      review_list: {},
      update : true,
      newtitle : null,
      newcontent : null,
      coummunityuser : null,
      nowuser : null,
      check : true,
      deletecheck : true,
      create: '',
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
    getCommunityDetail: function (event) {
      console.log(event,'이벤트')
      console.log(this.$route.params,'hey')
      const communityId = event
      this.community_id = communityId
      
      console.log(communityId,"커뮤아이디")
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/${communityId}`,
        headers: this.setToken()  // 'JWT token~~~'
      })
        .then(res => {
          // console.log(res)
          console.log(res.data, '커뮤')
          this.communityInfo = res.data
          const create = res.data.created_at.slice(0, 10)
          this.create = create
          console.log(this.create)
          if (this.communityInfo.like_users.includes(user_id)) { 
              this.like = true
            } else {
              this.like = false
            }
            if (this.communityInfo.hate_users.includes(user_id)) { 
              this.hate = true
            } else {
              this.hate = false
            }
           this.likeCount = this.communityInfo.like_users.length
           this.hateCount = this.communityInfo.hate_users.length
           this.nowuser= user_id
           this.coummunityuser = this.communityInfo.user.pk
           this.getReviews()
          
        })
        .catch(err => {
          console.log(err)
        })
      
    },
    gotoBack: function() {
      this.$router.push({name:"Community"})
    },
    movieLike : function () { 
      const communityId = this.community_id
      console.log(communityId,'좋아요')
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/community/${communityId}/like/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.like = res.data.like
            this.likeCount  = res.data.count
            this.getCommunityDetail(this.community_id)
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    movieHate : function () { 
      const communityId = this.community_id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/community/${communityId}/hate/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.hate = res.data.like
            this.hateCount  = res.data.count
            this.getCommunityDetail(this.community_id)
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    getReviews: function () {
        // const movieId = this.$route.params.movieId
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/${this.community_id}/review_create/`,
        headers: this.setToken()
      })
      .then(res => {
        console.log(res,'겟리뷰')
        this.review_list = res.data
        // console.log('성공')
      })
      .catch(err => {
        console.log(err)
        console.log('실패')
      })
      
    },
    updateDetail : function () {
      const communityId = this.community_id
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const likeItem = {
        user: user_id
      }
      // console.log(movieId)
      axios({
          method: 'post',
          url: `${SERVER_URL}/community/${communityId}/update/`,
          data: likeItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('리센트무비')
            this.hate = res.data.like
            this.hateCount  = res.data.count
            this.getCommunityDetail(this.community_id)
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
    },
    updateReview: function () {
      if (this.nowuser === this.coummunityuser) {
        this.update = false
      } else {
        this.check = false
      }
    },
    pushReview: function() {
      const communityId = this.communityInfo.id 
      // const token = localStorage.getItem('jwt')
      // const user_id = jwtDecode(token).user_id
      const movieItem = {
        // user : user_id,
        movie: this.communityInfo.movie,
        community_title: this.newtitle,
        movie_title : this.communityInfo.movie_title,
        content : this.newcontent,
        poster_path: this.communityInfo.poster_path,
        // image: this.image
      }
      console.log(movieItem ,'무비아이템')
      if (movieItem.community_title && movieItem.movie_title && movieItem.content) 
      {
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/${communityId}/update/`,
          data: movieItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            
            this.getCommunityDetail(this.community_id)
          })
          .catch(err => {
            console.log(err.data)
            console.log('실패해떠염')
          })


        }
        
        this.update = true
        
      },
      deleteDetail : function () {
        const communityId = this.communityInfo.id 
        const userId = this.communityInfo.user.pk
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/${userId}/delete/${communityId}/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            
            this.getCommunityDetail(this.community_id)
          })
          .catch(err => {
            console.log(err.data)
            console.log('실패해떠염')
            this.deletecheck = false
          })
      }
    },
  created: function() {
    if (localStorage.getItem('jwt')) {
       
        let community = this.$route.params.community_id
        // let communityId = parseInt(community)
        this.community_id = community
        console.log()
        console.log(this.communityInfo,'커뮤인포')
        this.setToken()
        this.getCommunityDetail(community)
        this.getReviews()
      } else {
        this.$router.push({ name: 'Login' })
      }
    
  },
  computed: {
  imgSrc : function () {
    const imgsrc = this.communityInfo.poster_path
    console.log(imgsrc)
    return imgsrc
    }
  }
}
</script>

<style lang="scss" scoped>
/* ----- Variables ----- */
$color-primary: #4c4c4c;
$color-secondary: #a6a6a6;
$color-highlight: #ff3f40;

/* ----- Global ----- */
* {
	box-sizing: border-box;
}

.d-flex {
  display: flex;
  justify-content : space-around;
}


.html,
.body {
	height: 100%;
  margin-top: 0px!important;
}

.body {
	display: grid;
	grid-template-rows: 1fr;
	font-family: "Raleway", sans-serif;
}

.body2 {
  display : row;
  height: 100%;
  grid-template-rows: 1fr;
	font-family: "Raleway", sans-serif;
	background-color: #010704;
}

h3 {
	font-size: 0.7em;
	letter-spacing: 1.2px;
	color: $color-secondary;
}

// img {
// 			max-width: 100%;
// 			filter: drop-shadow(1px 1px 3px $color-secondary);
// 		}

/* ----- Product Section ----- */
.product {
	display: grid;
	grid-template-columns: 0.9fr 1fr;
	margin: auto;
	padding: 2.5em 0;
	min-width: 600px;
	background-color: white;
	border-radius: 5px;
}
.product2 {
	display: row;
	grid-template-columns: 0.9fr 1fr;
	margin: auto;
	padding: 2.5em 0;
	min-width: 600px;
	background-color: white;
	border-radius: 5px;
}

/* ----- Photo Section ----- */
.product__photo {
	position: relative;
}

.photo-container {
	position: absolute;
	left: -2.5em;
	display: grid;
	grid-template-rows: 1fr;
	width: 100%;
	height: 100%;
	border-radius: 6px;
	box-shadow: 4px 4px 25px -2px rgba(0, 0, 0, 0.3);
}

.photo-main {
	border-radius: 6px 6px 0 0;
	background-color: #9be010;
	background: radial-gradient(#343a40, #343a40);

	.controls {
		display: flex;
		justify-content: space-between;
		padding: 0.8em;
		color: #fff;

		i {
			cursor: pointer;
		}
	}

	img {
		position: absolute;
		left: 1.5em;
		top: 1.5em;
		max-width: 110%;
		filter: saturate(150%) contrast(120%) hue-rotate(10deg)
			drop-shadow(1px 20px 10px rgba(0, 0, 0, 0.3));
	}
}

.photo-album {
	padding: 0.7em 1em;
	border-radius: 0 0 6px 6px;
	background-color: #fff;

	ul {
		display: flex;
		justify-content: space-around;
	}

	li {
		float: left;
		width: 55px;
		height: 55px;
		padding: 7px;
		border: 1px solid $color-secondary;
		border-radius: 3px;
	}
}

/* ----- Informations Section ----- */
.product__info {
	padding: 0.8em 0;
}

.title {
	h1 {
		margin-bottom: 0.1em;
		color: $color-primary;
		font-size: 1.5em;
		font-weight: 900;
	}

	span {
		font-size: 0.7em;
		color: $color-secondary;
	}
}

.price {
	margin: 1.5em 0;
	color: $color-highlight;
	font-size: 1.2em;

	span {
		padding-left: 0.15em;
		font-size: 2.9em;
	}
}

.variant {
	overflow: auto;

	h3 {
		margin-bottom: 1.1em;
	}

	li {
		float: left;
		width: 35px;
		height: 35px;
		padding: 3px;
		border: 1px solid transparent;
		border-radius: 3px;
		cursor: pointer;

		&:first-child,
		&:hover {
			border: 1px solid $color-secondary;
		}
	}

	li:not(:first-child) {
		margin-left: 0.1em;
	}
}

.description {
	clear: left;
	margin: 2em 0;

	h3 {
		margin-bottom: 1em;
	}

	ul {
		font-size: 0.8em;
		list-style: disc;
		margin-left: 1em;
	}

	li {
		text-indent: -0.6em;
		margin-bottom: 0.5em;
	}
}

.buy--btn {
	padding: 1.5em 3.1em;
	border: none;
	border-radius: 7px;
	font-size: 0.8em;
	font-weight: 700;
	letter-spacing: 1.3px;
	color: #fff;
	background-color: $color-highlight;
	box-shadow: 2px 2px 25px -7px $color-primary;
	cursor: pointer;

	&:active {
		transform: scale(0.97);
	}
}

/* ----- Footer Section ----- */
footer {
	padding: 1em;
	text-align: center;
	color: #fff;

	a {
		color: $color-primary;

		&:hover {
			color: $color-highlight;
		}
	}
}



</style>