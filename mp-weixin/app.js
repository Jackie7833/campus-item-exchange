
if (wx.cloud) {
  wx.cloud.init({
    env: 'prod-d2glavkbz3c97ef18',
    traceUser: true
  })
}

require('./common/runtime.js')
require('./common/vendor.js')
require('./common/main.js')
