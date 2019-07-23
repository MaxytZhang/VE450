<template>
    <div>
        <el-row type="flex" class="step"></el-row>
        <el-steps :active="calActive" finish-status="success">
            <el-step title="Step 1"></el-step>
            <el-step title="Step 2"></el-step>
            <el-step title="Step 3"></el-step>
        </el-steps>
        <router-view></router-view>
        <!--<el-row type="flex">-->
            <!--<el-col :span="4">-->
                <!--<el-button style="margin-top: 12px; float: left" @click="pre" v-show="show_pre">Previous</el-button>-->
            <!--</el-col>-->
            <!--<el-col :span="16"></el-col>-->
            <!--<el-col :span="4">-->
                <!--<el-button type="primary" style="margin-top: 12px; float: right" @click="next" id="finish">{{finish}}</el-button>-->
            <!--</el-col>-->
        <!--</el-row>-->
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "NewMeetingMain",
        data() {
            return {
                show_pre: false,
                active: 0,
                finish: 'Next',
            };
        },
        methods: {
            next() {
                if (this.active < 3) this.active++;
                console.log((this.active));
                if (this.active === 1) this.finish = 'Submit';
                else if (this.active === 2) this.finish = 'Finish';
                if (this.active > 0) this.show_pre = true;
                if (this.active < 3) {
                    this.$router.push("/new_meeting/step" + (this.active + 1).toString());
                }
                if (this.active === 2) {
                    this.$notify({
                        type: 'success',
                        message: 'Submit successfully!',
                        duration: 3000
                    });
                }
                if (this.active === 3) {
                    this.$notify({
                        type: 'success',
                        message: 'You have successfully started a new meeting',
                        duration: 3000
                    });
                    this.active--;
                }

                if (this.finish === 'Finish') {
                    let formData = new FormData();
                    formData.append('name', 'DJ');
                    formData.append('age', '20');
                    console.log(formData.get('name'));
                    let config = {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    };

                    axios.post("http://127.0.0.1:5000/backend/api/v1.0/test_upload", formData, config).then(function (res) {
                        if (res.status === 200) {
                            console.log(res)
                        }
                    });
                }

                if (this.finish === 'Next'){
                    let formData = new FormData();
                }
            },
            pre() {
                if (this.active > 0) this.active--;
                console.log(this.active);
                if (this.active === 0) {
                    this.show_pre = false;
                    this.finish = 'Next'
                }
                if (this.active === 1){
                    this.finish = 'Submit'
                }
                this.$router.push("/new_meeting/step" + (this.active + 1).toString());

            },
        },
        computed: {
            calActive() {
                if (this.$route.path === '/new_meeting'){
                    return 0
                }
                else if (this.$route.path === '/new_meeting/step1'){
                    return 0
                }
                else if (this.$route.path === '/new_meeting/step2'){
                    return 1
                }
                else if (this.$route.path === '/new_meeting/step3'){
                    return 2
                }
            }
        }
    }
</script>

<style scoped>

    .step {
        margin-top: 40px;
    }
</style>
