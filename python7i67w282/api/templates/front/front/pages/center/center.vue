<template>
	<view class="content">
		<view class="center-page">
			<view v-if="user&&user.id" @tap="onPageTap('../user-info/user-info')" class="header" v-bind:class="{'status':isH5Plus}">
				<view v-if="tableName=='yonghu'" class="userinfo">
					<image class="avatar-img" :src="user.touxiang?baseUrl+user.touxiang:require('../../static/gen/upload.png')"></image>
					<view class="info profile-info">
						<view class="name-row">
							<text class="name-text">{{user.zhanghao}}<text v-if="user.vip&& user.vip=='是'">(VIP)</text></text>
							<image v-if="tableName=='yonghu' && user.sfsh == '是'" class="verified-badge" mode="aspectFit" :src="avator"></image>
							<text v-if="tableName=='yonghu'" class="reputation-tag" :class="getReputationClass(user.xinyudengji)">{{user.xinyudengji || '普通'}}</text>
						</view>
					</view>
					
					<view class="info contact-info">
						<view class="contact-card">
							<text class="contact-label">手机：</text>
							<text class="contact-value">{{user.shouji}}</text>
						</view>
					</view>
				</view>
				<view class="setting">
					<text class="icon iconfont icon-qita6 setting-icon"></text>
					<text class="setting-text">设置</text>
				</view>
			</view>
			
			<view v-else @tap="loginClick" class="header" v-bind:class="{'status':isH5Plus}">
				<view class="login-entry">登录/注册</view>
			</view>
			
			<view class="list">
				
				<view class="service-section">
					<view class="service-title-wrap">
						<view class="service-title">我的校园事务</view>
					</view>
					<view class="mine-grid">
						<view class="mine-card" @tap="openMineList('lost')">
							<view class="mine-card-head">
								<view>
									<view class="mine-card-title">我的失物发布</view>
									<view class="mine-card-count">{{profileStats.lost}} 条</view>
								</view>
								<text class="icon iconfont icon-jinru mine-card-arrow"></text>
							</view>
							<view v-if="myLostList.length" class="mine-card-record" @tap.stop="openRecordDetail('lost', myLostList[0])">
								<view class="record-name">{{myLostList[0].wupinmingcheng || myLostList[0].biaoti}}</view>
								<view class="record-meta">
									<text class="status-tag">{{getLostStatus(myLostList[0])}}</text>
									<text>{{formatDate(myLostList[0].addtime)}}</text>
								</view>
							</view>
							<view v-else class="mine-card-empty">暂未发布</view>
						</view>
						<view class="mine-card" @tap="openMineList('secondhand')">
							<view class="mine-card-head">
								<view>
									<view class="mine-card-title">我的二手发布</view>
									<view class="mine-card-count">{{profileStats.secondhand}} 条</view>
								</view>
								<text class="icon iconfont icon-jinru mine-card-arrow"></text>
							</view>
							<view v-if="mySecondhandList.length" class="mine-card-record" @tap.stop="openRecordDetail('secondhand', mySecondhandList[0])">
								<view class="record-name">{{mySecondhandList[0].shangpinmingcheng}}</view>
								<view class="record-meta">
									<text class="status-tag" :class="Number(mySecondhandList[0].shuliang) > 0 ? 'tag-success' : 'tag-muted'">{{getSecondhandStatus(mySecondhandList[0])}}</text>
									<text>数量 {{mySecondhandList[0].shuliang || 0}}</text>
								</view>
							</view>
							<view v-else class="mine-card-empty">暂未发布</view>
						</view>
						<view class="mine-card" @tap="openMineList('claims')">
							<view class="mine-card-head">
								<view>
									<view class="mine-card-title">我的认领申请</view>
									<view class="mine-card-count">{{profileStats.claims}} 条</view>
								</view>
								<text class="icon iconfont icon-jinru mine-card-arrow"></text>
							</view>
							<view v-if="myClaimList.length" class="mine-card-record" @tap.stop="openRecordDetail('claims', myClaimList[0])">
								<view class="record-name">{{myClaimList[0].wupinmingcheng || myClaimList[0].biaoti}}</view>
								<view class="record-meta">
									<text class="status-tag" :class="getClaimTagClass(myClaimList[0])">{{getClaimStatus(myClaimList[0])}}</text>
									<text>{{myClaimList[0].shhf || '等待审核'}}</text>
								</view>
							</view>
							<view v-else class="mine-card-empty">暂无记录</view>
						</view>
						<view class="mine-card" @tap="openMineList('orders')">
							<view class="mine-card-head">
								<view>
									<view class="mine-card-title">我的购买订单</view>
									<view class="mine-card-count">{{profileStats.orders}} 条</view>
								</view>
								<text class="icon iconfont icon-jinru mine-card-arrow"></text>
							</view>
							<view v-if="myOrderList.length" class="mine-card-record" @tap.stop="openRecordDetail('orders', myOrderList[0])">
								<view class="record-name">{{myOrderList[0].shangpinmingcheng}}</view>
								<view class="record-meta">
									<text class="status-tag" :class="myOrderList[0].ispay == '已支付' ? 'tag-success' : 'tag-warn'">{{getOrderStatus(myOrderList[0])}}</text>
									<text>￥{{myOrderList[0].jine || 0}} · {{myOrderList[0].shuliang || 0}} 件</text>
								</view>
							</view>
							<view v-else class="mine-card-empty">暂无记录</view>
						</view>
						<view class="mine-card" @tap="openMineList('favorites')">
							<view class="mine-card-head">
								<view>
									<view class="mine-card-title">我的收藏</view>
									<view class="mine-card-count">{{profileStats.favorites}} 条</view>
								</view>
								<text class="icon iconfont icon-jinru mine-card-arrow"></text>
							</view>
							<view v-if="myFavoriteList.length" class="mine-card-record" @tap.stop="openRecordDetail('favorites', myFavoriteList[0])">
								<view class="record-name">{{myFavoriteList[0].name}}</view>
								<view class="record-meta">
									<text class="status-tag">{{getFavoriteType(myFavoriteList[0])}}</text>
									<text>{{formatDate(myFavoriteList[0].addtime)}}</text>
								</view>
							</view>
							<view v-else class="mine-card-empty">暂无收藏</view>
						</view>
					</view>
					<view v-if="user&&user.id" @tap="passwordShow()" class="account-action" hover-class="hover">
						<view class="cuIcon-lock account-action-icon"></view>
						<view class="account-action-text">修改密码</view>
						<view class="icon iconfont icon-jinru"></view>
					</view>
				</view>
			</view>
			
			<!-- 推荐 -->
			<view class="bottom-spacer"></view>
		</view>
		<uni-popup class="popup-content" ref="passwordPopup" type="bottom">
			<view class="passwordForm">
				<view class="passwordInput">
					<input type="password" v-model="passwordForm.mima" placeholder="原密码" />
				</view>
				<view class="passwordInput">
					<input type="password" v-model="passwordForm.newmima" placeholder="新密码" />
				</view>
				<view class="passwordInput">
					<input type="password" v-model="passwordForm.newmima1" placeholder="确认密码" />
				</view>
				<view class="passwordBtnView">
					<button class="passwordBtn" @click="updatePassword">更新</button>
				</view>
			</view>
		</uni-popup>
	</view>
