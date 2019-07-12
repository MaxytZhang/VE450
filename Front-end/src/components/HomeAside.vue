<template>
    <div>
    <div id="side" >
        <div class="block">
            <el-avatar :size="100"><img class="side-img" src="../assets/profile.jpeg" alt=""></el-avatar>
        </div>
        <el-row class="block">
            <h1>董靖</h1>
            <p>ID: 123456</p>
            <p>Department: Artificial Intelligence</p>
        </el-row>
        <el-row id="notice">
        <div class="block">
            <el-collapse class="infinite-list">
                <el-collapse-item v-for="i in count" :title="'Notice-' + i" :name="i">
                    <div>{{i}}</div>
                </el-collapse-item>
            </el-collapse>
            <el-button type="primary" plain="" @click="load">More</el-button>
        </div>
            <el-button align="bottom" @click="log_out">Log out</el-button>
        </el-row>
    </div>
    </div>
</template>

<script>
    export default {
        name: "HomeSide",
        data () {
            return {
                isHidden: true,
                count: 3,
            }
        },
        methods: {
            load () {
                if (this.count < 20) {
                    this.count += 4
                }
            },
            log_out () {
                this.$router.push("/")
            }
        }
    }
</script>

<style scoped>
#notice {
    height: 50vh;
}
    .hidden {
        width: 0;
    }
</style>

