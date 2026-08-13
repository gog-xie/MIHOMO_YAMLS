# 📂 gogyt (通用进阶配置)

[🔙 返回上一级](../README.md)

> 🤖 自动技术分析 | 9 个配置文件

## ⚔️ 配置横向对比

| 特性 | `RulePlus.yaml` | `GeoLite.yaml` | `Geo.yaml` | `GeoLitePro.yaml` | `RuleLitePro.yaml` | `RuleLite.yaml` | `GeoPro.yaml` | `RulePro.yaml` | `Rule.yaml` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **大小** | 56.5 KB | 28.0 KB | 35.0 KB | 34.6 KB | 38.8 KB | 32.1 KB | 43.7 KB | 51.0 KB | 41.2 KB |
| **混合端口** | 7893 | 7893 | 7893 | 7893 | 7893 | 7893 | 7893 | 7893 | 7893 |
| **面板地址** | 0.0.0.0:9090 | 0.0.0.0:9090 | 0.0.0.0:9090 | 0.0.0.0:9090 | 0.0.0.0:9090 | 0.0.0.0:9090 | 0.0.0.0:9090 | 0.0.0.0:9090 | 0.0.0.0:9090 |
| **运行模式** | rule | rule | rule | rule | rule | rule | rule | rule | rule |
| **TUN** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **策略组** | **122** | **39** | **59** | **63** | **63** | **39** | **98** | **93** | **59** |
| **规则数** | **61** | **31** | **51** | **31** | **32** | **32** | **60** | **61** | **52** |

## 📄 配置详情

