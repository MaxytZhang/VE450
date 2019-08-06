<template>
    <div>
        <el-dialog
                title="Notice"
                :visible.sync="dialogVisible"
                width="30%">
            <span>You have no ongoing meeting! Take a rest!</span>
            <span slot="footer" class="dialog-footer">
            <el-button type="primary" @click = "back_to_homepage" >Back to homepage</el-button>
        </span>
        </el-dialog>
        <el-progress :percentage="percentage" :format="format"></el-progress>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Name</span></el-col>
            <el-col :span="10">
                <span>{{meetingForm.meeting_name}}</span>
            </el-col>
        </el-row>
            <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Topic</span></el-col>
            <el-col :span="10">
                <span>{{meetingForm.meeting_topic}}</span>
            </el-col>
            </el-row>
            <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Name</span></el-col>
            <el-col :span="10">
                <span>{{meetingForm.meeting_name}}</span>
            </el-col>
            </el-row>
            <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Schedule</span></el-col>
            <el-col :span="10">
                <span>{{meetingForm.date}} {{meetingForm.startTime}} - {{meetingForm.endTime}}</span>
            </el-col>
            </el-row>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Memo</span></el-col>
            <el-col :span="10">
                <div v-for="(item, i) in meetingForm.meeting_outline" :key="i">
                    <span>Step{{i}}: {{item}}</span>
                <el-input class="input"
                          type="textarea"
                          :autosize="{ minRows: 4, maxRows: 10}"
                          placeholder="Please enter description"
                          v-model="memo[i]">
                </el-input>
                </div>
            </el-col>
        </el-row>
        <el-button type="primary" @click="end_meeting">End this meeting</el-button>
    </div>
</template>

<script>
    export default {
        name: "OngoingMeetingMain",
        created() {
            this.get_ongoing_meeting()
        },
        data() {
            return {
                meetingForm: {},
                percentage: 70,
                dialogVisible: false,
                user_info: JSON.parse(this.$store.state.UserInfo),
                memo: [],
            }
        },
        methods: {
            format(percentage) {
                return percentage === 100 ? '满' : `${percentage}%`;
            },
            get_ongoing_meeting() {
                let _this = this;
                this.$http.post("/v1.0/get_ongoing_meeting", this.user_info.EmployeeID).then(function (res) {
                    console.log(res);
                    if ((res.status === 200) && (res.data.going === true)) {
                        console.log(res.data);
                        _this.meetingForm = res.data
                    }
                    else {
                        _this.dialogVisible = true
                    }
                })
            },
            back_to_homepage() {
                this.$router.replace('/home')
            },
            end_meeting() {
                let _this = this;
                let meeting_memo = {};
                for (let i=0; i++; i<this.memo.length){
                    meeting_memo[this.meetingForm.meeting_outline[i]] = this.memo[i]
                }
                let meeting_end = {};
                meeting_end['id'] = this.meetingForm.id;
                meeting_end['memo'] = meeting_memo;
                console.log(meeting_memo);
                this.$http.post("/v1.0/end_meeting", meeting_end).then(function (res) {
                    console.log(res);
                    if ((res.status === 200) && (res.data === true)) {
                        _this.$notify({
                            type: 'success',
                            message: _this.user_info.EmployName + ": You have successfully ended this meeting",
                            duration: 3000
                        });
                    }
                    else {
                        _this.$notify({
                            type: 'error',
                            message: _this.user_info.EmployName + ": Something wrong happened. We're working on it!",
                            duration: 3000
                        });
                    }
                });
                this.$router.replace('/home')
            }
        }
    }
</script>

<style scoped>

</style>
