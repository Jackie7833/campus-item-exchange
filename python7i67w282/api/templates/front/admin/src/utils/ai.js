import http from '@/utils/http'

function normalizeAiError(error) {
  const message = error && error.response && error.response.data && error.response.data.msg
    ? error.response.data.msg
    : 'AI 服务暂不可用，请稍后再试'
  return Promise.reject(new Error(message))
}

function post(url, data) {
  return http({
    url,
    method: 'post',
    data
  }).then(({ data }) => data).catch(normalizeAiError)
}

function get(url, params) {
  return http({
    url,
    method: 'get',
    params
  }).then(({ data }) => data).catch(normalizeAiError)
}

export default {
  moderate(payload) {
    return post('ai/moderate', payload)
  },
  matchLostfound(params) {
    return get('ai/lostfound/match', params)
  },
  explainRecommendation(payload) {
    return post('ai/recommend/explain', payload)
  },
  generateListing(payload) {
    return post('ai/listing/generate', payload)
  },
  verifyStudentCard(payload) {
    return post('ai/student-card/verify', payload)
  }
}
