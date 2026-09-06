# 📂 Aethersailor (通用进阶配置)

[🔙 返回上一级](../README.md)

> 🤖 自动技术分析 | 12 个配置文件

## ⚔️ 配置横向对比

| 特性 | `Complete_YAML_Configuration_Template.yaml` | `Custom_Clash_Lite.yaml` | `Custom_Clash_GFW_Fallback.yaml` | `Custom_Clash_Full_Fallback.yaml` | `Custom_Clash_GFW.yaml` | `Custom_Clash.yaml` | `Custom_Clash_Selfhosted_Manual_Fallback.yaml` | `Custom_Clash_Full.yaml` | `Custom_Clash_DIY&Airport.yaml` | `Custom_Clash_Selfhosted_Provider_Fallback.yaml` | `Custom_Clash_Fallback.yaml` | `Custom_Clash_Lite_Fallback.yaml` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **大小** | 44.0 KB | 11.2 KB | 3.1 KB | 37.1 KB | 3.1 KB | 17.4 KB | 45.8 KB | 37.3 KB | 17.9 KB | 45.4 KB | 43.2 KB | 20.5 KB |
| **混合端口** | 7893 | - | - | - | - | - | - | - | - | - | - | - |
| **面板地址** | 0.0.0.0:9090 | - | - | - | - | - | - | - | 127.0.0.1:9090 | - | - | - |
| **运行模式** | rule | rule | rule | rule | rule | rule | rule | rule | rule | rule | rule | rule |
| **TUN** | ✅ | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 | 🚫 |
| **策略组** | **35** | **19** | **2** | **53** | **3** | **35** | **36** | **53** | **33** | **36** | **35** | **19** |
| **规则数** | **47** | **26** | **5** | **55** | **5** | **47** | **47** | **55** | **51** | **47** | **47** | **26** |

## 📄 配置详情

