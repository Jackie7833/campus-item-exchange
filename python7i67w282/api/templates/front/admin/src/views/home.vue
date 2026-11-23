<template>
  <div v-if="isHomeLanding" class="home-landing-page">
    <section class="home-landing-hero">
      <div class="home-landing-copy">
        <p class="eyebrow">校园物品流转后台</p>
        <h1>基于小程序的校园物品流转平台</h1>
        <p class="subtext">后台首页保留为清晰的业务入口。统计数据、待处理事项和 AI 辅助线索已拆分到“工作台”。</p>
        <div class="home-landing-actions">
          <el-button type="primary" class="admin-ai-button" @click="$router.push('/workbench')">
            查看工作台
          </el-button>
          <el-button @click="$router.push('/ershouliuzhuan')">管理二手流转</el-button>
          <el-button @click="$router.push('/shiwuzhaoling')">管理失物招领</el-button>
        </div>
      </div>
    </section>

    <section class="home-entry-grid">
      <div v-for="item in homeEntries" :key="item.path" class="home-entry-card" @click="$router.push(item.path)">
        <div class="home-entry-icon"><i :class="item.icon"></i></div>
        <div>
          <h2>{{ item.title }}</h2>
          <p>{{ item.desc }}</p>
        </div>
      </div>
    </section>
  </div>

  <div v-else class="dashboard-page">
    <section class="dashboard-hero">
      <div>
        <p class="eyebrow">校园物品流转后台</p>
        <h1>数据总览仪表盘</h1>
        <p class="subtext">汇总二手商品、购买订单、支付状态、失物招领和待审核事项，便于日常管理和答辩展示。</p>
      </div>
      <el-button type="primary" class="admin-ai-button" :loading="loading" @click="loadDashboard">
        <i class="el-icon-refresh"></i>
        刷新数据
      </el-button>
    </section>

    <section class="metric-grid">
      <div v-for="item in metrics" :key="item.key" class="metric-card">
        <div class="metric-icon" :class="item.key"><i :class="item.icon"></i></div>
        <div>
          <div class="metric-value">{{ item.value }}</div>
          <div class="metric-label">{{ item.label }}</div>
          <div class="metric-note">{{ item.note }}</div>
        </div>
      </div>
    </section>

    <section class="dashboard-grid">
      <div class="dashboard-panel">
        <div class="panel-head">
          <div>
            <h2>订单状态概览</h2>
            <p>成交、待支付与购买数量集中展示。</p>
          </div>
        </div>
        <div class="status-grid">
          <div class="status-item paid">
            <span>已支付订单</span>
            <strong>{{ summary.paidOrderCount }}</strong>
          </div>
          <div class="status-item unpaid">
            <span>未支付订单</span>
            <strong>{{ summary.unpaidOrderCount }}</strong>
          </div>
          <div class="status-item rate">
            <span>订单转化率</span>
            <strong>{{ paidRate }}%</strong>
          </div>
        </div>
      </div>

      <div class="dashboard-panel">
        <div class="panel-head">
          <div>
            <h2>待处理事项</h2>
            <p>优先处理影响用户体验的审核和匹配事项。</p>
          </div>
        </div>
        <div class="todo-list">
          <div class="todo-item">
            <span>待审核认领申请</span>
            <strong>{{ summary.pendingClaimCount }}</strong>
          </div>
          <div class="todo-item">
            <span>失物招领信息</span>
            <strong>{{ summary.lostfoundCount }}</strong>
          </div>
          <div class="todo-item">
            <span>二手商品库存</span>
            <strong>{{ summary.secondhandStock }}</strong>
          </div>
        </div>
      </div>
    </section>

    <section class="dashboard-panel">
      <div class="panel-head">
        <div>
          <h2>AI 辅助线索</h2>
          <p>AI 只提供辅助判断，认领与审核仍由管理员人工确认。</p>
        </div>
        <el-button size="mini" type="primary" class="admin-ai-button" :loading="aiLoading" @click="loadAiMatches">
          刷新 AI
        </el-button>
      </div>
      <div v-if="aiLoading" class="empty-state">
        <i class="el-icon-loading"></i>
        正在分析失物与认领申请
      </div>
      <div v-else-if="aiMatches.length" class="ai-match-list">
        <div v-for="(item, index) in aiMatches" :key="index" class="ai-match-item">
          <div class="ai-match-title">
            <span>{{ item.itemName || item.title || '高匹配线索' }}</span>
            <el-tag size="mini" type="warning">{{ item.score || item.matchScore || '-' }}</el-tag>
          </div>
          <p>{{ item.reason || item.matchReason || '建议人工核验后再处理' }}</p>
        </div>
      </div>
      <div v-else class="empty-state">暂无高匹配 AI 线索</div>
    </section>
  </div>
