<template>
  <div>
    <div class="d-flex justify-content-center align-items-center">
      <div class="rating-system3">
        <input type="radio" name='rate3' id="star5_3" value="5" @click="rating" />
        <label for="star5_3"></label>
        <input type="radio" name='rate3' id="star4_3" value="4" @click="rating" />
        <label for="star4_3"></label>
        <input type="radio" name='rate3' id="star3_3" value="3" @click="rating" />
        <label for="star3_3"></label>
        <input type="radio" name='rate3' id="star2_3" value="2" @click="rating" />
        <label for="star2_3"></label>
        <input type="radio" name='rate3' id="star1_3" value="1" @click="rating" />
        <label for="star1_3"></label>

        <div class="text"></div>
      </div>
      <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <div class="form__group mx-5 mb-3">
          <input style="border: 1px solid black" v-model="reviewContent" type="text" class="form__input" id="name" required="" />
        </div>
      <b-button style="height: 40px; " class="mx-5" @click="createReview">작성하기</b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: "CommunityReviewForm",
  data: function () {
    return {
      reviewContent: null,
      ratingValue: null,
    }
  },
  props: {
    community_id: String
  },
  methods : {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    rating: function(event) {
      console.log(event.target.value)
      this.ratingValue = event.target.value
    },
    createReview: function () {
      const token = localStorage.getItem('jwt')
      const user_id = jwtDecode(token).user_id
      const ReviewItem = {
        user : user_id,
        community: this.community_id,
        rank: this.ratingValue,
        content : this.reviewContent
      }
      // console.log(this.reviewContent)
      // console.log(this.movie)
      if (ReviewItem.content) {
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/${this.community_id}/review_create/`,
          data: ReviewItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res,'폼')
            // console.log('성공')
            this.$emit('update-reviews')
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

<style lang="scss" scoped>
*,
*::after,
*::before {
  margin: 0;
  padding: 0;
  box-sizing: inherit;
  font-size: 62,5%;
}

body{
  font-family: 'Verdana';
  background:#222;
}
h3{
  font-size:14px;
  color:gray;
}
.showcase{
  text-align:center;
  position: absolute;
  top:50%;
  left:50%;
  transform:translateY(-50%) translateX(-50%);
}
.rating-system1,
.rating-system2,
.rating-system3,
.rating-system4{
  width:auto;
  display:inline-block;
  margin:20px;
  position: relative;
} 

span{
  display:inline-block;
  width:10px;
  height:10px;
  background:red;
  position: absolute;
  left:20px;
}

input{
  display:none;
}

label{
  float:right;
  display:inline-block;
  width:20px;
  height:5px;
  background:#ccc;
  margin:4px;
  position: relative;
  transition:all .3s;
}
.rating-system1 label:before{
  content: '';
  position: absolute;
  width:100%;
  height:100%;
  background: inherit;
  top:0;
  left:0;
  transition:all 0.3s;
}
.rating-system1 input:checked ~ label,
.rating-system1 label:hover ~ label,
.rating-system1 label:hover{
  background:seagreen;
}
.rating-system1 input:checked ~ label:before{
  transform:rotate(90deg);
}  
.text{
  color:#ccc;
  padding:10px 0;
  position: absolute;
  width:100%;
  top:100%;  
}
/*second*/
.rating-system2 label{
  width:10px;
  height:10px;
  border-radius:100%; 
  margin:0 10px;
}

.ratings-system2 label:before{display:none;}
.rating-system2 label:hover ~ label,
.rating-system2 label:hover
{
  box-shadow: 0 0 0 2px gold,
              inset 0 0 0 5px #333;
  
} 

.rating-system2 input:checked ~ label{
  background:gold;
  box-shadow: 0 0 0 2px gold;
  
}

/*rating system 3*/

.rating-system3 label{
  width:10px;
  height:10px;
  margin:0 10px;
}
.rating-system3 label:hover,
.rating-system3 label:hover ~ label
{
  background:crimson;
  border-radius:100%
}

.rating-system3 input:checked ~ label{
  border-radius: 100%;
  background: crimson;
  box-shadow: 6px 0 crimson, 3px 1px 0 7px #222,3px 1px 0 9px crimson;
  
}

.rating-system3 input:checked ~ label:after{
  content: '';  
  width: 100%;
  height: 100%;
  position: absolute;
  background: crimson;
  transform: rotate(-45deg);
  border-bottom-left-radius: 15%;
  top: 30%;
  left: 3px;
}

/** rating system 4*/

.rating-system4 label{
    
  width:40px;
  height:50px;
  background:url('https://i.imgur.com/q1tk5E7.gif'); 
  background-size:70%;
  background-repeat:no-repeat;
} 
  

.rating-system4 label:hover,
.rating-system4 label:hover ~ label
{
  background:url('https://i.imgur.com/YgAna9g.gif');
  background-size:100%;
  background-repeat:no-repeat;
  
}


.rating-system4 input:checked ~ label{
  background:url('https://i.imgur.com/GO4qjoa.gif');
  background-size:70%;
  background-repeat:no-repeat;
  
}


/*selecting*/
input:nth-of-type(5):checked  ~ .text:before{
  content:"Not bad";
}

label:nth-of-type(5):hover  ~ .text:before{
  content:"Not bad"!important;
}

input:nth-of-type(4):checked  ~ .text:before{
  content:"Its Ok";
}

label:nth-of-type(4):hover  ~ .text:before
{
  content:"Its Ok"!important;
}


input:nth-of-type(3):checked  ~ .text:before{
  content:"Good!";
}

label:nth-of-type(3):hover  ~ .text:before{
    content:"Good!"!important;
}


input:nth-of-type(2):checked  ~ .text:before{
  content:"Very Good!";
}
label:nth-of-type(2):hover  ~ .text:before{
  content:"Very Good!"!important;
}

input:nth-of-type(1):checked  ~ .text:before{
  content:"Awesome!!";
}
label:nth-of-type(1):hover  ~ .text:before{
  content:"Awesome!!"!important;
}

.form__label {
  font-family: 'Roboto', sans-serif;
  font-size: 1.2rem;
  margin-left: 2rem;
  margin-top: 0.7rem;
  display: block;
  transition: all 0.3s;
  transform: translateY(0rem);
}

.form__input {
  font-family: 'Roboto', sans-serif;
  color: #333;
  font-size: 1.2rem;
	// margin: 0 auto;
  margin-top: 15px;
  padding: 0px;
  border-radius: 0.2rem;
  background-color: rgb(255, 255, 255);
  border: none;
  width: 90%;
  display: block;
  border-bottom: 0.3rem solid transparent;
  transition: all 0.3s;
}

.form__input:placeholder-shown + .form__label {
  opacity: 0;
  visibility: hidden;
  -webkit-transform: translateY(-4rem);
  transform: translateY(-4rem);
}
</style>