import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
	import news from '@/views/modules/news/list'
	import renlingshenqing from '@/views/modules/renlingshenqing/list'
	import goumaidingdan from '@/views/modules/goumaidingdan/list'
	import sensitivewords from '@/views/modules/sensitivewords/list'
	import storeup from '@/views/modules/storeup/list'
	import ershouliuzhuan from '@/views/modules/ershouliuzhuan/list'
	import shiwuzhaoling from '@/views/modules/shiwuzhaoling/list'
	import yonghu from '@/views/modules/yonghu/list'
	import discussnews from '@/views/modules/discussnews/list'
	import shangpinleixing from '@/views/modules/shangpinleixing/list'
	import discussershouliuzhuan from '@/views/modules/discussershouliuzhuan/list'
	import config from '@/views/modules/config/list'
	import discussshiwuzhaoling from '@/views/modules/discussshiwuzhaoling/list'
	import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
	path: '/',
	name: '首页',
	component: Index,
	children: [{
		path: '/',
		name: '首页',
		component: Home,
		meta: {icon:'', title:'home', affix: true}
	}, {
		path: '/workbench',
		name: '工作台',
		component: Home,
		meta: {icon:'', title:'workbench', affix: true}
	}, {
		path: '/updatePassword',
		name: '修改密码',
		component: UpdatePassword,
		meta: {icon:'', title:'updatePassword'}
	}, {
		path: '/pay',
		name: '支付',
		component: pay,
		meta: {icon:'', title:'pay'}
	}, {
		path: '/center',
		name: '个人信息',
		component: center,
		meta: {icon:'', title:'center'}
	}
	,{
		path: '/news',
		name: '校园动态',
		component: news
	}
	,{
		path: '/renlingshenqing',
		name: '认领申请',
		component: renlingshenqing
	}
	,{
		path: '/goumaidingdan',
		name: '购买订单',
		component: goumaidingdan
	}
	,{
		path: '/sensitivewords',
		name: '敏感词',
		component: sensitivewords
	}
	,{
		path: '/storeup',
		name: '我的收藏',
		component: storeup
	}
	,{
		path: '/ershouliuzhuan',
		name: '二手流转',
		component: ershouliuzhuan
	}
	,{
		path: '/shiwuzhaoling',
		name: '失物招领',
		component: shiwuzhaoling
	}
	,{
		path: '/yonghu',
		name: '用户',
		component: yonghu
	}
	,{
		path: '/discussnews',
		name: '校园动态',
		component: discussnews
	}
	,{
		path: '/shangpinleixing',
		name: '商品类型',
		component: shangpinleixing
	}
	,{
		path: '/discussershouliuzhuan',
		name: '二手流转评论',
		component: discussershouliuzhuan
	}
	,{
		path: '/config',
		name: '轮播图管理',
		component: config
	}
	,{
		path: '/discussshiwuzhaoling',
		name: '失物招领评论',
		component: discussshiwuzhaoling
	}
	,{
		path: '/newstype',
		name: '校园动态分类',
		component: newstype
	}
	]
	},
	{
		path: '/login',
		name: 'login',
		component: Login,
		meta: {icon:'', title:'login'}
	},
	{
		path: '/register',
		name: 'register',
		component: register,
		meta: {icon:'', title:'register'}
	},
	{
		path: '*',
		component: NotFound
	}
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
	mode: 'hash',
	/*hash模式改为history*/
	routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}
export default router;