</template>
<script>
	import avator from '@/static/verified_badge.png'
	import menu from '@/utils/menu'
	export default {
		data() {
			return {
				isH5Plus: true,
				user: {},
				tableName:'',
				role: '',
				menuList: [],
				iconArr: [
					'cuIcon-same',
					'cuIcon-deliver',
					'cuIcon-evaluate',
					'cuIcon-shop',
					'cuIcon-ticket',
					'cuIcon-cascades',
					'cuIcon-discover',
					'cuIcon-question',
					'cuIcon-pic',
					'cuIcon-filter',
					'cuIcon-footprint',
					'cuIcon-pulldown',
					'cuIcon-pullup',
					'cuIcon-moreandroid',
					'cuIcon-refund',
					'cuIcon-qrcode',
					'cuIcon-remind',
					'cuIcon-profile',
					'cuIcon-home',
					'cuIcon-message',
					'cuIcon-link',
					'cuIcon-lock',
					'cuIcon-unlock',
					'cuIcon-vip',
					'cuIcon-weibo',
					'cuIcon-activity',
					'cuIcon-friendadd',
					'cuIcon-friendfamous',
					'cuIcon-friend',
					'cuIcon-goods',
					'cuIcon-selection'
				],
				passwordForm: {
					mima: '',
					newmima: '',
					newmima1: '',
				},
				profileStats: {
					lost: 0,
					secondhand: 0,
					claims: 0,
					orders: 0,
					favorites: 0
				},
				myLostList: [],
				mySecondhandList: [],
				myClaimList: [],
				myOrderList: [],
				myFavoriteList: [],
				centerLoading: false,
				// lwn 
				avator
			};
		},
		computed: {
			baseUrl() {
				return this.$base.url;
			},
		},
		async onLoad(){
			let menus = menu.list();
			this.menuList = menus;
		},
		async onShow(){
            uni.removeStorageSync("useridTag");
			this.role = uni.getStorageSync("appRole");
			await this.getSession()
			this.getThumbsup()
			this.getStoreup()
			this.tableName = uni.getStorageSync("nowTable");
			await this.loadPersonalCenterData()
			let menus = menu.list();
			this.menuList = menus;
			this.$forceUpdate()
		},
		methods: {
			getReputationClass(level) {
				if (level === '优秀') return 'rep-excellent'
				if (level === '良好') return 'rep-good'
				if (level === '需谨慎') return 'rep-risk'
				return 'rep-normal'
			},
			async getSession(){
				let table = uni.getStorageSync("nowTable");
				let res = await this.$api.session(table);
				this.user = res.data;
				this.$forceUpdate()
			},
			async getThumbsup(){
				if(!this.user||!this.user.id){
					return false
				}
				let res = await this.$api.page('storeup',{userid: this.user.id,type: 21})
				this.user.thumbsnum = Number(res.data.total)
				this.$forceUpdate()
			},
			async getStoreup(){
				if(!this.user||!this.user.id){
					return false
				}
				let res = await this.$api.page('storeup',{userid: this.user.id,type: 1})
				this.user.storenum = Number(res.data.total)
				this.$forceUpdate()
			},
			resetPersonalCenterData() {
				this.profileStats = { lost: 0, secondhand: 0, claims: 0, orders: 0, favorites: 0 }
				this.myLostList = []
				this.mySecondhandList = []
				this.myClaimList = []
				this.myOrderList = []
				this.myFavoriteList = []
			},
			async loadPersonalCenterData() {
				if (!this.user || !this.user.zhanghao || this.tableName !== 'yonghu') {
					this.resetPersonalCenterData()
					return
				}
				this.centerLoading = true
				const baseParams = { page: 1, limit: 3, sort: 'addtime', order: 'desc' }
				try {
					const lostRes = await this.$api.list('shiwuzhaoling', Object.assign({}, baseParams, { zhanghao: this.user.zhanghao }))
					const secondhandRes = await this.$api.list('ershouliuzhuan', Object.assign({}, baseParams, { zhanghao: this.user.zhanghao }))
					const claimRes = await this.$api.list('renlingshenqing', Object.assign({}, baseParams, { renlinghao: this.user.zhanghao }))
					const orderRes = await this.$api.list('goumaidingdan', Object.assign({}, baseParams, { goumaihao: this.user.zhanghao }))
					const favoriteRes = await this.$api.page('storeup', Object.assign({}, baseParams, { userid: this.user.id, type: 1 }))
					this.myLostList = lostRes.data.list || []
					this.mySecondhandList = secondhandRes.data.list || []
					this.myClaimList = claimRes.data.list || []
					this.myOrderList = orderRes.data.list || []
					this.myFavoriteList = favoriteRes.data.list || []
					this.profileStats = {
						lost: Number(lostRes.data.total || this.myLostList.length),
						secondhand: Number(secondhandRes.data.total || this.mySecondhandList.length),
						claims: Number(claimRes.data.total || this.myClaimList.length),
						orders: Number(orderRes.data.total || this.myOrderList.length),
						favorites: Number(favoriteRes.data.total || this.myFavoriteList.length)
					}
				} catch (e) {
					this.resetPersonalCenterData()
				}
				this.centerLoading = false
				this.$forceUpdate()
			},
			formatDate(value) {
				return value ? String(value).split(' ')[0] : ''
			},
			getLostStatus(item) {
				return item && item.zhuangtai ? item.zhuangtai : '待认领'
			},
			getSecondhandStatus(item) {
				return item && Number(item.shuliang) > 0 ? '在售' : '已售出'
			},
			getClaimStatus(item) {
				if (!item) return '待审核'
				if (item.sfsh == '是') return '已通过'
				if (item.sfsh == '否') return '未通过'
				return '待审核'
			},
			getClaimTagClass(item) {
				if (!item) return 'tag-warn'
				if (item.sfsh == '是') return 'tag-success'
				if (item.sfsh == '否') return 'tag-danger'
				return 'tag-warn'
			},
			getOrderStatus(item) {
				return item && item.ispay ? item.ispay : '未支付'
			},
			getFavoriteType(item) {
				if (!item) return '收藏'
				const typeMap = {
					ershouliuzhuan: '二手商品',
					shiwuzhaoling: '失物招领',
					news: '校园动态'
				}
				return typeMap[item.tablename] || '收藏'
			},
			openMineList(type) {
				if (!this.user || !this.user.zhanghao) return
				const owner = encodeURIComponent(this.user.zhanghao)
				const map = {
					lost: '../shiwuzhaoling/list?centerScope=publishedLost&owner=' + owner,
					secondhand: '../ershouliuzhuan/list?centerScope=publishedSecondhand&owner=' + owner,
					claims: '../renlingshenqing/list?centerScope=myClaims&owner=' + owner,
					orders: '../goumaidingdan/list?centerScope=myOrders&owner=' + owner,
					favorites: '../storeup/list?centerScope=myFavorites&userid=' + this.user.id + '&menuJump=1'
				}
				if (map[type]) {
					uni.removeStorageSync("useridTag")
					uni.navigateTo({
						url: map[type],
						fail: function() {
							uni.switchTab({ url: map[type] })
						}
					})
				}
			},
			openRecordDetail(type, item) {
				if (!item || !item.id) return
				if (type === 'favorites') {
					this.openFavoriteDetail(item)
					return
				}
				const map = {
					lost: '../shiwuzhaoling/detail?id=' + item.id + '&userid=' + this.user.id,
					secondhand: '../ershouliuzhuan/detail?id=' + item.id + '&userid=' + this.user.id,
					claims: '../renlingshenqing/detail?id=' + item.id + '&userid=' + this.user.id,
					orders: '../goumaidingdan/detail?id=' + item.id + '&userid=' + this.user.id
				}
				if (map[type]) this.onPageTap(map[type])
			},
			openFavoriteDetail(item) {
				if (!item || !item.refid || !item.tablename) return
				if (item.tablename == 'news') {
					this.onPageTap('../news-detail/news-detail?id=' + item.refid)
					return
				}
				if (item.tablename == 'ershouliuzhuan') {
					this.onPageTap('../ershouliuzhuan/detail?id=' + item.refid + '&userid=' + this.user.id)
					return
				}
				if (item.tablename == 'shiwuzhaoling') {
					this.onPageTap('../shiwuzhaoling/detail?id=' + item.refid + '&userid=' + this.user.id)
					return
				}
				this.onPageTap('../' + item.tablename + '/detail?id=' + item.refid)
			},
			loginClick(){
				uni.navigateTo({
					url: '../login/login'
				});
			},
			onPageTap(url) {
                uni.setStorageSync("useridTag",1);
				uni.navigateTo({
					url: url,
					fail: function() {
						uni.switchTab({
							url: url
						});
					}
				});
			},
			menuPageTap(child) {
				if (!child) return;
				this.onPageTap('../' + child.tableName + '/list?userid=' + this.user.id + '&menuJump=' + child.menuJump);
			},
			hasTranslate(){
				for(let x in this.menuList){
					if(this.menuList[x].roleName == this.role){
						for(let i in this.menuList[x].backMenu){
							if(this.menuList[x].backMenu[i].child.length) {
								for(let j in this.menuList[x].backMenu[i].child) {
									if(this.menuList[x].backMenu[i].child[j].tableName=='hasTranslate'){
										return true
									}
								}
							}
						}
					}
				}
				return false
			},
			recommendDetail(id) {
				uni.navigateTo({
					url: `../${this.recommendTable}/detail?id=${id}`,
					fail: function() {
						uni.switchTab({
							url: `../${this.recommendTable}/detail?id=${id}`
						});
					}
				});
			},
			passwordShow() {
				this.passwordForm = {
					mima: '',
					newmima: '',
					newmima1: '',
				}
				this.$forceUpdate()
				this.$refs.passwordPopup.open()
			},
			async updatePassword() {
				if (this.passwordForm.mima == ''){
					this.$utils.msg('原密码不能为空')
					return false
				}
				if (this.passwordForm.newmima == ''){
					this.$utils.msg('新密码不能为空')
					return false
				}
				if (this.passwordForm.newmima1 == ''){
					this.$utils.msg('确认密码不能为空')
					return false
				}
				let password = ''
				if (this.user.mima) {
					password = this.user.mima;
				} else if (this.user.password) {
					password = this.user.password;
				}
				if (this.tableName == 'yonghu') {
				}
				let newpassword = this.passwordForm.mima
				if(password != newpassword){
					this.$utils.msg('原密码不正确')
					return false
				}
				if (this.passwordForm.newmima != this.passwordForm.newmima1){
					this.$utils.msg('两次密码不一致')
					return false
				}
				if (this.passwordForm.mima == this.passwordForm.newmima){
					this.$utils.msg('新密码与原密码相同！')
					return false
				}
				this.user.password = this.passwordForm.newmima
				this.user.mima = this.passwordForm.newmima
				await this.$api.update(this.tableName,this.user)
				this.$utils.msg('修改密码成功,下次登录系统生效')
				this.$refs.passwordPopup.close()
				this.getSession()
			},
		}
	}
