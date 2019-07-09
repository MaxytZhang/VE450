<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <!--<div>-->
      <!--<p>-->
        <!--If Element is successfully added to this project, you'll see an-->
        <!--<code v-text="'<el-button>'"></code>-->
        <!--below-->
      <!--</p>-->
      <!--<el-button>el-button</el-button>-->
    <!--</div>-->
    <!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <!--<ul>-->
      <!--<li><router-link to="/">Hello页面</router-link></li>-->
      <!--<li><router-link to="/word">word页面</router-link></li>-->
    <!--</ul>-->
    <!--<router-view></router-view>-->
    <HomeLayout/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import HomeLayout from './components/HomeLayout'

export default {
  name: 'app',
  components: {
      HomeLayout
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