#### 📝 RulePlus.yaml
- **路径**: `RulePlus.yaml` | **大小**: 56.5 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/RulePlus.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (122个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 Github | `select` |
| 👆 油管视频 | `select` |
| 👆 谷歌FCM | `select` |
| 👆 谷歌服务 | `select` |
| 👆 Gemini | `select` |
| 👆 Claude | `select` |
| 👆 ChatGPT | `select` |
| 👆 Grok | `select` |
| 👆 AI服务 | `select` |
| 👆 维基百科 | `select` |
| 👆 即时通讯 | `select` |
| 👆 国外电商 | `select` |
| 👆 加密货币 | `select` |
| 👆 社交媒体 | `select` |
| 👆 国外娱乐 | `select` |
| 👆 TikTok | `select` |
| 👆 奈飞视频 | `select` |
| 👆 迪士尼+ | `select` |
| ... | 还有 102 个 |
</details>

#### 📝 GeoLite.yaml
- **路径**: `GeoLite.yaml` | **大小**: 28.0 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/GeoLite.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (39个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 漏网之鱼 | `select` |
| 👆 网络测试 | `select` |
| 👆 直接连接 | `select` |
| 👆 狮城策略 | `select` |
| 👆 香港策略 | `select` |
| 👆 日本策略 | `select` |
| 👆 美国策略 | `select` |
| 👆 台湾策略 | `select` |
| 👆 欧洲策略 | `select` |
| 👆 韩国策略 | `select` |
| 👆 其他策略 | `select` |
| ⚖️ 香港散列 | `load-balance` |
| ⚖️ 台湾散列 | `load-balance` |
| ⚖️ 狮城散列 | `load-balance` |
| ⚖️ 日本散列 | `load-balance` |
| ⚖️ 韩国散列 | `load-balance` |
| ⚖️ 美国散列 | `load-balance` |
| ⚖️ 欧洲散列 | `load-balance` |
| ... | 还有 19 个 |
</details>

#### 📝 Geo.yaml
- **路径**: `Geo.yaml` | **大小**: 35.0 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/Geo.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (59个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 Github | `select` |
| 👆 油管视频 | `select` |
| 👆 谷歌服务 | `select` |
| 👆 AI服务 | `select` |
| 👆 国外电商 | `select` |
| 👆 加密货币 | `select` |
| 👆 即时通讯 | `select` |
| 👆 国外娱乐 | `select` |
| 👆 社交媒体 | `select` |
| 👆 TikTok | `select` |
| 👆 奈飞视频 | `select` |
| 👆 迪士尼+ | `select` |
| 👆 HBO | `select` |
| 👆 Prime Video | `select` |
| 👆 Spotify | `select` |
| 👆 Bing(Copilot) | `select` |
| 👆 微软服务 | `select` |
| 👆 苹果服务 | `select` |
| ... | 还有 39 个 |
</details>

#### 📝 GeoLitePro.yaml
- **路径**: `GeoLitePro.yaml` | **大小**: 34.6 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/GeoLitePro.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (63个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 漏网之鱼 | `select` |
| 👆 网络测试 | `select` |
| 👆 直接连接 | `select` |
| 👆 狮城策略 | `select` |
| 👆 香港策略 | `select` |
| 👆 日本策略 | `select` |
| 👆 美国策略 | `select` |
| 👆 台湾策略 | `select` |
| 👆 欧洲策略 | `select` |
| 👆 韩国策略 | `select` |
| 👆 其他策略 | `select` |
| ⚖️ [主] 香港散列 | `load-balance` |
| ⚖️ [主] 台湾散列 | `load-balance` |
| ⚖️ [主] 狮城散列 | `load-balance` |
| ⚖️ [主] 日本散列 | `load-balance` |
| ⚖️ [主] 韩国散列 | `load-balance` |
| ⚖️ [主] 美国散列 | `load-balance` |
| ⚖️ [主] 欧洲散列 | `load-balance` |
| ... | 还有 43 个 |
</details>

#### 📝 RuleLitePro.yaml
- **路径**: `RuleLitePro.yaml` | **大小**: 38.8 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/RuleLitePro.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (63个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 漏网之鱼 | `select` |
| 👆 网络测试 | `select` |
| 👆 直接连接 | `select` |
| 👆 狮城策略 | `select` |
| 👆 香港策略 | `select` |
| 👆 日本策略 | `select` |
| 👆 美国策略 | `select` |
| 👆 台湾策略 | `select` |
| 👆 欧洲策略 | `select` |
| 👆 韩国策略 | `select` |
| 👆 其他策略 | `select` |
| ⚖️ [主] 香港散列 | `load-balance` |
| ⚖️ [主] 台湾散列 | `load-balance` |
| ⚖️ [主] 狮城散列 | `load-balance` |
| ⚖️ [主] 日本散列 | `load-balance` |
| ⚖️ [主] 韩国散列 | `load-balance` |
| ⚖️ [主] 美国散列 | `load-balance` |
| ⚖️ [主] 欧洲散列 | `load-balance` |
| ... | 还有 43 个 |
</details>

#### 📝 RuleLite.yaml
- **路径**: `RuleLite.yaml` | **大小**: 32.1 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/RuleLite.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (39个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 漏网之鱼 | `select` |
| 👆 网络测试 | `select` |
| 👆 直接连接 | `select` |
| 👆 狮城策略 | `select` |
| 👆 香港策略 | `select` |
| 👆 日本策略 | `select` |
| 👆 美国策略 | `select` |
| 👆 台湾策略 | `select` |
| 👆 欧洲策略 | `select` |
| 👆 韩国策略 | `select` |
| 👆 其他策略 | `select` |
| ⚖️ 香港散列 | `load-balance` |
| ⚖️ 台湾散列 | `load-balance` |
| ⚖️ 狮城散列 | `load-balance` |
| ⚖️ 日本散列 | `load-balance` |
| ⚖️ 韩国散列 | `load-balance` |
| ⚖️ 美国散列 | `load-balance` |
| ⚖️ 欧盟散列 | `load-balance` |
| ... | 还有 19 个 |
</details>

#### 📝 GeoPro.yaml
- **路径**: `GeoPro.yaml` | **大小**: 43.7 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/GeoPro.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (98个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 Github | `select` |
| 👆 油管视频 | `select` |
| 👆 谷歌FCM | `select` |
| 👆 谷歌服务 | `select` |
| 👆 Gemini | `select` |
| 👆 Claude | `select` |
| 👆 ChatGPT | `select` |
| 👆 Grok | `select` |
| 👆 AI服务 | `select` |
| 👆 维基百科 | `select` |
| 👆 即时通讯 | `select` |
| 👆 国外电商 | `select` |
| 👆 加密货币 | `select` |
| 👆 社交媒体 | `select` |
| 👆 国外娱乐 | `select` |
| 👆 TikTok | `select` |
| 👆 奈飞视频 | `select` |
| 👆 迪士尼+ | `select` |
| ... | 还有 78 个 |
</details>

#### 📝 RulePro.yaml
- **路径**: `RulePro.yaml` | **大小**: 51.0 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/RulePro.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (93个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 Github | `select` |
| 👆 油管视频 | `select` |
| 👆 谷歌FCM | `select` |
| 👆 谷歌服务 | `select` |
| 👆 Gemini | `select` |
| 👆 Claude | `select` |
| 👆 ChatGPT | `select` |
| 👆 Grok | `select` |
| 👆 AI服务 | `select` |
| 👆 维基百科 | `select` |
| 👆 即时通讯 | `select` |
| 👆 国外电商 | `select` |
| 👆 加密货币 | `select` |
| 👆 社交媒体 | `select` |
| 👆 国外娱乐 | `select` |
| 👆 TikTok | `select` |
| 👆 奈飞视频 | `select` |
| 👆 迪士尼+ | `select` |
| ... | 还有 73 个 |
</details>

#### 📝 Rule.yaml
- **路径**: `Rule.yaml` | **大小**: 41.2 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/gogyt/Rule.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (59个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 👆 默认直连 | `select` |
| 👆 Github | `select` |
| 👆 油管视频 | `select` |
| 👆 谷歌服务 | `select` |
| 👆 AI服务 | `select` |
| 👆 国外电商 | `select` |
| 👆 加密货币 | `select` |
| 👆 即时通讯 | `select` |
| 👆 国外娱乐 | `select` |
| 👆 社交媒体 | `select` |
| 👆 TikTok | `select` |
| 👆 奈飞视频 | `select` |
| 👆 迪士尼+ | `select` |
| 👆 HBO | `select` |
| 👆 Prime Video | `select` |
| 👆 Spotify | `select` |
| 👆 Bing(Copilot) | `select` |
| 👆 微软服务 | `select` |
| 👆 苹果服务 | `select` |
| ... | 还有 39 个 |
</details>
