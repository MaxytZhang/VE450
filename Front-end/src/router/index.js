import Vue from 'vue';
import VueRouter from 'vue-router'
import HomeLayout from '../components/HomeLayout'
import HomeMain from '../components/HomeMain'
import Login from '../components/Login'
import NewMeetingMain from '../components/NewMeetingMain'
import MeetingHistory from '../components/MeetingHistory'
import NewMeetingStep1 from '../components/NewMeetingStep1'
import NewMeetingStep2 from '../components/NewMeetingStep2'
import NewMeetingStep3 from '../components/NewMeetingStep3'
Vue.use(VueRouter);


export default new VueRouter({
    routes: [
        {
            path: '/',
            component: Login,
        },
        {
            path:'/home',
            component: HomeLayout,
            children: [
                {
                    path:'/home',
                    component: HomeMain,
                },
                {
                    path: '/new_meeting',
                    component: NewMeetingMain,
                    children: [
                        {
                            path:'/new_meeting',
                            // redirect: '/new_meeting/step1',
                            component: NewMeetingStep1,
                        },
                        {
                            path:'/new_meeting/step1',
                            component: NewMeetingStep1,
                        },
                        {
                            path:'/new_meeting/step2',
                            component: NewMeetingStep2,
                        },
                        {
                            path:'/new_meeting/step3',
                            component: NewMeetingStep3,
                        },
                    ]
                },
                {
                    path: '/meeting_history',
                    component: MeetingHistory
                },
            ]
        },
    ]
})
