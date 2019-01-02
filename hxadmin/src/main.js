import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// if (process.env.NODE_ENV !== 'production') {
//   var VConsole = require('vconsole/dist/vconsole.min.js');
//   var vConsole = new VConsole();
// }

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
