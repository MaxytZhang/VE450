<template>
    <div>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Topic</span></el-col>
            <el-col :span="10">
                <el-input v-model="input" placeholder="Please input meeting topic"></el-input>
            </el-col>
        </el-row>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Schedule</span></el-col>
            <el-col :span="10">
                <el-date-picker
                        v-model="value1"
                        type="datetimerange"
                        range-separator="to"
                        start-placeholder="start"
                        end-placeholder="end">
                </el-date-picker>
            </el-col>
        </el-row>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Attendances</span></el-col>
            <el-col :span="10">
                <el-cascader
                        :options="options"
                        :props="props"
                        clearable :show-all-levels="show_all"
                        placeholder="Please select attendances">
                </el-cascader>
            </el-col>
        </el-row>

        <el-row type="flex">
            <el-col :span="4"><span>Meeting Sites</span></el-col>
            <el-col :span="10">
                <el-checkbox-group v-model="checkboxGroup1">
                    <el-checkbox-button v-for="site in sites" :label="site" :key="site">{{site}}</el-checkbox-button>
                </el-checkbox-group>
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
                input: '',
                active: 0,
                show_pre: false,
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
                show_all: false,
                value1: [new Date(), new Date()],
                sites: siteOptions,
                checkboxGroup1: [],
            };
        },
    }
</script>

<style scoped>
    .block {
        margin: 40px 0;
    }
</style>
