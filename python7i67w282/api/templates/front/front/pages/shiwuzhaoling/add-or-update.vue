<template>
<view class="content">
	<view :style='{"minHeight":"100%","width":"100%","padding":"0","position":"relative","background":"#fff","height":"auto"}'>
		<form :style='{"width":"100%","padding":"24rpx","background":"none","display":"block","height":"auto"}' class="app-update-pv">
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">标题</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.biaoti" v-model="ruleForm.biaoti" placeholder="标题"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">物品名称</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.wupinmingcheng" v-model="ruleForm.wupinmingcheng" placeholder="物品名称"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">物品类型</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.wupinleixing" v-model="ruleForm.wupinleixing" placeholder="物品类型"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="" @tap="tupianTap">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">图片</view>
				<image :style='{"width":"80rpx","borderRadius":"100%","objectFit":"cover","display":"block","height":"80rpx"}' class="avator" v-if="ruleForm.tupian" :src="baseUrl+ruleForm.tupian.split(',')[0]" mode="aspectFill"></image>
				<image :style='{"width":"80rpx","borderRadius":"100%","objectFit":"cover","display":"block","height":"80rpx"}' class="avator" v-else src="../../static/gen/upload.png" mode="aspectFill"></image>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">拾取地点</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.shiqudidian" v-model="ruleForm.shiqudidian" placeholder="拾取地点"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class=" select">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">状态</view>
				<picker :disabled="ro.zhuangtai" :style='{"width":"100%","flex":"1","height":"auto"}' @change="zhuangtaiChange" :value="zhuangtaiIndex" :range="zhuangtaiOptions">
					<view :style='{"width":"100%","lineHeight":"80rpx","fontSize":"28rpx","color":"#000"}' class="uni-input">{{ruleForm.zhuangtai?ruleForm.zhuangtai:"请选择状态"}}</view>
				</picker>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">账号</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.zhanghao" v-model="ruleForm.zhanghao" placeholder="账号"  type="text"></input>
			</view>
          
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#ccc","borderWidth":"0 0 2rpx 0","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"100%","lineHeight":"80rpx","fontSize":"28rpx","color":"#333","fontWeight":"500"}' class="title">物品详情</view>
				<xia-editor ref="wupinxiangqing" :style='{"minHeight":"300rpx","border":"2rpx solid #efefef","width":"100%","height":"auto"}' v-model="ruleForm.wupinxiangqing" placeholder="物品详情" @editorChange="wupinxiangqingChange"></xia-editor>
			</view>
			<view :style='{"padding":"20rpx","margin":"0 0 24rpx","border":"2rpx solid #DDE9F6","borderRadius":"12rpx","background":"#F7FBFF"}'>
				<view :style='{"fontSize":"30rpx","fontWeight":"600","color":"#1F4E79","margin":"0 0 12rpx"}'>AI 失物发布助手</view>
				<view :style='{"fontSize":"24rpx","lineHeight":"1.7","color":"#526579","margin":"0 0 16rpx"}'>自动生成招领标题、物品详情、核验问题和风险提示；模型不判断真实归属，认领仍需人工复核。</view>
				<button :loading="aiLoading" :disabled="aiLoading" :style='{"border":"none","padding":"0","margin":"0 0 16rpx","color":"#fff","borderRadius":"12rpx","background":"#1F7A8C","width":"100%","lineHeight":"72rpx","fontSize":"28rpx","height":"72rpx"}' @tap="onAiGenerateTap">AI 优化招领信息</button>
				<view v-if="aiResult" :style='{"fontSize":"24rpx","lineHeight":"1.7","color":"#34495E"}'>
					<view v-if="aiResult.verifyQuestions">核验问题：{{aiResult.verifyQuestions.join('；')}}</view>
					<view v-if="aiResult.moderation">风险：{{aiResult.moderation.summary}}</view>
					<view :style='{"color":"#7A4E00"}'>{{aiResult.modelBoundary}}</view>
				</view>
			</view>
			
			<view :style='{"width":"100%","flexWrap":"wrap","display":"flex","gap":"20rpx","height":"auto"}' class="btn" >
				<button :style='{"border":"none","padding":"0px","margin":"0 20rpx","color":"#fff","borderRadius":"20rpx","background":"linear-gradient( 135deg, #469CF5 0%, #25CCB4 100%)","width":"100%","lineHeight":"80rpx","fontSize":"32rpx","height":"80rpx"}' @tap="onSubmitTap" class="bg-red">提交</button>
			</view>
		</form>

	</view>
