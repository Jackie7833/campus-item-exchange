<template>
<view class="content">
	<view class="box" :style='{"minHeight":"100%","width":"100%","padding":"0","position":"relative","background":"#fff","height":"auto"}'>
		<view :style='{"width":"100%","padding":"24rpx","background":"none","display":"block","height":"auto"}'>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yonghu'" class="">
				<view class="title" :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}'>账号</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' disabled="true"  v-model="ruleForm.zhanghao" placeholder="账号"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yonghu'" class="">
				<view class="title" :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}'>昵称</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}'   v-model="ruleForm.nicheng" placeholder="昵称"></input>
			</view>
			<view v-if="tableName=='yonghu'" :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class=" select">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">性别</view>
				<picker :style='{"width":"100%","flex":"1","height":"auto"}'  @change="yonghuxingbieChange" :value="yonghuxingbieIndex" :range="yonghuxingbieOptions">
					<view :style='{"border":"none","padding":"0 40rpx","color":"#000","borderRadius":"40rpx","width":"100%","lineHeight":"80rpx","fontSize":"28rpx"}' class="uni-input picker-select-input">{{ruleForm.xingbie?ruleForm.xingbie:"请选择性别"}}</view>
				</picker>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yonghu'" class="">
				<view class="title" :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}'>手机</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}'   v-model="ruleForm.shouji" placeholder="手机"></input>
			</view>
			<view v-if="tableName=='yonghu'" :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class=" select">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">身份</view>
				<picker :style='{"width":"100%","flex":"1","height":"auto"}'  @change="yonghushenfenChange" :value="yonghushenfenIndex" :range="yonghushenfenOptions">
					<view :style='{"border":"none","padding":"0 40rpx","color":"#000","borderRadius":"40rpx","width":"100%","lineHeight":"80rpx","fontSize":"28rpx"}' class="uni-input picker-select-input">{{ruleForm.shenfen?ruleForm.shenfen:"请选择身份"}}</view>
				</picker>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yonghu'" class="">
				<view class="title" :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}'>邮箱</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}'   v-model="ruleForm.youxiang" placeholder="邮箱"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yonghu'" @tap="yonghutouxiangTap" class="">
				<view class="title" :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}'>头像</view>
				<image :style='{"width":"80rpx","borderRadius":"100%","objectFit":"cover","display":"block","height":"80rpx"}' v-if="ruleForm.touxiang" style="margin: 0;" class="avator" :src="baseUrl+ruleForm.touxiang" mode=""></image>
				<image :style='{"width":"80rpx","borderRadius":"100%","objectFit":"cover","display":"block","height":"80rpx"}' v-else class="avator" style="margin: 0;" src="../../static/gen/upload.png" mode=""></image>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yonghu'" class="">
				<view class="title" :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}'>姓名</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}'   v-model="ruleForm.xingming" placeholder="姓名"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yonghu'" @tap="yonghushenfenzhengTap" class="">
				<view class="title" :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}'>学生证</view>
				<image :style='{"width":"80rpx","borderRadius":"100%","objectFit":"cover","display":"block","height":"80rpx"}' v-if="ruleForm.shenfenzheng" style="margin: 0;" class="avator" :src="baseUrl+ruleForm.shenfenzheng" mode=""></image>
				<image :style='{"width":"80rpx","borderRadius":"100%","objectFit":"cover","display":"block","height":"80rpx"}' v-else class="avator" style="margin: 0;" src="../../static/gen/upload.png" mode=""></image>
				<view v-if="ruleForm.sfsh" :style='{"margin":"0 0 0 20rpx","fontSize":"24rpx","color":"#64748B"}'>{{ruleForm.sfsh=='是'?'已认证':(ruleForm.sfsh=='否'?'认证未通过':'待审核')}}</view>
			</view>
			<view :style='{"width":"100%","flexDirection":"column","justifyContent":"center","display":"flex","gap":"20rpx","height":"auto"}' class="btn">
				<button @tap="update()" class="cu-btn lg" :style='{"border":"none","padding":"0px","margin":"0 20rpx","color":"#fff","borderRadius":"20rpx","background":"linear-gradient( 135deg, #469CF5 0%, #25CCB4 100%)","width":"100%","lineHeight":"80rpx","fontSize":"32rpx","height":"80rpx"}'>保存</button>
				<button @tap="logout()" class="cu-btn lg" :style='{"border":"none","padding":"0px","margin":"0 20rpx","color":"#000000","borderRadius":"20rpx","background":"#D9D9D9","width":"100%","lineHeight":"80rpx","fontSize":"32rpx","height":"80rpx"}'>退出登录</button>
			</view>
		</view>
	</view>
</view>
</template>

