<template>
  <div>
    <p>{{smovie.title}}</p>
    <img :src="imgSrc" alt="#">
    <br>
    <button @click="goToDetail">가자!</button>
  </div>
</template>

<script>
export default {
  name : "simmilar",
  props : {
    smovie: Object
  },
  methods: {
    goToDetail : function () {
      window.scrollTo(0,0)
      this.$router.push(
        { name : 'MovieDetails', 
          params: {
            movieId : this.smovie.id,
          }
      })
    }
  },
  computed: {
    imgSrc : function() {
      const imgsrc = this.smovie.poster_path
      return imgsrc
    }
  }
}
</script>

<style>

</style>