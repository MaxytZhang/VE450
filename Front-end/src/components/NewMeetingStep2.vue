<template>
    <div>
        <div v-for="i in count" :title="'Notice-' + i" :name="i">
        <el-row type="flex">
            <el-col :span="4">
                <span>Meeting Outline #{{i}}</span>
            </el-col>
            <el-col :span="10">
                <el-input class="input" v-model="outlines[i-1]" :value="'test_' + i" placeholder="Please enter outline">
                    <!--<el-select size="300px" v-model="select" slot="prepend" placeholder="Period">-->
                        <!--<el-option label="5" value="1"></el-option>-->
                        <!--<el-option label="10" value="2"></el-option>-->
                        <!--<el-option label="15" value="3"></el-option>-->
                        <!--<el-option label="20" value="4"></el-option>-->
                    <!--</el-select>-->
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
    import axios from 'axios';
    import qs from 'qs'
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
                let form_data = new FormData();
                form_data.append("meeting_outline", this.outlines);
                this.$store.commit('setStep2', {
                    Step2: form_data
                });
                let total_form_data = new FormData();
                total_form_data.append("type", "meeting");
                total_form_data.append("meeting_name", "test");
                total_form_data.append("meeting_topic", this.$store.state.Step1.meeting_topic);
                total_form_data.append('start_timestamp', this.$store.state.Step1.start_timestamp);
                total_form_data.append('end_timestamp', this.$store.state.Step1.end_timestamp);
                total_form_data.append('attendees', this.$store.state.Step1.attendees);
                total_form_data.append('sites', this.$store.state.Step1.sites);
                total_form_data.append('is_routine', this.$store.state.Step1.is_routine);
                total_form_data.append('need_hw_support', this.$store.state.Step1.need_hw_support);
                total_form_data.append('initiator', '1239084');
                total_form_data.append("meeting_outline", this.outlines);
                let config = {
                    // headers: {
                    //     'Content-Type': 'multipart/form-data'
                    // }
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
                    }
                };

                let test = {
                    'site': JSON.stringify(this.$store.state.Step1.sites),
                    'attendees': JSON.stringify(this.$store.state.Step1),
                };
                var test2 = {
                    'site': this.$store.state.Step1.sites,
                    'attendees': this.$store.state.Step1,
                };
                axios.post("/v1.0/test", test2, config).then(function (res) {
                    if (res.status === 200) {
                        console.log(res)
                    }
                });
                console.log(test);
                console.log(this.outlines);
                console.log(total_form_data.get('meeting_outline'));
                // axios.post("/v1.0/meetings", qs.stringify(total_form_data), config).then(function (res) {
                //     if (res.status === 200) {
                //         console.log(res)
                //     }
                // });
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
