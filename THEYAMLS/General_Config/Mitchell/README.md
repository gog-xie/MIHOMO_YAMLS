# 📂 Mitchell (通用进阶配置)

[🔙 返回上一级](../README.md)

> 🤖 自动技术分析 | 2 个配置文件

## ⚔️ 配置横向对比

| 特性 | `config_version2.yaml` | `config.yaml` |
| :--- | :--- | :--- |
| **大小** | 30.9 KB | 28.5 KB |
| **混合端口** | 7893 | 7893 |
| **面板地址** | 127.0.0.1:9090 | 127.0.0.1:9090 |
| **运行模式** | rule | rule |
| **TUN** | ✅ | ✅ |
| **策略组** | **27** | **25** |
| **规则数** | **41** | **35** |

## 📄 配置详情

#### 📝 config_version2.yaml
- **路径**: `config_version2.yaml` | **大小**: 30.9 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Mitchell/config_version2.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (27个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 Proxy | `select` |
| 👆 AI | `select` |
| 🔧 AI_稳定节点 | `fallback` |
| ♻️ AI_自动优选 | `url-test` |
| ♻️ 香港均衡加速 | `url-test` |
| ♻️ 美国均衡加速 | `url-test` |
| ♻️ 新加坡均衡加速 | `url-test` |
| 👆 香港故转 | `select` |
| 👆 美国故转 | `select` |
| 👆 新加坡故转 | `select` |
| ♻️ 香港自动 | `url-test` |
| ♻️ 美国自动 | `url-test` |
| ♻️ 新加坡自动 | `url-test` |
| ♻️ 自动选择 | `url-test` |
| 👆 TikTok | `select` |
| 👆 YouTube | `select` |
| ♻️ Netflix | `url-test` |
| ♻️ Disney+ | `url-test` |
| 👆 Speedtest | `select` |
| 👆 OneDrive | `select` |
| ... | 还有 7 个 |
</details>

#### 📝 config.yaml
- **路径**: `config.yaml` | **大小**: 28.5 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Mitchell/config.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (25个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 Proxy | `select` |
| 👆 AI | `select` |
| 🔧 AI_稳定节点 | `fallback` |
| ♻️ AI_自动优选 | `url-test` |
| ⚖️ 香港均衡加速 | `load-balance` |
| ⚖️ 美国均衡加速 | `load-balance` |
| ⚖️ 新加坡均衡加速 | `load-balance` |
| 🔧 香港故转 | `fallback` |
| 🔧 美国故转 | `fallback` |
| 🔧 新加坡故转 | `fallback` |
| ♻️ 香港自动 | `url-test` |
| ♻️ 美国自动 | `url-test` |
| ♻️ 新加坡自动 | `url-test` |
| ♻️ 自动选择 | `url-test` |
| 👆 TikTok | `select` |
| 👆 YouTube | `select` |
| 👆 Speedtest | `select` |
| 👆 OneDrive | `select` |
| 👆 Trackerslist | `select` |
| 👆 香港节点 | `select` |
| ... | 还有 5 个 |
</details>
