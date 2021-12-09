<template>
  <div>
    <!-- <b-column> -->
      <b-col>
        <b-card
          :img-src="imgSrc"
          img-alt="Image"
          img-width="280px"
          img-height="450px"
          style="width: 290px; height: 528px;"
          class="my-3"
          @click="selectMovie" 
          :data-movie-title="result.title"
          v-show="result.filterCheck"
        >

        <b-card-text>
          <p>{{result.title}}</p>
        </b-card-text>
        
        </b-card>
      </b-col>
      <!-- <b-row>
        <b-col cols="8" style="text: center">{{result.title}}</b-col>
      
        <b-form-checkbox cols="4"
        v-model="check"
        >
        </b-form-checkbox>
      </b-row> -->
      
        
        <!-- img-width="280px"
        img-height="450px"
        style="width: 290px; height: 528px;" -->

    <!-- </b-column> -->
  </div>

  <!-- img-top 
    img-width="280px"
    img-height="450px"
    style="width: 290px; height: 528px;" -->
</template>

<script>
export default {
  name: "SearchMovieList",
  props: {
    result : Object,
  },
  data : function () {
    return {
      check: false
    }
  },
  methods : {
    selectMovie : function (event) {
      // 추후 수정
      console.log(event)
      if (this.check) {
        this.check = false
      } else {
        this.check = true
      }
      this.$store.state.selectMovie = this.result
      this.$emit("changeresult",this.result)
      this.$emit('clickidMovieInfo', this.result)

    }
  },
  computed: {
    imgSrc : function () {
      const imgsrc = this.result.poster_path
      return imgsrc
    },

  }
}
</script>

<style scoped>

</style>