</view>
</template>

<script>
	import wPicker from "@/components/w-picker/w-picker.vue";
	import xiaEditor from '@/components/xia-editor/xia-editor';
	import multipleSelect from "@/components/momo-multipleSelect/momo-multipleSelect";
	export default {
		data() {
			return {
				cross:'',
				ruleForm: {
				biaoti: '',
				wupinmingcheng: '',
				wupinleixing: '',
				tupian: '',
				wupinxiangqing: '',
				shiqudidian: '',
					zhuangtai: '待认领' ,
				zhanghao: '',
				discussnum: '',
				storeupnum: '',
				},
				zhuangtaiOptions: [],
				zhuangtaiIndex: 0,
				// 登录用户信息
				user: {},
				ro:{
				   biaoti : false,
				   wupinmingcheng : false,
				   wupinleixing : false,
				   tupian : false,
				   wupinxiangqing : false,
				   shiqudidian : false,
				   zhuangtai : false,
				   zhanghao : false,
				   discussnum : false,
				   storeupnum : false,
				},
				virtualPay: false,
				aiLoading: false,
				aiResult: null,
			}
		},
		components: {
			wPicker,
			xiaEditor,
			multipleSelect,
		},
		computed: {
			baseUrl() {
				return this.$base.url;
			},



		},
		async onLoad(options) {
			if(options.virtualPay){
				this.virtualPay = true
			}
			let table = uni.getStorageSync("nowTable");
			// 获取用户信息
			let res = await this.$api.session(table);
			this.user = res.data;
			
			// ss读取
			this.ruleForm.zhanghao = this.user.zhanghao
			this.ro.zhanghao = true;

			this.ro.zhuangtai = true;

			// 自定义下拉框值
			this.zhuangtaiOptions = "已认领,待认领".split(',')

			// 如果有登录，获取登录后保存的userid
			this.ruleForm.userid = uni.getStorageSync("appUserid")
			if (options.refid) {
				// 如果上一级页面传递了refid，获取改refid数据信息
				this.ruleForm.refid = Number(options.refid);
				this.ruleForm.nickname = uni.getStorageSync("nickname");
			}
			// 如果是更新操作
			if (options.id) {
				this.ruleForm.id = options.id;
				// 获取信息
				res = await this.$api.info(`shiwuzhaoling`, this.ruleForm.id);
				this.ruleForm = res.data;
			}
			// 跨表
			this.cross = options.cross;
			if(options.cross){
				var obj = uni.getStorageSync('crossObj');
				for (var o in obj){
					if(o=='biaoti'){
						this.ruleForm.biaoti = obj[o];
						this.ro.biaoti = true;
						continue;
					}
					if(o=='wupinmingcheng'){
						this.ruleForm.wupinmingcheng = obj[o];
						this.ro.wupinmingcheng = true;
						continue;
					}
					if(o=='wupinleixing'){
						this.ruleForm.wupinleixing = obj[o];
						this.ro.wupinleixing = true;
						continue;
					}
					if(o=='tupian'){
						this.ruleForm.tupian = obj[o].split(",")[0];
						this.ro.tupian = true;
						continue;
					}
					if(o=='wupinxiangqing'){
						this.ruleForm.wupinxiangqing = obj[o];
						this.ro.wupinxiangqing = true;
						continue;
					}
					if(o=='shiqudidian'){
						this.ruleForm.shiqudidian = obj[o];
						this.ro.shiqudidian = true;
						continue;
					}
					if(o=='zhuangtai'){
						this.ruleForm.zhuangtai = obj[o];
						this.ro.zhuangtai = true;
						continue;
					}
					if(o=='zhanghao'){
						this.ruleForm.zhanghao = obj[o];
						this.ro.zhanghao = true;
						continue;
					}
					if(o=='discussnum'){
						this.ruleForm.discussnum = obj[o];
						this.ro.discussnum = true;
						continue;
					}
					if(o=='storeupnum'){
						this.ruleForm.storeupnum = obj[o];
						this.ro.storeupnum = true;
						continue;
					}
				}
			}
			this.styleChange()
			this.$forceUpdate()
			if (uni.getStorageSync('raffleType') && uni.getStorageSync('raffleType') != null) {
				uni.removeStorageSync('raffleType')
				setTimeout(() => {
					this.onSubmitTap()
				}, 300)
			}
		},
		methods: {
			wupinxiangqingChange(e) {
				this.ruleForm.wupinxiangqing = e
			},
			async onAiGenerateTap() {
				this.aiLoading = true
				try {
					let res = await this.$api.aiGenerateListing(Object.assign({scene: 'lostfound'}, this.ruleForm))
					this.aiResult = res.data
					if(!this.ruleForm.biaoti && res.data.title){
						this.ruleForm.biaoti = res.data.title
					}
					if(!this.ruleForm.wupinleixing && res.data.category){
						this.ruleForm.wupinleixing = res.data.category
					}
					if(!this.ruleForm.wupinxiangqing && res.data.description){
						this.ruleForm.wupinxiangqing = res.data.description
					}
					this.$utils.msg('AI 已生成招领草稿，请确认后提交')
				} catch(e) {
					this.$utils.msg('AI 失物助手暂不可用，请继续手动填写')
				}
				this.aiLoading = false
			},
			styleChange() {
				this.$nextTick(()=>{
					// document.querySelectorAll('.app-update-pv . .uni-input-input').forEach(el=>{
					//   el.style.backgroundColor = this.addUpdateForm.input.content.backgroundColor
					// })
				})
			},

			// 多级联动参数



			// 下拉变化
			zhuangtaiChange(e) {
				this.zhuangtaiIndex = e.target.value
				this.ruleForm.zhuangtai = this.zhuangtaiOptions[this.zhuangtaiIndex]
			},

			tupianTap() {
				let _this = this;
				this.$api.upload(function(res) {
					_this.ruleForm.tupian = 'upload/' + res.file;
					_this.tupianbaiduAdvancedGeneral(res.file);
					_this.$forceUpdate();
					_this.$nextTick(()=>{
						_this.styleChange()
					})
				});
			},
			async tupianbaiduAdvancedGeneral(fileName) {
				let res = await this.$api.baiduIdentify(`shiwuzhaoling`, 'advancedGeneral', fileName);
				this.ruleForm.wupinmingcheng = res.data.keyword;
			},

			getUUID () {
				return new Date().getTime();
			},
			async onSubmitTap() {
				let that = this
				//跨表计算判断
				var obj;
				if((!this.ruleForm.biaoti)){
					this.$utils.msg(`标题不能为空`);
					return
				}
				if((!this.ruleForm.wupinmingcheng)){
					this.$utils.msg(`物品名称不能为空`);
					return
				}
				if((!this.ruleForm.wupinleixing)){
					this.$utils.msg(`物品类型不能为空`);
					return
				}
				if((!this.ruleForm.zhuangtai)){
					this.$utils.msg(`状态不能为空`);
					return
				}
				if(this.ruleForm.discussnum&&(!this.$validate.isIntNumer(this.ruleForm.discussnum))){
					this.$utils.msg(`评论数应输入整数`);
					return
				}
				if(this.ruleForm.storeupnum&&(!this.$validate.isIntNumer(this.ruleForm.storeupnum))){
					this.$utils.msg(`收藏数应输入整数`);
					return
				}
				//更新跨表属性
				var crossuserid;
				var crossrefid;
				var crossoptnum;
				if(this.cross){
					uni.setStorageSync('crossCleanType',true);
					var statusColumnName = uni.getStorageSync('statusColumnName');
					var statusColumnValue = uni.getStorageSync('statusColumnValue');
					if(statusColumnName!='') {
						if(!obj) {
							obj = uni.getStorageSync('crossObj');
						}
						if(!statusColumnName.startsWith("[")) {
							for (var o in obj){
								if(o==statusColumnName){
									obj[o] = statusColumnValue;
								}

							}
							var table = uni.getStorageSync('crossTable');
							await this.$api.update(`${table}`, obj);
						} else {
							   crossuserid=Number(uni.getStorageSync('appUserid'));
							   crossrefid=obj['id'];
							   crossoptnum=uni.getStorageSync('statusColumnName');
							   crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
						}
					}
				}
				if(crossrefid && crossuserid) {
					this.ruleForm.crossuserid=crossuserid;
					this.ruleForm.crossrefid=crossrefid;
					let params = {
						page: 1,
						limit:10,
						crossuserid:crossuserid,
						crossrefid:crossrefid,
					}
					let res = await this.$api.list(`shiwuzhaoling`, params);
					if (res.data.total >= crossoptnum) {
						this.$utils.msg(uni.getStorageSync('tips'));
						uni.removeStorageSync('crossCleanType');
						return false;
					} else {
				//跨表计算
						let oet = {}
						if(this.ruleForm.id){
							await this.$api.update(`shiwuzhaoling`, this.ruleForm);
						}else{
							oet = await this.$api.add(`shiwuzhaoling`, this.ruleForm);
						}

						this.$utils.msgBack('提交成功');
					}
				} else {
				//跨表计算
					let oet = {}
					if(this.ruleForm.id){
						await this.$api.update(`shiwuzhaoling`, this.ruleForm);
					}else{
						oet = await this.$api.add(`shiwuzhaoling`, this.ruleForm);
					}

					this.$utils.msgBack('提交成功');
				}
			},
			optionsChange(e) {
				this.index = e.target.value
			},
			bindDateChange(e) {
				this.date = e.target.value
			},
			getDate(type) {
				const date = new Date();
				let year = date.getFullYear();
				let month = date.getMonth() + 1;
				let day = date.getDate();
				if (type === 'start') {
					year = year - 60;
				} else if (type === 'end') {
					year = year + 2;
				}
				month = month > 9 ? month : '0' + month;;
				day = day > 9 ? day : '0' + day;
				return `${year}-${month}-${day}`;
			},
			toggleTab(str) {
				if(this.ro[str]){
					return false
				}
				this.$refs[str].show();
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
	.app-update-pv {
		padding: 24rpx !important;
		border-radius: 18rpx !important;
		background: #fff !important;
		box-shadow: 0 10rpx 30rpx rgba(24, 35, 47, .07) !important;
	}
	.app-update-pv > view {
		margin-bottom: 18rpx !important;
		padding: 8rpx 0 16rpx !important;
		border-color: #edf2f5 !important;
		align-items: flex-start !important;
	}
	.title {
		width: 168rpx !important;
		text-align: left !important;
		color: #44515d !important;
		font-size: 27rpx !important;
	}
	input,
	.uni-input,
	textarea {
		min-height: 76rpx !important;
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
		border-radius: 14rpx !important;
		background: #12b3a8 !important;
		box-shadow: 0 8rpx 18rpx rgba(18, 179, 168, .18) !important;
	}
</style>
