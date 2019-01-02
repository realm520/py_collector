import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'

const Home = resolve => {
  require.ensure(['./views/Home.vue'], () => {
      resolve(require('./views/Home.vue'))
  })
}

const About = resolve => {
  require.ensure(['./views/About.vue'], () => {
      resolve(require('./views/About.vue'))
  })
}

Vue.use(Router)

let base = `${process.env.BASE_URL}`

export default new Router({
  mode: 'history',
  base: base,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
