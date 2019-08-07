<template>
    <div>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>You're all set!</span></el-col>
        </el-row>
        <el-row type="flex" class="block">
            <el-button type="primary" style="margin-top: 12px; float: right" @click="end" id="end">Back to homepage</el-button>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "NewMeetingStep4",
        data() {
            return {
                test: "this is test",
            }
        },
        methods: {
            end() {
                this.$router.push("/home");
            }
        }
    }
</script>

<style scoped>

</style>