</template>

<script>
import router from '@/router/router-static'
import ai from '@/utils/ai'

const emptySummary = {
  secondhandCount: 0,
  secondhandStock: 0,
  orderCount: 0,
  purchaseQuantity: 0,
  paidOrderCount: 0,
  unpaidOrderCount: 0,
  paidAmount: 0,
  lostfoundCount: 0,
  pendingClaimCount: 0
}

export default {
  data() {
    return {
      summary: Object.assign({}, emptySummary),
      loading: false,
      aiMatches: [],
      aiLoading: false
    }
  },
  computed: {
    isHomeLanding() {
      return this.$route.path === '/'
    },
    homeEntries() {
      return [
        { title: '用户管理', desc: '查看用户资料、学生证图片和审核状态。', path: '/yonghu', icon: 'el-icon-user' },
        { title: '二手流转', desc: '管理商品发布、库存、订单和交易状态。', path: '/ershouliuzhuan', icon: 'el-icon-shopping-bag-1' },
        { title: '失物招领', desc: '处理失物信息、认领申请和 AI 匹配线索。', path: '/shiwuzhaoling', icon: 'el-icon-box' },
        { title: '内容与配置', desc: '维护校园动态、分类、敏感词和轮播配置。', path: '/news', icon: 'el-icon-setting' }
      ]
    },
    metrics() {
      return [
        { key: 'secondhand', label: '二手商品发布数', value: this.summary.secondhandCount, note: `当前库存 ${this.summary.secondhandStock}`, icon: 'el-icon-shopping-bag-1' },
        { key: 'orders', label: '购买订单数', value: this.summary.orderCount, note: '全部购买记录', icon: 'el-icon-tickets' },
        { key: 'quantity', label: '购买总数量', value: this.summary.purchaseQuantity, note: '订单购买数量汇总', icon: 'el-icon-data-line' },
        { key: 'amount', label: '已支付成交金额', value: this.formatMoney(this.summary.paidAmount), note: '仅统计已支付订单', icon: 'el-icon-wallet' },
        { key: 'paid', label: '已支付订单数', value: this.summary.paidOrderCount, note: '订单状态为已支付', icon: 'el-icon-circle-check' },
        { key: 'unpaid', label: '未支付订单数', value: this.summary.unpaidOrderCount, note: '待支付或未完成', icon: 'el-icon-time' },
        { key: 'lost', label: '失物招领数', value: this.summary.lostfoundCount, note: '已发布失物信息', icon: 'el-icon-box' },
        { key: 'claims', label: '待审核认领', value: this.summary.pendingClaimCount, note: '需要管理员处理', icon: 'el-icon-finished' }
      ]
    },
    paidRate() {
      if (!this.summary.orderCount) return 0
      return Math.round(this.summary.paidOrderCount * 100 / this.summary.orderCount)
    }
  },
  mounted() {
    this.init()
  },
  watch: {
    '$route.path'() {
      if (!this.isHomeLanding) {
        this.loadDashboard()
        this.loadAiMatches()
      }
    }
  },
  methods: {
    init() {
      if (this.$storage.get('Token')) {
        this.$http({
          url: `${this.$storage.get('sessionTable')}/session`,
          method: 'get'
        }).then(({ data }) => {
          if (data && data.code !== 0) {
            router.push({ name: 'login' })
          }
        })
      } else {
        router.push({ name: 'login' })
      }
      if (!this.isHomeLanding) {
        this.loadDashboard()
        this.loadAiMatches()
      }
    },
    loadDashboard() {
      this.loading = true
      this.$http({
        url: 'dashboard/summary',
        method: 'get'
      }).then(({ data }) => {
        if (data && data.code === 0) {
          this.summary = Object.assign({}, emptySummary, data.data || {})
        } else {
          return this.loadDashboardFallback()
        }
      }).catch(() => {
        return this.loadDashboardFallback()
      }).finally(() => {
        this.loading = false
      })
    },
    async loadDashboardFallback() {
      try {
        const [secondhandRes, orderRes, lostRes, claimRes] = await Promise.all([
          this.$http({ url: 'ershouliuzhuan/list', method: 'get', params: { page: 1, limit: 10000 } }),
          this.$http({ url: 'goumaidingdan/list', method: 'get', params: { page: 1, limit: 10000 } }),
          this.$http({ url: 'shiwuzhaoling/list', method: 'get', params: { page: 1, limit: 1 } }),
          this.$http({ url: 'renlingshenqing/list', method: 'get', params: { page: 1, limit: 1, sfsh: '待审核' } })
        ])
        const secondhandPage = secondhandRes.data && secondhandRes.data.data ? secondhandRes.data.data : {}
        const orderPage = orderRes.data && orderRes.data.data ? orderRes.data.data : {}
        const secondhandList = secondhandPage.list || []
        const orderList = orderPage.list || []
        const paidOrders = orderList.filter(item => item.ispay === '已支付')
        const unpaidOrders = orderList.filter(item => item.ispay !== '已支付')
        this.summary = {
          secondhandCount: Number(secondhandPage.total || 0),
          secondhandStock: secondhandList.reduce((sum, item) => sum + Number(item.shuliang || 0), 0),
          orderCount: Number(orderPage.total || 0),
          purchaseQuantity: orderList.reduce((sum, item) => sum + Number(item.shuliang || 0), 0),
          paidOrderCount: paidOrders.length,
          unpaidOrderCount: unpaidOrders.length,
          paidAmount: paidOrders.reduce((sum, item) => sum + Number(item.jine || 0), 0),
          lostfoundCount: Number((lostRes.data && lostRes.data.data && lostRes.data.data.total) || 0),
          pendingClaimCount: Number((claimRes.data && claimRes.data.data && claimRes.data.data.total) || 0)
        }
      } catch (error) {
        this.summary = Object.assign({}, emptySummary)
      }
    },
    loadAiMatches() {
      this.aiLoading = true
      ai.matchLostfound().then(res => {
        const data = res.data
        this.aiMatches = Array.isArray(data) ? data : (data && data.matches) || []
      }).catch(() => {
        this.aiMatches = []
      }).finally(() => {
        this.aiLoading = false
      })
    },
    formatMoney(value) {
      return `¥${Number(value || 0).toLocaleString('zh-CN')}`
    }
  }
}
</script>

