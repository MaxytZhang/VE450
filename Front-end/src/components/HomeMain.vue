<template>
    <div>
    <el-row :gutter="20" type="flex">
        <el-col :span="12">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>Ongoing Meeting</span>
                    <el-button style="float: right; padding: 3px 0" type="text" @click="to_ongoing">check</el-button>
                </div>
                <div class="text item">
                    16:45 : 18:00 R305
                </div>
            </el-card>
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>Next Meetings</span>
                    <el-button style="float: right; padding: 3px 0" type="text">check</el-button>
                </div>
                <div v-for="i in 3" class="text item">
                    <el-button>No. {{i}}</el-button>
                </div>
            </el-card>
            <!--<el-button type="primary" @click="this.to_new">Start A New Meeting</el-button>-->
            <el-button type="primary" @click="to_new">Start A New Meeting</el-button>
            <el-button type="primary" @click="test">Test</el-button>

        </el-col>
        <el-col :span="12">
            <el-calendar v-model="value">
            </el-calendar>
        </el-col>
    </el-row>
    <el-row>
        <el-col :span="12">
        </el-col>
    </el-row>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "HomeMain",
        data(){
            return {
                value: new Date(),
            }
        },
        methods: {
            to_new() {
                this.$router.push("/new_meeting")
            },
            to_ongoing(){
                this.$router.push("/ongoing_meeting")
            },
            test() {
                axios.get("http://127.0.0.1:5000/backend/api/v1.0/test").then(function(r) {
                    console.log(r);
                    alert(r.data.message)})}
            ,
        }
    }
</script>

<style scoped>

    div {
        justify-content: left;
        text-align: left;
    }

    .box-card {
        margin-bottom: 5vh;
    }

    .text {
        font-size: 14px;
    }

    .item {
        margin-bottom: 18px;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }
    .clearfix:after {
        clear: both
    }

    .box-card {
        width: 480px;
    }
</style>
