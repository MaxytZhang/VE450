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
                <el-collapse-item v-for="i in count" :title="'Notice-' + i" :name="i">
                    <div>{{i}}</div>
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
        beforeMount () {
            console.log(this.$store.state.UserInfo);
            console.log(this.$cookieStore.getCookie('name'))
        },
        data () {
            return {
                user_info: JSON.parse(this.$store.state.UserInfo),
                user_name: this.$cookieStore.getCookie('name'),
                isHidden: true,
                count: 3,
            }
        },
        methods: {
            load () {
                if (this.count < 20) {
                    this.count += 4
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
            }
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

