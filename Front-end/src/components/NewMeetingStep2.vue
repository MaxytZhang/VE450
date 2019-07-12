<template>
    <div>
        <div v-for="i in count" :title="'Notice-' + i" :name="i">
        <el-row type="flex">
            <el-col :span="4">
                <span>Meeting Outline #{{i}}</span>
            </el-col>
            <el-col :span="10">
                <el-input class="input" v-model="input" placeholder="Please enter outline">
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
                        v-model="textarea1">
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
    </div>
</template>

<script>
    export default {
        name: "NewMeetingStep2",
        data() {
            return {
                count: 1,
                input: '',
                textarea1: '',
                select:''
            }
        },
        methods: {
            minus() {
                this.count--;
            },
            add(){
                this.count++;
            },
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
