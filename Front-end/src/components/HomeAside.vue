<template>
    <div>
    <div id="side" >
        <div class="block">
            <el-avatar :size="100"><img class="side-img" src="../assets/profile.jpeg" alt=""></el-avatar>
        </div>
        <el-row class="block">
            <h1>{{this.user_name}}</h1>
            <p>ID: {{this.user_info.EmployeeID}}</p>
            <p>Site: {{this.user_info.SiteID}}</p>
        </el-row>
        <el-row id="notice">
        <div class="block">
            <el-collapse class="infinite-list">
                <el-collapse-item v-for="(item, i) in notices" :title="'Notice-' + i" :name="i">
                    <div>{{item}}</div>
                </el-collapse-item>
            </el-collapse>
            <el-button type="primary" plain="" @click="load">More</el-button>
        </div>
            <el-button align="bottom" @click="log_out">Log out</el-button>
        </el-row>
    </div>
    </div>
</template>

<script>
    export default {
        name: "HomeSide",
        created() {
            this.get_notice();
        },
        beforeMount () {
            this.get_notice();
        },
        data () {
            return {
                user_info: JSON.parse(this.$store.state.UserInfo),
                user_name: this.$cookieStore.getCookie('name'),
                isHidden: true,
                count: 0,
                notices: [],
            }
        },
        methods: {
            load () {
                if (this.count < 20) {
                    this.count += 3;
                    let _this = this;
                    this.$http.post("/v1.0/get_notice", this.user_info.EmployeeID).then(function(res) {
                        if (res.status === 200) {
                            console.log(res.data);
                            console.log(_this.notices);
                            console.log(res.data == _this.notices);
                            if (res.data.length > _this.count){
                                _this.notices = res.data.slice(0, _this.count)
                            }
                            else if ((res.data.length <= _this.count) && (_this.notices != res.data) ){
                                _this.notices = res.data;
                                _this.count = res.data.length
                            }
                            else if (_this.notices == res.data){
                                _this.notices = res.data;
                                _this.count = res.data.length;
                                _this.$notify({
                                    type: 'error',
                                    message: _this.user_name + ': You have no more notice',
                                    duration: 3000
                                });
                            }
                        }})
                }
            },
            log_out () {
                this.$cookieStore.delCookie('name');
                this.$store.commit('delLogin');
                this.$store.commit('delUserInfo');
                this.$router.push("/login")
            },
            get_user () {
                this.$http.post("/v1.0/get_user", this.user_name).then(function(r) {
                    console.log(r);
                    alert(r.data.message)})
            },
            check_open() {
                let _this = this;
                this.myInterval = window.setInterval(() => {
                    setTimeout(() => { //调用接口的方法
                        this.$http.post("/v1.0/check_open", this.user_info.EmployeeID).then(function(res) {
                            if ((res.status === 200) && (res.data === true)) {
                                console.log(res);
                                _this.$notify({
                                    type: 'success',
                                    message: _this.user_name + ': Meeting Room has been opened for you',
                                    duration: 3000
                                });
                            }})
                    }, 1)
                }, 5000);
            },
            check_notice() {
                let _this = this;
                this.myInterval = window.setInterval(() => {
                    setTimeout(() => { //调用接口的方法
                        this.$http.post("/v1.0/check_notice", this.user_info.EmployeeID).then(function(res) {
                            if ((res.status === 200) && (res.data === true)) {
                                console.log(res);
                                _this.$notify({
                                    type: 'success',
                                    message: _this.user_name + ': You have a new notice',
                                    duration: 3000
                                });
                            }})
                    }, 1)
                }, 5000);
            },

            get_notice() {
                let _this = this;
                this.$http.post("/v1.0/get_notice", this.user_info.EmployeeID).then(function(res) {
                    if (res.status === 200) {
                        console.log(res);
                        _this.notices = res.data;
                        if (res.data.length > 3){
                            _this.notices = res.data.slice(0, 3)
                        }
                        _this.count = _this.notices.length;
                    }})
            },

        },
        destroyed() {
            clearInterval(this.myInterval)
        },
        mounted() {
            // this.check_open();
            // this.check_notice();
        }
    }
</script>

<style scoped>
#notice {
    height: 50vh;
}
    .hidden {
        width: 0;
    }
</style>

