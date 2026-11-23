<template>
	<view :style='{"minHeight":"100%","width":"100%","padding":"24rpx","position":"relative","background":"#F9FAFA","height":"auto"}'>
		<view class="title" :style='{"lineHeight":"1.5","fontSize":"32rpx","color":"#000000","textAlign":"center","fontWeight":"600"}'>{{detail.title}}</view>
		
		<view :style='{"padding":"0 0 12rpx 0","borderColor":"#C4C4C4","alignItems":"center","borderWidth":"0 0 2rpx 0","display":"flex","width":"100%","borderStyle":"solid","justifyContent":"center"}'>
		  <view :style='{"padding":"0"}'>
		    <text class="icon iconfont icon-shijian21" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
		    <text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>发布时间：{{detail.addtime}}</text>
		  </view>
		  <view :style='{"padding":"0"}'>
		    <text class="icon iconfont icon-geren16" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
		    <text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{detail.name}}</text>
		  </view>
		  <view :style='{"padding":"0"}'>
		    <text class="icon iconfont icon-zan10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
		    <text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{detail.thumbsupnum}}</text>
		  </view>
		  <view :style='{"padding":"0"}'>
		    <text class="icon iconfont icon-shoucang10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
		    <text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{detail.storeupnum}}</text>
		  </view>
		  <view :style='{"padding":"0"}'>
		    <text class="icon iconfont icon-chakan9" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
		    <text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{detail.clicknum}}</text>
		  </view>
		</view>
		
		<view :style='{"margin":"20rpx 0 0","justifyContent":"space-between","display":"flex"}'>
		  <view :style='{"padding":"4rpx 60rpx","borderRadius":"10rpx","color":"#fff","background":"linear-gradient( 90deg, #2BC8BA 0%, #459FEF 100%)","display":"flex"}' @click="likeClick">
		    <text class="icon iconfont" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"28rpx","color":"inherit"}' :class="likeType?'icon-zan10':'icon-zan10'"></text>
		    <text :style='{"color":"inherit","lineHeight":"1.5","fontSize":"28rpx"}'>{{likeType?'已':''}}赞</text>
		  </view>
		  <view :style='{"padding":"4rpx 40rpx","borderRadius":"10rpx","color":"#8F8F8F","background":"#D7F0EE","display":"flex"}' @click="collectClick">
		    <text class="icon iconfont" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"28rpx","color":"inherit"}' :class="collectType?'icon-shoucang10':'icon-shoucang10'"></text>
		    <text :style='{"color":"inherit","lineHeight":"1.5","fontSize":"28rpx"}'>{{collectType?'已':''}}收藏</text>
		  </view>
		</view>
		
		<view class="content" :style='{"width":"100%","height":"auto"}'>
			<rich-text :nodes="detail.content"></rich-text>
		</view>
		
		<div :style='{"width":"100%","padding":"0 40rpx","justifyContent":"center","display":"flex","height":"auto"}'>
		  <div @click="prepDetailClick" :style='{"padding":"0 20rpx","lineHeight":"66rpx","fontSize":"28rpx","color":"#fff","background":"linear-gradient( 90deg, #2BC8BA 0%, #459FEF 100%)"}'>上一篇：prev</div>
		  <div @click="nextDetailClick" :style='{"padding":"0 20rpx","lineHeight":"66rpx","fontSize":"28rpx","color":"#8F8F8F","background":"#D7F0EE"}'>下一篇：next</div>
		</div>
		
		<view class="time-content" :style='{"width":"100%","padding":"0 0 20rpx","margin":"24rpx 0 0 0","background":"#fff","height":"auto"}'>
			<view class="comoment-header" :style='{"width":"100%","boxShadow":"rgb(0 0 0 / 30%) 0px 2rpx 12rpx","justifyContent":"space-between","display":"flex","height":"auto"}'>
				<view :style='{"padding":"0 24rpx","lineHeight":"80rpx","fontSize":"28rpx","color":"#333"}'>评论</view>
				<view :style='{"padding":"0 20rpx","background":"linear-gradient( 316deg, #2BC8BA 0%, #459FEF 99%)","display":"flex"}' @click="onCommentTap" class="btn-comment-content" style="display: flex;align-items: center;">
					<text class="icon iconfont icon-tianjia14" :style='{"margin":"0 8rpx 0 0","lineHeight":"80rpx","fontSize":"28rpx","color":"#fff"}'></text>
					<text :style='{"color":"#fff","lineHeight":"80rpx","fontSize":"28rpx"}'>添加评论</text>
				</view>
			</view>
			<view :style='{"border":"2rpx solid #2BC8BA","boxShadow":"none","padding":"24rpx","margin":"24rpx 0 0 0","borderRadius":"10rpx","background":"#fff","width":"100%","height":"auto"}' v-for="(item,index) in commentList" v-bind:key="index" class="cu-item comment-item">
				<view :style='{"width":"100%","display":"flex","height":"auto"}'>
					<image :style='{"width":"60rpx","margin":"0 8rpx 0 0","borderRadius":"100%","display":"block","height":"60rpx"}' v-if="item.avatarurl" mode="aspectFill" :src="avator"></image>
					<view :style='{"color":"#333","lineHeight":"60rpx","fontSize":"28rpx"}' class="text-grey">某同学_{{item.userid.toString().slice(-4)}}</view>
				</view>
				<view :style='{"margin":"8rpx 0","lineHeight":"1.5","fontSize":"28rpx","color":"#666"}' v-html="item.content"></view>
				<view :style='{"color":"#999","lineHeight":"24rpx","fontSize":"24rpx"}'>{{item.addtime}}</view>
				<view v-if="item.reply" :style='{"margin":"8rpx 0","lineHeight":"1.5","fontSize":"28rpx","color":"#666"}' class="text-gray text-content text-df">
					回复:<view v-html="item.reply"></view>
				</view>
				<view style="display: flex;display: flex;justify-content: flex-end;padding: 6rpx 0;" v-if="userid==item.userid">
					<view style="color: #999;font-size: 16rpx;" @click="delClick(item.id)">删除</view>
				</view>
			</view>
		</view>

		<!-- 热门 -->
		<view class="hot" :style='{"width":"100%","padding":"0 0 40rpx 0","margin":"40rpx 0 0","background":"none","height":"auto"}'>
		  <view :style='{"padding":"8rpx 0 0","margin":"0","color":"#fff","background":"url(http://codegen.caihongy.cn/20250219/f42cc2e72e884f0ab71bbf038eb06c49.png) no-repeat center / 100% 100%","display":"flex","width":"100%","fontSize":"32rpx","position":"relative","justifyContent":"center","fontWeight":"600","height":"136rpx"}'>热门信息</view>
		  <view :style='{"padding":"0","margin":"40rpx 0 0","flexWrap":"wrap","background":"none","display":"flex","gap":"20rpx","width":"100%","justifyContent":"space-between","height":"auto"}'>
		    <view v-for="(item,index) in hotList" :key="index" :style='{"border":"none","padding":"20rpx","alignItems":"center","background":"#F5FFFF","flexDirection":"column","display":"flex","width":"48%","position":"relative","justifyContent":"center","height":"auto"}' @click="toDetail(item.id)">
			  <image :style='{"width":"100%","objectFit":"cover","borderRadius":"20rpx","display":"block","height":"160rpx"}' mode="aspectFill" :src="baseUrl + item.picture"></image>
		      <view :style='{"padding":"0","overflow":"hidden","whiteSpace":"nowrap","color":"#010F33","maxHeight":"80rpx","textAlign":"center","width":"100%","lineHeight":"40rpx","fontSize":"28rpx","textOverflow":"ellipsis"}'>{{ item.title }}</view>
		      <view :style='{"padding":"12rpx","lineHeight":"24rpx","fontSize":"24rpx","color":"#000","textAlign":"center","background":"none"}'>{{ item.addtime }}</view>
		    </view>
		  </view>
		</view>
		<!-- 推荐 -->
		<view class="recommend" :style='{"width":"100%","padding":"0 0 40rpx 0","margin":"40rpx 0 0","background":"none","height":"auto"}'>
		  <view :style='{"padding":"8rpx 0 0","margin":"0","color":"#fff","background":"url(http://codegen.caihongy.cn/20250219/f42cc2e72e884f0ab71bbf038eb06c49.png) no-repeat center / 100% 100%","display":"flex","width":"100%","fontSize":"32rpx","position":"relative","justifyContent":"center","fontWeight":"600","height":"136rpx"}'>推荐信息</view>
		  <view :style='{"padding":"0","margin":"40rpx 0 0","flexWrap":"wrap","background":"none","display":"flex","gap":"20rpx","width":"100%","justifyContent":"space-between","height":"auto"}'>
		    <view v-for="(item,index) in recommendList" :key="index" :style='{"border":"none","padding":"20rpx","alignItems":"center","background":"#F5FFFF","flexDirection":"column","display":"flex","width":"48%","position":"relative","justifyContent":"center","height":"auto"}' @click="toDetail(item.id)">
		      <image :style='{"width":"100%","objectFit":"cover","borderRadius":"20rpx","display":"block","height":"160rpx"}' mode="aspectFill" :src="baseUrl + item.picture"></image>
			  <view :style='{"padding":"0","overflow":"hidden","whiteSpace":"nowrap","color":"#010F33","maxHeight":"80rpx","textAlign":"center","width":"100%","lineHeight":"40rpx","fontSize":"28rpx","textOverflow":"ellipsis"}'>{{ item.title }}</view>
		      <view :style='{"padding":"12rpx","lineHeight":"24rpx","fontSize":"24rpx","color":"#000","textAlign":"center","background":"none"}'>{{ item.addtime }}</view>
		    </view>
		  </view>
		</view>

	</view>
