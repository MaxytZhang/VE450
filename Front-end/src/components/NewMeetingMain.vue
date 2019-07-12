<template>
    <div>
        <el-row type="flex" class="step"></el-row>
        <el-steps :active="active" finish-status="success">
            <el-step title="Step 1"></el-step>
            <el-step title="Step 2"></el-step>
            <el-step title="Step 3"></el-step>
        </el-steps>
        <router-view></router-view>
        <el-row type="flex">
            <el-col :span="4">
                <el-button style="margin-top: 12px; float: left" @click="pre" v-show="show_pre">Previous</el-button>
            </el-col>
            <el-col :span="16"></el-col>
            <el-col :span="4">
                <el-button type="primary" style="margin-top: 12px; float: right" @click="next" id="finish">{{finish}}</el-button>
            </el-col>
        </el-row>
    </div>
</template>

<script>
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
                console.log((this.active));
                if (this.active === 1) this.finish = 'Submit';
                if (this.active < 2) this.active++;
                if (this.active > 0) this.show_pre = true;
                this.$router.push("/new_meeting/step" + (this.active + 1).toString())
            },
            pre() {
                if (this.active > 0) this.active--;
                if (this.active === 0) this.show_pre = false;
                this.$router.push("/new_meeting/step" + (this.active + 1).toString())
            },
            // change(selected) {
            //     console.log(selected);
            //     for (let i of this.options){
            //         for (let j of selected){
            //             if (j[0] == 'history') {
            //                 for (let option of i.children) {
            //                     if (i.value != 'history' && option.value == j[1]) {
            //                         this.selected.push([i.value, option.value]);
            //                         break
            //                     }
            //                 }
            //             }
            //         }
            //     }
            // }
        },
    }
</script>

<style scoped>

    .step {
        margin-top: 40px;
    }
</style>