<style lang="scss" scoped>
.home-landing-page {
  display: grid;
  gap: 16px;
  min-height: 100%;
  padding: 18px 24px 32px;
  background: #EEF3F5;
}

.home-landing-hero {
  min-height: 310px;
  overflow: hidden;
  border: 1px solid #DDE6EA;
  border-radius: 12px;
  background-image:
    linear-gradient(90deg, rgba(255, 255, 255, .95) 0%, rgba(255, 255, 255, .86) 43%, rgba(255, 255, 255, .22) 76%),
    url('~@/assets/img/admin-home-campus-flow.jpg');
  background-size: cover;
  background-position: center;
}

.home-landing-copy {
  max-width: 680px;
  padding: 42px 44px;

  .eyebrow {
    margin: 0 0 10px;
    color: #12A99D;
    font-weight: 800;
  }

  h1 {
    margin: 0;
    color: #10272C;
    font-size: 34px;
    line-height: 1.22;
  }

  .subtext {
    max-width: 600px;
    margin: 14px 0 0;
    color: #4F606A;
    font-size: 16px;
    line-height: 1.75;
  }
}

.home-landing-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 24px;
}

.home-entry-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(180px, 1fr));
  gap: 14px;
}

.home-entry-card {
  display: flex;
  gap: 14px;
  min-height: 122px;
  padding: 18px;
  border: 1px solid #DDE6EA;
  border-radius: 10px;
  background: #FFFFFF;
  cursor: pointer;
  transition: transform .16s ease, border-color .16s ease, box-shadow .16s ease;

  &:hover {
    transform: translateY(-2px);
    border-color: rgba(18, 169, 157, .45);
    box-shadow: 0 10px 24px rgba(20, 40, 50, .08);
  }

  h2 {
    margin: 0;
    color: #182B33;
    font-size: 18px;
  }

  p {
    margin: 8px 0 0;
    color: #687782;
    line-height: 1.55;
  }
}

