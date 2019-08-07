<template>
    <div>
        <el-dialog
                title="Notice"
                :visible.sync="dialogVisible"
                width="30%">
            <span>You're all set! Take your time!</span>
            <span slot="footer" class="dialog-footer">
            <el-button type="primary" @click = "back_to_homepage" >Back to homepage</el-button>
        </span>
        </el-dialog>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Room Recommendation</span></el-col>
            <el-cascader-panel :options="options" :props="props" v-model="meeting_room"></el-cascader-panel>
        </el-row>
        <el-row type="flex">
            <el-col :span="4">
                <el-button style="margin-top: 12px; float: left" @click="pre">Previous</el-button>
            </el-col>
            <el-col :span="16"></el-col>
            <el-col :span="4">
                <el-button type="primary" style="margin-top: 12px; float: right" @click="finish" id="finish">Finish</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "NewMeetingStep3",
        data() {
            return{
                options: [
                    {
                        value: 's1',
                        label: 'Site 1',
                        children: [{
                            value: 'ea',
                            label: 'Room 001',
                        },
                            {
                                value: 'eb',
                                label: 'Room 002',
                            },
                            {
                                value: 'ec',
                                label: 'Room 007',
                            },]
                    },
                    {
                        value: 's2',
                        label: 'Site 2',
                        children: [{
                            value: 'ed',
                            label: 'Room 123',
                        },
                            {
                                value: 'ee',
                                label: 'Room 023',
                            },
                            {
                                value: 'ef',
                                label: 'Room 497',
                            },]
                    },
                    {
                        value: 's3',
                        label: 'Site3',
                        // disabled: true,
                        children: [{
                            value: 'ea',
                            label: 'No Meeting Room Available',
                            disabled: true,
                        },]
                    },

                ],
                props: {multiple: true},
                active: 2,
                meeting_room: [],
                dialogVisible: false
            }
        },
        created() {
            this.get_recommendation();
        },
        methods: {
            finish() {
                let _this = this;
                let meetingForm = this.$store.state.Step1;
                meetingForm['meeting_room'] = _this.meeting_room;
                this.$http.post("/v1.0/finish_recommendation", meetingForm).then(function (res) {
                    console.log(res);
                    if (res.status === 200) {
                        // _this.dialogVisible = true
                    }
                    else {

                    }
                }).catch(function(error) {
                    console.log(error) // error
                });
                this.$router.push("/new_meeting/step4");
            },
            pre() {
                this.$router.push("/new_meeting/step2");
            },
            get_recommendation() {
                // let meetingForm = this.$store.state.Step1;
                let options = this.$store.state.Step2;
                this.options = options;
                // console.log(meetingForm);
                console.log(options)
            },
            back_to_homepage() {
                this.$router.replace('/home')
            },
        }
    }
</script>

<style scoped>

</style>
