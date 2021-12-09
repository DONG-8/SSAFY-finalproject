<template>
  <div>
    <p> 리뷰들 </p>
      <!-- <review-list 
        v-for="(review,idx) in review_list" :key="idx"
        :review = 'review' :movie = "movie"
        @update-review="getReviews"> 

      </review-list> -->
      <li
        v-for="(review,idx) in review_list" :key="idx"
        :review = 'review' :movie = "movie"
        @update-review="getReviews"> 
        {{review.title}}
      </li>

    <p>----------------------------------</p>
    <p>리뷰폼</p>
    <review-form :movie="movie"
      @update-review="getReviews">
      
    </review-form>
  </div>

</template>

 <script>       
// import ReviewForm from './ReviewForm.vue'
// // import ReviewList from './ReviewList.vue'
// import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

// export default {
//   name : 'Review',
//   components: { 
//     ReviewForm ,
//     // ReviewList
//     },
//   props: {
//     movie:{ 
//       type: Object,
//       review_list:Object
//     }
//   },
//   component: {
//     ReviewForm
//   },
//   data: function() {
//     return {
//       // review_list: {},
//       }
//   },
//   methods : {
//     setToken: function () {
//       const token = localStorage.getItem('jwt')
//       const config = {
//         Authorization: `JWT ${token}`
//       }
//       return config
//     },
//     getReviews: function () {
//       console.log(this.review_list,'리뷰창')
//       const movieId = this.movie.id
//         // console.log(movieId)
//         axios({
//         method: 'get',
//         url: `${SERVER_URL}/movies/${movieId}/review_create/`,
//         headers: this.setToken()
//       })
//         .then(res => {
//           console.log(res)
//           this.review_list = res.data
//           console.log('성공')
//         })
//         .catch(err => {
//           console.log(err)
//           console.log('실패')
//         })
//       }

      
      
//   },
//   conputed: function () {
//     // this.setToken()
//     // this.getReviews()
//   },
//   created: function () {
//     // this.setToken()
//     // this.getReviews()
//   }
// }
// </script>

<style>

</style>