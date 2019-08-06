<template>
	<el-container>
		<el-header class="header" height="100px">
			<h1>Foxconn</h1>
			<p>Intelligent Meeting Room Management System</p>
		</el-header>
		<el-main>
			<el-row type="flex" justify="center">
				<el-form ref="loginForm" :model="user" :rules="rules" status-icon label-width="80px">
					<el-form-item label="Account" prop="name">
						<el-input v-model="user.name" style="width:200px" placeholder="Please Enter Account" clearable></el-input>
					</el-form-item>
					<el-form-item label="Password" prop="password">
						<el-input v-model="user.password" style="width:200px" placeholder="Please Enter Password" clearable show-password></el-input>
					</el-form-item>
					<el-form-item>
						<el-button type="primary" icon="el-icon-upload" @click="login">Login</el-button>
					</el-form-item>
				</el-form>
			</el-row>
		</el-main>
	</el-container>
</template>

<script>
    import { mapMutations } from 'vuex';
	export default{
		methods: {
            ...mapMutations(['changeLogin', 'setUserInfo']),
			login() {
                let _this = this;
				this.$refs.loginForm.validate((valid) => {
				if (valid) {
                    this.$http.post("/v1.0/validate_login", this.user).then(function (res) {
                        console.log(res);
                        if ((res.status === 200) && (res.data.pass === true)) {
                            console.log(res);
                            _this.$notify({
                                type: 'success',
                                message: 'Welcome ' + _this.user.name,
                                duration: 3000
                            });
                            _this.userToken = res.data.token;
                            _this.userInfo = JSON.stringify(res.data.info);
                            _this.$cookieStore.setCookie( 'name' , _this.user.name);
                            _this.changeLogin({ Authorization: _this.userToken });
                            _this.setUserInfo({UserInfo: _this.userInfo});
                            console.log(_this.$store.state.Authorization);
                            let name = _this.$cookieStore.getCookie('name');
                            console.log(name);
                            _this.$router.replace('/home')
                        }
                    });
					// if (this.user.name === "admin" && this.user.pass === "123123") {
					// 	this.$notify({
					// 	type: 'success',
					// 	message: 'Welcome ' + this.user.name,
					// 	duration: 3000
					// 	});
                    //     this.$cookieStore.setCookie( 'name' , this.user.name);
                    //     let name = this.$cookieStore.getCookie('name');
                    //     console.log(name);
					// 	this.$router.replace('/home')
					// }
					// else {
					// 	this.$message ({
					// 		type: 'error',
					// 		message: 'Wrong Account or Password',
					// 		showClose: true
					// 	})
					// }
				}
				else {return false}
				})
			},
		},
		data () {
			return {
				user:{},
				rules: {
					name: [
						{required: true, message: 'Account Cannot Be Empty', trigger: 'blur'}
					],
                    password: [
						{required: true, message: 'Password Cannot Be Empty', trigger: 'blur'}
					]
				}
			}
		}
	}
</script>

<style>
  .header{
    background-color: #409EFF;
    color: white;
  }
</style>
