# 📂 Smart 模式 / 路由专用 (Smart Mode)

[🔙 返回主页](../../README.md)

> 🤖 自动技术分析 | 14 个配置文件

## ⚔️ 配置横向对比

| 特性 | `clash-fallback-smart-std.yaml` | `clash-all-fallback-smart.yaml` | `clash-all-smart.yaml` | `smart.yaml` | `OneSmart_Config.yaml` | `OneSmart_Lite_Config.yaml` | `mihomo_smart.yaml` | `GeoSmartAIO.yaml` | `RuleSmartAIO.yaml` | `MihomoSmartProPlus.yaml` | `MihomoSmartAIO.yaml` | `MihomoSmartProMax.yaml` | `THESmart.yaml` | `OneSmartProMCX.yaml` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **大小** | 17.7 KB | 18.2 KB | 15.1 KB | 13.0 KB | 20.2 KB | 12.5 KB | 15.1 KB | 32.6 KB | 41.2 KB | 24.1 KB | 30.2 KB | 23.6 KB | 37.3 KB | 38.1 KB |
| **混合端口** | 7893 | 7893 | 7893 | 7890 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 7893 | N/A |
| **面板地址** | 0.0.0.0:9090 | 0.0.0.0:9090 | 0.0.0.0:9090 | - | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | 0.0.0.0:9090 | N/A |
| **运行模式** | rule | rule | rule | rule | 解析失败 | 解析失败 | 解析失败 | 解析失败 | 解析失败 | 解析失败 | 解析失败 | 解析失败 | rule | 解析失败 |
| **TUN** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **策略组** | **36** | **57** | **38** | **28** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **66** | **0** |
| **规则数** | **42** | **48** | **43** | **23** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **49** | **0** |

## 📄 配置详情

### 👤 666OS

#### 📝 OneSmart_Config.yaml
- **路径**: `666OS/OneSmart_Config.yaml` | **大小**: 20.2 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/666OS/OneSmart_Config.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

#### 📝 OneSmart_Lite_Config.yaml
- **路径**: `666OS/OneSmart_Lite_Config.yaml` | **大小**: 12.5 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/666OS/OneSmart_Lite_Config.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

---
### 👤 HenryChiao

#### 📝 MihomoSmartProPlus.yaml
- **路径**: `HenryChiao/MihomoSmartProPlus.yaml` | **大小**: 24.1 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/HenryChiao/MihomoSmartProPlus.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

#### 📝 MihomoSmartAIO.yaml
- **路径**: `HenryChiao/MihomoSmartAIO.yaml` | **大小**: 30.2 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/HenryChiao/MihomoSmartAIO.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

#### 📝 MihomoSmartProMax.yaml
- **路径**: `HenryChiao/MihomoSmartProMax.yaml` | **大小**: 23.6 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/HenryChiao/MihomoSmartProMax.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

