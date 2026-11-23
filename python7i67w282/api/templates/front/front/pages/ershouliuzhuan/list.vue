<template>
<!-- category 1 -->
	<mescroll-uni @init="mescrollInit" :up="upOption" :down="downOption" @down="downCallback" @up="upCallback">
		<view class="content">
			<view :style='{"minHeight":"100%","padding":"0 20rpx","flexWrap":"wrap","background":"#F9FAFA","display":"flex","width":"100%","position":"relative","height":"auto"}'>
				<view class="cu-bar bg-white search" :style='{"padding":"20rpx 0 0 0","margin":"0","background":"none","display":"flex","width":"100%","position":"relative","height":"auto","order":"1"}'>
					<view :style='{"border":"2rpx solid #ACACAC","margin":"0","borderRadius":"20rpx","flex":"1","background":"#fff","lineHeight":"80rpx","position":"relative","height":"80rpx"}' class="search-form round">
						<text class="icon iconfont icon-fangdajing07" :style='{"color":"rgb(153, 153, 153)","left":"0px","textAlign":"center","width":"80rpx","fontSize":"40rpx","lineHeight":"80rpx","position":"absolute","right":"0px"}'></text>
						<input placeholder-style="color: #333" :style='{"border":"0","padding":"12rpx 20rpx 12rpx 80rpx","color":"#333","borderRadius":"40rpx","background":"none","width":"100%","lineHeight":"80rpx","fontSize":"28rpx","height":"80rpx"}' v-model="searchForm.shangpinmingcheng" type="text" placeholder="AI智能搜索，如 300以内自行车" ></input>
					</view>
					<button :style='{"border":"0","padding":"0px","margin":"0","color":"#fff","right":"0px","borderRadius":"20rpx","top":"20rpx","background":"linear-gradient( 104deg, #489DF3 0%, #28CBB6 100%)","width":"172rpx","lineHeight":"80rpx","fontSize":"28rpx","position":"absolute","height":"80rpx","zIndex":"99"}' @tap="search" class="cu-btn shadow-blur round">AI搜索</button>
				</view>
			

				<view :style='{"width":"100%","margin":"20rpx 0","flexWrap":"wrap","display":"flex","order":"4"}'>
					<view @click="sortClick('clicknum')" :style='{"border":"2rpx solid rgb(153, 152, 152)","padding":"0 12rpx","margin":"0 20rpx 0 0","outline":"0","borderRadius":"8rpx","display":"flex"}'>
						<text :style='{"color":"#333","lineHeight":"48rpx","fontSize":"24rpx"}'>点击量</text>
						<text v-if="listSort!='clicknum'" class="icon iconfont icon-xiaoliang13" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
						<text v-else-if="listSort=='clicknum'&&listOrder=='asc'" class="icon iconfont icon-xiaoliang13" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
						<text v-else-if="listSort=='clicknum'&&listOrder=='desc'" class="icon iconfont icon-xiaoliang13" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
					</view>
					<view @click="sortClick('addtime')" :style='{"border":"2rpx solid rgb(153, 152, 152)","padding":"0 12rpx","margin":"0 20rpx 0 0","outline":"0","borderRadius":"8rpx","display":"flex"}'>
						<text :style='{"color":"#333","lineHeight":"48rpx","fontSize":"24rpx"}'>按日期</text>
						<text v-if="listSort!='addtime'" class="icon iconfont icon-shijian18" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
						<text v-else-if="listSort=='addtime'&&listOrder=='asc'" class="icon iconfont icon-shijian18" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
						<text v-else-if="listSort=='addtime'&&listOrder=='desc'" class="icon iconfont icon-shijian18" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
					</view>
				</view>
				<view :style='{"width":"100%","flexWrap":"wrap","background":"none","display":"flex","height":"auto","order":"5"}'>
					<scroll-view scroll-x="true" class="category-one" :style='{"padding":"0","margin":"0","whiteSpace":"nowrap","borderRadius":"20rpx","background":"#EEEEEE","display":"flex","width":"100%","height":"auto"}'>
						<view :class='categoryName === item.shangpinleixing ? "active" : ""' class="tab" v-for="(item,index) in categoryList" :key="index" @tap="categoryClick(item.shangpinleixing)">{{item.shangpinleixing}}</view>
					</scroll-view>
					<!-- 样式1 -->
					<view class="uni-product-list product-card-list" :style='{"padding":"0","margin":"0","flexWrap":"wrap","flex":"auto","display":"flex","width":"0","justifyContent":"space-between","height":"auto"}'>
						<view @tap="onDetailTap(product)" class="uni-product product-card" :style='{"width":"48%","boxShadow":"none","margin":"0 0 20rpx","backgroundColor":"#F3F9FF","height":"auto"}' v-for="(product,index) in list" :key="index">
							<view class="uni-product-title card-title">{{product.shangpinmingcheng}}</view>
							<view class="card-stock" :class="product.shuliang > 0 ? 'in-stock' : 'sold-out'">{{product.shuliang > 0 ? "数量:" + product.shuliang : "已售出"}}</view>
							<view v-if="product.aiReason" class="ai-match-tag">AI匹配 {{product.aiScore || 0}} · {{product.aiReason}}</view>
							<image class="uni-product-image card-cover" mode="aspectFill" v-if="preHttp(product.tupian)" :src="withImageVersion(product.tupian.split(',')[0])"></image>
							<image class="uni-product-image card-cover" mode="aspectFill" v-else :src="product.tupian?withImageVersion(baseUrl+product.tupian.split(',')[0]):''"></image>

							<view :style='{"border":"none","padding":"0 0 0 20rpx","margin":"20rpx 0 0","textAlign":"left"}'>
								<text class="icon iconfont icon-shijian21" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.addtime.split(' ')[0].replace(/\-/g,'-')}}</text>
							</view>
							<view :style='{"padding":"0 20rpx"}'>
								<text class="icon iconfont icon-geren16" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.zhanghao}}</text>
								<text v-if="product.xinyudengji" class="reputation-tag" :class="getReputationClass(product.xinyudengji)">{{product.xinyudengji}}</text>
							</view>
							<view :style='{"padding":"0 20rpx"}'>
								<text class="icon iconfont icon-zan10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.thumbsupnum}}</text>
							</view>
							<view :style='{"padding":"0 20rpx"}'>
								<text class="icon iconfont icon-shoucang10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.storeupnum}}</text>
							</view>
							<view :style='{"padding":"0 20rpx"}'>
								<text class="icon iconfont icon-chakan9" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.clicknum}}</text>
							</view>
							<!-- #ifdef MP-WEIXIN -->
							<view :style='{"width":"100%","padding":"8rpx 0","justifyContent":"space-between","display":"flex","height":"auto"}'>
								<view :style='{"padding":"8rpx 12rpx","background":"#6683A2","display":"flex"}' v-if="(userid && isAuth('ershouliuzhuan','修改')) || (!userid && isAuthFront('ershouliuzhuan','修改'))" @tap.stop.proevent="onUpdate" :data-row="product">
									<text :style='{"margin":"0 8rpx 0 0","fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}' class="cuIcon-edit"></text>
									<text :style='{"fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}'>修改</text>
								</view>
								<view :style='{"padding":"8rpx 12rpx","background":"#6683A2","display":"flex"}' v-if="(userid && isAuth('ershouliuzhuan','删除')) || (!userid && isAuthFront('ershouliuzhuan','删除'))" @tap.stop.proevent="onDelete" :data-row="product">
									<text :style='{"margin":"0 8rpx 0 0","fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}' class="cuIcon-delete"></text>
									<text :style='{"fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}'>删除</text>
								</view>
							</view>
							<!-- #endif -->
							<!-- #ifndef MP-WEIXIN -->
							<view :style='{"width":"100%","padding":"8rpx 0","justifyContent":"space-between","display":"flex","height":"auto"}'>
								<view :style='{"padding":"8rpx 12rpx","background":"#6683A2","display":"flex"}' v-if="(userid && isAuth('ershouliuzhuan','修改')) || (!userid && isAuthFront('ershouliuzhuan','修改'))" @tap.stop.proevent="onUpdateTap(product)">
									<text :style='{"margin":"0 8rpx 0 0","fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}' class="cuIcon-edit"></text>
									<text :style='{"fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}'>修改</text>
								</view>
								<view :style='{"padding":"8rpx 12rpx","background":"#6683A2","display":"flex"}' v-if="(userid && isAuth('ershouliuzhuan','删除')) || (!userid && isAuthFront('ershouliuzhuan','删除'))" @tap.stop.proevent="onDeleteTap(product.id)">
									<text :style='{"margin":"0 8rpx 0 0","fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}' class="cuIcon-delete"></text>
									<text :style='{"fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}'>删除</text>
								</view>
							</view>
							<!-- #endif -->
						</view>
					</view>
					<view v-if="!list.length && !hasNext" class="center-empty">{{centerScope ? '暂未发布' : '暂无记录'}}</view>
			
			
			


			
			
			
			
				</view>
				<button :style='{"border":"0","boxShadow":"0 2rpx 12rpx #00000030","margin":"20rpx 0 0","color":"#fff","bottom":"0","outline":"none","borderRadius":"20rpx","left":"0","background":"linear-gradient( 104deg, #489DF3 0%, #28CBB6 100%)","width":"120rpx","lineHeight":"70rpx","fontSize":"28rpx","position":"relative","height":"70rpx","zIndex":"1","order":"2"}' class="add-btn" @click="screenBoxShow=true">筛</button>
				<button :style='{"border":"0","boxShadow":"0 2rpx 12rpx rgba(0,0,0,.3)","margin":"20rpx 0 0 20rpx","color":"rgb(255, 255, 255)","outline":"none","borderRadius":"20rpx","background":"linear-gradient( 104deg, #489DF3 0%, #28CBB6 100%)","width":"120rpx","lineHeight":"70rpx","fontSize":"28rpx","position":"relative","height":"70rpx","zIndex":"1","order":"3"}' class="add-btn publish-btn" @click="onAddTap()">发布</button>
				<view v-if="scrollTop > 200" class="back-top" @tap="scrollTopClick">
					<text class="icon iconfont icon-jiantou07"></text>
				</view>
				<view :style='{"top":"0","left":"0","background":"rgba(0, 0, 0, .3)","width":"100%","position":"absolute","height":"100%","zIndex":"665"}' v-if="screenBoxShow" @click="screenBoxShow=false"></view>
				<view class="screenBox" :class="screenBoxShow?'screenBoxActive':''">
					<view :style='{"width":"100%","padding":"20rpx 0 20rpx 0","alignItems":"center","flexWrap":"wrap","justifyContent":"space-around","display":"flex"}'>
						<view :style='{"width":"100%","padding":"0 0 0 20rpx","fontSize":"24rpx"}'>品牌</view>
						<input :style='{"border":"2rpx solid rgb(162, 144, 104)","padding":"0 20rpx 0 20rpx","borderRadius":"40rpx","background":"none","width":"90%","fontSize":"24rpx","height":"60rpx"}' placeholder="请输入品牌" v-model="searchForm.pinpai">
					</view>
					<view :style='{"width":"100%","padding":"20rpx 0 20rpx 0"}'>
						<view :style='{"width":"100%","padding":"0 0 20rpx 20rpx","fontSize":"24rpx"}'>价格区间</view>
						<view :style='{"width":"100%","alignItems":"center","flexWrap":"wrap","justifyContent":"center","display":"flex"}'>
							<input :style='{"border":"2rpx solid rgb(162, 144, 104)","borderRadius":"40rpx","textAlign":"center","background":"none","width":"40%","lineHeight":"60rpx","height":"60rpx"}' v-model="searchForm.jiagestart" placeholder="请输入开始价格">
							<view :style='{"padding":"0 10rpx","fontSize":"20rpx"}'>-</view>
							<input :style='{"border":"2rpx solid rgb(162, 144, 104)","borderRadius":"40rpx","textAlign":"center","background":"none","width":"40%","lineHeight":"60rpx","height":"60rpx"}' v-model="searchForm.jiageend" placeholder="请输入结束价格">
						</view>
					</view>
					<view :style='{"width":"100%","padding":"40rpx 0 0","alignItems":"center","justifyContent":"space-around","display":"flex"}'>
						<div :style='{"width":"40%","lineHeight":"60rpx","color":"#888","textAlign":"center","background":"#EDEDED","height":"60rpx"}' @click="screenReset">重置</div>
						<div :style='{"width":"40%","lineHeight":"60rpx","color":"#fff","textAlign":"center","background":"linear-gradient( 133deg, #459FEF 0%, #2BC8BA 96%)","height":"60rpx"}' @click="search">搜索</div>
					</view>
				</view>
			</view>
		</view>
	</mescroll-uni>
