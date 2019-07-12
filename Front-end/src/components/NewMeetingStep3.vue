<template>
    <div>
        <el-row type="flex" class="block">
            <el-col :span="4"><span>Meeting Room Recommendation</span></el-col>
            <el-cascader-panel :options="options" :props="props"></el-cascader-panel>
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
            }
        }
    }
</script>

<style scoped>

</style>
