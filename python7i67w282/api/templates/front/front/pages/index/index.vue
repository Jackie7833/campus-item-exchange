<template>
	<view class="content">
		<view :style='{"width":"100%","padding":"0 0 40rpx 0","background":"#F9FAFA","flexDirection":"column","display":"flex","height":"auto"}'>
			<view class="list-swiper-4" :style='{"width":"100%","position":"relative","height":"360rpx"}' @touchstart="touchStart" @touchmove="touchMove" @touchend="touchEnd">
				<view :style='{"width":"100%","position":"absolute","top":"0%","left":"0%","background":"#fff","height":"360rpx"}' class="item animate__animated" :class="prevNumList4 == index  ? 'animate__backOutRight' : (numList4 == index  ? 'animate__backInLeft' : '')" v-for="(swiper,index) in swiperList" :key="index" v-if="numList4 == index || prevNumList4 == index">
					<image :style='{"width":"100%","objectFit":"cover","display":"block","height":"360rpx"}' mode="aspectFill" :src="baseUrl+swiper.img" @tap="onSwiperTap(swiper)"></image>
					<view :style='{"padding":"8rpx 20rpx","margin":"-20rpx 0 0 0","transform":"translate3d(-50%, -50%, 0)","top":"50%","color":"#000","left":"50%","background":"rgba(255, 255, 255, 0.3)","display":"none","lineHeight":"1.5","fontSize":"40rpx","position":"absolute"}'>{{ swiper.title }}</view>
				</view>
				<view class="animate__navigation" :style='{"alignItems":"center","left":"0%","bottom":"0%","background":"rgba(0,0,0,.3)","display":"flex","width":"100%","position":"absolute","justifyContent":"center","height":"40rpx"}'>
					<block v-for="(swiper,index) in swiperList" :key="index">
						<text class="navigation-item" v-if="numList4 == index" :style='{"width":"16rpx","margin":"0 4rpx","borderRadius":"100%","background":"#F7EFDB","height":"16rpx"}'></text>
						<text class="navigation-item" v-if="numList4 != index" :style='{"width":"16rpx","margin":"0 4rpx","borderRadius":"100%","background":"#fff","height":"16rpx"}'></text>
					</block>
				</view>
			</view>
			<!-- menu -->
			<view v-if="true" class="menu_view">
				<block v-for="(item,index1) in menuList" v-bind:key="item.roleName">
					<block v-if="index1==0" v-bind:key="index" v-for=" (menu,index) in item.frontMenu">
						<block v-bind:key="sort" v-for=" (child,sort) in menu.child">
							<block v-bind:key="sort2" v-for=" (button,sort2) in child.buttons">
								<view class="menu-item" v-if="button=='查看' && child.tableName!='yifahuodingdan' && child.tableName!='yituikuandingdan' &&child.tableName!='yiquxiaodingdan' && child.tableName!='weizhifudingdan' && child.tableName!='yizhifudingdan' && child.tableName!='yiwanchengdingdan' " @tap="onPageTap2(child.tableName)">
									<view class="iconarr" :class="child.appFrontIcon"></view>
									
									<view class="text">{{child.menu.split("列表")[0]}}</view>
								</view>
							</block>
						</block>
					</block>
				</block>
			</view>
			<!-- 商品推荐 -->
			<!-- 商品推荐 -->
			
			<!-- 商品列表 -->
			<view class="listBox list" :style='{"width":"100%","padding":"0 20rpx","margin":"40rpx 0 0","background":"none","order":"4"}'>
				<view class="title" :style='{"padding":"0","margin":"0","background":"url(http://codegen.caihongy.cn/20250219/f42cc2e72e884f0ab71bbf038eb06c49.png) no-repeat center / 100% 100%","display":"flex","width":"100%","position":"relative","justifyContent":"center","height":"136rpx"}'>
					<view :style='{"letterSpacing":"2rpx","fontSize":"32rpx","lineHeight":"60rpx","color":"#FFFFFF","fontWeight":"600"}'>失物招领</view>
					<view :style='{"padding":"0 20rpx","alignItems":"center","top":"12rpx","color":"#FFFFFF","background":"linear-gradient( 270deg, #39B3D6 0%, #2AC8B9 100%)","display":"flex","position":"absolute","right":"0px","justifyContent":"center"}' @tap="onPageTap('shiwuzhaoling')">
					  <text :style='{"color":"inherit","fontSize":"28rpx"}'>查看更多</text>
					  <text class="icon iconfont icon-gengduo1" :style='{"color":"inherit","fontSize":"28rpx"}'></text>
					</view>
				</view>
				<!-- 样式3 -->
				<view v-if="3 == 3" class="list-box style3" :style='{"width":"100%","padding":"24rpx","margin":"0","background":"#FFFFFF","height":"auto"}'>
					<view @tap="onDetailTap('shiwuzhaoling',product.id)" v-for="(product,index) in homeshiwuzhaolinglist" :key="index" class="list-item" :style='{"boxShadow":"none","padding":"12rpx","margin":"0 0 40rpx","borderRadius":"12rpx","flexWrap":"wrap","background":"#F5FFFF","display":"flex","width":"100%","height":"auto"}'>
						<image :style='{"width":"200rpx","objectFit":"cover","borderRadius":"10rpx","display":"block","height":"200rpx"}' class="list-item-image" mode="aspectFill" v-if="product.tupian.substring(0,4)=='http'" :src="product.tupian"></image>
						<image :style='{"width":"200rpx","objectFit":"cover","borderRadius":"10rpx","display":"block","height":"200rpx"}' class="list-item-image" mode="aspectFill" v-else :src="product.tupian?baseUrl+product.tupian.split(',')[0]:''"></image>
						<view class="list-item-body" :style='{"width":"calc(100% - 200rpx)","padding":"0 20rpx","margin":"0","height":"auto"}'>
							<view :style='{"padding":"0","margin":"0","color":"#010F33","width":"100%","lineHeight":"48rpx","fontSize":"28rpx","fontWeight":"600"}' class="list-item-title">{{product.biaoti}}</view>
							<view :style='{"padding":"0","margin":"0","color":"#010F33","width":"100%","lineHeight":"48rpx","fontSize":"28rpx","fontWeight":"600"}' class="list-item-title">状态:{{product.zhuangtai}}</view>
							<view :style='{"padding":"0"}'>
								<text class="icon iconfont icon-shijian21" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#959595"}'></text>
								<text :style='{"color":"#959595","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.addtime.split(' ')[0].replace(/\-/g,'-')}}</text>
							</view>
							<view :style='{"padding":"0 16rpx 0 0","display":"inline-block"}'>
								<text class="icon iconfont icon-geren16" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.zhanghao}}</text>
							</view>
							<view :style='{"padding":"0 16rpx 0 0","display":"inline-block"}'>
								<text class="icon iconfont icon-shoucang10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.storeupnum}}</text>
							</view>
						</view>
					</view>
				</view>
			</view>
			<view class="listBox list" :style='{"width":"100%","padding":"0 20rpx","margin":"40rpx 0 0","background":"none","order":"4"}'>
				<view class="title" :style='{"padding":"0","margin":"0","background":"url(http://codegen.caihongy.cn/20250219/f42cc2e72e884f0ab71bbf038eb06c49.png) no-repeat center / 100% 100%","display":"flex","width":"100%","position":"relative","justifyContent":"center","height":"136rpx"}'>
					<view :style='{"letterSpacing":"2rpx","fontSize":"32rpx","lineHeight":"60rpx","color":"#FFFFFF","fontWeight":"600"}'>二手流转</view>
					<view :style='{"padding":"0 20rpx","alignItems":"center","top":"12rpx","color":"#FFFFFF","background":"linear-gradient( 270deg, #39B3D6 0%, #2AC8B9 100%)","display":"flex","position":"absolute","right":"0px","justifyContent":"center"}' @tap="onPageTap('ershouliuzhuan')">
					  <text :style='{"color":"inherit","fontSize":"28rpx"}'>查看更多</text>
					  <text class="icon iconfont icon-gengduo1" :style='{"color":"inherit","fontSize":"28rpx"}'></text>
					</view>
				</view>
				<!-- 样式3 -->
				<view v-if="3 == 3" class="list-box style3" :style='{"width":"100%","padding":"24rpx","margin":"0","background":"#FFFFFF","height":"auto"}'>
					<view @tap="onDetailTap('ershouliuzhuan',product.id)" v-for="(product,index) in homeershouliuzhuanlist" :key="index" class="list-item" :style='{"boxShadow":"none","padding":"12rpx","margin":"0 0 40rpx","borderRadius":"12rpx","flexWrap":"wrap","background":"#F5FFFF","display":"flex","width":"100%","height":"auto"}'>
						<image :style='{"width":"200rpx","objectFit":"cover","borderRadius":"10rpx","display":"block","height":"200rpx"}' class="list-item-image" mode="aspectFill" v-if="product.tupian.substring(0,4)=='http'" :src="product.tupian"></image>
						<image :style='{"width":"200rpx","objectFit":"cover","borderRadius":"10rpx","display":"block","height":"200rpx"}' class="list-item-image" mode="aspectFill" v-else :src="product.tupian?baseUrl+product.tupian.split(',')[0]:''"></image>
						<view class="list-item-body" :style='{"width":"calc(100% - 200rpx)","padding":"0 20rpx","margin":"0","height":"auto"}'>
							<view :style='{"padding":"0","margin":"0","color":"#010F33","width":"100%","lineHeight":"48rpx","fontSize":"28rpx","fontWeight":"600"}' class="list-item-title">{{product.shangpinmingcheng}}</view>
							<view :style='{"padding":"0","margin":"0","color":"#010F33","width":"100%","lineHeight":"48rpx","fontSize":"28rpx","fontWeight":"600"}' class="list-item-title">数量:{{product.shuliang}}</view>
							<view :style='{"padding":"0"}'>
								<text class="icon iconfont icon-shijian21" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#959595"}'></text>
								<text :style='{"color":"#959595","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.addtime.split(' ')[0].replace(/\-/g,'-')}}</text>
							</view>
							<view :style='{"padding":"0 16rpx 0 0","display":"inline-block"}'>
								<text class="icon iconfont icon-geren16" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.zhanghao}}</text>
							</view>
							<view :style='{"padding":"0 16rpx 0 0","display":"inline-block"}'>
								<text class="icon iconfont icon-zan10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.thumbsupnum}}</text>
							</view>
							<view :style='{"padding":"0 16rpx 0 0","display":"inline-block"}'>
								<text class="icon iconfont icon-shoucang10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.storeupnum}}</text>
							</view>
							<view :style='{"padding":"0 16rpx 0 0","display":"inline-block"}'>
								<text class="icon iconfont icon-chakan9" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.clicknum}}</text>
							</view>
						</view>
					</view>
				</view>
			</view>
			<!-- 商品列表 -->
			<!-- 新闻资讯 -->
			<view class="listBox news" :style='{"width":"100%","padding":"0 20rpx","margin":"40rpx 0 0","background":"none","order":"2"}'>
				<view class="title" :style='{"padding":"0","margin":"0","background":"url(http://codegen.caihongy.cn/20250219/f42cc2e72e884f0ab71bbf038eb06c49.png) no-repeat center / 100% 100%","display":"flex","width":"100%","position":"relative","justifyContent":"center","height":"136rpx"}'>
					<view :style='{"letterSpacing":"2rpx","fontSize":"32rpx","lineHeight":"60rpx","color":"#FFFFFF","fontWeight":"600"}'>校园动态</view>
					<view :style='{"padding":"0 20rpx","alignItems":"center","top":"12rpx","color":"#FFFFFF","background":"linear-gradient( 270deg, #39B3D6 0%, #2AC8B9 100%)","display":"flex","position":"absolute","right":"0px","justifyContent":"center"}' @tap="onPageTap('news')">
					  <text :style='{"color":"inherit","fontSize":"28rpx"}'>查看更多</text>
					  <text class="icon iconfont icon-gengduo1" :style='{"color":"inherit","fontSize":"28rpx"}'></text>
					</view>
				</view>
				<!-- 样式7 -->
				<view class="news-box4" :style='{"width":"100%","padding":"24rpx","margin":"0","background":"#FFFFFF","height":"auto"}'>
					<block v-for="(item,index) in news" :key="index">
						<view @tap="onNewsDetailTap(item.id)" v-if="index%2==0" class="list-item" :style='{"width":"100%","boxShadow":"0 2rpx 12rpx rgba(0,0,0,.3)","margin":"0 0 20rpx","flexWrap":"wrap","display":"flex","height":"auto"}'>
							<image :style='{"width":"200rpx","objectFit":"cover","display":"block","height":"200rpx"}' mode="aspectFill" class="listmpic" :src="baseUrl+item.picture"></image>
							<view class="list-item-body" :style='{"width":"calc(100% - 200rpx)","padding":"0","margin":"0","height":"auto"}'>
								<view :style='{"width":"100%","padding":"0 20rpx","lineHeight":"1.5","fontSize":"28rpx","color":"#000","fontWeight":"600"}' class="title ">{{item.title}}</view>
								<view :style='{"padding":"0 20rpx","margin":"0","overflow":"hidden","whiteSpace":"nowrap","color":"#666","width":"100%","lineHeight":"1.5","fontSize":"28rpx","textOverflow":"ellipsis"}' class="text">{{item.introduction}}</view>
								<view :style='{"padding":"0 20rpx"}'>
									<text class="icon iconfont icon-shijian21" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.addtime.replace(/\-/g,'-').replace(/\:/g,':')}}</text>
								</view>
								<view :style='{"padding":"0 20rpx"}'>
									<text class="icon iconfont icon-geren16" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.name}}</text>
								</view>
								<view :style='{"padding":"0 20rpx","display":"inline-block"}'>
									<text class="icon iconfont icon-zan10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.thumbsupnum}}</text>
								</view>
								<view :style='{"padding":"0 20rpx","display":"inline-block"}'>
									<text class="icon iconfont icon-shoucang10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.storeupnum}}</text>
								</view>
								<view :style='{"padding":"0 20rpx","display":"inline-block"}'>
									<text class="icon iconfont icon-chakan9" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.clicknum}}</text>
								</view>
							</view>
						</view>
						<view @tap="onNewsDetailTap(item.id)" v-if="index%2==1" class="list-item" :style='{"width":"100%","boxShadow":"0 2rpx 12rpx rgba(0,0,0,.3)","margin":"0 0 20rpx","flexWrap":"wrap","display":"flex","height":"auto"}'>
							<view class="list-item-body" :style='{"width":"calc(100% - 200rpx)","padding":"0","margin":"0","height":"auto"}'>
								<view :style='{"width":"100%","padding":"0 20rpx","lineHeight":"1.5","fontSize":"28rpx","color":"#000","fontWeight":"600"}' class="title ">{{item.title}}</view>
								<view :style='{"padding":"0 20rpx","margin":"0","overflow":"hidden","whiteSpace":"nowrap","color":"#666","width":"100%","lineHeight":"1.5","fontSize":"28rpx","textOverflow":"ellipsis"}' class="text">{{item.introduction}}</view>
								<view :style='{"padding":"0 20rpx"}'>
									<text class="icon iconfont icon-shijian21" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.addtime.replace(/\-/g,'-').replace(/\:/g,':')}}</text>
								</view>
								<view :style='{"padding":"0 20rpx"}'>
									<text class="icon iconfont icon-geren16" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.name}}</text>
								</view>
								<view :style='{"padding":"0 20rpx","display":"inline-block"}'>
									<text class="icon iconfont icon-zan10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.thumbsupnum}}</text>
								</view>
								<view :style='{"padding":"0 20rpx","display":"inline-block"}'>
									<text class="icon iconfont icon-shoucang10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.storeupnum}}</text>
								</view>
								<view :style='{"padding":"0 20rpx","display":"inline-block"}'>
									<text class="icon iconfont icon-chakan9" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
									<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{item.clicknum}}</text>
								</view>
							</view>
							<image :style='{"width":"200rpx","objectFit":"cover","display":"block","height":"200rpx"}' mode="aspectFill" class="listmpic" :src="baseUrl+item.picture"></image>
						</view>
					</block>
				</view>
			</view>
			<!-- 新闻资讯 -->
			<view v-if="scrollTop>200" @tap="scrollTopClick" :style='{"boxShadow":"0 8rpx 16rpx rgba(0,0,0,.3)","borderRadius":"50%","textAlign":"center","bottom":"20%","background":"#ff000030","width":"60rpx","lineHeight":"60rpx","position":"fixed","right":"20rpx","height":"60rpx"}'>
				<span class="icon iconfont icon-jiantou07" :style='{"color":"#fff"}'></span>
			</view>
		</view>
	</view>
