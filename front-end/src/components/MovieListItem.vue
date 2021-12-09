<template>
  <b-carousel-slide>
    <template #img>
      <img :src="imgSrc" alt="" width="35%" @click="movieDetailInfo">
    </template>
  </b-carousel-slide>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: Object
  },
  methods:{
    movieDetailInfo: function() {
      this.$router.push(
        { name : 'MovieDetails', 
          params: {
            movieId : this.movie.id,
          }
      })
    }
  },
  computed: {
    imgSrc : function() {
      const imgsrc = this.movie.poster_path
      return imgsrc
    }
  }
}
</script>

<style>

</style>