</template>
<script>
	import avator from '@/static/avator.jpeg'
	export default {
		
		data() {
			return {
				detail: {},
				id: '',
				likeType: false,
				likeForm: {},
				collectType: false,
				collectForm: {},
				commentList: [],
				page: 1,
				allList: [],
				currentIndex: 0,
				hotList: [],
				recommendList: [],
				// lwn
				avator,
			}
		},
		async onLoad(options) {
			this.id = options.id;
			this.getInfo()
			
			this.getHotList()
			this.getRecommendList()
		},
		onShow() {
			let cleanType = uni.getStorageSync('discussnewsCleanType')
			if(cleanType){
				uni.removeStorageSync('discussnewsCleanType')
				this.page = 1
				this.commentList = []
				this.getCommentList()
			}
		},
		onReachBottom() {
			this.page++
			this.getCommentList()
		},
		computed:{
			baseUrl() {
				return this.$base.url;
			},
			userid(){
				return uni.getStorageSync('appUserid')
			}
		},
		methods: {
			async getInfo(){
				let res = await this.$api.info('news', this.id)
				res.data.content = res.data.content.replace(/<img/g,'<img style="width: 100%;"');
				this.detail = res.data;
				uni.pageScrollTo({
					scrollTop: 0,
					duration: 100,
				})
				this.getLike()
				this.getCollect()
				this.getCommentList()
				res = await this.$api.list('news',{page:1,limit:100,sort:'addtime',order:'desc'})
				for(let x in res.data.list){
					if(res.data.list[x].id == this.id){
						this.currentIndex = Number(x)
						break
					}
				}
				this.allList = res.data.list
				
			},
			// 获取点赞状态
			async getLike() {
				let res = await this.$api.list('storeup', {
					page: 1,
					limit: 1,
					type: '21',
					userid: uni.getStorageSync('appUserid'),
					refid: this.id,
					tablename: 'news'
				})
				if (res.data.list.length) {
					this.likeType = true
					this.likeForm = res.data.list[0]
				} else {
					this.likeType = false
					this.likeForm = {}
				}
			},
			// 获取热门列表
			async getHotList(){
				let res = await this.$api.recommend('news',{page:1, limit: 4,sort:'addtime',order:'desc'})
				this.hotList = res.data.list;
			},
			// 获取推荐列表	
			async getRecommendList(){
				let res;
				if(uni.getStorageSync("appUserid")){
					res = await this.$api.recommend2('news',{page:1, limit: 4,sort:'addtime',order:'desc'})
				}else{
					res = await this.$api.recommend('news',{page:1, limit: 4,sort:'addtime',order:'desc'})
				}
				
				this.recommendList = res.data.list;
			},
			// 上一篇
			prepDetailClick(){
				if(this.currentIndex == 0){
					this.$utils.msg('已经是第一篇了')
					return false
				}
				this.currentIndex--
				this.id = this.allList[this.currentIndex].id
				this.page = 1
				this.getInfo()
			},
			// 下一篇
			nextDetailClick(){
				if(this.currentIndex == this.allList.length - 1){
					this.$utils.msg('已经是最后一篇了')
					return false
				}
				this.currentIndex++
				this.id = this.allList[this.currentIndex].id
				this.page = 1
				this.getInfo()
			},
			toDetail(id){
				this.id = id
				this.getInfo()
			},
			// 获取收藏状态
			async getCollect() {
				let res = await this.$api.list('storeup', {
					page: 1,
					limit: 1,
					type: '1',
					userid: uni.getStorageSync('appUserid'),
					refid: this.id,
					tablename: 'news'
				})
				if (res.data.list.length) {
					this.collectType = true
					this.collectForm = res.data.list[0]
				} else {
					this.collectType = false
					this.collectForm = {}
				}
			},
			// 点赞按钮
			async likeClick() {
				let that = this
				if(!uni.getStorageSync('appUserid')){
					this.$utils.msg("请先登录")
					setTimeout(()=>{
						that.$utils.jump('../login/login')
					},1500)
					return false
				}
				if(!this.$utils.requireVerified()){
					return false
				}
				if (this.likeType) {
					uni.showModal({
						title: '提示',
						content: '是否取消点赞？',
						async success(res) {
							if (res.confirm) {
								await that.$api.del('storeup', JSON.stringify([that.likeForm.id]))
								that.$utils.msg('取消成功')
								that.detail.thumbsupnum--
								await that.$api.update('news', that.detail)
								that.getLike()
							}
						}
					})
				} else {
					await that.$api.add('storeup', {
						userid: uni.getStorageSync('appUserid'),
						refid: this.id,
						type: '21',
						name: this.detail.title,
						picture: this.detail.picture,
						tablename: 'news',
					})
					this.$utils.msg('点赞成功')
					that.detail.thumbsupnum++
					await that.$api.update('news', that.detail)
					this.getLike()
				}
			},
			// 收藏按钮
			async collectClick() {
				let that = this
				if(!uni.getStorageSync('appUserid')){
					this.$utils.msg("请先登录")
					setTimeout(()=>{
						that.$utils.jump('../login/login')
					},1500)
					return false
				}
				if(!this.$utils.requireVerified()){
					return false
				}
				if (this.collectType) {
					uni.showModal({
						title: '提示',
						content: '是否取消收藏？',
						async success(res) {
							if (res.confirm) {
								await that.$api.del('storeup', JSON.stringify([that.collectForm.id]))
								that.$utils.msg('取消成功')
								that.detail.storeupnum--
								await that.$api.update('news', that.detail)
								that.getCollect()
							}
						}
					})
				} else {
					await that.$api.add('storeup', {
						userid: uni.getStorageSync('appUserid'),
						refid: this.id,
						type: '1',
						name: this.detail.title,
						picture: this.detail.picture,
						tablename: 'news',
					})
					this.$utils.msg('收藏成功')
					that.detail.storeupnum++
					await that.$api.update('news', that.detail)
					this.getCollect()
				}
			},
			// 获取评论列表
			async getCommentList() {
				if(this.page == 1){
					this.commentList = []
				}
				let res = await this.$api.list('discussnews', {
					page: this.page,
					limit: 10,
					refid: this.id
				});
				if(res.data.list.length==0){
					this.page--
				}
				this.commentList = this.commentList.concat(res.data.list)
			},
			// 跳转新增评论
			async onCommentTap() {
				let that = this
				if(!uni.getStorageSync('appUserid')){
					this.$utils.msg("请先登录")
					setTimeout(()=>{
						that.$utils.jump('../login/login')
					},1500)
					return false
				}
				if(!this.$utils.requireVerified()){
					return false
				}
				this.$utils.jump(`../discussnews/add-or-update?refid=${this.id}`)
			},
			// 删除当前评论
			delClick(id) {
				let that = this
				uni.showModal({
					title: '提示',
					content: '是否删除此评论？',
					async success(res) {
						if (res.confirm) {
							await that.$api.del('discussnews', JSON.stringify([id]))
							that.$utils.msg('删除成功')
							setTimeout(() => {
								that.page = 1
								that.commentList = []
								that.getCommentList()
							}, 1500)
						}
					}
				})
			},
		}
	}