.home-entry-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 44px;
  width: 44px;
  height: 44px;
  border-radius: 10px;
  color: #0B756F;
  background: #E8F7F5;
  font-size: 21px;
}

.dashboard-page {
  display: grid;
  gap: 16px;
  min-height: 100%;
  padding: 18px 24px 32px;
  background: #EEF3F5;
}

.dashboard-hero,
.metric-card,
.dashboard-panel {
  border: 1px solid #DDE6EA;
  border-radius: 10px;
  background: #FFFFFF;
  box-shadow: none;
}

.dashboard-hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  min-height: 118px;
  padding: 22px 24px;
  background: linear-gradient(135deg, rgba(18, 169, 157, .12), rgba(255, 255, 255, .94) 42%), #fff;

  .eyebrow {
    margin: 0 0 8px;
    color: #12A99D;
    font-weight: 700;
  }

  h1 {
    margin: 0;
    color: #10272C;
    font-size: 26px;
    line-height: 1.25;
  }

  .subtext {
    margin: 8px 0 0;
    color: #687782;
    line-height: 1.6;
  }
}

.metric-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(160px, 1fr));
  gap: 14px;
}

.metric-card {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 112px;
  padding: 18px;
}

.metric-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 44px;
  width: 44px;
  height: 44px;
  border-radius: 10px;
  color: #0B756F;
  background: #E8F7F5;
  font-size: 21px;
}

.metric-value {
  color: #10272C;
  font-size: 28px;
  font-weight: 800;
  line-height: 1;
}

.metric-label {
  margin-top: 8px;
  color: #44545D;
  font-weight: 600;
}

.metric-note {
  margin-top: 4px;
  color: #7A8991;
  font-size: 12px;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(320px, .75fr);
  gap: 16px;
}

.dashboard-panel {
  padding: 18px;
}

.panel-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 14px;

  h2 {
    margin: 0;
    color: #182B33;
    font-size: 18px;
  }

  p {
    margin: 6px 0 0;
    color: #687782;
    line-height: 1.6;
  }
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.status-item,
.todo-item,
.ai-match-item {
  border: 1px solid #EDF2F4;
  border-radius: 8px;
  background: #FBFDFD;
}

.status-item {
  padding: 14px;

  span {
    color: #687782;
  }

  strong {
    display: block;
    margin-top: 8px;
    color: #10272C;
    font-size: 24px;
  }
}

.todo-list,
.ai-match-list {
  display: grid;
  gap: 10px;
}

.todo-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 14px;

  span {
    color: #52636B;
  }

  strong {
    color: #12A99D;
    font-size: 22px;
  }
}

.ai-match-item {
  padding: 12px;

  p {
    margin: 8px 0 0;
    color: #687782;
    line-height: 1.55;
  }
}

.ai-match-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-weight: 700;
}

.empty-state {
  padding: 26px;
  border: 1px dashed #DDE6EA;
  border-radius: 8px;
  color: #7A8991;
  text-align: center;
}

@media (max-width: 1280px) {
  .home-entry-grid {
    grid-template-columns: repeat(2, minmax(180px, 1fr));
  }

  .metric-grid {
    grid-template-columns: repeat(2, minmax(180px, 1fr));
  }

  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 760px) {
  .home-landing-copy {
    padding: 28px 22px;

    h1 {
      font-size: 26px;
    }
  }

  .home-entry-grid {
    grid-template-columns: 1fr;
  }
}
</style>
