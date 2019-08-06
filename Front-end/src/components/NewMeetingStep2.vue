<template>
    <div>
        <div v-for="i in count" :title="'Notice-' + i" :name="i">
        <el-row type="flex">
            <el-col :span="4">
                <span>Meeting Outline #{{i}}</span>
            </el-col>
            <el-col :span="10">
                <el-input class="input" v-model="outlines[i-1]" :value="'test_' + i" placeholder="Please enter outline">
                </el-input>
                <el-input class="input"
                        type="textarea"
                        :autosize="{ minRows: 4, maxRows: 10}"
                        placeholder="Please enter description"
                        v-model="descriptions[i-1]">
                </el-input>
            </el-col>
        </el-row>
        </div>
        <el-row type="flex">
            <el-col :span="14">
                <el-button type="primary" plain style="margin-top: 12px; float: right" @click="add">Add</el-button>
                <el-button style="margin-top: 12px; float: right" @click="minus">Delete</el-button>
            </el-col>
        </el-row>
        <el-row type="flex">
            <el-col :span="4">
                <el-button style="margin-top: 12px; float: left" @click="pre">Previous</el-button>
            </el-col>
            <el-col :span="16"></el-col>
            <el-col :span="4">
                <el-button type="primary" style="margin-top: 12px; float: right" @click="submit" id="finish">Submit</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "NewMeetingStep2",
        data() {
            return {
                active: 1,
                count: 1,
                outlines: [''],
                descriptions: [''],
                select:''
            }
        },
        methods: {
            minus() {
                this.count--;
                this.outlines.pop();
                this.descriptions.pop();
            },
            add(){
                this.count++;
                this.outlines.push('');
                this.descriptions.push('');

            },
            submit(){
                let _this = this;
                let meetingForm = this.$store.state.Step1;
                meetingForm["meeting_outline"] = this.outlines;
                meetingForm["outline_descriptions"] = this.descriptions;
                console.log(meetingForm);
                this.$store.commit('setStep1', {
                    Step1: meetingForm
                });
                this.$http.post("/v1.0/meetings", meetingForm).then(function (res) {
                    if (res.status === 200) {
                        console.log(res);
                        _this.$store.commit('setStep2', {
                            Step2: res.data
                        });
                    }
                });
                this.$router.push("/new_meeting/step3");
            },
            pre(){
                this.$router.push("/new_meeting/step1");
            }
        }
    }
</script>

<style scoped>
.input {
    margin-bottom: 15px;
}
</style>

<!--<style>-->
    <!--el-select {-->
        <!--width: 50px !important;-->
    <!--}-->
<!--</style>-->
