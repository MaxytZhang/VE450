<template>
    <div>
    <el-row :gutter="20" type="flex">
        <el-col :span="12">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>Ongoing Meeting</span>

                </div>
                <div class="text item" v-for="(item, i) in meeting_history.present">
                    No{{i}}   {{item}} <el-button style="float: right; padding: 3px 0" type="text" @click="to_ongoing">check</el-button>
                </div>
            </el-card>
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>Next Meetings</span>
                </div>
                <div class="text item" v-for="(item, i) in meeting_history.future">
                    {{item.Name}} {{item.MeetingTopic}} {{item.date}} <el-button style="float: right; padding: 3px 0" type="text">check</el-button>
                </div>
            </el-card>
            <!--<el-button type="primary" @click="this.to_new">Start A New Meeting</el-button>-->
            <el-button type="primary" @click="to_new">Start A New Meeting</el-button>
            <el-button type="primary" @click="test">Test</el-button>

        </el-col>
        <!--<el-col :span="12">-->
            <!--<el-calendar v-model="value">-->
            <!--</el-calendar>-->
        <!--</el-col>-->
    </el-row>
    <el-row>
        <el-col :span="12">
        </el-col>
    </el-row>
    </div>
</template>

<script>
    export default {
        name: "HomeMain",
        created() {
            this.get_meeting_history()
        },
        data(){
            return {
                user_info: JSON.parse(this.$store.state.UserInfo),
                value: new Date(),
                user_name: this.$cookieStore.getCookie('name'),
                meeting_history: {},
            }
        },
        methods: {
            to_new() {
                console.log(this.user_name);
                this.$router.push("/new_meeting")
            },
            to_ongoing(){
                this.$router.push("/ongoing_meeting")
            },
            test() {
                this.$http.get("/v1.0/test").then(function(r) {
                        console.log(r);
                        // console.log(this.$cookieStore.getCookie('name'));
                        alert(r.data.message)})
            },
            get_meeting_history() {
                let _this = this;
                this.$http.post("/v1.0/get_meeting_history", {'id': this.user_info.EmployeeID}).then(function(res) {
                    console.log(res);
                    // console.log(this.$cookieStore.getCookie('name'));
                    _this.meeting_history = res.data;
                    console.log(_this.meeting_history)
                })
            }
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
