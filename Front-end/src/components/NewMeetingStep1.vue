<template>
    <div>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Name</span></el-col>
            <el-col :span="10">
                <el-input v-model="meeting_name" placeholder="Please input meeting name"></el-input>
            </el-col>
        </el-row>

        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Topic</span></el-col>
            <el-col :span="10">
                <el-input v-model="meeting_topic" placeholder="Please input meeting topic"></el-input>
            </el-col>
        </el-row>

        <el-row type="flex">
            <el-col :span="4"><span>Routine Meeting</span></el-col>
            <el-switch
                    v-model="is_routine"
                    active-text="Yes"
                    inactive-text="No">
            </el-switch>
        </el-row>

        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Schedule</span></el-col>
            <el-col :span="10">
                <div style="margin-bottom: 20px">
                    <el-date-picker
                            v-model="date"
                            align="right"
                            type="date"
                            format="yyyy-MM-dd"
                            placeholder="Select Date"
                            :picker-options="datePickerOptions">
                    </el-date-picker>
                </div>
                <el-time-select
                        style="margin-right: 20px"
                        v-model="startTime"
                        :picker-options="{
                            start: '00:00',
                            step: '00:15',
                            end: '23:45'
                        }"
                        placeholder="Select Start Time">
                </el-time-select>
                <el-time-select
                        placeholder="Select End Time"
                        v-model="endTime"
                        :picker-options="{
                        start: '00:00',
                        step: '00:15',
                        end: '23:45',
                        minTime: startTime
                        }">
                </el-time-select>
            </el-col>
        </el-row>

        <el-row type="flex">
            <el-col :span="4"><span>Meeting Sites</span></el-col>
            <el-col :span="10">
                <el-checkbox-group v-model="selected_sites">
                    <el-checkbox-button v-for="site in sites" :label="site" :key="site">{{site}}</el-checkbox-button>
                </el-checkbox-group>
            </el-col>
        </el-row>

        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Attendances</span></el-col>
            <el-col :span="10">
                <el-cascader
                        v-model="selected_employees"
                        :options="options"
                        :props="props"
                        clearable :show-all-levels="show_all"
                        placeholder="Please select attendances">
                </el-cascader>
            </el-col>
        </el-row>


        <el-row type="flex">
            <el-col :span="4"><span>Hardware Support</span></el-col>
            <el-switch
                    v-model="need_support"
                    active-text="Yes"
                    inactive-text="No">
            </el-switch>
        </el-row>

        <el-row type="flex">
            <el-col :span="4">
            </el-col>
            <el-col :span="16"></el-col>
            <el-col :span="4">
                <el-button type="primary" style="margin-top: 12px; float: right" @click="next">Next</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    const siteOptions = ['Site1', 'Site2', 'Site3', 'Site4'];
    export default {
        name: "NewMeetingStep1",
        data() {
            return {
                meeting_name: '',
                meeting_topic: '',
                is_routine: false,
                active: 0,
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
                props: {multiple: true},
                selected_employees: [],
                show_all: false,
                date: "",
                sites: siteOptions,
                selected_sites: [],
                need_support: false,
                startTime: '',
                endTime: '',
                datePickerOptions: {
                    disabledDate(time) {
                        return time.getTime() > Date.now();
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
            };
        },
        methods: {
            next() {
                console.log(this.$cookieStore.getCookie('name'));
                console.log(this.date);
                console.log(this.startTime);
                let step1_form = {
                    'meeting_name': this.meeting_name,
                    'meeting_topic': this.meeting_topic,
                    'is_routine': Number(this.is_routine),
                    'need_hw_support': Number(this.need_support),
                    'start_timestamp': Number(this.date.getTime()),
                    'end_timestamp': Number(this.date.getTime()),
                    'attendees': this.selected_employees,
                    'sites': this.selected_sites,
                };
                this.$store.commit('setStep1', {
                    Step1: step1_form
                });
                console.log(this.$store.state.Step1);
                this.$router.push("/new_meeting/step2");
            }
        }
    }
</script>

<style scoped>
    .block {
        margin: 40px 0;
    }
</style>
