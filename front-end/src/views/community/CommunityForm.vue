<template>
  <div class="html">
    <div>
      <b-button v-b-modal.modal-lg
        style="margin-bottom:0px;margin-top: 100px;"
        >영화 검색하기!
        </b-button>

        <b-modal  id="modal-lg" size="lg" scrollable title="영화검색">
          <b-form-input  placeholder="Enter Movie Title"
            v-model.trim = "search_name"
            @keyup.enter="filtering"
            >
          </b-form-input>

          <hr>
          <h3 style="text-align:center;">검색결과</h3>
          <div v-if="!firstinput" style="">
            <p>카드를 클릭하시면 자동으로 기입됩니다</p>
            <p>한번 더 선택하면, 자동으로 초기 검색 결과를 보여줍니다</p>
          </div>
          <div v-if="!movienull">
            <br>
            <h3 style="text-align:center;">검색 결과가 없어용</h3>
            <h4 style="text-align:center;">뿌잉 ㅠㅠ</h4>
            <br>
            <div style="display: table; margin-left: auto; margin-right: auto;">
              <img src="https://m.whodadoc.com/assets/consumer/mobile/img/map/img_schNoData.png" alt="">
            </div>
          </div>      
          <b-form id="modal-scrollable" scrollable>
            <b-card-group deck
              class="d-flex justify-content-center"
            >
              <search-movie-list
                v-for="result in clickByResult" :key="result.id"
                :result ="result"
                @changeresult="changeResults"
                @clickidMovieInfo="movieInfosave"
                >
              </search-movie-list>
            </b-card-group>
          </b-form>
        </b-modal>
    </div>
     
    <div class="html" style="height: 1000px;">
      <div class="body"> 
        <section class="product" style="width: 800px;margin-top: 50px;padding-bottom: 0px;margin-bottom: 100px;height: 640px;">
          <div class="product__photo" style="width: 300px; height: 435px;">
            <div class="photo-container">
              <div class="photo-main">
                <div class="controls">
                  <div v-if="movieInfo">
                    <img :src="imgSrc" alt="없어염" style="width: 300px; height: 435px;">

                  </div>
                </div>
              </div>
            </div>
          </div>
             <div class="product__info" style="margin-right: 20px;">
              
              <div class="title" style="margin-right: 20px;">
                <p>게시글 제목</p>
                 <b-form-textarea
                    id="textarea-state"
                    :state="community_title.length >= 1"
                    placeholder="Enter at least 1 characters"
                    
                    v-model = "community_title"
                  ></b-form-textarea>
                        
              </div>
              
              <div class="description" style="height: 300px; overflow: auto">
                <p>게시글 내용</p>
              <b-form-textarea
                id="textarea-rows"
                placeholder="Tall textarea"
                rows="20"
                v-model="content"
              ></b-form-textarea>
            </div>

              <b-btn
              @click="createCommunity"
              style="margin-top: 20px;"
              >
              작성하기
              </b-btn>
            </div>
              
            
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import SearchMovieList from './SearchMovieList.vue'
import axios from 'axios'
import jwtDecode from "jwt-decode"
import _ from 'lodash'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: "CommunityForm",
  components : {
    SearchMovieList
  },
  data: function () {
    return {
      search_name : null,
      community_title : "",
      content :null,
      movie_list : null,
      results: [],
      movieInfo : null,
      modalShow: false,
      movienull : true,
      firstinput : false,
      movieInfoContent : null,
    }
  },
  methods :  {
    getMovie : function () {
      this.movie_list = this.$store.state.communityMovie
      console.log(this.movie)
    },
    filtering : function () {
      this.movieInfo = null
      // console.log(this.$store.state.communityMovie)
      let results = this.$store.state.communityMovie.filter(movie =>
        movie.title.includes(this.search_name)
        )
      this.results = results.map(result => {
        return {
          ...result,
          filterCheck : true,
          flag : false
        }
        
      })
      // console.log(this.results)
      if (this.results.length === 0) {
        this.movienull = false
      } else {
        this.movienull = true
      }
      this.firstinput= true
    },
    changeResults : function(selectMovie) {
      
      this.results = this.results.map(result => {
        if (selectMovie.flag === false) {
          if (result===selectMovie) { 
            return {
              ...selectMovie,
              flag: true
            }
          } else {
            return {
              ...result,
              filterCheck: !result.filterCheck
            }
          }
        } else {
          return {
            ...result,
            flag : false,
            filterCheck : true
          }
        }

      })   
    },
    movieInfosave: function (movieInfo) {
      if (this.movieInfo == null) {
        this.movieInfo = movieInfo
        this.movieInfoContent = _.replace(movieInfo.content, "[", "")
        this.movieInfoContent = _.replace(this.movieInfoContent, "]", "")

        console.log(this.movieInfo,'무비인포')
        this.poster_path = this.movieInfo.poster_path
        console.log(this.movieInfo.poster_path)
      } else {
        this.movieInfo = null
        // console.log(this.movieInfo)
      }
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    gotoCommunity: function () {
      this.$router.push({name:'Community'})
    },
    createCommunity: function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const movieItem = {
        user : user_id,
        movie: this.movieInfo.id,
        community_title: this.community_title,
        movie_title : this.movieInfo.title,
        content : this.content,
        poster_path: this.movieInfo.poster_path,
        // image: this.image
      }
      console.log(movieItem)
      if (movieItem.community_title && movieItem.movie_title && movieItem.content) 
      {
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/community_create/`,
          data: movieItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            console.log('성공')
            this.gotoCommunity()
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })


        }
    },
    // EditImage(){
    //   this.image = this.$refs.serveyImage.files
    //   console.log(this.image)
    // }
  
  },
  created : function  () {
    this.getMovie()
    console.log(this.movie_list,' 무비시르트')
  },
  computed : {
    clickByResult : function () {
      return this.results.filter(result => {
        return result.filterCheck
      });
    },
    imgSrc : function() {
      console.log(this.movieInfo, '컴퓻')
      const imgsrc = this.movieInfo.poster_path
      return imgsrc
    },
  }
     // 재 정재
    // 반복해서 hidden이란걸 넣을건데
    // 클릭빼고 전부 false 
  

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

.html,
.body {
	height: 100%;
  background-color: #343a40;
  margin-top: 0px!important;
}

.body {
	display: grid;
	grid-template-rows: 1fr;
	font-family: "Raleway", sans-serif;
	background-color: #343a40!important;
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