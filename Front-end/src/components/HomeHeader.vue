<template>
    <div>
        <el-menu :default-active="activeIndex" mode="horizontal">
            <el-menu-item index="1" @click="to_home">Home</el-menu-item>
            <el-menu-item index="2" @click="to_new">New Meeting</el-menu-item>
            <el-menu-item index="3" @click="to_ongoing">Ongoing Meeting</el-menu-item>
            <el-menu-item index="4" @click="to_calendar">Weekly Calendar</el-menu-item>
            <el-menu-item index="5" @click="to_history">Meeting History</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "HomeHeader",
        data() {
            return {
                activeIndex: '1',
            };
        },
        methods: {
            to_home() {
                this.$router.push("/home")
            },
            to_new() {
                this.$router.push("/new_meeting")
            },
            to_ongoing(){
                this.$router.push("/ongoing_meeting")
            },
            to_calendar(){
                this.$router.push("/weekly_calendar")
            },
            to_history(){
                this.$router.push("/meeting_history")
            },
        }
    }
</script>

<style scoped>

</style>