</template>

<script>
    import menu from '@/utils/menu'
	import '@/assets/css/global-restaurant.css'
	import uniIcons from "@/components/uni-ui/lib/uni-icons/uni-icons.vue"
	export default {
		components: {
			uniIcons
		},
		data() {
			return {
				startX: 0,
				prevNumList4: '',
				numList4: 0,
				timerList4: null,
				flagList4: false,
				navigationActive: {"width":"16rpx","margin":"0 4rpx","borderRadius":"100%","background":"#F7EFDB","height":"16rpx"},
				navigationDefault: {"width":"16rpx","margin":"0 4rpx","borderRadius":"100%","background":"#fff","height":"16rpx"},
				options2: {
					effect: 'flip',
					loop : true
				},
				options3: {
					effect: 'cube',
					loop : true,
					cubeEffect: {
						shadow: true,
						slideShadows: true,
						shadowOffset: 20,
						shadowScale: 0.94,
					}
				},
				rows: 2,
				column: 4,
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
				role : '',
				menuList: [],
				swiperMenuList:[],
				user: {},
				tableName:'',

				//轮播
				swiperList: [],
				homeshiwuzhaolinglist: [],
				homeershouliuzhuanlist: [],
				news: [],
				scrollTop: 0,
			}
		},
		onPageScroll(e) {
			this.scrollTop = e.scrollTop
		},
		watch: {
		},
		mounted() {
		},
		computed: {
			baseUrl() {
				return this.$base.url;
			},
		},
		async onLoad(){
			if (Array.isArray(this.menuColor)) {
				this.menuColor = this.menuColor.sort(()=> {
					return (0.5-Math.random());
				});
			}
		},
		async onShow() {
			if (this.timerList4&&this.timerList4!=null) clearInterval(this.timerList4)
			this.swiperMenuList = []
			this.role = uni.getStorageSync("appRole");
			let table = uni.getStorageSync("nowTable");
			let res = null;
			if (table && uni.getStorageSync("appToken")) {
				try {
					res = await this.$api.session(table);
					this.user = res.data || {};
				} catch (e) {
					this.user = {};
				}
			} else {
				this.user = {};
			}
			this.tableName = table;
			let menus = menu.list();
			this.menuList = menus;
			this.menuList.forEach((item,key) => {
				if(key==0) {
					item.frontMenu.forEach((item2,key2) => {
						if(item2.child[0].buttons.indexOf("查看")>-1) {
							this.swiperMenuList.push(item2);
						}
					})
				}
			})
			// let res;
			// 轮播图
			let swiperList = []
			try {
				res = await this.$api.list('config', {
					page: 1,
					limit: 5
				});
				for (let item of ((res.data && res.data.list) || [])) {
					if (item.name.indexOf('picture') >= 0 && item.value && item.value!="" && item.value!=null ) {
						swiperList.push({
							img: item.value,
							title: item.name,
							url: item.url
						});
					}
				}
			} catch (e) {
				swiperList = []
			}
			if (swiperList) {
				this.swiperList = swiperList;
			}
			
			this.prevNumList4 = this.swiperList.length - 1
			if (this.swiperList.length > 1) {
				this.timerList4 = setInterval(this.autoPlayList4, 3000)
			}

			this.getRecommendList().catch(()=>{})
			this.getHomeList().catch(()=>{})
			this.getNewsList().catch(()=>{})
		},
		methods: {
			scrollTopClick(){
				uni.pageScrollTo({
					scrollTop: 0
				})
			},
			uGetRect(selector, all) {
				return new Promise(resolve => {
					uni.createSelectorQuery()
					.in(this)
					[all ? 'selectAll' : 'select'](selector)
					.boundingClientRect(rect => {
						if (all && Array.isArray(rect) && rect.length) {
							resolve(rect);
						}
						if (!all && rect) {
							resolve(rect);
						}
					})
					.exec();
				});
			},
			cloneData(data) {
				return JSON.parse(JSON.stringify(data));
			},
			newsTabClick2(index){
				this.newsIndex2 = index
				this.getNewsList()
			},
			async getNewsList(){
				let res;
				let params = {
					page: 1,
					limit: 4,
					sort: 'id',
					order: 'desc',
				}
				// 校园动态
				try {
					res = await this.$api.list('news', params)
					this.news = (res.data && res.data.list) || []
				} catch (e) {
					this.news = []
				}
			},
			homeTabClick2(index,name){
				this['home' + name + 'Index2'] = index
				this.getHomeList()
			},
			async getHomeList(){
				let res;
				let params;
				params = {
					page:1,
					limit: 4,
				}
				try {
					res = await this.$api.list('shiwuzhaoling', params);
					this.homeshiwuzhaolinglist = (res.data && res.data.list) || []
				} catch (e) {
					this.homeshiwuzhaolinglist = []
				}
				params = {
					page:1,
					limit: 4,
				}
				try {
					res = await this.$api.list('ershouliuzhuan', params);
					this.homeershouliuzhuanlist = (res.data && res.data.list) || []
				} catch (e) {
					this.homeershouliuzhuanlist = []
				}
			},
			recommendTabClick2(index,name){
				this[name + 'Index2'] = index
				this.getRecommendList()
			},
			async getRecommendList(){
				let res;
				let params;
			},
			autoPlayList4() {
				this.prevNumList4 = this.numList4
			
				if (!this.swiperList.length) return
				this.numList4++
				if (this.numList4 == this.swiperList.length) this.numList4 = 0
			},
			touchStart(event) {
				this.startX = event.touches[0].clientX
				
				clearInterval(this.timerList4)
				this.flagList4 = true
			},
			touchMove(event) {
				const currentX = event.touches[0].clientX;
				const deltaX = currentX - this.startX;
				
				if (deltaX > 50) {
					// 向右滑动逻辑
					if (this.flagList4) {
						this.flagList4 = false
						
						this.prevNumList4 = this.numList4
						this.numList4++
						if (this.numList4 == this.swiperList.length) this.numList4 = 0
					}
					
				} else if (deltaX < -50) {
					// 向左滑动逻辑
					if (this.flagList4) {
						this.flagList4 = false
						
						this.prevNumList4 = this.numList4
						this.numList4--
						if (this.numList4 < 0) this.numList4 = this.swiperList.length - 1
					}
				}
			},
			touchEnd() {
				this.startX = 0
				this.timerList4 = setInterval(this.autoPlayList4, 3000)
				this.flagList4 = false
			},
			//轮播图跳转
			onSwiperTap(e) {
				if(e.url) {
					if (e.url.indexOf('https') != -1) {
						// #ifdef MP-WEIXIN
						uni.navigateTo({
						    url: '../../common/linkOthers/linkOthers?url=' + encodeURIComponent(e.url),
						});
						return false
						// #endif
						window.open(e.url)
					} else {
						this.$utils.jump(e.url)
					}
				}
			},
			// 新闻详情
			onNewsDetailTap(id) {
				this.$utils.jump(`../news-detail/news-detail?id=${id}`)
			},
			// 推荐列表点击详情
			onDetailTap(tableName, id) {
				this.$utils.jump(`../${tableName}/detail?id=${id}`)
			},
			onPageTap(tableName){
				uni.navigateTo({
					url: `../${tableName}/list`,
					fail: function(){
						uni.switchTab({
							url: `../${tableName}/list`
						});
					}
				});
				// this.$utils.jump(`../${tableName}/list`)
			},
			onPageTap2(index) {
				let url = '../' + index + '/list'
				uni.setStorageSync("useridTag",0);
				uni.navigateTo({
					url: url,
					fail: function() {
						uni.switchTab({
							url: url
						});
					}
				});
			}
		}
	}
