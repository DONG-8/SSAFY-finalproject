<template>
  <div>
    <div v-if="select==='Communities'" class="row gallery">
      <div class="col-md-4" v-for="(movie, idx) in paginatedData" :key="idx" :movie="movie">
        <img @click="communityDetail(movie.id)" class="mx-3 my-2" :src="movie.poster_path"/>
      </div>
      <div class="btn-cover" style="margin-left:12rem; margin-top:48px; margin-bottom:48px">
        <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
          이전
        </button>
        <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
        <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
          다음
        </button>
      </div>
    </div>
    <div v-else class="row gallery">
      <div class="col-md-4" v-for="(movie, idx) in paginatedData" :key="idx" :movie="movie">
        <img @click="movieDetailInfo(movie.id)" class="mx-3 my-2" :src="movie.poster_path"/>
      </div>
      <div class="btn-cover" style="margin-left:12rem; margin-top:48px; margin-bottom:48px">
        <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
          이전
        </button>
        <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
        <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
          다음
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileItem",
  data() {
    return {
      pageNum: 0,
    }
  },
  props: {
    listArray: {
      type: Array,
      required: true,
    },
    pageSize: {
      type: Number,
      required: false,
      default: 6,
    },
    select: {
      type: String,
    }
  },

  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
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
    communityDetail : function (com_id) {
      // console.log(this.communityContents.id)
      const community_id = com_id
      console.log(community_id)
      this.$router.push({name:"communityDetail",params:{community_id : community_id}})
    }  
  },
  computed: {
    pageCount () {
      console.log(this.listArray, 'ㅇㅇ')
      let listLeng = this.listArray.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.listArray.slice(start, end);
    }
  }

}
</script>

<style>
.btn-cover {
  display: block;
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}

</style>