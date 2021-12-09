import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
import createPersistedState from 'vuex-persistedstate'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    detailMovieInfo : null,
    communityMovie : null,
    selectMovie : null,
    loginUserID : null,
    movieDetailInfo: null,
    youtubeVideos: [],
    all : null,
    communityList : null,
    movieToday: null,
    TodayUser: null,
    movieWeek: null,
    movie1: null,
    movie2: null,
    movie3: null,
    movie4: null,
    movie5: null,
    movie6: null,
    movie7: null,
    movie8: null,
    movie9: null,
    movie10: null,
    movie11: null,
    movie12: null,
    movieKorea: null,
    movie13: null,
    movieFavorite: null,
    day : null
  },
  mutations: {
    MOVIE_13(state, res) {
      state.movie13 = res
    },
    MOVIE_TODAY(state, res) {
      state.movieToday = _.sampleSize(res.movies, 20)
      state.TodayUser = res.user
    },
    MOVIE_WEEK(state, res) {
      state.movieWeek = _.sampleSize(res, 12)
      state.movie1 = state.movieWeek[0]
      state.movie2 = state.movieWeek[1]
      state.movie3 = state.movieWeek[2]
      state.movie4 = state.movieWeek[3]
      state.movie5 = state.movieWeek[4]
      state.movie6 = state.movieWeek[5]
      state.movie7 = state.movieWeek[6]
      state.movie8 = state.movieWeek[7]
      state.movie9 = state.movieWeek[8]
      state.movie10 = state.movieWeek[9]
      state.movie11 = state.movieWeek[10]
      state.movie12 = state.movieWeek[11]
    },
    MOVIE_KOREA(state, res) {
      state.movieKorea = res
    },
    COMMUNITY_LIST(state, res) {
      state.communityList = res
    }
  },
  actions: {
    movie13({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/movie_list/`,
        headers: token,
      })
      .then(res => {
        console.log('gpgp')
        commit('MOVIE_13', res.data)
      })
      .catch(err => console.log(err))
    },
    movieToday({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/recommendation/today_user_list/`,
        headers: token,
      })
      .then(res => {
        console.log(res.data, '확인좀')
        commit('MOVIE_TODAY', res.data)
      })
      .catch(err => console.log(err))
    },
    movieWeek({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/recommendation/recommend_by_day_of_week/`,
        headers: token,
      })
      .then(res => {
        commit('MOVIE_WEEK', res.data)
      })
      .catch(err => console.log(err))
    },
    movieKorea({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/recommendation/recommend_by_korea/`,
        headers: token,
      })
      .then(res => {
        commit('MOVIE_KOREA', res.data)
      })
      .catch(err => console.log(err))
    },
    communityList({ commit }, token) {
      axios({
        method: 'get',
        url: `${SERVER_URL}/community/`,
        headers: token
      })
        .then(res => {
          commit('COMMUNITY_LIST', _.orderBy(res.data, 'id', 'desc'))
        })
        .catch(err => console.log(err))
    }
  },
  modules: {

  }
})
