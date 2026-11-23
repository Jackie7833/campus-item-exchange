<template>
  <el-dialog
    class="ai-result-dialog"
    :title="title"
    :visible.sync="innerVisible"
    width="720px"
    :append-to-body="true"
    @close="$emit('update:visible', false)"
  >
    <div v-if="loading" class="ai-loading">
      <i class="el-icon-loading"></i>
      <span>AI 正在分析，请稍候</span>
    </div>
    <div v-else class="ai-result-content">
      <div v-if="summary" class="ai-summary">
        <div class="ai-summary-title">结论</div>
        <div class="ai-summary-text">{{ summary }}</div>
      </div>

      <div v-if="riskLevel" class="ai-risk-row">
        <span class="ai-label">风险等级</span>
        <el-tag :type="riskTagType" size="small">{{ riskLevelText }}</el-tag>
      </div>

      <div v-if="hits && hits.length" class="ai-section">
        <div class="ai-section-title">命中内容</div>
        <div class="ai-tags">
          <el-tag v-for="item in hits" :key="item" size="small" type="warning">{{ item }}</el-tag>
        </div>
      </div>

      <div v-if="matches && matches.length" class="ai-section">
        <div class="ai-section-title">匹配线索</div>
        <div v-for="item in matches" :key="item.lostId + '-' + item.claimId" class="ai-match-card">
          <div class="ai-match-head">
            <strong>{{ item.itemName || '待核验物品' }}</strong>
            <el-tag size="small" type="success">{{ item.score }} 分</el-tag>
          </div>
          <p>{{ item.reason }}</p>
          <ul v-if="item.verifyQuestions && item.verifyQuestions.length">
            <li v-for="question in item.verifyQuestions" :key="question">{{ question }}</li>
          </ul>
        </div>
      </div>

      <div v-if="recommendation" class="ai-section">
        <div class="ai-section-title">推荐解释</div>
        <p>{{ recommendation.reason || recommendation.boundary }}</p>
        <p v-if="recommendation.boundary" class="ai-muted">{{ recommendation.boundary }}</p>
      </div>

      <div v-if="guardrails && guardrails.length" class="ai-section">
        <div class="ai-section-title">处理建议</div>
        <ul>
          <li v-for="item in guardrails" :key="item">{{ item }}</li>
        </ul>
      </div>

      <div v-if="isEmpty" class="ai-empty">暂无 AI 结果</div>
    </div>
    <span slot="footer">
      <el-button type="primary" @click="innerVisible = false">知道了</el-button>
    </span>
  </el-dialog>
</template>

<script>
export default {
  name: 'AiResultDialog',
  props: {
    visible: Boolean,
    title: {
      type: String,
      default: 'AI 辅助分析'
    },
    loading: Boolean,
    result: {
      type: Object,
      default: () => ({})
    }
  },
  computed: {
    innerVisible: {
      get() {
        return this.visible
      },
      set(value) {
        this.$emit('update:visible', value)
      }
    },
    payload() {
      return this.result && this.result.data ? this.result.data : (this.result || {})
    },
    summary() {
      return this.payload.summary || this.payload.reason || this.payload.status || ''
    },
    riskLevel() {
      return this.payload.riskLevel || ''
    },
    riskLevelText() {
      const map = { low: '低风险', medium: '中风险', high: '高风险' }
      return map[this.riskLevel] || this.riskLevel
    },
    riskTagType() {
      const map = { low: 'success', medium: 'warning', high: 'danger' }
      return map[this.riskLevel] || 'info'
    },
    hits() {
      return this.payload.hits || []
    },
    matches() {
      return Array.isArray(this.payload) ? this.payload : (this.payload.matches || [])
    },
    guardrails() {
      return this.payload.guardrails || this.payload.verifyQuestions || []
    },
    recommendation() {
      return this.payload.recommendation || null
    },
    isEmpty() {
      return !this.summary && !this.riskLevel && !this.hits.length && !this.matches.length && !this.recommendation && !this.guardrails.length
    }
  }
}
</script>

<style lang="scss" scoped>
.ai-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  min-height: 180px;
  color: #12A99D;
  font-size: 15px;
}

.ai-result-content {
  color: #24303f;
}

.ai-summary {
  padding: 14px 16px;
  border: 1px solid #DCEDEA;
  border-radius: 8px;
  background: #F4FBFA;
}

.ai-summary-title,
.ai-section-title,
.ai-label {
  font-weight: 600;
  color: #10242f;
}

.ai-summary-text {
  margin-top: 6px;
  line-height: 1.7;
}

.ai-risk-row,
.ai-section {
  margin-top: 16px;
}

.ai-risk-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ai-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 10px;
}

.ai-match-card {
  margin-top: 10px;
  padding: 12px;
  border: 1px solid #E5EAF0;
  border-radius: 8px;
  background: #fff;
}

.ai-match-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ai-match-card p,
.ai-section p {
  margin: 8px 0 0;
  line-height: 1.7;
}

ul {
  margin: 8px 0 0;
  padding-left: 18px;
  line-height: 1.8;
}

.ai-muted {
  color: #7B8794;
}

.ai-empty {
  padding: 48px 0;
  color: #7B8794;
  text-align: center;
}
</style>
