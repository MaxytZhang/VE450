<template>
    <p>global</p>
</template>

<script>
    function to_new() {
        console.log('to_new');
        this.$router.push("/new_meeting")
    }
    export default {
        to_new,
        name: "Global",
        methods: {
            to_new() {
                this.$router.push("/new_meeting")
            },
            to_home() {
                this.$router.push("/home")
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
