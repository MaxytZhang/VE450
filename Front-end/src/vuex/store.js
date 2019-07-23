import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const state = {
    // 初始化A和B组件的数据，等待获取
    Step1: null,
    Step2: null,
    Step3: null,
};

const mutations = {
    setStep1(state, payload) {
        // 将A组件的数据存放于state
        state.Step1 = payload.Step1
    },
    setStep2(state, payload) {
        // 将B组件的数据存放于state
        state.Step2 = payload.Step2
    },
    setStep3(state, payload){
        state.Step3 = payload.Step3
    }
};

export default new Vuex.Store({
    state,
    mutations
})
