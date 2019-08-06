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
import NewMeetingStep4 from '../components/NewMeetingStep4'
import NewMeetingForm from  '../components/NewMeetingStepForm'
import OngoingMeetingMain from '../components/OngoingMeetingMain'
Vue.use(VueRouter);


const router =  new VueRouter({
    routes: [
        {
            path: '/',
            redirect: '/login',
        },
        {
            path: '/login',
            component: Login
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
                            component: NewMeetingForm,
                        },
                        {
                            path:'/new_meeting/step1',
                            component: NewMeetingForm,
                        },
                        {
                            path:'/new_meeting/step2',
                            component: NewMeetingStep2,
                        },
                        {
                            path:'/new_meeting/step3',
                            component: NewMeetingStep3,
                        },
                        {
                            path:'/new_meeting/step4',
                            component: NewMeetingStep4,
                        },
                        {
                            path:'/new_meeting/step_form',
                            component: NewMeetingForm,
                        }
                    ]
                },
                {
                    path: '/meeting_history',
                    component: MeetingHistory
                },
                {
                    path: '/ongoing_meeting',
                    component: OngoingMeetingMain
                },
            ]
        },
    ]
});


router.beforeEach((to, from, next) => {
    if (to.path === '/login') {
        next();
    } else {
        let token = localStorage.getItem('Authorization');
        console.log(token);
        if (token === null || token === '') {
            console.log(next);
            next('/login');
        } else {
            next();
        }
    }
});

export default router;