</template>

<script>
	export default {
		data() {
			return {
				btnColor: ['#409eff','#67c23a','#909399','#e6a23c','#f56c6c','#356c6c','#351c6c','#f093a9','#a7c23a','#104eff','#10441f','#a21233','#503319'],
				clicknumColor: ['#409eff','#67c23a','#909399','#e6a23c','#f56c6c','#356c6c','#351c6c','#f093a9','#a7c23a','#104eff','#10441f','#a21233','#503319'],
				list: [],
				lists: [],
                userid: '',
				centerScope: '',
				owner: '',
				mescroll: null, //mescroll实例对象
				downOption: {
					auto: false //是否在初始化后,自动执行下拉回调callback; 默认true
				},
				upOption: {
					noMoreSize: 5, //如果列表已无数据,可设置列表的总数量要大于半页才显示无更多数据;避免列表数据过少(比如只有一条数据),显示无更多数据会不好看; 默认5
					textNoMore: '~ 没有更多了 ~',
				},
				hasNext: true,
				searchForm:{
					shangpinmingcheng: '',
					pinpai: '',
					jiagestart: '',
					jiageend: '',
				},
				categoryList:[],
				categoryName :'全部',
				CustomBar: '0',
				listSort: 'id',
				listOrder: 'desc',
				screenBoxShow: false,
				scrollTop: 0,
				aiSearchActive: false,
				reputationCache: {},
			};
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
		async onShow() {
            if(this.centerScope){
                // 个人中心入口使用精确 owner 过滤，不走旧 useridTag 菜单逻辑。
            } else if(uni.getStorageSync("useridTag")==1){
                this.userid=uni.getStorageSync("useridTag");
                uni.removeStorageSync("useridTag");
            } else {
                this.userid = "";
            }
			this.btnColor = this.btnColor.sort(()=> {
				return (0.5-Math.random());
			});
			this.clicknumColor = this.clicknumColor.sort(()=> {
				return (0.5-Math.random());
			});
            let res = {};
            if(this.userid) {
                res = await this.$api.page('shangpinleixing', {page:1,limit:100});
            } else {
                res = await this.$api.list('shangpinleixing', {page:1,limit:100});
            }
			res.data.list.splice(0,0,{id:0,shangpinleixing:'全部'})
			this.categoryList = res.data.list;
			this.hasNext = true
			// 重新加载数据
			if (this.mescroll) this.mescroll.resetUpScroll()
		},
		async onLoad(options) {
			this.centerScope = options.centerScope || ''
			this.owner = options.owner ? decodeURIComponent(options.owner) : ''
			if (this.centerScope) uni.removeStorageSync("useridTag")
            if(this.centerScope) {
                this.userid = "";
            } else if(options.userid) {
                this.userid=options.userid;
            } else if(!this.centerScope && uni.getStorageSync("useridTag")==1){
                this.userid=uni.getStorageSync("useridTag");
                uni.removeStorageSync("useridTag");
            } else {
                this.userid = "";
            }
			this.hasNext = true
			// 重新加载数据
			// if (this.mescroll) this.mescroll.resetUpScroll()
		},
		onPageScroll(e) {
			this.scrollTop = e.scrollTop || 0
		},
		components: {
		},
		methods: {
			scrollTopClick() {
				uni.pageScrollTo({
					scrollTop: 0,
					duration: 240
				})
				if (this.mescroll && this.mescroll.scrollTo) {
					this.mescroll.scrollTo(0, 240)
				}
			},
			screenReset(){
				this.searchForm = {}
				this.search()
				this.$forceUpdate()
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
			sortClick(type){
				if(this.listSort==type){
					if(this.listOrder == 'desc'){
						this.listOrder = 'asc'
					}else{
						this.listOrder = 'desc'
					}
				}else{
					this.listSort = type
					this.listOrder = 'desc'
				}
				this.search()
			},
            priceChange(price) {
                return Number(price).toFixed(2);
            },
            preHttp(str) {
                return str && str.substr(0,4)=='http';
            },
            withImageVersion(url) {
                if (!url) return '';
                return url + (url.indexOf('?') > -1 ? '&' : '?') + 'v=20260525';
            },
			getReputationClass(level) {
				if (level === '优秀') return 'rep-excellent'
				if (level === '良好') return 'rep-good'
				if (level === '需谨慎') return 'rep-risk'
				return 'rep-normal'
			},
			async getSellerReputation(account) {
				if (!account) return {}
				if (this.reputationCache[account]) return this.reputationCache[account]
				try {
					let res = await this.$api.list('yonghu', {page: 1, limit: 1, zhanghao: account})
					let user = ((res.data && res.data.list) || [])[0] || {}
					this.reputationCache[account] = {
						xinyudengji: user.xinyudengji || '普通',
						xinyufen: user.xinyufen || 60,
						xinyushuoming: user.xinyushuoming || ''
					}
				} catch (e) {
					this.reputationCache[account] = {xinyudengji: '普通', xinyufen: 60, xinyushuoming: ''}
				}
				return this.reputationCache[account]
			},
			async enrichReputation(items) {
				let list = items || []
				for (let item of list) {
					let reputation = await this.getSellerReputation(item.zhanghao)
					item.xinyudengji = reputation.xinyudengji
					item.xinyufen = reputation.xinyufen
					item.xinyushuoming = reputation.xinyushuoming
				}
				return list
			},
			applySecondhandFilters(items) {
				let list = items || []
				if (this.categoryName && this.categoryName != '全部') {
					list = list.filter(item => String(item.shangpinleixing || '').indexOf(this.categoryName) > -1)
				}
				if (this.searchForm.pinpai) {
					list = list.filter(item => String(item.pinpai || '').indexOf(this.searchForm.pinpai) > -1)
				}
				if (this.searchForm.jiagestart) {
					list = list.filter(item => Number(item.jiage || 0) >= Number(this.searchForm.jiagestart))
				}
				if (this.searchForm.jiageend) {
					list = list.filter(item => Number(item.jiage || 0) <= Number(this.searchForm.jiageend))
				}
				return list
			},
			async runAiSearch() {
				let keyword = (this.searchForm.shangpinmingcheng || '').trim()
				if (!keyword || this.centerScope) return null
				let aiRes = await this.$api.aiSearch({query: keyword})
				let matches = ((aiRes.data || [])).filter(item => item.type === 'ershouliuzhuan')
				let list = []
				for (let match of matches) {
					try {
						let detailRes = await this.$api.info('ershouliuzhuan', match.id)
						if (detailRes && detailRes.data) {
							list.push(Object.assign({}, detailRes.data, {
								aiReason: match.reason,
								aiScore: match.score
							}))
						}
					} catch (e) {}
				}
				return await this.enrichReputation(this.applySecondhandFilters(list))
			},
			async fetchList(params) {
				if (this.centerScope === 'publishedSecondhand' && this.owner) {
					params.zhanghao = this.owner
					return await this.$api.list('ershouliuzhuan', params)
				}
				if(this.userid) {
					return await this.$api.page('ershouliuzhuan', params)
				}
				return await this.$api.list('ershouliuzhuan', params)
			},
			//类别搜索
			categoryClick(categoryName){
				this.categoryName = categoryName;
				this.hasNext = true;
				if (this.mescroll && this.mescroll.resetUpScroll) {
					this.mescroll.resetUpScroll();
					return;
				}
				this.search();
			},
			// mescroll组件初始化的回调,可获取到mescroll对象
			mescrollInit(mescroll) {
				this.mescroll = mescroll;
			},
			/*下拉刷新的回调 */
			downCallback(mescroll) {
				this.hasNext = true
				// 重置分页参数页数为1
				mescroll.resetUpScroll()
			},
			/*上拉加载的回调: mescroll携带page的参数, 其中num:当前页 从1开始, size:每页数据条数,默认10 */
			async upCallback(mescroll) {
				if ((this.searchForm.shangpinmingcheng || '').trim() && !this.centerScope) {
					if (mescroll.num > 1) {
						this.hasNext = false
						mescroll.endSuccess(0, false)
						return
					}
					try {
						let aiList = await this.runAiSearch()
						if (aiList && aiList.length) {
							this.aiSearchActive = true
							this.list = aiList
							this.lists = [this.list]
							this.hasNext = false
							mescroll.endSuccess(this.list.length, false)
							return
						}
						this.aiSearchActive = false
					} catch (e) {
						this.aiSearchActive = false
						this.$utils.msg('智能搜索暂不可用，已使用普通搜索')
					}
				}
				let params = {
					page: mescroll.num,
					limit: mescroll.size,
				}
				params['sort'] = this.listSort;
				params['order'] = this.listOrder;

				if(this.categoryName!='全部'){
					params.shangpinleixing = '%' + this.categoryName + '%'
				}
				if(this.searchForm.shangpinmingcheng){
					params['shangpinmingcheng'] = '%' + this.searchForm.shangpinmingcheng + '%'
				}
				if(this.searchForm.pinpai){
					params['pinpai'] = '%' + this.searchForm.pinpai + '%'
				}
				if(this.searchForm.jiage){
					params['jiage'] = '%' + this.searchForm.jiage + '%'
				}
				let user = uni.getStorageSync("appUserid")?JSON.parse(uni.getStorageSync('userSession')):{}
                let res = await this.fetchList(params)

				// 如果是第一页数据置空
				if (mescroll.num == 1) this.list = [];
				let rows = await this.enrichReputation(res.data.list || [])
				this.list = this.list.concat(rows);
				this.$forceUpdate()
				
				let length = Math.ceil(this.list.length/6)
				let arr = [];
				for (let i = 0; i<length; i++){
					arr[i] = this.list.slice(i*6, (i+1)*6)
				}
				this.lists = arr
				if ((res.data.list || []).length == 0) this.hasNext = false;
				mescroll.endSuccess(mescroll.size, this.hasNext);
			},
			// 详情
			onDetailTap(item) {
                uni.setStorageSync("useridTag",this.userid);
				uni.navigateTo({
					url: `./detail?id=${item.id}&userid=${this.userid || ''}`
				})
			},
			onUpdate(e){
				this.onUpdateTap(e.currentTarget.dataset.row)
			},
			// 修改
			onUpdateTap(row){
                uni.setStorageSync("useridTag",this.userid);
				this.$utils.jump(`./add-or-update?id=${row.id}`)
			},
			// 添加
			onAddTap(){
				if(!uni.getStorageSync("appUserid")){
					this.$utils.msg('请先登录')
					setTimeout(() => {
						this.$utils.jump('../login/login')
					}, 800)
					return
				}
				if(!this.$utils.requireVerified()){
					return
				}
                uni.setStorageSync("useridTag",this.userid);
				this.$utils.jump(`./add-or-update`)
			},
			onDelete(e){
				this.onDeleteTap(e.currentTarget.dataset.row.id)
			},
			onDeleteTap(id){
				var _this = this;
				uni.showModal({
					title: '提示',
					content: '是否确认删除',
					success: async function(res) {
						if (res.confirm) {
							await _this.$api.del('ershouliuzhuan', JSON.stringify([id]));
							let obj = await _this.$api.list('storeup',{
								page: 1,
								limit: 100,
								tablename: 'ershouliuzhuan',
								refid: id,
							})
							if(obj.data.list.length){
								let arr = []
								for(let x in obj.data.list){
									arr.push(obj.data.list[x].id)
								}
								await _this.$api.del('storeup',JSON.stringify(arr))
							}
							_this.$utils.msg('删除成功');
							_this.hasNext = true
							// 重置分页参数页数为1
							_this.search()
						}
					}
				});
			},
			// 搜索
			async search(){
				if (this.mescroll && this.mescroll.resetUpScroll) {
					this.hasNext = true
					this.mescroll.resetUpScroll()
					this.screenBoxShow = false
					return
				}
				this.mescroll.num = 1
				let searchForm = {
					page: this.mescroll.num,
					limit: this.mescroll.size,
				}
				searchForm['sort'] = this.listSort;
				searchForm['order'] = this.listOrder;

				if(this.searchForm.shangpinmingcheng){
					searchForm['shangpinmingcheng'] = '%' + this.searchForm.shangpinmingcheng + '%'
				}
				if(this.categoryName!='全部'){
					searchForm.shangpinleixing = '%' + this.categoryName + '%'
				}
				if(this.searchForm.pinpai){
					searchForm['pinpai'] = '%' + this.searchForm.pinpai + '%'
				}
				if(this.searchForm.jiagestart){
					searchForm['jiagestart'] = this.searchForm.jiagestart
				}
				if(this.searchForm.jiageend){
					searchForm['jiageend'] = this.searchForm.jiageend
				}
                let res = await this.fetchList(searchForm)
				// 如果是第一页数据置空
				if (this.mescroll.num == 1) this.list = [];
				let rows = await this.enrichReputation(res.data.list || [])
				this.list = this.list.concat(rows);
				
				let length = Math.ceil(this.list.length/6)
				let arr = [];
				for (let i = 0; i<length; i++){
					arr[i] = this.list.slice(i*6, (i+1)*6)
				}
				this.lists = arr
				if ((res.data.list || []).length == 0) this.hasNext = false;
				this.mescroll.endSuccess(this.mescroll.size, this.hasNext);
				this.screenBoxShow = false
			}
		}
	};
</script>

<style lang="scss" scoped>
	.content {
		min-height: calc(100vh - 44px);
		box-sizing: border-box;
	}
	.category-one .tab {
		cursor: pointer;
		border-radius: 0;
		padding: 0;
		color: #000;
		background: none;
		display: inline-block;
		width: 100%;
		font-size: 28rpx;
		line-height: 80rpx;
		text-align: center;
	}
	
	.category-one .tab.active {
		cursor: pointer;
		border-radius: 0;
		padding: 0;
		color: #fff;
		background: linear-gradient( 104deg, #489DF3 0%, #28CBB6 100%);
		display: inline-block;
		width: 100%;
		font-size: 28rpx;
		line-height: 80rpx;
		text-align: center;
	}
	.screenBox {
		padding: 20rpx 0 20rpx 0;
		transform: translate3d(100%, 0, 0);
		z-index: 666;
		top: 0;
		background: #fff;
		width: 80%;
		position: absolute;
		right: 0;
		transition: transform .3s;
		height: 100%;
		.screenTab {
			border: 2rpx solid rgb(162, 144, 104);
			border-radius: 40rpx;
			margin: 10rpx 0 10rpx 0;
			background: none;
			width: calc(100% / 3 - 24rpx);
			line-height: 72rpx;
			text-align: center;
		}
		.screenTabActive {
			border-radius: 40rpx;
			margin: 10rpx 0 10rpx 0;
			color: #fff;
			background: linear-gradient( 133deg, #459FEF 0%, #2BC8BA 96%);
			width: calc(100% / 3 - 20rpx);
			line-height: 72rpx;
			text-align: center;
		}
	}
	.screenBoxActive {
		transform: translate3d(0, 0, 0);
	}
	.content {
		background: #f5f7f8 !important;
		padding-bottom: 40rpx !important;
	}
	.search {
		margin: 20rpx 24rpx 0 !important;
		width: calc(100% - 48rpx) !important;
		padding: 0 !important;
		border-radius: 0 !important;
		background: transparent !important;
		box-shadow: none !important;
	}
	.search .search-form {
		height: 78rpx !important;
		border: 1rpx solid #d8e3e8 !important;
		border-radius: 16rpx !important;
		background: #fff !important;
		box-shadow: 0 10rpx 28rpx rgba(29, 41, 57, .06) !important;
	}
	.search input {
		height: 78rpx !important;
		line-height: 78rpx !important;
		font-size: 28rpx !important;
	}
	.search .cu-btn {
		top: 0 !important;
		right: 0 !important;
		width: 150rpx !important;
		height: 78rpx !important;
		line-height: 78rpx !important;
		border-radius: 16rpx !important;
		background: #13b8a7 !important;
		box-shadow: 0 10rpx 24rpx rgba(19, 184, 167, .20) !important;
	}
	.category-one {
		margin: 0 0 22rpx !important;
		padding: 8rpx !important;
		width: 100% !important;
		flex: 0 0 100% !important;
		white-space: nowrap !important;
		border: 1rpx solid #e6edf0 !important;
		border-radius: 16rpx !important;
		overflow: hidden !important;
		background: #fff !important;
		box-shadow: 0 10rpx 28rpx rgba(29, 41, 57, .05) !important;
	}
	.category-one .tab {
		width: auto !important;
		min-width: 128rpx !important;
		height: 58rpx !important;
		line-height: 58rpx !important;
		display: inline-block !important;
		margin: 0 8rpx 0 0 !important;
		padding: 0 22rpx !important;
		border-radius: 14rpx !important;
		color: #344054 !important;
		background: #f2f5f6 !important;
		font-size: 25rpx !important;
	}
	.category-one .tab.active,
	.screenBox .screenTabActive {
		background: #13b8a7 !important;
		color: #fff !important;
		font-weight: 600 !important;
	}
	.uni-product-list {
		width: 100% !important;
		flex: 0 0 100% !important;
		gap: 20rpx 0 !important;
	}
	.uni-product {
		width: 48.4% !important;
		border-radius: 16rpx !important;
		background: #fff !important;
		border: 1rpx solid #e6edf0 !important;
		box-shadow: 0 10rpx 28rpx rgba(29, 41, 57, .06) !important;
		overflow: hidden !important;
		padding-bottom: 16rpx !important;
	}
	.uni-product-image,
	.card-cover {
		height: 248rpx !important;
		margin: 14rpx 18rpx 10rpx !important;
		width: calc(100% - 36rpx) !important;
		border-radius: 14rpx !important;
		background: #f3f7f8 !important;
		object-fit: cover !important;
		display: block !important;
	}
	.uni-product-title,
	.card-title {
		color: #1d2939 !important;
		font-size: 26rpx !important;
		line-height: 42rpx !important;
		min-height: 56rpx !important;
		max-height: 96rpx !important;
		padding: 14rpx 18rpx 4rpx !important;
		white-space: normal !important;
		overflow: hidden !important;
		text-overflow: clip !important;
		word-break: break-all !important;
	}
	.card-stock,
	.uni-product-title:nth-child(2) {
		color: #0f9f93 !important;
		font-size: 24rpx !important;
		line-height: 38rpx !important;
		font-weight: 600 !important;
		min-height: 44rpx !important;
		padding: 2rpx 18rpx 4rpx !important;
		margin-bottom: 10rpx !important;
		white-space: normal !important;
	}
	.card-stock.sold-out {
		color: #d9534f !important;
	}
	.ai-match-tag {
		margin: 8rpx 18rpx 12rpx;
		padding: 8rpx 12rpx;
		border-radius: 10rpx;
		background: #e8f7ff;
		color: #116a9c;
		font-size: 22rpx;
		line-height: 32rpx;
	}
	.reputation-tag {
		display: inline-block;
		margin-left: 8rpx;
		padding: 2rpx 8rpx;
		border-radius: 8rpx;
		font-size: 20rpx;
		line-height: 28rpx;
		vertical-align: middle;
	}
	.rep-excellent {
		background: #e6f7ed;
		color: #16834a;
	}
	.rep-good {
		background: #e7f8f6;
		color: #0f9f93;
	}
	.rep-normal {
		background: #eef2f5;
		color: #63717c;
	}
	.rep-risk {
		background: #fff2df;
		color: #b25b00;
	}
	image {
		border-radius: 14rpx !important;
	}
	.add-btn {
		margin: 20rpx 16rpx 0 0 !important;
		width: 132rpx !important;
		height: 64rpx !important;
		line-height: 64rpx !important;
		border-radius: 14rpx !important;
		background: #13b8a7 !important;
		box-shadow: none !important;
	}
	.back-top {
		position: fixed;
		right: 24rpx;
		bottom: 150rpx;
		z-index: 680;
		width: 72rpx;
		height: 72rpx;
		border-radius: 50%;
		background: #ffffff;
		border: 1rpx solid #e6edf0;
		box-shadow: 0 10rpx 28rpx rgba(29, 41, 57, .12);
		display: flex;
		align-items: center;
		justify-content: center;
		color: #13b8a7;
	}
	.back-top .icon {
		font-size: 36rpx;
		line-height: 1;
	}
	.center-empty {
		width: 100%;
		margin: 40rpx 0;
		padding: 44rpx 20rpx;
		border-radius: 18rpx;
		background: #fff;
		color: #8b98a4;
		text-align: center;
		font-size: 26rpx;
		box-shadow: 0 8rpx 24rpx rgba(24, 35, 47, .05);
	}
</style>