</script>

<style scoped lang="scss">
	page {
		background: #f6f8fa;
	}
	.title {
		padding: 20rpx 8rpx 12rpx !important;
		line-height: 44rpx !important;
		font-size: 36rpx !important;
		color: #12202b !important;
		text-align: left !important;
		font-weight: 700 !important;
	}
	.content {
		margin-top: 24rpx !important;
		padding: 24rpx !important;
		border-radius: 18rpx !important;
		background: #fff !important;
		box-shadow: 0 10rpx 30rpx rgba(24, 35, 47, .06) !important;
		line-height: 48rpx !important;
		color: #26323d !important;
	}
	.time-content,
	.hot,
	.recommend {
		border-radius: 18rpx !important;
		background: #fff !important;
		box-shadow: 0 10rpx 30rpx rgba(24, 35, 47, .06) !important;
		overflow: hidden !important;
	}
	.comoment-header {
		box-shadow: none !important;
		border-bottom: 1rpx solid #edf2f5 !important;
	}
	.comment-item {
		border: 1rpx solid #edf2f5 !important;
		border-radius: 16rpx !important;
	}
	.btn-comment-content {
		border-radius: 0 18rpx 0 18rpx !important;
		background: #12b3a8 !important;
	}
	.hot > view:first-child,
	.recommend > view:first-child {
		height: auto !important;
		padding: 24rpx 24rpx 0 !important;
		background: none !important;
		color: #12202b !important;
		font-size: 32rpx !important;
		justify-content: flex-start !important;
	}
	.hot image,
	.recommend image {
		background: #f3f7f8 !important;
	}
	._div > view {
		border-radius: 14rpx !important;
	}
</style>