</script>

<style lang="scss" scoped>
	.content {
		height: calc(100vh - 94px);
		box-sizing: border-box;
	}
	.center-page {
		min-height: 100%;
		width: 100%;
		padding: 0;
		position: relative;
		background: #F9FAFA;
		height: auto;
	}
	.passwordForm {
		width: 100%;
		padding: 10px 20px 60px;
		background: #fff;
	
		.passwordInput {
			background: #eee;
			margin: 0 0 10px;
			padding: 0 10px;
	
			input {
				height: 36px;
				line-height: 36px;
				font-size: 14px;
			}
		}
	
		.passwordBtnView {
			width: 100%;
			display: flex;
			align-items: center;
			justify-content: center;
			padding: 10px 0;
	
			.passwordBtn {
				padding: 0 20px;
				width: auto;
				height: 20px;
				line-height: 20px;
				font-size: 14px;
				color: #fff;
				background: #007aff;
				border: none;
				border-radius: 5px;
	
			}
		}
	}
	.me-menu-view {
		padding: 0 24rpx;
		background: #fff;
		display: flex;
		width: 100%;
		flex-wrap: wrap;
		height: auto;
		.me-menu-item {
			display: flex;
			width: 100%;
			border-color: #ccc;
			border-width: 0 0 2rpx;
			align-items: center;
			border-style: solid;
			height: auto;
			.me-menu-icon {
				color: rgba(0, 186, 189, 1);
				font-size: 40rpx;
				line-height: 1;
			}
			.text {
				padding: 0 20rpx;
				color: #333;
				flex: 1;
				width: 100%;
				font-size: 28rpx;
				line-height: 88rpx;
			}
			.icon {
				color: #999;
				width: 28rpx;
				font-size: 28rpx;
				line-height: 28rpx;
			}
		}
	}
	.content {
		background: #f6f8fa !important;
		padding: 24rpx 24rpx 40rpx !important;
	}
	.me-info {
		border-radius: 20rpx !important;
		background: linear-gradient(135deg, #12b3a8 0%, #1f8fcb 100%) !important;
		box-shadow: 0 14rpx 36rpx rgba(18, 179, 168, .22) !important;
		overflow: hidden !important;
	}
	.me-menu-view {
		margin-top: 22rpx !important;
		padding: 8rpx 24rpx !important;
		border-radius: 18rpx !important;
		box-shadow: 0 10rpx 30rpx rgba(24, 35, 47, .07) !important;
		.me-menu-item {
			border-color: #edf2f5 !important;
			.me-menu-icon {
				color: #12b3a8 !important;
			}
			.text {
				color: #26323f !important;
			}
		}
	}
	.passwordBtn {
		background: #12b3a8 !important;
		border-radius: 12rpx !important;
	}
	.header {
		display: flex;
		position: relative;
		height: auto;
		margin: 0 0 24rpx !important;
		width: 100% !important;
		padding: 32rpx 28rpx !important;
		min-height: 188rpx !important;
		border-radius: 22rpx !important;
		background: #fff !important;
		box-shadow: 0 12rpx 36rpx rgba(24, 35, 47, .08) !important;
	}
	.header image {
		width: 112rpx !important;
		height: 112rpx !important;
		border: 4rpx solid #fff !important;
		box-shadow: 0 8rpx 24rpx rgba(24, 35, 47, .12) !important;
	}
	.header .userinfo {
		display: flex;
		flex: 1;
		height: 100%;
		flex-wrap: wrap;
		align-content: flex-start !important;
		align-items: center !important;
	}
	.avatar-img {
		width: 112rpx !important;
		height: 112rpx !important;
		padding: 0 !important;
		margin: 0 20rpx 0 0 !important;
		border-radius: 100% !important;
		flex: 0 0 112rpx !important;
	}
	.header .info {
		color: #12202b !important;
	}
	.profile-info {
		width: 240rpx;
		flex: 1;
		flex-direction: column;
		justify-content: center;
		display: flex;
		min-width: 0;
	}
	.name-row {
		display: flex !important;
		align-items: center !important;
		gap: 10rpx !important;
		min-width: 0 !important;
		width: 100% !important;
		line-height: 36rpx !important;
		font-size: 24rpx !important;
		color: #000000 !important;
	}
	.name-text {
		max-width: 260rpx !important;
		overflow: hidden !important;
		text-overflow: ellipsis !important;
		white-space: nowrap !important;
		color: #12202b !important;
		font-size: 30rpx !important;
		font-weight: 600 !important;
	}
	.verified-badge {
		width: 38rpx !important;
		height: 38rpx !important;
		flex: 0 0 38rpx !important;
		border: 0 !important;
		box-shadow: none !important;
		border-radius: 50% !important;
	}
	.reputation-tag {
		padding: 4rpx 10rpx;
		border-radius: 8rpx;
		font-size: 22rpx;
		line-height: 30rpx;
		white-space: nowrap;
	}
	.rep-excellent { background: #e6f7ed; color: #16834a; }
	.rep-good { background: #e7f8f6; color: #0f9f93; }
	.rep-normal { background: #eef2f5; color: #63717c; }
	.rep-risk { background: #fff2df; color: #b25b00; }
	.contact-info {
		padding: 20rpx 0 !important;
		margin: 20rpx 0 0 !important;
		color: #000000 !important;
		flex-direction: row !important;
		background: #FFFFFF !important;
		display: flex !important;
		gap: 20rpx !important;
		width: 100% !important;
		flex-flow: wrap !important;
		justify-content: center !important;
	}
	.contact-card {
		padding: 8rpx !important;
		border-radius: 12rpx !important;
		color: inherit !important;
		text-align: center !important;
		background: none !important;
		flex-direction: column !important;
		display: flex !important;
		width: 30% !important;
		line-height: 36rpx !important;
		font-size: 24rpx !important;
	}
	.contact-label,
	.contact-value {
		color: inherit !important;
	}
	.setting {
		padding: 0 0 0 20rpx !important;
		align-items: center !important;
		flex-direction: column !important;
		display: flex !important;
		width: 84rpx !important;
		position: absolute !important;
		justify-content: center !important;
		height: auto !important;
		top: 28rpx !important;
		right: 28rpx !important;
	}
	.setting-icon {
		border: 0 !important;
		width: 48rpx !important;
		line-height: 48rpx !important;
		font-size: 48rpx !important;
		color: #000000 !important;
		border-radius: 0 !important;
	}
	.setting-text {
		color: #000000 !important;
		line-height: 2 !important;
		font-size: 24rpx !important;
	}
	.setting image,
	.setting img {
		width: 64rpx !important;
		height: 64rpx !important;
		box-shadow: none !important;
		border: 0 !important;
	}
	.list > view > view:first-child {
		height: auto !important;
		padding: 0 0 16rpx !important;
		justify-content: flex-start !important;
		color: #12202b !important;
		background: none !important;
		font-size: 32rpx !important;
	}
	.list > view > view:first-child > view {
		width: auto !important;
		height: auto !important;
		padding: 0 !important;
		background: none !important;
		color: #12202b !important;
		font-size: 32rpx !important;
		justify-content: flex-start !important;
	}
	.login-entry {
		align-items: center;
		color: #000;
		display: flex;
		width: 100%;
		font-size: 36rpx;
		justify-content: center;
		height: 100%;
	}
	.list {
		width: 100%;
		background: none;
		height: auto;
	}
	.service-section {
		width: 100%;
		margin: 40rpx 0 0;
		height: auto;
	}
	.service-title-wrap {
		padding: 20rpx 0 0;
		margin: 0;
		color: #fff;
		background: none;
		display: flex;
		width: 100%;
		letter-spacing: 2rpx;
		font-size: 32rpx;
		position: relative;
		justify-content: center;
		font-weight: 600;
		height: 152rpx;
	}
	.service-title {
		padding: 8rpx 0 0;
		margin: 0;
		color: #fff;
		background: linear-gradient(135deg, #12b3a8 0%, #1f8fcb 100%);
		border-radius: 18rpx;
		display: flex;
		width: 100%;
		font-size: 32rpx;
		position: relative;
		justify-content: center;
		align-items: center;
		font-weight: 600;
		height: 88rpx;
	}
	.bottom-spacer {
		width: 100%;
		height: 80px;
	}
	.me-menu-view {
		width: 100% !important;
		margin: 0 !important;
	}
	.me-menu-view .me-menu-item {
		min-height: 92rpx !important;
	}
	.mine-grid {
		display: grid;
		grid-template-columns: repeat(2, minmax(0, 1fr));
		gap: 20rpx;
		width: 100%;
	}
	.mine-card {
		padding: 24rpx;
		border-radius: 18rpx;
		background: #fff;
		box-shadow: 0 10rpx 28rpx rgba(24, 35, 47, .06);
		min-height: 220rpx;
	}
	.mine-card-head {
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		gap: 12rpx;
	}
	.mine-card-title {
		color: #12202b;
		font-size: 28rpx;
		font-weight: 600;
		line-height: 38rpx;
	}
	.mine-card-count {
		margin-top: 8rpx;
		color: #12b3a8;
		font-size: 34rpx;
		font-weight: 700;
		line-height: 42rpx;
	}
	.mine-card-arrow {
		color: #9aa7b2;
		font-size: 26rpx;
		line-height: 34rpx;
	}
	.mine-card-record {
		margin-top: 20rpx;
		padding-top: 18rpx;
		border-top: 2rpx solid #edf2f5;
	}
	.record-name {
		color: #24313d;
		font-size: 26rpx;
		font-weight: 600;
		line-height: 36rpx;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}
	.record-meta {
		display: flex;
		align-items: center;
		gap: 10rpx;
		margin-top: 12rpx;
		color: #788590;
		font-size: 22rpx;
		line-height: 32rpx;
		min-width: 0;
	}
	.record-meta text:last-child {
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}
	.status-tag {
		flex: 0 0 auto;
		padding: 4rpx 12rpx;
		border-radius: 999rpx;
		background: #eef9f7;
		color: #12a79d;
		font-size: 22rpx;
		line-height: 30rpx;
	}
	.tag-success {
		background: #eef9f7;
		color: #12a79d;
	}
	.tag-warn {
		background: #fff7e8;
		color: #c77a12;
	}
	.tag-danger {
		background: #fff1f1;
		color: #d94d4d;
	}
	.tag-muted {
		background: #eef1f4;
		color: #6f7d89;
	}
	.mine-card-empty {
		margin-top: 26rpx;
		padding: 22rpx 0;
		border-radius: 14rpx;
		background: #f7fafb;
		color: #8b98a4;
		text-align: center;
		font-size: 24rpx;
		line-height: 34rpx;
	}
	.account-action {
		display: flex;
		align-items: center;
		margin-top: 22rpx;
		padding: 0 24rpx;
		min-height: 92rpx;
		border-radius: 18rpx;
		background: #fff;
		box-shadow: 0 10rpx 28rpx rgba(24, 35, 47, .06);
	}
	.account-action-icon {
		color: #12b3a8;
		font-size: 40rpx;
		line-height: 1;
	}
	.account-action-text {
		flex: 1;
		padding: 0 20rpx;
		color: #26323f;
		font-size: 28rpx;
		line-height: 92rpx;
	}
	.passwordForm {
		border-radius: 28rpx 28rpx 0 0 !important;
	}
	.passwordForm .passwordInput {
		border-radius: 14rpx !important;
		background: #f3f7f8 !important;
	}
	.passwordForm .passwordBtn {
		height: 72rpx !important;
		line-height: 72rpx !important;
		border-radius: 14rpx !important;
		background: #12b3a8 !important;
	}
</style>
