<template>
    <div>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Room Recommendation</span></el-col>
            <el-cascader-panel :options="options" :props="props"></el-cascader-panel>
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
                active: 2
            }
        },
        created() {
        },
        methods: {
            finish() {
                this.$router.push("/new_meeting/step4");
            },
            pre() {
                this.$router.push("/new_meeting/step2");
            }
        }
    }
</script>

<style scoped>

</style>
