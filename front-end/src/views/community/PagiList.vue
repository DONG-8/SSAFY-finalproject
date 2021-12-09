<template>
  <div>
    <table
      id="fl-table"
      :per-page="perPage"
      :current-page="currentPage"
    >
      <thead>
        <tr>
          <th>#</th>
          <th>영화포스터</th>
          <th>영화</th>
          <th>게시글 제목</th>
          <th>작성자</th>
          <th>Detail</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(community, idx) in paginatedData" :key="idx" :community="community">
          <td>{{community.id}}</td>
          <td>
            <img :src="community.poster_path" />
          </td>
          <td><h5>{{ community.movie_title }}</h5></td>
          <td><h5>{{ community.community_title }}</h5></td>
          <td><h5 @click="goToUserProfile(community.user.pk)">{{ community.user.nickname }}</h5></td>
          <td><b-button @click="communityDetail(community.id)">Detail</b-button></td>
        </tr>
      </tbody> -->
    </table>
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PagiList',
  data () {
    return {
      pageNum: 0
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
      default: 5,
    }
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    goToUserProfile: function (user_id) {
      console.log(user_id)
      this.$router.push({
        name: 'profile',
        params: {
          user_id: user_id
        }
      })
    },
    communityDetail : function (com_id) {
      // console.log(this.communityContents.id)
      const community_id = com_id
      console.log(community_id,'페이지리스트의 커뮤티니티아이디')
      this.$router.push({name:"communityDetail",params:{community_id : community_id}})
    }  
  },
  computed: {
    pageCount () {
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

<style lang="scss" scoped>
*{
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
}
body{
    font-family: Helvetica;
    -webkit-font-smoothing: antialiased;
    background: rgba( 71, 147, 227, 1);
}
h2{
    text-align: center;
    font-size: 18px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: white;
    padding: 30px 0;
}

img{
  width: 80px;
  height: 110px;
}

/* Table Styles */

.table-wrapper{
    margin: 10px 70px 70px;
    box-shadow: 0px 35px 50px rgba( 0, 0, 0, 0.2 );
}

#fl-table {
    border-radius: 5px;
    font-size: 12px;
    font-weight: normal;
    border: none;
    border-collapse: collapse;
    width: 80%;
    max-width: 100%;
    white-space: nowrap;
    background-color: rgba(255, 255, 255, 0.8);
}

#fl-table td, #fl-table th {
    text-align: center;
    padding: 8px;
}

#fl-table td {
    border-right: 1px solid #f8f8f8;
    font-size: 12px;
}

#fl-table thead th {
    color: #ffffff;
    background: #324960;
}


// .fl-table thead th:nth-child(odd) {
//     color: #ffffff;
//     background: #324960;
// }

// .fl-table tr:nth-child(even) {
//     background: #F8F8F8;
// }

/* Responsive */

@media (max-width: 767px) {
    #fl-table {
        display: block;
        width: 100%;
    }
    .table-wrapper:before{
        content: "Scroll horizontally >";
        display: block;
        text-align: right;
        font-size: 11px;
        color: white;
        padding: 0 0 10px;
    }
    #fl-table thead, #fl-table tbody, #fl-table thead th {
        display: block;
    }
    #fl-table thead th:last-child{
        border-bottom: none;
    }
    #fl-table thead {
        float: left;
    }
    #fl-table tbody {
        width: auto;
        position: relative;
        overflow-x: auto;
    }
    #fl-table td, #fl-table th {
        padding: 20px .625em .625em .625em;
        height: 60px;
        vertical-align: middle;
        box-sizing: border-box;
        overflow-x: hidden;
        overflow-y: auto;
        width: 120px;
        font-size: 13px;
        text-overflow: ellipsis;
    }
    #fl-table thead th {
        text-align: left;
        border-bottom: 1px solid #f7f7f9;
    }
    #fl-table tbody tr {
        display: table-cell;
    }
    #fl-table tbody tr:nth-child(odd) {
        background: none;
    }
    #fl-table tr:nth-child(even) {
        background: transparent;
    }
    #fl-table tr td:nth-child(odd) {
        background: #F8F8F8;
        border-right: 1px solid #E6E4E4;
    }
    #fl-table tr td:nth-child(even) {
        border-right: 1px solid #E6E4E4;
    }
    #fl-table tbody td {
        display: block;
        text-align: center;
    }
}


.btn-cover {
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