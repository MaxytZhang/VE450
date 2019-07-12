<template>
    <el-container>
        <el-aside width="400px" v-bind:class="{hidden: isHidden}" align="middle">
        <HomeAside/>
        </el-aside>
        <el-row type="flex" align="middle">
            <el-button id="hide" style="height: 25vh" @click="toggle_side">hide</el-button>
        </el-row>
        <el-container>
            <el-header>
            <HomeHeader/>
            </el-header>
            <el-main>
            <router-view></router-view>
            </el-main>
            <el-footer>
            <HomeFooter/>
            </el-footer>
        </el-container>
    </el-container>
</template>

<script>
    import HomeHeader from './HomeHeader'
    import HomeAside from './HomeAside'
    import HomeFooter from './HomeFooter'
    import HomeMain from './HomeMain'

    export default {
        name: "HomeLayout",
        data() {
            return {
                isHidden: false,
            };
        },
        methods: {
            toggle_side() {
                this.isHidden = !this.isHidden;
                let hide = document.getElementById("hide");
                console.log(hide.innerText);
                if (hide.innerText == "hide"){
                    hide.innerText = "expand"
                }
                else if (hide.innerText == "expand"){
                    hide.innerText = "expand"
                }
            }
        },
        components: {
            HomeHeader, HomeAside, HomeFooter, HomeMain
        }
    }

    // Vue.component('HomeLayout')
</script>

<style scoped>
    .hidden {
        width: 0!important;
    }
</style>
