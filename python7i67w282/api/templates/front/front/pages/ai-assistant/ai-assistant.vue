<template>
	<view class="content">
		<view class="hero">
			<view class="hero-title">AI校园物品流转助手</view>
			<view class="hero-subtitle">自然语言搜索、失物匹配、内容审核和推荐解释集中体验。</view>
		</view>
		<view class="panel">
			<view class="tabs">
				<view class="tab" :class="{active: mode == 'search'}" @tap="mode='search'">智能搜索</view>
				<view class="tab" :class="{active: mode == 'match'}" @tap="mode='match'">失物匹配</view>
				<view class="tab" :class="{active: mode == 'moderate'}" @tap="mode='moderate'">内容审核</view>
			</view>
			<textarea v-if="mode != 'match'" class="input" v-model="query" :placeholder="placeholder"></textarea>
			<button class="primary" :loading="loading" :disabled="loading" @tap="runAiTask">{{buttonText}}</button>
		</view>
		<view class="result" v-if="result">
			<view class="result-title">AI 结果</view>
			<block v-if="mode == 'search'">
				<view class="empty" v-if="result.length == 0">暂未找到相关内容，可换一种描述。</view>
				<view class="item" v-for="(item,index) in result" :key="index" @tap="goDetail(item)">
					<view class="item-title">{{item.title}}</view>
					<view class="item-meta">{{item.type}} · 匹配分 {{item.score}}</view>
					<view class="item-reason">{{item.reason}}</view>
				</view>
			</block>
			<block v-if="mode == 'match'">
				<view class="empty" v-if="result.length == 0">暂无可疑似匹配的认领申请。</view>
				<view class="item" v-for="(item,index) in result" :key="index">
					<view class="item-title">{{item.itemName}}</view>
					<view class="item-meta">失物 #{{item.lostId}} · 认领 #{{item.claimId}} · {{item.score}}分</view>
					<view class="item-reason">{{item.reason}}</view>
					<view class="item-reason">核验：{{item.verifyQuestions.join('；')}}</view>
				</view>
			</block>
			<block v-if="mode == 'moderate'">
				<view class="item">
					<view class="item-title">风险等级：{{result.riskLevel}}</view>
					<view class="item-meta">处理建议：{{result.action}}</view>
					<view class="item-reason">{{result.summary}}</view>
					<view class="item-reason">边界：{{result.guardrails.join('；')}}</view>
				</view>
			</block>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				mode: 'search',
				query: '',
				loading: false,
				result: null
			}
		},
		computed: {
			placeholder() {
				if (this.mode == 'search') {
					return '例如：我想买一辆300以内的二手自行车，或者我丢了黑色蓝牙耳机'
				}
				return '粘贴商品描述、评论或认领申请，检测隐私、诈骗、违规交易风险'
			},
			buttonText() {
				if (this.mode == 'search') return '开始智能搜索'
				if (this.mode == 'match') return '生成失物匹配'
				return '检测内容风险'
			}
		},
		methods: {
			async runAiTask() {
				if (this.mode != 'match' && !this.query) {
					this.$utils.msg('请先输入内容')
					return
				}
				this.loading = true
				try {
					let res
					if (this.mode == 'search') {
						res = await this.$api.aiSearch({query: this.query})
					} else if (this.mode == 'match') {
						res = await this.$api.aiLostfoundMatch({})
					} else {
						res = await this.$api.aiModerate({text: this.query})
					}
					this.result = res.data
				} catch(e) {
					this.$utils.msg('AI助手暂不可用')
				}
				this.loading = false
			},
			goDetail(item) {
				if (!item || !item.id) return
				uni.navigateTo({
					url: `/pages/${item.type}/detail?id=${item.id}`
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.content {
		min-height: calc(100vh - 44px);
		background: #f4f7fb;
		padding: 24rpx;
		box-sizing: border-box;
	}
	.hero {
		padding: 28rpx 8rpx 20rpx;
	}
	.hero-title {
		font-size: 40rpx;
		font-weight: 700;
		color: #102a43;
		line-height: 1.4;
	}
	.hero-subtitle {
		font-size: 26rpx;
		color: #526579;
		line-height: 1.6;
		margin-top: 8rpx;
	}
	.panel,
	.result {
		background: #fff;
		border-radius: 12rpx;
		padding: 24rpx;
		margin-top: 20rpx;
	}
	.tabs {
		display: flex;
		gap: 12rpx;
		margin-bottom: 20rpx;
	}
	.tab {
		flex: 1;
		text-align: center;
		font-size: 26rpx;
		line-height: 64rpx;
		color: #526579;
		background: #eef3f8;
		border-radius: 8rpx;
	}
	.tab.active {
		color: #fff;
		background: #1f7a8c;
	}
	.input {
		width: 100%;
		min-height: 180rpx;
		box-sizing: border-box;
		border: 2rpx solid #d9e2ec;
		border-radius: 8rpx;
		padding: 20rpx;
		font-size: 26rpx;
		color: #102a43;
		margin-bottom: 20rpx;
	}
	.primary {
		width: 100%;
		height: 76rpx;
		line-height: 76rpx;
		background: #1f7a8c;
		color: #fff;
		border-radius: 10rpx;
		font-size: 28rpx;
	}
	.result-title {
		font-size: 30rpx;
		font-weight: 700;
		color: #102a43;
		margin-bottom: 12rpx;
	}
	.item {
		border-top: 2rpx solid #eef3f8;
		padding: 18rpx 0;
	}
	.item-title {
		font-size: 28rpx;
		font-weight: 600;
		color: #102a43;
		line-height: 1.5;
	}
	.item-meta,
	.item-reason,
	.empty {
		font-size: 24rpx;
		color: #526579;
		line-height: 1.6;
		margin-top: 6rpx;
	}
</style>
