import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import router from './router/index';
import global_methods from './plugins/global_methods'
import axios from 'axios'
import store from './vuex/store'
import {setCookie, getCookie, delCookie} from './util/util.js';

Vue.config.productionTip = false;
Vue.use(global_methods);
Vue.prototype.$http=axios;
Vue.prototype.$cookieStore = {
    setCookie,
    getCookie,
    delCookie,
};

axios.defaults.timeout = 50000;
axios.defaults.baseURL = '/api';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
axios.interceptors.request.use(
    config => {
        if (store.state.Authorization) {
            config.headers.Authorization = store.state.Authorization;
        }

        return config;
    },
    error => {
        return Promise.reject(error);
    });





axios.interceptors.response.use(
    response => {

        return response;
    },
    error => {
        if (error.response) {
            switch (error.response.status) {
                case 401:
                    this.$store.commit('delLogin');
                    router.replace({
                        path: '/login',
                        query: {redirect: router.currentRoute.fullPath}//登录成功后跳入浏览的当前页面
                    })
            }
        }
        return Promise.reject(error)
    });


new Vue({
    router,
  render: h => h(App),
    store,
}).$mount('#app');


