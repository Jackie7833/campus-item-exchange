<template>
	<div style="height: 100%;">
		<el-main class="admin-main" :style="mainStyle">
			<!-- top -->
			<index-header :style='{"border":"0","padding":"0 20px 0","alignItems":"center","color":"#333","display":"flex","justifyContent":"flex-end","top":"0","left":"0","background":"#fff","width":"100%","fontSize":"15px","position":"inherit","zIndex":"1001","height":"68px"}'></index-header>
			
			<!-- menu -->
			<template v-if="'vertical' == 'vertical'">
			  <template v-if="2 == 1">
				<index-aside :style='{"boxShadow":"1px 0 6px  rgba(64, 158, 255, .3)","overflow":"hidden","top":"0","left":"0","background":"#304156","bottom":"0","width":"210px","fontSize":"0px","position":"fixed","height":"100%","zIndex":"1001"}'></index-aside>
			  </template>
			  <template v-if="2 == 2">
				<index-aside :is-collapse="isCollapse" @oncollapsechange="collapseChange" :style='isCollapse ? {"boxShadow":"1px 0 6px  rgba(64, 158, 255, .3)","overflow":"hidden","top":"0","left":"0","background":"#304156","bottom":"0","width":"64px","fontSize":"0px","position":"fixed","transition":"width 0.3s","height":"100%","zIndex":"1001"} : {"border":"1px solid #F1F1F1","padding":"25px 0px","color":"#636C70","bottom":"0","display":"flex","transition":"width 0.3s","overflow":"hidden","top":"0px","left":"0","background":"#FFFFFF","width":"220px","fontSize":"15px","position":"fixed","fontWeight":"400","height":"100%","zIndex":"1001"}'></index-aside>
			  </template>
			</template>
			<template v-if="'vertical' == 'horizontal'">
			  <template v-if="2 == 1">
				<index-aside :style='{"width":"100%","borderColor":"#efefef","borderStyle":"solid","background":"#304156","borderWidth":"0 0 1px 0","height":"auto"}'></index-aside>
			  </template>
			  <template v-if="2 == 2">
				<index-aside :style='{"borderColor":"#efefef","background":"#FFF","borderWidth":"0 0 1px 0","display":"flex","width":"100%","borderStyle":"solid","height":"auto"}'></index-aside>
			  </template>
			</template>
			
			<!-- breadcrumb -->
			<bread-crumbs :title="title" :style='{"padding":"10px","margin":"10px 20px 0","borderColor":"#3b6885","borderWidth":"0 0 0px 0","background":" #FFFFFF","width":"calc(100% - 40px)","fontSize":"16px","borderStyle":"solid","boxSizing":"border-box"}' class="bread-crumbs"></bread-crumbs>
			
			<!-- TagsView -->
			<tags-view />
			<router-view class="router-view"></router-view>
		</el-main>
	</div>
</template>

<script>
	import IndexAside from '@/components/index/IndexAsideStatic'
	import IndexHeader from '@/components/index/IndexHeader'
	import TagsView from '@/components/index/TagsView'
	import menu from "@/utils/menu";
	export default {
		components: {
			IndexAside,
			IndexHeader,
			TagsView
		},
		data() {
			return {
				menuList: [],
				role: "",
				currentIndex: -2,
				itemMenu: [],
				title: '',
				isCollapse: false,
			};
		},
		computed: {
			mainStyle() {
				const sidebarWidth = this.isCollapse ? 64 : 220
				return {
					minHeight: '100%',
					padding: '0',
					margin: `0 0 0 ${sidebarWidth}px`,
					width: `calc(100% - ${sidebarWidth}px)`,
					maxWidth: `calc(100% - ${sidebarWidth}px)`,
					flexWrap: 'wrap',
					background: '#F3F6F8',
					flexDirection: 'column',
					display: 'flex',
					position: 'relative',
					boxSizing: 'border-box',
					overflowX: 'hidden'
				}
			}
		},
		mounted() {
			let menus = menu.list();
			this.menuList = menus;
			this.role = this.$storage.get("role");
		},
		created() {
			this.init();
		},
		methods: {
			init(){
				this.$nextTick(()=>{
					
				})
			},
			collapseChange(collapse) {
				this.isCollapse = collapse
			},
			menuHandler(menu) {
				this.$router.push({
					name: menu.tableName
				});
				this.title = menu.menu;
			},
			titleChange(index, menus) {
				this.currentIndex = index
				this.itemMenu = menus;
			},
			homeChange(index) {
				this.itemMenu = [];
				this.title = "工作台"
				this.currentIndex = index
				this.$router.push({
					name: '工作台'
				});
			},
			centerChange(index) {
				this.itemMenu = [{
					"buttons": ["新增", "查看", "修改", "删除"],
					"menu": "修改密码",
					"tableName": "updatePassword"
				}, {
					"buttons": ["新增", "查看", "修改", "删除"],
					"menu": "个人信息",
					"tableName": "center"
				}];
				this.title = ""
				this.currentIndex = index
				this.$router.push({
					name: '工作台'
				});
				
			}
		}
	};
</script>
<style lang="scss" scoped>
	a {
		text-decoration: none;
		color: #555;
	}

	a:hover {
		background: #00c292;
	}
	
	.el-main {
		padding: 0;
		display: block;
	}

	.admin-main {
		box-sizing: border-box;
		overflow-x: hidden;
		width: 100%;
	}

	.admin-main /deep/ .el-header,
	.admin-main /deep/ .bread-crumbs,
	.router-view {
		box-sizing: border-box;
		max-width: 100%;
	}

	.router-view {
		width: calc(100% - 40px);
		margin: 16px 20px 30px;
	}

	.nav-list {
		width: 100%;
		margin: 0 auto;
		text-align: left;
		margin-top: 20px;

		.nav-title {
			display: inline-block;
			font-size: 15px;
			color: #333;
			padding: 15px 25px;
			border: none;
		}

		.nav-title.active {
			color: #555;
			cursor: default;
			background-color: #fff;
		}
	}

	.nav-item {
		margin-top: 20px;
		background: #FFFFFF;
		padding: 15px 0;

		.menu {
			padding: 15px 25px;
		}
	}
	
	.detail-form-content {
	    background: transparent;
	}
</style>
