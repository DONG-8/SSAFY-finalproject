<template>
  <div>
    <p>리뷰내용</p>
    <input type="text" v-model="reviewContent">
  
    <p>평점</p>
    <!-- {{ratingValue}} -->
    <div class="star-rating">
      <input type="radio" id="5-stars" name="rating" value="5" @click="rating" />
      <label for="5-stars" class="star">&#9733;</label>
      <input type="radio" id="4-stars" name="rating" value="4" @click="rating"/>
      <label for="4-stars" class="star">&#9733;</label>
      <input type="radio" id="3-stars" name="rating" value="3" @click="rating"/>
      <label for="3-stars" class="star">&#9733;</label>
      <input type="radio" id="2-stars" name="rating" value="2" @click="rating"/>
      <label for="2-stars" class="star">&#9733;</label>
      <input type="radio" id="1-star" name="rating" value="1" @click="rating"/>
      <label for="1-star" class="star">&#9733;</label>
    </div>

    <button @click="createReview">작성하기</button>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL
// console.log(SERVER_URL)
export default {
  name: "ReviewForm",
  data: function () {
    return {
      reviewContent: null,
      ratingValue : null
    }
  },
  props: {
    movie: Object
  },
  methods : {
    rating: function(event) {
      this.ratingValue = event.target.value
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview: function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const ReviewItem = {
        user : user_id,
        movie: this.movie.id,
        rank: this.ratingValue,
        content : this.reviewContent
      }
      // console.log(this.reviewContent)
      console.log(this.movie)
      if (ReviewItem.rank && ReviewItem.content) {
        axios({
          method: 'post',
          url: `${SERVER_URL}/movies/${this.movie.id}/review_create/`,
          data: ReviewItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res,'폼')
            // console.log('성공')
            this.$emit('updatereviews')
          })
          .catch(err => {
            console.log(err)
            // console.log('실패')
          })
        }
    },

    }
  
}
</script>

<style scoped>

.star-rating {
  border:solid 1px #ccc;
  display:flex;
  flex-direction: row-reverse;
  font-size:1.5em;
  justify-content:space-around;
  padding:0 .2em;
  text-align:center;
  width:5em;
}

.star-rating input {
  display:none;
}

.star-rating label {
  color:#ccc;
  cursor:pointer;
}

.star-rating :checked ~ label {
  color:#f90;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  color:#fc0;
}

/* explanation */

article {
  background-color:#ffe;
  box-shadow:0 0 1em 1px rgba(0,0,0,.25);
  color:#006;
  font-family:cursive;
  font-style:italic;
  margin:4em;
  max-width:30em;
  padding:2em;
}

</style>