#### 📝 Complete_YAML_Configuration_Template.yaml
- **路径**: `Complete_YAML_Configuration_Template.yaml` | **大小**: 44.0 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Complete_YAML_Configuration_Template.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (35个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 🚀 手动选择 | `select` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 👆 💬 即时通讯 | `select` |
| 👆 🌐 社交媒体 | `select` |
| 👆 🚀 GitHub | `select` |
| 👆 🤖 ChatGPT | `select` |
| 👆 🤖 AI服务 | `select` |
| 👆 🎶 TikTok | `select` |
| 👆 📹 YouTube | `select` |
| 👆 🎥 Netflix | `select` |
| 👆 🎥 DisneyPlus | `select` |
| 👆 🎥 HBO | `select` |
| 👆 🎥 PrimeVideo | `select` |
| 👆 🎥 AppleTV+ | `select` |
| 👆 🎥 Emby | `select` |
| 👆 🎻 Spotify | `select` |
| 👆 📺 Bahamut | `select` |
| 👆 🌎 国外媒体 | `select` |
| 👆 🛒 国外电商 | `select` |
| 👆 📢 谷歌FCM | `select` |
| ... | 还有 15 个 |
</details>

#### 📝 Custom_Clash_Lite.yaml
- **路径**: `Custom_Clash_Lite.yaml` | **大小**: 11.2 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_Lite.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (19个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 🚀 手动选择 | `select` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 👆 🚀 GitHub | `select` |
| 👆 📢 谷歌FCM | `select` |
| 👆 🇬 谷歌服务 | `select` |
| 👆 🍎 苹果服务 | `select` |
| 👆 Ⓜ️ 微软服务 | `select` |
| 👆 🎮 游戏平台 | `select` |
| 👆 🎮 Steam | `select` |
| 👆 🚀 测速工具 | `select` |
| 👆 🐟 漏网之鱼 | `select` |
| 👆 🔀 非标端口 | `select` |
| ♻️ 🇭🇰 香港节点 | `url-test` |
| ♻️ 🇺🇸 美国节点 | `url-test` |
| ♻️ 🇯🇵 日本节点 | `url-test` |
| ♻️ 🇸🇬 新加坡节点 | `url-test` |
| ♻️ 🇼🇸 台湾节点 | `url-test` |
| ♻️ 🇰🇷 韩国节点 | `url-test` |
| 👆 🎯 全球直连 | `select` |
</details>

#### 📝 Custom_Clash_GFW_Fallback.yaml
- **路径**: `Custom_Clash_GFW_Fallback.yaml` | **大小**: 3.1 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_GFW_Fallback.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (2个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 🔧 🚀 故障转移 | `fallback` |
| 👆 🎯 全球直连 | `select` |
</details>

#### 📝 Custom_Clash_Full_Fallback.yaml
- **路径**: `Custom_Clash_Full_Fallback.yaml` | **大小**: 37.1 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_Full_Fallback.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (53个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 🔧 🚀 故障转移 | `fallback` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 🔧 💬 即时通讯 | `fallback` |
| 🔧 🌐 社交媒体 | `fallback` |
| 🔧 📞 Talkatone | `fallback` |
| 🔧 🚀 GitHub | `fallback` |
| 🔧 🤖 ChatGPT | `fallback` |
| 🔧 🤖 Copilot | `fallback` |
| 🔧 🤖 国外AI服务 | `fallback` |
| 👆 🤖 国内AI服务 | `select` |
| 🔧 🎶 TikTok | `fallback` |
| 🔧 📹 YouTube | `fallback` |
| 🔧 🎥 Netflix | `fallback` |
| 🔧 🎥 DisneyPlus | `fallback` |
| 🔧 🎥 HBO | `fallback` |
| 🔧 🎥 PrimeVideo | `fallback` |
| 🔧 🎥 AppleTV+ | `fallback` |
| 🔧 🎥 Emby | `fallback` |
| 🔧 🎻 Spotify | `fallback` |
| 🔧 📺 Bahamut | `fallback` |
| ... | 还有 33 个 |
</details>

#### 📝 Custom_Clash_GFW.yaml
- **路径**: `Custom_Clash_GFW.yaml` | **大小**: 3.1 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_GFW.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (3个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 🚀 手动选择 | `select` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 👆 🎯 全球直连 | `select` |
</details>

#### 📝 Custom_Clash.yaml
- **路径**: `Custom_Clash.yaml` | **大小**: 17.4 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (35个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 🚀 手动选择 | `select` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 👆 💬 即时通讯 | `select` |
| 👆 🌐 社交媒体 | `select` |
| 👆 🚀 GitHub | `select` |
| 👆 🤖 ChatGPT | `select` |
| 👆 🤖 AI服务 | `select` |
| 👆 🎶 TikTok | `select` |
| 👆 📹 YouTube | `select` |
| 👆 🎥 Netflix | `select` |
| 👆 🎥 DisneyPlus | `select` |
| 👆 🎥 HBO | `select` |
| 👆 🎥 PrimeVideo | `select` |
| 👆 🎥 AppleTV+ | `select` |
| 👆 🎥 Emby | `select` |
| 👆 🎻 Spotify | `select` |
| 👆 📺 Bahamut | `select` |
| 👆 🌎 国外媒体 | `select` |
| 👆 🛒 国外电商 | `select` |
| 👆 📢 谷歌FCM | `select` |
| ... | 还有 15 个 |
</details>

#### 📝 Custom_Clash_Selfhosted_Manual_Fallback.yaml
- **路径**: `Custom_Clash_Selfhosted_Manual_Fallback.yaml` | **大小**: 45.8 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_Selfhosted_Manual_Fallback.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (36个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 🔧 🚀 故障转移 | `fallback` |
| ♻️ 🏴‍☠️ 自建节点 | `url-test` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 🔧 💬 即时通讯 | `fallback` |
| 🔧 🌐 社交媒体 | `fallback` |
| 🔧 🚀 GitHub | `fallback` |
| 🔧 🤖 ChatGPT | `fallback` |
| 🔧 🤖 AI服务 | `fallback` |
| 🔧 🎶 TikTok | `fallback` |
| 🔧 📹 YouTube | `fallback` |
| 🔧 🎥 Netflix | `fallback` |
| 🔧 🎥 DisneyPlus | `fallback` |
| 🔧 🎥 HBO | `fallback` |
| 🔧 🎥 PrimeVideo | `fallback` |
| 🔧 🎥 AppleTV+ | `fallback` |
| 🔧 🎥 Emby | `fallback` |
| 🔧 🎻 Spotify | `fallback` |
| 🔧 📺 Bahamut | `fallback` |
| 🔧 🌎 国外媒体 | `fallback` |
| 🔧 🛒 国外电商 | `fallback` |
| ... | 还有 16 个 |
</details>

#### 📝 Custom_Clash_Full.yaml
- **路径**: `Custom_Clash_Full.yaml` | **大小**: 37.3 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_Full.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (53个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 🚀 手动选择 | `select` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 👆 💬 即时通讯 | `select` |
| 👆 🌐 社交媒体 | `select` |
| 👆 📞 Talkatone | `select` |
| 👆 🚀 GitHub | `select` |
| 👆 🤖 ChatGPT | `select` |
| 👆 🤖 Copilot | `select` |
| 👆 🤖 国外AI服务 | `select` |
| 👆 🤖 国内AI服务 | `select` |
| 👆 🎶 TikTok | `select` |
| 👆 📹 YouTube | `select` |
| 👆 🎥 Netflix | `select` |
| 👆 🎥 DisneyPlus | `select` |
| 👆 🎥 HBO | `select` |
| 👆 🎥 PrimeVideo | `select` |
| 👆 🎥 AppleTV+ | `select` |
| 👆 🎥 Emby | `select` |
| 👆 🎻 Spotify | `select` |
| 👆 📺 Bahamut | `select` |
| ... | 还有 33 个 |
</details>

#### 📝 Custom_Clash_DIY&Airport.yaml
- **路径**: `Custom_Clash_DIY&Airport.yaml` | **大小**: 17.9 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_DIY%26Airport.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (33个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 🔧 手动选择 | `fallback` |
| 🔧 即时通讯 | `fallback` |
| 🔧 社交媒体 | `fallback` |
| 🔧 GitHub | `fallback` |
| 🔧 AI服务 | `fallback` |
| 🔧 TikTok | `fallback` |
| 🔧 YouTube | `fallback` |
| 🔧 Netflix | `fallback` |
| 🔧 DisneyPlus | `fallback` |
| 🔧 HBO | `fallback` |
| 🔧 PrimeVideo | `fallback` |
| 🔧 AppleTV+ | `fallback` |
| 🔧 Emby | `fallback` |
| 🔧 Spotify | `fallback` |
| 🔧 国外媒体 | `fallback` |
| 🔧 国外电商 | `fallback` |
| 🔧 谷歌FCM | `fallback` |
| 🔧 谷歌服务 | `fallback` |
| 👆 苹果服务 | `select` |
| 👆 微软服务 | `select` |
| ... | 还有 13 个 |
</details>

#### 📝 Custom_Clash_Selfhosted_Provider_Fallback.yaml
- **路径**: `Custom_Clash_Selfhosted_Provider_Fallback.yaml` | **大小**: 45.4 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_Selfhosted_Provider_Fallback.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (36个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 🔧 🚀 故障转移 | `fallback` |
| ♻️ 🏴‍☠️ 自建节点 | `url-test` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 🔧 💬 即时通讯 | `fallback` |
| 🔧 🌐 社交媒体 | `fallback` |
| 🔧 🚀 GitHub | `fallback` |
| 🔧 🤖 ChatGPT | `fallback` |
| 🔧 🤖 AI服务 | `fallback` |
| 🔧 🎶 TikTok | `fallback` |
| 🔧 📹 YouTube | `fallback` |
| 🔧 🎥 Netflix | `fallback` |
| 🔧 🎥 DisneyPlus | `fallback` |
| 🔧 🎥 HBO | `fallback` |
| 🔧 🎥 PrimeVideo | `fallback` |
| 🔧 🎥 AppleTV+ | `fallback` |
| 🔧 🎥 Emby | `fallback` |
| 🔧 🎻 Spotify | `fallback` |
| 🔧 📺 Bahamut | `fallback` |
| 🔧 🌎 国外媒体 | `fallback` |
| 🔧 🛒 国外电商 | `fallback` |
| ... | 还有 16 个 |
</details>

#### 📝 Custom_Clash_Fallback.yaml
- **路径**: `Custom_Clash_Fallback.yaml` | **大小**: 43.2 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_Fallback.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (35个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 🔧 🚀 故障转移 | `fallback` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 🔧 💬 即时通讯 | `fallback` |
| 🔧 🌐 社交媒体 | `fallback` |
| 🔧 🚀 GitHub | `fallback` |
| 🔧 🤖 ChatGPT | `fallback` |
| 🔧 🤖 AI服务 | `fallback` |
| 🔧 🎶 TikTok | `fallback` |
| 🔧 📹 YouTube | `fallback` |
| 🔧 🎥 Netflix | `fallback` |
| 🔧 🎥 DisneyPlus | `fallback` |
| 🔧 🎥 HBO | `fallback` |
| 🔧 🎥 PrimeVideo | `fallback` |
| 🔧 🎥 AppleTV+ | `fallback` |
| 🔧 🎥 Emby | `fallback` |
| 🔧 🎻 Spotify | `fallback` |
| 🔧 📺 Bahamut | `fallback` |
| 🔧 🌎 国外媒体 | `fallback` |
| 🔧 🛒 国外电商 | `fallback` |
| 🔧 📢 谷歌FCM | `fallback` |
| ... | 还有 15 个 |
</details>

#### 📝 Custom_Clash_Lite_Fallback.yaml
- **路径**: `Custom_Clash_Lite_Fallback.yaml` | **大小**: 20.5 KB | [查看源码](https://github.com/gogyt/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/Aethersailor/Custom_Clash_Lite_Fallback.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (19个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 🔧 🚀 故障转移 | `fallback` |
| ♻️ ♻️ 自动选择 | `url-test` |
| 🔧 🚀 GitHub | `fallback` |
| 🔧 📢 谷歌FCM | `fallback` |
| 🔧 🇬 谷歌服务 | `fallback` |
| 👆 🍎 苹果服务 | `select` |
| 👆 Ⓜ️ 微软服务 | `select` |
| 👆 🎮 游戏平台 | `select` |
| 👆 🎮 Steam | `select` |
| 👆 🚀 测速工具 | `select` |
| 🔧 🐟 漏网之鱼 | `fallback` |
| 👆 🔀 非标端口 | `select` |
| ♻️ 🇭🇰 香港节点 | `url-test` |
| ♻️ 🇺🇸 美国节点 | `url-test` |
| ♻️ 🇯🇵 日本节点 | `url-test` |
| ♻️ 🇸🇬 新加坡节点 | `url-test` |
| ♻️ 🇼🇸 台湾节点 | `url-test` |
| ♻️ 🇰🇷 韩国节点 | `url-test` |
| 👆 🎯 全球直连 | `select` |
</details>
