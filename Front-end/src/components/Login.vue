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
					<el-form-item label="Password" prop="pass">
						<el-input v-model="user.pass" style="width:200px" placeholder="Please Enter Password" clearable show-password></el-input>
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
	export default{
		methods: {
			login() {
				this.$refs.loginForm.validate((valid) => {
				if (valid) {
					if (this.user.name === "admin" && this.user.pass === "123123") {
						this.$notify({
						type: 'success',
						message: 'Welcome ' + this.user.name,
						duration: 3000
						});
						this.$router.replace('/home')
					}
					else {
						this.$message ({
							type: 'error',
							message: 'Wrong Account or Password',
							showClose: true
						})
					}
				}
				else {return false}
				})
			}
		},
		data () {
			return {
				user:{},
				rules: {
					name: [
						{required: true, message: 'Account Cannot Be Empty', trigger: 'blur'}
					],
					pass: [
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
