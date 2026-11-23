<template>
<view class="content">
	<view :style='{"minHeight":"100%","width":"100%","padding":"0","position":"relative","background":"#fff","height":"auto"}'>
		<form :style='{"width":"100%","padding":"24rpx","background":"none","display":"block","height":"auto"}' class="app-update-pv">
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">商品名称</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.shangpinmingcheng" v-model="ruleForm.shangpinmingcheng" placeholder="商品名称"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class=" select">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">商品类型</view>
				<picker :disabled="ro.shangpinleixing" :style='{"width":"100%","flex":"1","height":"auto"}' @change="shangpinleixingChange" :value="shangpinleixingIndex" :range="shangpinleixingOptions">
					<view :style='{"width":"100%","lineHeight":"80rpx","fontSize":"28rpx","color":"#000"}' class="uni-input">{{ruleForm.shangpinleixing?ruleForm.shangpinleixing:"请选择商品类型"}}</view>
				</picker>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">品牌</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.pinpai" v-model="ruleForm.pinpai" placeholder="品牌"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">规格</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.guige" v-model="ruleForm.guige" placeholder="规格"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">价格</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.jiage" v-model.number="ruleForm.jiage" placeholder="价格" type="number"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">数量</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.shuliang" v-model.number="ruleForm.shuliang" placeholder="数量" type="number"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="" @tap="tupianTap">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">图片</view>
				<image :style='{"width":"80rpx","borderRadius":"100%","objectFit":"cover","display":"block","height":"80rpx"}' class="avator" v-if="ruleForm.tupian" :src="baseUrl+ruleForm.tupian.split(',')[0]" mode="aspectFill"></image>
				<image :style='{"width":"80rpx","borderRadius":"100%","objectFit":"cover","display":"block","height":"80rpx"}' class="avator" v-else src="../../static/gen/upload.png" mode="aspectFill"></image>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">账号</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.zhanghao" v-model="ruleForm.zhanghao" placeholder="账号"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">交易地址</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.jiaoyidizhi" v-model="ruleForm.jiaoyidizhi" placeholder="交易地址"  type="text"></input>
			</view>
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#7D7D7D","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"160rpx","padding":"0 20rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#6683A2","textAlign":"right"}' class="title">手机</view>
				<input :style='{"border":"none","padding":"0px 24rpx","margin":"0px","color":"rgb(0, 0, 0)","borderRadius":"40rpx","flex":"1","background":"rgba(255, 255, 255, 0)","fontSize":"28rpx","height":"80rpx"}' :disabled="ro.shouji" v-model="ruleForm.shouji" placeholder="手机"  type="text"></input>
			</view>
                
			<view :style='{"padding":"12rpx 0","margin":"0 0 24rpx 0","borderColor":"#ccc","borderWidth":"0 0 2rpx 0","width":"100%","borderStyle":"solid","height":"auto"}' class="">
				<view :style='{"width":"100%","lineHeight":"80rpx","fontSize":"28rpx","color":"#333","fontWeight":"500"}' class="title">描述</view>
				<xia-editor ref="miaoshu" :style='{"minHeight":"300rpx","border":"2rpx solid #efefef","width":"100%","height":"auto"}' v-model="ruleForm.miaoshu" placeholder="描述" @editorChange="miaoshuChange"></xia-editor>
			</view>
			<view :style='{"padding":"20rpx","margin":"0 0 24rpx","border":"2rpx solid #DDE9F6","borderRadius":"12rpx","background":"#F7FBFF"}'>
				<view :style='{"fontSize":"30rpx","fontWeight":"600","color":"#1F4E79","margin":"0 0 12rpx"}'>AI 发布助手</view>
				<view :style='{"fontSize":"24rpx","lineHeight":"1.7","color":"#526579","margin":"0 0 16rpx"}'>根据已填写内容生成标题、分类、描述、参考价和交易风险提示，结果需人工确认后再提交。</view>
				<button :loading="aiLoading" :disabled="aiLoading" :style='{"border":"none","padding":"0","margin":"0 0 16rpx","color":"#fff","borderRadius":"12rpx","background":"#1F7A8C","width":"100%","lineHeight":"72rpx","fontSize":"28rpx","height":"72rpx"}' @tap="onAiGenerateTap">AI 优化发布信息</button>
				<view v-if="aiResult" :style='{"fontSize":"24rpx","lineHeight":"1.7","color":"#34495E"}'>
					<view v-if="aiResult.priceSuggestion">参考价：{{aiResult.priceSuggestion.min}}-{{aiResult.priceSuggestion.max}} 元</view>
					<view v-if="aiResult.moderation">风险：{{aiResult.moderation.summary}}</view>
					<view v-if="aiResult.tradeTips">提示：{{aiResult.tradeTips.join('；')}}</view>
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
				shangpinmingcheng: '',
				shangpinleixing: '',
				pinpai: '',
				guige: '',
				jiage: '',
				shuliang: '',
				tupian: '',
				miaoshu: '',
				zhanghao: '',
				jiaoyidizhi: '',
				shouji: '',
				discussnum: '',
				storeupnum: '',
				},
				shangpinleixingOptions: [],
				shangpinleixingIndex: 0,
				// 登录用户信息
				user: {},
				ro:{
				   shangpinmingcheng : false,
				   shangpinleixing : false,
				   pinpai : false,
				   guige : false,
				   jiage : false,
				   shuliang : false,
				   tupian : false,
				   miaoshu : false,
				   zhanghao : false,
				   jiaoyidizhi : false,
				   shouji : false,
				   thumbsupnum : false,
				   crazilynum : false,
				   clicknum : false,
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
			this.ruleForm.shouji = this.user.shouji
			this.ro.shouji = true;


			// 下拉框
			await this.loadShangpinleixingOptions();

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
				res = await this.$api.info(`ershouliuzhuan`, this.ruleForm.id);
				this.ruleForm = res.data;
			}
			// 跨表
			this.cross = options.cross;
			if(options.cross){
				var obj = uni.getStorageSync('crossObj');
				for (var o in obj){
					if(o=='shangpinmingcheng'){
						this.ruleForm.shangpinmingcheng = obj[o];
						this.ro.shangpinmingcheng = true;
						continue;
					}
					if(o=='shangpinleixing'){
						this.ruleForm.shangpinleixing = obj[o];
						this.ro.shangpinleixing = true;
						continue;
					}
					if(o=='pinpai'){
						this.ruleForm.pinpai = obj[o];
						this.ro.pinpai = true;
						continue;
					}
					if(o=='guige'){
						this.ruleForm.guige = obj[o];
						this.ro.guige = true;
						continue;
					}
					if(o=='jiage'){
						this.ruleForm.jiage = obj[o];
						this.ro.jiage = true;
						continue;
					}
					if(o=='shuliang'){
						this.ruleForm.shuliang = obj[o];
						this.ro.shuliang = true;
						continue;
					}
					if(o=='tupian'){
						this.ruleForm.tupian = obj[o].split(",")[0];
						this.ro.tupian = true;
						continue;
					}
					if(o=='miaoshu'){
						this.ruleForm.miaoshu = obj[o];
						this.ro.miaoshu = true;
						continue;
					}
					if(o=='zhanghao'){
						this.ruleForm.zhanghao = obj[o];
						this.ro.zhanghao = true;
						continue;
					}
					if(o=='jiaoyidizhi'){
						this.ruleForm.jiaoyidizhi = obj[o];
						this.ro.jiaoyidizhi = true;
						continue;
					}
					if(o=='shouji'){
						this.ruleForm.shouji = obj[o];
						this.ro.shouji = true;
						continue;
					}
					if(o=='thumbsupnum'){
						this.ruleForm.thumbsupnum = obj[o];
						this.ro.thumbsupnum = true;
						continue;
					}
					if(o=='crazilynum'){
						this.ruleForm.crazilynum = obj[o];
						this.ro.crazilynum = true;
						continue;
					}
					if(o=='clicknum'){
						this.ruleForm.clicknum = obj[o];
						this.ro.clicknum = true;
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
			miaoshuChange(e) {
				this.ruleForm.miaoshu = e
			},
			async onAiGenerateTap() {
				this.aiLoading = true
				try {
					let res = await this.$api.aiGenerateListing(Object.assign({scene: 'secondhand'}, this.ruleForm))
					this.aiResult = res.data
					if(!this.ruleForm.shangpinmingcheng && res.data.title){
						this.ruleForm.shangpinmingcheng = res.data.title
					}
					if((!this.ruleForm.shangpinleixing || this.ruleForm.shangpinleixing == '请选择商品类型') && res.data.category){
						this.ruleForm.shangpinleixing = res.data.category
					}
					if(!this.ruleForm.miaoshu && res.data.description){
						this.ruleForm.miaoshu = res.data.description
					}
					if(!this.ruleForm.jiage && res.data.priceSuggestion){
						this.ruleForm.jiage = res.data.priceSuggestion.min
					}
					this.$utils.msg('AI 已生成草稿，请确认后提交')
				} catch(e) {
					this.$utils.msg('AI 发布助手暂不可用，请继续手动填写')
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
			normalizeShangpinleixingOptions(data) {
				let list = Array.isArray(data) ? data : []
				return list.map(item => {
					if (typeof item === 'string') return item
					if (item && item.shangpinleixing) return item.shangpinleixing
					return ''
				}).filter(item => item)
			},
			async loadShangpinleixingOptions() {
				let options = []
				try {
					let res = await this.$api.list(`shangpinleixing`, {page: 1, limit: 100})
					options = this.normalizeShangpinleixingOptions(res.data && res.data.list)
				} catch (e) {
					options = []
				}
				if (!options.length) {
					try {
						let res = await this.$api.option(`shangpinleixing`,`shangpinleixing`,{})
						options = this.normalizeShangpinleixingOptions(res.data)
					} catch (e) {
						options = []
					}
				}
				if (!options.length) {
					options = ['数码设备', '学习资料', '宿舍用品', '运动出行', '其他']
				}
				this.shangpinleixingOptions = ['请选择商品类型', ...options]
			},
			shangpinleixingChange(e) {
				this.shangpinleixingIndex = Number(e.detail ? e.detail.value : e.target.value)
				this.ruleForm.shangpinleixing = this.shangpinleixingIndex === 0 ? '' : this.shangpinleixingOptions[this.shangpinleixingIndex]
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
				let res = await this.$api.baiduIdentify(`ershouliuzhuan`, 'advancedGeneral', fileName);
				this.ruleForm.shangpinmingcheng = res.data.keyword;
			},

			getUUID () {
				return new Date().getTime();
			},
			async onSubmitTap() {
				let that = this
				//跨表计算判断
				var obj;
				if((!this.ruleForm.shangpinmingcheng)){
					this.$utils.msg(`商品名称不能为空`);
					return
				}
				if((!this.ruleForm.shangpinleixing || this.ruleForm.shangpinleixing == '请选择商品类型')){
					this.$utils.msg(`商品类型不能为空`);
					return
				}
				if((!this.ruleForm.pinpai)){
					this.$utils.msg(`品牌不能为空`);
					return
				}
				if((!this.ruleForm.guige)){
					this.$utils.msg(`规格不能为空`);
					return
				}
				if((!this.ruleForm.jiage)){
					this.$utils.msg(`价格不能为空`);
					return
				}
				if(this.ruleForm.jiage&&(!this.$validate.isIntNumer(this.ruleForm.jiage))){
					this.$utils.msg(`价格应输入整数`);
					return
				}
				if((!this.ruleForm.shuliang)){
					this.$utils.msg(`数量不能为空`);
					return
				}
				if(this.ruleForm.shuliang&&(!this.$validate.isIntNumer(this.ruleForm.shuliang))){
					this.$utils.msg(`数量应输入整数`);
					return
				}
				if((!this.ruleForm.miaoshu)){
					this.$utils.msg(`描述不能为空`);
					return
				}
				if((!this.ruleForm.jiaoyidizhi)){
					this.$utils.msg(`交易地址不能为空`);
					return
				}
				if(this.ruleForm.shouji&&(!this.$validate.isMobile(this.ruleForm.shouji))){
					this.$utils.msg(`手机应输入手机格式`);
					return
				}
				if(this.ruleForm.thumbsupnum&&(!this.$validate.isIntNumer(this.ruleForm.thumbsupnum))){
					this.$utils.msg(`赞应输入整数`);
					return
				}
				if(this.ruleForm.crazilynum&&(!this.$validate.isIntNumer(this.ruleForm.crazilynum))){
					this.$utils.msg(`踩应输入整数`);
					return
				}
				if(this.ruleForm.clicknum&&(!this.$validate.isIntNumer(this.ruleForm.clicknum))){
					this.$utils.msg(`点击次数应输入整数`);
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
					let res = await this.$api.list(`ershouliuzhuan`, params);
					if (res.data.total >= crossoptnum) {
						this.$utils.msg(uni.getStorageSync('tips'));
						uni.removeStorageSync('crossCleanType');
						return false;
					} else {
				//跨表计算
						let oet = {}
						if(this.ruleForm.id){
							await this.$api.update(`ershouliuzhuan`, this.ruleForm);
						}else{
							oet = await this.$api.add(`ershouliuzhuan`, this.ruleForm);
						}

						this.$utils.msgBack('提交成功');
					}
				} else {
				//跨表计算
					let oet = {}
					if(this.ruleForm.id){
						await this.$api.update(`ershouliuzhuan`, this.ruleForm);
					}else{
						oet = await this.$api.add(`ershouliuzhuan`, this.ruleForm);
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
