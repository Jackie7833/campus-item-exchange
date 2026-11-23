<template>
<!-- category 1 -->
	<mescroll-uni @init="mescrollInit" :up="upOption" :down="downOption" @down="downCallback" @up="upCallback">
		<view class="content">
			<view :style='{"minHeight":"100%","padding":"0 20rpx","flexWrap":"wrap","background":"#F9FAFA","display":"flex","width":"100%","position":"relative","height":"auto"}'>
				<view class="cu-bar bg-white search" :style='{"padding":"20rpx 0 0 0","margin":"0","background":"none","display":"flex","width":"100%","position":"relative","height":"auto","order":"1"}'>
					<view :style='{"border":"2rpx solid #ACACAC","margin":"0","borderRadius":"20rpx","flex":"1","background":"#fff","lineHeight":"80rpx","position":"relative","height":"80rpx"}' class="search-form round">
						<text class="icon iconfont icon-fangdajing07" :style='{"color":"rgb(153, 153, 153)","left":"0px","textAlign":"center","width":"80rpx","fontSize":"40rpx","lineHeight":"80rpx","position":"absolute","right":"0px"}'></text>
						<input placeholder-style="color: #333" :style='{"border":"0","padding":"12rpx 20rpx 12rpx 80rpx","color":"#333","borderRadius":"40rpx","background":"none","width":"100%","lineHeight":"80rpx","fontSize":"28rpx","height":"80rpx"}' v-model="searchForm.searchKeyword" type="text" placeholder="AI失物匹配，如 黑色水杯 图书馆" ></input>
					</view>
					<button :style='{"border":"0","padding":"0px","margin":"0","color":"#fff","right":"0px","borderRadius":"20rpx","top":"20rpx","background":"linear-gradient( 104deg, #489DF3 0%, #28CBB6 100%)","width":"172rpx","lineHeight":"80rpx","fontSize":"28rpx","position":"absolute","height":"80rpx","zIndex":"99"}' @tap="search" class="cu-btn shadow-blur round">匹配</button>
				</view>
			

				<view :style='{"width":"100%","margin":"20rpx 0","flexWrap":"wrap","display":"flex","order":"4"}'>
					<view @click="sortClick('addtime')" :style='{"border":"2rpx solid rgb(153, 152, 152)","padding":"0 12rpx","margin":"0 20rpx 0 0","outline":"0","borderRadius":"8rpx","display":"flex"}'>
						<text :style='{"color":"#333","lineHeight":"48rpx","fontSize":"24rpx"}'>按日期</text>
						<text v-if="listSort!='addtime'" class="icon iconfont icon-shijian18" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
						<text v-else-if="listSort=='addtime'&&listOrder=='asc'" class="icon iconfont icon-shijian18" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
						<text v-else-if="listSort=='addtime'&&listOrder=='desc'" class="icon iconfont icon-shijian18" :style='{"margin":"0 4rpx 0 0","lineHeight":"48rpx","fontSize":"24rpx","color":"#333"}'></text>
					</view>
				</view>
				<view :style='{"width":"100%","flexWrap":"wrap","background":"none","display":"flex","height":"auto","order":"5"}'>
					<!-- 样式1 -->
					<view class="uni-product-list product-card-list" :style='{"padding":"0","margin":"0","flexWrap":"wrap","flex":"auto","display":"flex","width":"0","justifyContent":"space-between","height":"auto"}'>
						<view @tap="onDetailTap(product)" class="uni-product product-card" :style='{"width":"48%","boxShadow":"none","margin":"0 0 20rpx","backgroundColor":"#F3F9FF","height":"auto"}' v-for="(product,index) in list" :key="index">
							<view class="uni-product-title card-title">{{product.biaoti}}</view>
							<view v-if="product.aiReason" class="ai-match-tag">AI匹配 {{product.aiScore || 0}} · {{product.aiReason}}</view>
							<image class="uni-product-image card-cover" mode="aspectFill" v-if="preHttp(product.tupian)" :src="withImageVersion(product.tupian.split(',')[0])"></image>
							<image class="uni-product-image card-cover" mode="aspectFill" v-else :src="product.tupian?withImageVersion(baseUrl+product.tupian.split(',')[0]):''"></image>
							<view class="card-stock">状态:{{product.zhuangtai}}</view>

							<view :style='{"border":"none","padding":"0 0 0 20rpx","margin":"20rpx 0 0","textAlign":"left"}'>
								<text class="icon iconfont icon-shijian21" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.addtime.split(' ')[0].replace(/\-/g,'-')}}</text>
							</view>
							<view :style='{"padding":"0 20rpx"}'>
								<text class="icon iconfont icon-geren16" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.zhanghao}}</text>
							</view>
							<view :style='{"padding":"0 20rpx"}'>
								<text class="icon iconfont icon-shoucang10" :style='{"margin":"0 4rpx 0 0","lineHeight":"1.5","fontSize":"24rpx","color":"#666"}'></text>
								<text :style='{"color":"#666","lineHeight":"1.5","fontSize":"24rpx"}'>{{product.storeupnum}}</text>
							</view>
							<!-- #ifdef MP-WEIXIN -->
							<view :style='{"width":"100%","padding":"8rpx 0","justifyContent":"space-between","display":"flex","height":"auto"}'>
								<view :style='{"padding":"8rpx 12rpx","background":"#6683A2","display":"flex"}' v-if="(userid && isAuth('shiwuzhaoling','修改')) || (!userid && isAuthFront('shiwuzhaoling','修改'))" @tap.stop.proevent="onUpdate" :data-row="product">
									<text :style='{"margin":"0 8rpx 0 0","fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}' class="cuIcon-edit"></text>
									<text :style='{"fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}'>修改</text>
								</view>
								<view :style='{"padding":"8rpx 12rpx","background":"#6683A2","display":"flex"}' v-if="(userid && isAuth('shiwuzhaoling','删除')) || (!userid && isAuthFront('shiwuzhaoling','删除'))" @tap.stop.proevent="onDelete" :data-row="product">
									<text :style='{"margin":"0 8rpx 0 0","fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}' class="cuIcon-delete"></text>
									<text :style='{"fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}'>删除</text>
								</view>
							</view>
							<!-- #endif -->
							<!-- #ifndef MP-WEIXIN -->
							<view :style='{"width":"100%","padding":"8rpx 0","justifyContent":"space-between","display":"flex","height":"auto"}'>
								<view :style='{"padding":"8rpx 12rpx","background":"#6683A2","display":"flex"}' v-if="(userid && isAuth('shiwuzhaoling','修改')) || (!userid && isAuthFront('shiwuzhaoling','修改'))" @tap.stop.proevent="onUpdateTap(product)">
									<text :style='{"margin":"0 8rpx 0 0","fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}' class="cuIcon-edit"></text>
									<text :style='{"fontSize":"24rpx","lineHeight":"1","color":"#fff","display":"inline-block"}'>修改</text>
								</view>
								<view :style='{"padding":"8rpx 12rpx","background":"#6683A2","display":"flex"}' v-if="(userid && isAuth('shiwuzhaoling','删除')) || (!userid && isAuthFront('shiwuzhaoling','删除'))" @tap.stop.proevent="onDeleteTap(product.id)">
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
				<view :style='{"top":"0","left":"0","background":"rgba(0, 0, 0, .3)","width":"100%","position":"absolute","height":"100%","zIndex":"665"}' v-if="screenBoxShow" @click="screenBoxShow=false"></view>
				<view class="screenBox" :class="screenBoxShow?'screenBoxActive':''">
					<view :style='{"width":"100%","padding":"20rpx 0 20rpx 0","alignItems":"center","flexWrap":"wrap","justifyContent":"space-around","display":"flex"}'>
						<view :style='{"width":"100%","padding":"0 0 0 20rpx","fontSize":"24rpx"}'>物品名称</view>
						<input :style='{"border":"2rpx solid rgb(162, 144, 104)","padding":"0 20rpx 0 20rpx","borderRadius":"40rpx","background":"none","width":"90%","fontSize":"24rpx","height":"60rpx"}' placeholder="请输入物品名称" v-model="searchForm.wupinmingcheng">
					</view>
					<view :style='{"width":"100%","padding":"20rpx 0 20rpx 0","alignItems":"center","flexWrap":"wrap","justifyContent":"space-around","display":"flex"}'>
						<view :style='{"width":"100%","padding":"0 0 0 20rpx","fontSize":"24rpx"}'>物品类型</view>
						<input :style='{"border":"2rpx solid rgb(162, 144, 104)","padding":"0 20rpx 0 20rpx","borderRadius":"40rpx","background":"none","width":"90%","fontSize":"24rpx","height":"60rpx"}' placeholder="请输入物品类型" v-model="searchForm.wupinleixing">
					</view>
					<view :style='{"width":"100%","padding":"20rpx 0 20rpx 0","alignItems":"center","flexWrap":"wrap","justifyContent":"space-around","display":"flex"}'>
						<view :style='{"width":"100%","padding":"0 0 0 20rpx","fontSize":"24rpx"}'>拾取地点</view>
						<input :style='{"border":"2rpx solid rgb(162, 144, 104)","padding":"0 20rpx 0 20rpx","borderRadius":"40rpx","background":"none","width":"90%","fontSize":"24rpx","height":"60rpx"}' placeholder="请输入拾取地点" v-model="searchForm.shiqudidian">
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
					searchKeyword: '',
					wupinmingcheng: '',
					wupinleixing: '',
					shiqudidian: '',
				},
				CustomBar: '0',
				listSort: 'id',
				listOrder: 'desc',
				screenBoxShow: false,
				aiMatchActive: false,
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
		components: {
		},
		methods: {
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
                return url + (url.indexOf('?') > -1 ? '&' : '?') + 'v=20260525b';
            },
			applyLostFilters(items) {
				let list = items || []
				if (this.searchForm.wupinmingcheng) {
					list = list.filter(item => String(item.wupinmingcheng || '').indexOf(this.searchForm.wupinmingcheng) > -1)
				}
				if (this.searchForm.wupinleixing) {
					list = list.filter(item => String(item.wupinleixing || '').indexOf(this.searchForm.wupinleixing) > -1)
				}
				if (this.searchForm.shiqudidian) {
					list = list.filter(item => String(item.shiqudidian || '').indexOf(this.searchForm.shiqudidian) > -1)
				}
				return list
			},
			getLostKeyword() {
				return (this.searchForm.searchKeyword || '').trim()
			},
			async runAiLostMatch() {
				let keyword = this.getLostKeyword()
				if (!keyword || this.centerScope) return null
				let aiRes = await this.$api.aiLostfoundMatch({query: keyword})
				let matches = aiRes.data || []
				let seen = {}
				let list = []
				for (let match of matches) {
					if (!match.lostId || seen[match.lostId]) continue
					seen[match.lostId] = true
					try {
						let detailRes = await this.$api.info('shiwuzhaoling', match.lostId)
						if (detailRes && detailRes.data) {
							list.push(Object.assign({}, detailRes.data, {
								aiReason: match.reason,
								aiScore: match.score
							}))
						}
					} catch (e) {}
				}
				return this.applyLostFilters(list)
			},
			async runPlainLostKeywordSearch() {
				let keyword = this.getLostKeyword()
				let params = {
					page: 1,
					limit: 100,
					sort: this.listSort,
					order: this.listOrder,
				}
				if(this.searchForm.wupinmingcheng){
					params['wupinmingcheng'] = '%' + this.searchForm.wupinmingcheng + '%'
				}
				if(this.searchForm.wupinleixing){
					params['wupinleixing'] = '%' + this.searchForm.wupinleixing + '%'
				}
				if(this.searchForm.shiqudidian){
					params['shiqudidian'] = '%' + this.searchForm.shiqudidian + '%'
				}
				let res = await this.fetchList(params)
				let list = (res.data && res.data.list) || []
				if (keyword) {
					list = list.filter(item => {
						let text = [
							item.biaoti,
							item.wupinmingcheng,
							item.wupinleixing,
							item.wupinxiangqing,
							item.shiqudidian
						].join(' ')
						return text.indexOf(keyword) > -1
					})
				}
				return list
			},
			async fetchList(params) {
				if (this.centerScope === 'publishedLost' && this.owner) {
					params.zhanghao = this.owner
					return await this.$api.list('shiwuzhaoling', params)
				}
				if(this.userid) {
					return await this.$api.page('shiwuzhaoling', params)
				}
				return await this.$api.list('shiwuzhaoling', params)
			},
			//类别搜索
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
				if (this.getLostKeyword() && !this.centerScope) {
					if (mescroll.num > 1) {
						this.hasNext = false
						mescroll.endSuccess(0, false)
						return
					}
					try {
						let aiList = await this.runAiLostMatch()
						if (aiList && aiList.length) {
							this.aiMatchActive = true
							this.list = aiList
							this.lists = [this.list]
							this.hasNext = false
							mescroll.endSuccess(this.list.length, false)
							return
						}
						this.aiMatchActive = false
					} catch (e) {
						this.aiMatchActive = false
						this.$utils.msg('失物匹配暂不可用，已使用普通搜索')
					}
					let plainList = await this.runPlainLostKeywordSearch()
					this.list = plainList
					this.lists = [this.list]
					this.hasNext = false
					if (!this.list.length) this.$utils.msg('暂未找到高相似度记录')
					mescroll.endSuccess(this.list.length, false)
					return
				}
				let params = {
					page: mescroll.num,
					limit: mescroll.size,
				}
				params['sort'] = this.listSort;
				params['order'] = this.listOrder;

				if(this.searchForm.wupinmingcheng){
					params['wupinmingcheng'] = '%' + this.searchForm.wupinmingcheng + '%'
				}
				if(this.searchForm.wupinleixing){
					params['wupinleixing'] = '%' + this.searchForm.wupinleixing + '%'
				}
				if(this.searchForm.shiqudidian){
					params['shiqudidian'] = '%' + this.searchForm.shiqudidian + '%'
				}
				let user = uni.getStorageSync("appUserid")?JSON.parse(uni.getStorageSync('userSession')):{}
                let res = await this.fetchList(params)

				// 如果是第一页数据置空
				if (mescroll.num == 1) this.list = [];
				this.list = this.list.concat(res.data.list);
				this.$forceUpdate()
				
				let length = Math.ceil(this.list.length/6)
				let arr = [];
				for (let i = 0; i<length; i++){
					arr[i] = this.list.slice(i*6, (i+1)*6)
				}
				this.lists = arr
				if (res.data.list.length == 0) this.hasNext = false;
				mescroll.endSuccess(mescroll.size, this.hasNext);
			},
			// 详情
			onDetailTap(item) {
                uni.setStorageSync("useridTag",this.userid);
				this.$utils.jump(`./detail?id=${item.id}&userid=`+this.userid)
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
							await _this.$api.del('shiwuzhaoling', JSON.stringify([id]));
							let obj = await _this.$api.list('storeup',{
								page: 1,
								limit: 100,
								tablename: 'shiwuzhaoling',
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

				if (this.getLostKeyword() && !this.centerScope) {
					let plainList = await this.runPlainLostKeywordSearch()
					this.list = plainList
					this.lists = [this.list]
					this.hasNext = false
					this.mescroll.endSuccess(this.list.length, false)
					this.screenBoxShow = false
					return
				}
				if(this.searchForm.wupinmingcheng){
					searchForm['wupinmingcheng'] = '%' + this.searchForm.wupinmingcheng + '%'
				}
				if(this.searchForm.wupinleixing){
					searchForm['wupinleixing'] = '%' + this.searchForm.wupinleixing + '%'
				}
				if(this.searchForm.shiqudidian){
					searchForm['shiqudidian'] = '%' + this.searchForm.shiqudidian + '%'
				}
                let res = await this.fetchList(searchForm)
				// 如果是第一页数据置空
				if (this.mescroll.num == 1) this.list = [];
				this.list = this.list.concat(res.data.list);
				
				let length = Math.ceil(this.list.length/6)
				let arr = [];
				for (let i = 0; i<length; i++){
					arr[i] = this.list.slice(i*6, (i+1)*6)
				}
				this.lists = arr
				if (res.data.list.length == 0) this.hasNext = false;
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
		background: #f6f8fa !important;
	}
	.search {
		margin: 20rpx 24rpx !important;
		width: calc(100% - 48rpx) !important;
		border-radius: 18rpx !important;
		background: #fff !important;
		box-shadow: 0 8rpx 24rpx rgba(24, 35, 47, .06) !important;
	}
	.category-one {
		margin: 0 20rpx 0 0 !important;
		width: 160rpx !important;
		flex: 0 0 160rpx !important;
		border-radius: 16rpx !important;
		overflow: hidden !important;
		background: #fff !important;
	}
	.category-one .tab.active,
	.screenBox .screenTabActive {
		background: #12b3a8 !important;
	}
	.uni-product {
		border-radius: 18rpx !important;
		background: #fff !important;
		border: 1rpx solid #e5edf1 !important;
		box-shadow: 0 10rpx 30rpx rgba(24, 35, 47, .07) !important;
		overflow: hidden !important;
		padding: 14rpx 14rpx 18rpx !important;
	}
	.uni-product-title,
	.card-title {
		padding: 6rpx 4rpx !important;
		line-height: 42rpx !important;
		min-height: 42rpx !important;
		max-height: 84rpx !important;
		font-size: 28rpx !important;
		color: #12202b !important;
		white-space: normal !important;
		overflow: hidden !important;
		word-break: break-all !important;
	}
	.uni-product-image,
	.card-cover {
		width: 100% !important;
		height: 256rpx !important;
		margin: 10rpx 0 14rpx !important;
		border-radius: 14rpx !important;
		background: #f3f7f8 !important;
		object-fit: cover !important;
		display: block !important;
	}
	.card-stock {
		padding: 2rpx 4rpx 8rpx !important;
		color: #0f9f93 !important;
		font-size: 24rpx !important;
		line-height: 38rpx !important;
		font-weight: 600 !important;
		white-space: normal !important;
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
	image {
		border-radius: 14rpx !important;
	}
	.add-btn,
	.cu-btn {
		background: #12b3a8 !important;
		border-radius: 14rpx !important;
		box-shadow: 0 8rpx 18rpx rgba(18, 179, 168, .18) !important;
	}
	.screenBox {
		border-radius: 24rpx 0 0 24rpx !important;
		box-shadow: -8rpx 0 32rpx rgba(24, 35, 47, .12) !important;
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
