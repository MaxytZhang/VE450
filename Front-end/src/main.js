import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router/index';
import global_methods from './plugins/global_methods'
import axios from 'axios'
import store from './vuex/store'

Vue.config.productionTip = false;
Vue.use(global_methods);

new Vue({
    router,
  render: h => h(App),
    store,
    // components:{
    //   'HomeLayout': HomeLayout,
    // }
}).$mount('#app');

