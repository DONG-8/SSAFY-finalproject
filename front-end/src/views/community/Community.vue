<template>
  <div id="topp">
    <div class="table-wrapper">
      <div id="transe" style="background-color: rgba(0, 0, 0, 0.5);text-align: center;width: 300px;height: 80px;margin-left: auto;margin-right: auto;border-radius: 20px;margin-top: 100px;margin-bottom: 100px;">
        <h1 style="color: white;display: inline-block;padding-top: auto;padding-top: 20px; opacity: 1; ">Community</h1>
      </div>
      
        <div class="overflow-auto">
          <center>
            <b-button style="width: 80%;" block variant="secondary" @click="writeContent">Create Community</b-button>
            <br>
            <pagi-list
              :list-array="communityList"
            >
            </pagi-list>
          </center>
        </div>
      <pre>


      </pre>
    </div>
  </div>
</template>

<script>
import PagiList from '@/views/community/PagiList'

export default {
  name: "Community",
  components: {
    PagiList
  },
  data: function () {
    return {
      pageNum: 0
    }
  },
  methods: {
    writeContent: function() {
       this.$router.push({ name : 'CommunityForm'})
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
    }
    return config
    },
  },
  computed: {
    communityList: function () {
      return this.$store.state.communityList
    },
    rows() {
      console.log(this.communityList.length)
      return this.communityList.length
    }
  },
  created : function() {
    this.$store.dispatch("communityList", this.setToken())
  }
}

</script>

<style scoped>

#topp::before{
  position: fixed; 
  top: 0; 
  left: 0; 
  right: 0; 
  bottom: 0;
  background-image: url("https://www.10wallpaper.com/wallpaper/1920x1080/1107/The_incredible_hulk_wallpaper_The_Incredible_Hulk_Game_1920x1080.jpg");
  background-size: 100% 100%;
  /* filter: blur(2px);  */
  z-index: -1; 
  content: "";
}

h1{
    text-align: center;
    font-size: 36px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: white;
    padding: 30px 0;
}
</style>