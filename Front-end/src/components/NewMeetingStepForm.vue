<template>
    <el-form :model="meetingForm" :rules="rules" ref="meetingForm" label-width="160px" class="demo-ruleForm" label-position="right">
        <el-form-item label="Meeting Name" prop="meeting_name">
            <el-input v-model="meetingForm.meeting_name"></el-input>
        </el-form-item>

        <el-form-item label="Meeting Topic" prop="meeting_topic">
            <el-input v-model="meetingForm.meeting_topic"></el-input>
        </el-form-item>

        <el-form-item label="Routine Meeting" prop="routine">
            <el-switch
                    v-model="meetingForm.routine"
                    active-text="Yes"
                    inactive-text="No">
            </el-switch>
        </el-form-item>

        <el-form-item label="Meeting Schedule" required>
            <el-row>
            <el-col :span="6">
                <el-form-item prop="date">
                    <el-date-picker
                            v-model="meetingForm.date"
                            align="right"
                            type="date"
                            format="yyyy-MM-dd"
                            value-format="yyyy-MM-dd"
                            placeholder="Select Date"
                            :picker-options="datePickerOptions">
                    </el-date-picker>
                </el-form-item>
            </el-col>
            </el-row>
            <el-row>
            <el-col :span="12">
                <el-form-item prop="startTime" style="display: inline-block">
                    <el-time-select
                            v-model="meetingForm.startTime"
                            :picker-options="{
                            start: '00:00',
                            step: '00:15',
                            end: '23:45'
                        }"
                            placeholder="Select Start Time">
                    </el-time-select>
                </el-form-item>
                <el-form-item prop="endTime" style="display: inline-block; margin-top: 20px">
                    <el-time-select
                            placeholder="Select End Time"
                            v-model="meetingForm.endTime"
                            :picker-options="{
                            start: '00:00',
                            step: '00:15',
                            end: '23:45',
                            minTime: meetingForm.startTime
                        }">
                    </el-time-select>
                </el-form-item>
            </el-col>
            </el-row>
        </el-form-item>

        <el-form-item label="Meeting Site" required prop="sites">
            <el-checkbox-group v-model="meetingForm.sites" @change="handle_change">
                <el-checkbox-button v-for="site in sites" :label="site" :key="site">{{site}}</el-checkbox-button>
            </el-checkbox-group>
        </el-form-item>

        <el-form-item label="Meeting Attendance" required prop="attendees">
            <el-cascader
                    v-model="meetingForm.attendees"
                    :options="options"
                    :props="props"
                    clearable :show-all-levels="show_all"
                    placeholder="Please select attendances">
            </el-cascader>
        </el-form-item>

        <el-form-item label="Hardware Support" prop="support">
            <el-switch
                    v-model="meetingForm.support"
                    active-text="Yes"
                    inactive-text="No">
            </el-switch>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="submitForm('meetingForm')">Next</el-button>
            <el-button @click="resetForm('meetingForm')">Reset</el-button>
        </el-form-item>
    </el-form>

</template>

