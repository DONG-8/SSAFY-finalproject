import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
// import MovieList from '@/views/movies/MovieList'
import Movie from '@/views/movies/Movie'
import MovieDetails from '@/views/movies/MovieDetails'
import profile from '@/views/accounts/profile'
import CommunityForm from '@/views/community/CommunityForm'
import Community from '@/views/community/Community'
import communityDetail from '@/views/community/communityDetail'
import statusSetting from '@/views/accounts/statusSetting'
import Recommendation from '@/views/recommendation/Recommendation'
import Favorite from '@/views/recommendation/RecoFavorite'
// import Review from '@/views/movies/Review'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies/',
    name: 'Movie',
    component: Movie,
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetails',
    component: MovieDetails,
  },
  {
    path: '/accounts/profile/:user_id/',
    name: 'profile',
    component: profile,
  },
  {
    path: '/community/CommunityForm',
    name: 'CommunityForm',
    component: CommunityForm,
  },
  {
    path: '/community/',
    name: 'Community',
    component: Community,
  },
  {
    path: '/accounts/profile/setting/',
    name: 'Setting',
    component: statusSetting,
  },
  {
    path: '/recommendation/',
    name: 'Recommendation',
    component: Recommendation,
  },
  {
    path: '/community/:community_id/',
    name: 'communityDetail',
    component: communityDetail,
  },
  {
    path: '/favorite/',
    name: 'Favorite',
    component: Favorite
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
