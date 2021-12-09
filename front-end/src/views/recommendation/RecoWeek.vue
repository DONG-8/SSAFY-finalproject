<template>
  <div id="toaa">
    <pre>



    </pre>
    <div class="container">
        <header class="main-header clearfix">
          <h1 class="name" style="font-size: 2em; margin-bottom: 0px;">오늘의 요일 추천 영화</h1>
        </header>

        <div class="content clearfix">

          <div class="cube-container">
            <div class="photo-cube">

              <img @click="movieDetailInfo(movie1.id)" class="front" :src="movie1.poster_path" alt="">
              <img @click="movieDetailInfo(movie2.id)"  class="back" :src="movie2.poster_path" alt="">
              <img @click="movieDetailInfo(movie3.id)"  class="left" :src="movie3.poster_path" alt="">
              <img @click="movieDetailInfo(movie4.id)"  class="right" :src="movie4.poster_path" alt="">

            </div>
          </div>	

          <div class="cube-container">
            <div class="photo-cube">

              <img @click="movieDetailInfo(movie5.id)"  class="front" :src="movie5.poster_path" alt="">
              <img @click="movieDetailInfo(movie6.id)"  class="back" :src="movie6.poster_path" alt="">
              <img @click="movieDetailInfo(movie7.id)"  class="left" :src="movie7.poster_path" alt="">
              <img @click="movieDetailInfo(movie8.id)"  class="right" :src="movie8.poster_path" alt="">

            </div>
          </div>	

          <div class="cube-container">
            <div class="photo-cube">

              <img @click="movieDetailInfo(movie9.id)"  class="front" :src="movie9.poster_path" alt="">
              <img @click="movieDetailInfo(movie10.id)"  class="back" :src="movie10.poster_path" alt="">
              <img @click="movieDetailInfo(movie11.id)"  class="left" :src="movie11.poster_path" alt="">
              <img @click="movieDetailInfo(movie12.id)"  class="right" :src="movie12.poster_path" alt="">

            </div>
          </div>	

        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: "RecoWeek",
  components:{
    // RecoMovieList
  },
  data: function () {
    return {
      day : ''
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
    movie1: function () {
      return this.$store.state.movie1
    },
    movie2: function () {
      return this.$store.state.movie2
    },
    movie3: function () {
      return this.$store.state.movie3
    },
    movie4: function () {
      return this.$store.state.movie4
    },
    movie5: function () {
      return this.$store.state.movie5
    },
    movie6: function () {
      return this.$store.state.movie6
    },
    movie7: function () {
      return this.$store.state.movie7
    },
    movie8: function () {
      return this.$store.state.movie8
    },
    movie9: function () {
      return this.$store.state.movie9
    },
    movie10: function () {
      return this.$store.state.movie10
    },
    movie11: function () {
      return this.$store.state.movie11
    },
    movie12: function () {
      return this.$store.state.movie12
    },
  },
  created : function() {
    this.getMovies()
    this.day = this.$store.state.day
    console.log(this.day ,'오늘의 요일')
  }
}
</script>

<style lang="scss" scoped>
/* ================================= 
  Base Element Styles
==================================== */

* {
	box-sizing: border-box;
}
body {
	font: 1em/1.5 'Open Sans', sans-serif;
	color: #373737;
	margin: 0;
}

#toaa {
  background: #1a1e23;
}

a {
	text-decoration: none;
}
h1,
h2,
h3 {
	text-transform: uppercase;
}
h2 {
	font-size: 1.125em;
	color: #4a89ca;
	font-weight: 600;
	margin: 0;
}
h3 {
	font-size: 1.3em;
	line-height: 1.25em;
	margin-top: .85em;
	margin-bottom: .5em;
}
p {
	font-size: .875em;
	line-height: 1.4;
	margin: 0 0 1.5em;
}


.container,
.content {
	margin: auto;
}
.container {
	width: 94.02985075%;
	max-width: 1200px;
	padding: 0 2.25em 4em;
	background: rgba(235, 235, 235, 0.6);
  border-radius: 50px;
  z-index: 1;
}
.main-header {
	text-align: center;
	padding: 2.8em 0 3.8em;
}
.cube-container {
	max-width: 200px;
	text-align: center;
	margin: 0 auto 4.5em;
}
/* ---- Page Elements ---- */

.name {
	font-size: 1.65em;
	font-weight: 800;
	margin: 0 0 1.5em;
	line-height: 1;
}
.name span {
	font-weight: 300;
	margin-left: -7px;
}
.logo {
	width: 45px;
	margin-bottom: .4em;
	cursor: pointer;
}
.button {
	font-size: .8em;
	color: #fff;
	width: 90%;
	line-height: 1.15;
	font-weight: 700;
	display: block;
	text-decoration: none;
	text-transform: uppercase;
	padding: .95em 0;
	border-radius: .5em;
	background: rgba(74,137,202, .8);
	margin: auto;
}
/* ---- Photo Overlay ---- */

.photo-desc {
	font-size: .85em;
	color: #fff;
	padding: 1.1em 1em 0;
	background: #345d88;
}
/* ---- Float clearfix ---- */

.clearfix::after {
	content: " ";
	display: table;
	clear: both;
}

/* ================================= 
  Media Queries
==================================== */

@media (min-width: 769px) {
	.cube-container {
		float: left;
		margin-left: 16.6%;
	}
}
@media (min-width: 1025px) {
	.cube-container:first-child {
		margin-left: 0;
	}
	.cube-container:last-child{
		float: right;
	}
	.content {
		max-width: 900px;
		margin: auto;
	}
}

/* ================================= 
  Button Transitions
==================================== */

.button {
	transition: background .3s;
}
.button:hover {
	background: rgba(74,137,202, 1);
}

/* ================================= 
  Photo 3D Transforms & Transitions
==================================== */

.cube-container {
	box-shadow: 0 18px 40px 5px rgba(0,0,0,.4);
  perspective: 800px;
}

.photo-cube {
transition: transform 4s ease-in-out; 
  width: 220px;
  height: 300px;
  transform-style: preserve-3d;
}

.photo-cube:hover {
transform: rotateY(-270deg);
}

.front,
.back,
.left,
.right {
width: 100%;
height: 100%;
display: block;
position: absolute;
}

.front {
transform: translate3d(0,0,110px);
}

.back {
transform: translateZ(-110px) rotateY(270deg);
  transform-origin: center left;
}

.left {
transform: rotateY(-270deg) translate3d(110px, 0, 0);
  transform-origin: top right;
}

.right {
transform: translateZ(-110px) rotateY(180deg);
 }
</style>