</script>

<style lang="scss" scoped>
	.content {
		min-height: calc(100vh - 44px);
		box-sizing: border-box;
	}
	.list-swiper-4 .animate__animated {
		--animate-delay: 300ms;
	}
	.recommend {
		.style2 {
			.tabView {
				.tab {
					border: 2rpx solid rgb(64, 158, 255);
					border-radius: 40rpx;
					padding: 0 30rpx;
					margin: 0 10rpx;
					color: rgb(64, 158, 255);
					background: #fff;
				}
				.tabActive {
					border: 2rpx solid rgb(64, 158, 255);
					border-radius: 40rpx;
					padding: 0 20rpx;
					margin: 0 10rpx;
					color: #fff;
					background: rgb(64, 158, 255);
				}
			}
		}
	}

	.menu_view {
		padding: 0;
		margin: 0 20rpx;
		background: linear-gradient( 180deg, #EEEEEE 0%, #FFFFFF 8%, #FFFFFF 100%, #FFFFFF 100%);
		display: flex;
		width: calc(100% - 40rpx);
		justify-content: flex-start;
		flex-wrap: wrap;
		height: auto;
		.menu-item {
			padding: 12rpx 0;
			margin: 10rpx 0;
			color: #39B3D6;
			width: 25%;
			height: auto;
			.iconarr {
				border-radius: 100%;
				padding: 0;
				margin: 0px auto;
				color: inherit;
				background: none;
				display: block;
				width: 64rpx;
				font-size: 64rpx;
				line-height: 64rpx;
				height: 64rpx;
			}
			.text {
				padding: 0;
				margin: 12rpx auto 0;
				color: inherit;
				width: 100%;
				font-size: 28rpx;
				line-height: 28rpx;
				text-align: center;
			}
		}
	}
	.content {
		background: #f5f7f8 !important;
		padding-bottom: 40rpx !important;
	}
	.list-swiper-4 {
		margin: 20rpx 24rpx 0 !important;
		width: calc(100% - 48rpx) !important;
		height: 328rpx !important;
		border-radius: 18rpx !important;
		overflow: hidden !important;
		box-shadow: 0 14rpx 34rpx rgba(29, 41, 57, .10) !important;
	}
	.list-swiper-4 .item,
	.list-swiper-4 image {
		height: 328rpx !important;
		border-radius: 18rpx !important;
	}
	.animate__navigation {
		height: 44rpx !important;
		background: linear-gradient(180deg, rgba(0, 0, 0, 0), rgba(0, 0, 0, .24)) !important;
	}
	.menu_view {
		margin: 22rpx 24rpx 0 !important;
		width: calc(100% - 48rpx) !important;
		padding: 20rpx 8rpx !important;
		border-radius: 16rpx !important;
		background: #fff !important;
		border: 1rpx solid #e6edf0 !important;
		box-shadow: 0 10rpx 28rpx rgba(29, 41, 57, .06) !important;
		.menu-item {
			color: #13b8a7 !important;
			.iconarr {
				width: 72rpx !important;
				height: 72rpx !important;
				line-height: 72rpx !important;
				border-radius: 16rpx !important;
				background: #e7f8f6 !important;
			}
			.text {
				color: #344054 !important;
				font-size: 24rpx !important;
				line-height: 32rpx !important;
			}
		}
	}
	.listBox {
		margin: 34rpx 24rpx 0 !important;
		padding: 0 !important;
		width: calc(100% - 48rpx) !important;
	}
	.listBox > .title {
		height: 72rpx !important;
		margin: 0 0 16rpx !important;
		padding: 0 !important;
		background: none !important;
		align-items: center !important;
		justify-content: space-between !important;
	}
	.listBox > .title > view:first-child {
		color: #1d2939 !important;
		font-size: 34rpx !important;
		line-height: 72rpx !important;
		letter-spacing: 0 !important;
	}
	.listBox > .title > view:last-child {
		position: relative !important;
		top: auto !important;
		right: auto !important;
		height: 52rpx !important;
		min-width: 132rpx !important;
		padding: 0 18rpx !important;
		border-radius: 14rpx !important;
		background: #e7f8f6 !important;
		color: #0f9f93 !important;
	}
	.listBox .list-box,
	.news-box4 {
		padding: 0 !important;
		border: 0 !important;
		background: transparent !important;
		box-shadow: none !important;
	}
	.listBox .list-item {
		margin: 0 0 18rpx !important;
		padding: 14rpx !important;
		border-radius: 16rpx !important;
		background: #fff !important;
		border: 1rpx solid #e6edf0 !important;
		box-shadow: 0 10rpx 28rpx rgba(29, 41, 57, .06) !important;
	}
	.list-item-body .list-item-title,
	.news-box4 .title {
		color: #1d2939 !important;
		font-size: 28rpx !important;
		line-height: 42rpx !important;
	}
	.news-box4 .text {
		color: #667085 !important;
		font-size: 24rpx !important;
		line-height: 36rpx !important;
	}
	image {
		border-radius: 14rpx !important;
		background: #edf4f6 !important;
	}
	.back-top,
	.content > view > view[style*="position:fixed"] {
		background: #ffffff !important;
		color: #13b8a7 !important;
		border: 1rpx solid #e6edf0 !important;
		box-shadow: 0 10rpx 28rpx rgba(29, 41, 57, .12) !important;
	}
</style>
