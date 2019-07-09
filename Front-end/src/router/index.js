import Vue from 'vue';
import VueRouter from 'vue-router'
import HomeMain from '../components/HomeMain'
import NewMeetingMain from '../components/NewMeetingMain';
Vue.use(VueRouter);


export default new VueRouter({
    routes: [
        {
            path: '/',
            component: HomeMain
        },
        {
            path:'/home',
            component:HomeMain
        },
        {
            path: '/new_meeting',
            component: NewMeetingMain
        },
    ]
})
