import Vue from 'vue'

// exports.install = function (Vue, options) {
//     Vue.prototype.to_new = function (){
//
//     };
// };


export default {
    install(Vue)  {
        Vue.prototype.to_new = function () {
            this.$router.push("/new_meeting")
        }
    }
}
