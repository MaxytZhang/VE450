import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router/index';
import global_methods from './plugins/global_methods'
import axios from 'axios'
import store from './vuex/store'

Vue.config.productionTip = false;
Vue.use(global_methods);
Vue.prototype.$http=axios;

axios.defaults.timeout = 5000;
axios.defaults.baseURL = '/api';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
axios.post('/v1.0/test', {
    name: 'cedric',
}).then((res) => {
    console.log(res.data)
});

new Vue({
    router,
  render: h => h(App),
    store,
    // components:{
    //   'HomeLayout': HomeLayout,
    // }
}).$mount('#app');

