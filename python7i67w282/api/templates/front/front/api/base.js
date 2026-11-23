const DEV_API_BASE = "http://localhost:8080/python7i67w282/"
// 体验版/正式版必须使用已在微信公众平台配置的 HTTPS 合法域名。
// 示例："https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/"
const RELEASE_API_BASE = "https://flask-2u3u-263262-10-1338167593.sh.run.tcloudbase.com/python7i67w282/"

function resolveApiBase() {
    try {
        const accountInfo = uni.getAccountInfoSync ? uni.getAccountInfoSync() : null
        const envVersion = accountInfo && accountInfo.miniProgram && accountInfo.miniProgram.envVersion
        if (envVersion === "develop") {
            return RELEASE_API_BASE
        }
    } catch (e) {}
    return RELEASE_API_BASE
}

const base = {
    url : resolveApiBase()
}
export default base