<script>

    import xiaEditor from '@/components/xia-editor/xia-editor';
    import multipleSelect from "@/components/momo-multipleSelect/momo-multipleSelect";
	export default {
		data() {
			return {
				ruleForm: {
				},
				tableName:"",
				yonghuxingbieOptions: [],
				yonghuxingbieIndex: 0,
				yonghushenfenOptions: [],
				yonghushenfenIndex: 0,
			}
		},
        components: {
            multipleSelect,
			xiaEditor
        },
		computed: {
			baseUrl() {
				return this.$base.url;
			}
		},
		async onLoad() {
			let table = uni.getStorageSync("nowTable");
			let that = this
			let res = {}
			this.tableName = table;
			this.getSession()
			// 自定义下拉框值
			if(this.tableName=='yonghu'){
				this.yonghuxingbieOptions = "男,女".split(',');
				this.yonghuxingbieOptions.forEach((item, index) => {
					if(item==this.ruleForm.xingbie) {
						this.yonghuxingbieIndex = index;
					}
				});
			}
			// 自定义下拉框值
			if(this.tableName=='yonghu'){
				this.yonghushenfenOptions = "学生,教职工".split(',');
				this.yonghushenfenOptions.forEach((item, index) => {
					if(item==this.ruleForm.shenfen) {
						this.yonghushenfenIndex = index;
					}
				});
			}
			this.styleChange()
            this.$forceUpdate()
		},
		methods: {
			async getSession(){
				let res = await this.$api.session(this.tableName)
				this.ruleForm = res.data;
				uni.setStorageSync('userSession',JSON.stringify(res.data))
			},
            // 下拉变化
            yonghuxingbieChange(e) {
                    this.yonghuxingbieIndex = e.target.value
                    this.ruleForm.xingbie = this.yonghuxingbieOptions[this.yonghuxingbieIndex]
            },
            // 下拉变化
            yonghushenfenChange(e) {
                    this.yonghushenfenIndex = e.target.value
                    this.ruleForm.shenfen = this.yonghushenfenOptions[this.yonghushenfenIndex]
            },
			yonghutouxiangTap() {
				let _this = this;
				this.$api.upload(function(res) {
					_this.ruleForm.touxiang = 'upload/' + res.file;
					_this.$forceUpdate();
				});
			},
			yonghushenfenzhengTap() {
				let _this = this;
				this.$api.upload(async function(res) {
					_this.ruleForm.shenfenzheng = 'upload/' + res.file;
					_this.ruleForm.sfsh = '待审核';
					_this.ruleForm.shhf = '学生证自动审核中';
					_this.$forceUpdate();
					if (_this.ruleForm.id) {
						let verifyRes = await _this.$api.verifyStudentCard({
							userId: _this.ruleForm.id,
							fileName: _this.ruleForm.shenfenzheng
						});
						if (verifyRes && verifyRes.data) {
							_this.ruleForm.sfsh = verifyRes.data.status;
							_this.ruleForm.shhf = verifyRes.data.reason;
							_this.$utils.msg(verifyRes.data.passed ? '认证成功' : verifyRes.data.reason);
							await _this.getSession();
						}
					}
				});
			},

            toggleTab(str) {
                this.$refs[str].show();
            },

			styleChange() {
				this.$nextTick(()=>{
					// document.querySelectorAll('. .uni-input-input').forEach(el=>{
					//   el.style.backgroundColor = this.userInfoForm.list.input.backgroundColor
					// })
				})
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			logout() {
				uni.clearStorageSync()
				this.$utils.jump('../login/login');
			},
			// 注册
			async update() {

				if((!this.ruleForm.zhanghao) && `yonghu` == this.tableName){
					this.$utils.msg(`账号不能为空`);
					return
				}

				if((!this.ruleForm.mima) && `yonghu` == this.tableName){
					this.$utils.msg(`密码不能为空`);
					return
				}

				if((!this.ruleForm.nicheng) && `yonghu` == this.tableName){
					this.$utils.msg(`昵称不能为空`);
					return
				}


				if((!this.ruleForm.shouji) && `yonghu` == this.tableName){
					this.$utils.msg(`手机不能为空`);
					return
				}
				if(`yonghu` == this.tableName && this.ruleForm.shouji&&(!this.$validate.isMobile(this.ruleForm.shouji))){
					this.$utils.msg(`手机应输入手机格式`);
					return
				}

				if((!this.ruleForm.shenfen) && `yonghu` == this.tableName){
					this.$utils.msg(`身份不能为空`);
					return
				}

				if(`yonghu` == this.tableName && this.ruleForm.youxiang&&(!this.$validate.isEmail(this.ruleForm.youxiang))){
					this.$utils.msg(`邮箱应输入邮件格式`);
					return
				}

				if((!this.ruleForm.touxiang) && `yonghu` == this.tableName){
					this.$utils.msg(`头像不能为空`);
					return
				}

				if((!this.ruleForm.xingming) && `yonghu` == this.tableName){
					this.$utils.msg(`姓名不能为空`);
					return
				}

				if((!this.ruleForm.shenfenzheng) && `yonghu` == this.tableName){
					this.$utils.msg(`学生证不能为空`);
					return
				}


				let table = uni.getStorageSync("nowTable");
				await this.$api.update(table, this.ruleForm);
				this.$utils.msgBack('修改成功');;
				this.getSession()
			},

		}
	}
</script>

<style lang="scss" scoped>
	.content {
		min-height: calc(100vh - 44px);
		box-sizing: border-box;
	}
	.content {
		background: #f6f8fa !important;
		padding: 24rpx !important;
	}
	.formView,
	.uni-forms {
		border-radius: 18rpx !important;
		background: #fff !important;
		padding: 20rpx 24rpx !important;
		box-shadow: 0 10rpx 30rpx rgba(24, 35, 47, .07) !important;
	}
	.uni-forms-item {
		margin-bottom: 18rpx !important;
	}
	button,
	.uni-button {
		border-radius: 14rpx !important;
		background: #12b3a8 !important;
		color: #fff !important;
	}
	image {
		border-radius: 14rpx !important;
	}
	.title {
		width: 168rpx !important;
		text-align: left !important;
		color: #44515d !important;
		font-size: 27rpx !important;
	}
	input,
	.uni-input,
	.picker-select-input {
		min-height: 76rpx !important;
		border: 1rpx solid #d8e3e8 !important;
		border-radius: 14rpx !important;
		background: #f7fafb !important;
	}
	.avator {
		width: 128rpx !important;
		height: 128rpx !important;
		border-radius: 14rpx !important;
		background: #f3f7f8 !important;
	}
	.btn button {
		margin: 8rpx 0 0 !important;
		box-shadow: 0 8rpx 18rpx rgba(18, 179, 168, .18) !important;
	}
</style>