#### 📝 THESmart.yaml
- **路径**: `HenryChiao/THESmart.yaml` | **大小**: 37.3 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/HenryChiao/THESmart.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (66个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 默认代理 | `select` |
| 🔧 故障转移 | `fallback` |
| 👆 国外流量 | `select` |
| 👆 代理QUIC | `select` |
| 👆 FCM服务 | `select` |
| 👆 国内流量 | `select` |
| 👆 兜底流量 | `select` |
| 👆 直接连接 | `select` |
| 👆 代理DNS | `select` |
| 👆 网络测试 | `select` |
| 👆 抖快书定位 | `select` |
| 👆 人机验证 | `select` |
| 👆 下载追踪 | `select` |
| 👆 Emby服 | `select` |
| 👆 油管视频 | `select` |
| 👆 奈飞视频 | `select` |
| 👆 国际媒体 | `select` |
| 👆 新闻媒体 | `select` |
| 👆 电报消息 | `select` |
| 👆 推特社交 | `select` |
| ... | 还有 46 个 |
</details>

---
### 👤 echs-top

#### 📝 mihomo_smart.yaml
- **路径**: `echs-top/mihomo_smart.yaml` | **大小**: 15.1 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/echs-top/mihomo_smart.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

---
### 👤 edison

#### 📝 OneSmartProMCX.yaml
- **路径**: `edison/OneSmartProMCX.yaml` | **大小**: 38.1 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/edison/OneSmartProMCX.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

---
### 👤 gog-xie

#### 📝 GeoSmartAIO.yaml
- **路径**: `gog-xie/GeoSmartAIO.yaml` | **大小**: 32.6 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/gog-xie/GeoSmartAIO.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

#### 📝 RuleSmartAIO.yaml
- **路径**: `gog-xie/RuleSmartAIO.yaml` | **大小**: 41.2 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/gog-xie/RuleSmartAIO.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

---
### 👤 liandu2024

#### 📝 clash-fallback-smart-std.yaml
- **路径**: `liandu2024/clash-fallback-smart-std.yaml` | **大小**: 17.7 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/liandu2024/clash-fallback-smart-std.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (36个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 AI | `select` |
| 👆 Meta AI | `select` |
| 👆 Perplexity | `select` |
| 👆 Stream Media | `select` |
| 👆 GitHub | `select` |
| 👆 Reddit | `select` |
| 👆 Nvidia | `select` |
| 👆 Apple | `select` |
| 👆 Microsoft | `select` |
| 👆 Games | `select` |
| 👆 Crypto | `select` |
| 👆 Test | `select` |
| 👆 Block | `select` |
| 👆 国外 | `select` |
| 👆 国内 | `select` |
| 👆 其他 | `select` |
| 👆 所有-手选 | `select` |
| 👆 所有-智选 | `smart` |
| 🔧 香港-故转 | `fallback` |
| 👆 香港-手选 | `select` |
| ... | 还有 16 个 |
</details>

#### 📝 clash-all-fallback-smart.yaml
- **路径**: `liandu2024/clash-all-fallback-smart.yaml` | **大小**: 18.2 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/liandu2024/clash-all-fallback-smart.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (57个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 ChatGPT | `select` |
| 👆 Gemini | `select` |
| 👆 Copilot | `select` |
| 👆 Perplexity | `select` |
| 👆 Claude | `select` |
| 👆 Meta AI | `select` |
| 👆 GitHub | `select` |
| 👆 Reddit | `select` |
| 👆 Telegram | `select` |
| 👆 WhatsApp | `select` |
| 👆 Facebook | `select` |
| 👆 YouTube | `select` |
| 👆 TikTok | `select` |
| 👆 Netflix | `select` |
| 👆 HBO | `select` |
| 👆 Disney | `select` |
| 👆 Amazon | `select` |
| 👆 Crunchyroll | `select` |
| 👆 Spotify | `select` |
| 👆 Nvidia | `select` |
| ... | 还有 37 个 |
</details>

#### 📝 clash-all-smart.yaml
- **路径**: `liandu2024/clash-all-smart.yaml` | **大小**: 15.1 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/liandu2024/clash-all-smart.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: ✅
<details>
<summary>🔍 策略组 (38个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 ChatGPT | `select` |
| 👆 Claude | `select` |
| 👆 Meta AI | `select` |
| 👆 Perplexity | `select` |
| 👆 GitHub | `select` |
| 👆 Telegram | `select` |
| 👆 Twitter(X) | `select` |
| 👆 WhatsApp | `select` |
| 👆 Facebook | `select` |
| 👆 YouTube | `select` |
| 👆 TikTok | `select` |
| 👆 Disney | `select` |
| 👆 Netflix | `select` |
| 👆 HBO | `select` |
| 👆 Spotify | `select` |
| 👆 Amazon | `select` |
| 👆 Apple | `select` |
| 👆 Microsoft | `select` |
| 👆 Google | `select` |
| 👆 Nvidia | `select` |
| ... | 还有 18 个 |
</details>

---
### 👤 qichiyuhub

#### 📝 smart.yaml
- **路径**: `qichiyuhub/smart.yaml` | **大小**: 13.0 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/Smart_Mode/qichiyuhub/smart.yaml)
- **模式**: rule | **TUN**: ✅ | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (28个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 🚀 默认代理 | `select` |
| 👆 📹 YouTube | `select` |
| 👆 🍀 Google | `select` |
| 👆 🤖 ChatGPT | `select` |
| 👆 👨🏿‍💻 GitHub | `select` |
| 👆 🐬 OneDrive | `select` |
| 👆 🪟 Microsoft | `select` |
| 👆 🎵 TikTok | `select` |
| 👆 📲 Telegram | `select` |
| 👆 🎥 NETFLIX | `select` |
| 👆 ✈️ Speedtest | `select` |
| 👆 💶 PayPal | `select` |
| 👆 🍎 Apple | `select` |
| 👆 🐟 漏网之鱼 | `select` |
| 👆 🇭🇰 香港节点 | `select` |
| 👆 🇯🇵 日本节点 | `select` |
| 👆 🇸🇬 狮城节点 | `select` |
| 👆 🇺🇲 美国节点 | `select` |
| 🔧 🔯 香港故转 | `fallback` |
| 🔧 🔯 日本故转 | `fallback` |
| ... | 还有 8 个 |
</details>

---