<script>
    export default {
        name: "NewMeetingStepForm",
        data() {
            return {
                meetingForm: {
                    type: 'meeting',
                    meeting_name: '',
                    meeting_topic: '',
                    routine: false,
                    date: '',
                    startTime: '',
                    endTime: '',
                    sites: [],
                    attendees: [],
                    support: false,
                    initiator: JSON.parse(this.$store.state.UserInfo).EmployeeID,
                    is_routine: 0,
                    need_hw_support: 0,
                },
                rules: {
                    meeting_name: [
                        { required: true, message: 'Please set meeting name', trigger: 'blur' },
                        { min: 3, message: 'at least 3 characters', trigger: 'blur' }
                    ],

                    date: [
                        { required: true, message: 'Please select date', trigger: 'blur' }
                    ],
                    startTime: [
                        { required: true, message: 'Please select start time', trigger: 'change' }
                    ],
                    endTime: [
                        { required: true, message: 'Please select end time', trigger: 'change' }
                    ],
                    sites: [
                        { type: 'array', required: true, message: 'Please select at least one site', trigger: 'change' }
                    ],
                    attendees: [
                        { required: true, message: 'Please select at least one attendance', trigger: 'change' }
                    ],
                },
                options: [
                    {
                        value: 's1',
                        label: 'Site 1',
                        children: [{
                            value: 'ea',
                            label: 'Employee A',
                        },
                            {
                                value: 'eb',
                                label: 'Employee B',
                            },
                            {
                                value: 'ec',
                                label: 'Employee C',
                            },]
                    },
                    {
                        value: 's2',
                        label: 'Site 2',
                        children: [{
                            value: 'ed',
                            label: 'Employee D',
                        },
                            {
                                value: 'ee',
                                label: 'Employee E',
                            },
                            {
                                value: 'ef',
                                label: 'Employee F',
                            },]
                    },
                    {
                        value: 'history',
                        label: 'Recent Selection',
                        children: [{
                            value: 'ea',
                            label: 'Employee A',
                        },
                            {
                                value: 'ed',
                                label: 'Employee D',
                            },
                            {
                                value: 'ee',
                                label: 'Employee E',
                            },]
                    },

                ],
                sites: [],
                user_info: JSON.parse(this.$store.state.UserInfo),
                props: {multiple: true},
                datePickerOptions: {
                    disabledDate(time) {
                        return time.getTime() < Date.now();
                    },
                    shortcuts: [{
                        text: 'Today',
                        onClick(picker) {
                            picker.$emit('pick', new Date());
                        }
                    }, {
                        text: 'Tomorrow',
                        onClick(picker) {
                            const date = new Date();
                            date.setTime(date.getTime() + 3600 * 1000 * 24);
                            picker.$emit('pick', date);
                        }
                    }, {
                        text: 'Next Week',
                        onClick(picker) {
                            const date = new Date();
                            date.setTime(date.getTime() + 3600 * 1000 * 24 * 7);
                            picker.$emit('pick', date);
                        }
                    }]
                },
                show_all: false,
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        console.log(this.$cookieStore.getCookie('name'));
                        this.meetingForm['start_timestamp'] = (new Date(this.meetingForm.date + " " + this.meetingForm.startTime)).getTime();
                        this.meetingForm['end_timestamp'] = (new Date(this.meetingForm.date + " " + this.meetingForm.endTime)).getTime();
                        this.meetingForm.is_routine = (this.meetingForm.routine === true) ? 1 : 0;
                        this.meetingForm.need_hw_support = (this.meetingForm.support === true) ? 1 : 0;
                        console.log(this.meetingForm);
                        this.$store.commit('setStep1', {
                            Step1: this.meetingForm
                        });
                        console.log(this.$store.state.Step1);
                        // alert('submit!');
                        this.$router.push("/new_meeting/step2");
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
            get_employee() {
                let _this = this;
                console.log(this.user_info.EmployeeID);
                this.$http.post("/v1.0/get_employee", {'id': _this.user_info.EmployeeID}).then(function (res) {
                    console.log(res);
                    if (res.status === 200) {
                        console.log(res.data);
                        _this.options = res.data;
                        _this.options_copy = res.data;
                    }
                    else {
                        _this.options = []
                    }
                })
            },
            get_sites() {
                let _this = this;
                console.log(this.user_info.EmployeeID);
                this.$http.post("/v1.0/get_sites", {'id': _this.user_info.EmployeeID}).then(function (res) {
                    console.log(res);
                    if (res.status === 200) {
                        console.log(res.data);
                        for ( let site of res.data){
                            _this.sites.push(site.siteName)
                        }
                        console.log(_this.sites)
                    }
                    else {
                        _this.sites = []
                    }
                })
            },
            handle_change(sites) {
                let _this = this;
                sites.push("Recent Selection");
                console.log(sites);
                // let new_options = [];
                let new_options = sites.map(function (s) {
                    for ( let site of _this.options_copy){
                        if (site.label === s) {
                            return site
                        }
                    }
                });
                sites.pop("Recent Selection");
                _this.options = new_options;
                console.log(new_options)
            },
        },
        created() {
            this.get_employee();
            this.get_sites();
        }
    }
</script>

<style scoped>

</style>
