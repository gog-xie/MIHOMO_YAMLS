# 📂 666OS (通用进阶配置)

[🔙 返回上一级](../README.md)

> 🤖 自动技术分析 | 5 个配置文件

## ⚔️ 配置横向对比

| 特性 | `OneTouch_Config.yaml` | `Pro_en.yaml` | `MihomoPro_Config.yaml` | `Mini_en.yaml` | `Lite_en.yaml` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **大小** | 12.2 KB | 14.9 KB | 22.3 KB | 4.8 KB | 10.0 KB |
| **混合端口** | N/A | 7893 | N/A | 7893 | 7893 |
| **面板地址** | N/A | 127.0.0.1:9090 | N/A | 127.0.0.1:9090 | 127.0.0.1:9090 |
| **运行模式** | 解析失败 | rule | 解析失败 | rule | rule |
| **TUN** | ❌ | 🚫 | ❌ | 🚫 | 🚫 |
| **策略组** | **0** | **37** | **0** | **3** | **17** |
| **规则数** | **0** | **30** | **0** | **8** | **19** |

## 📄 配置详情

#### 📝 OneTouch_Config.yaml
- **路径**: `OneTouch_Config.yaml` | **大小**: 12.2 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/666OS/OneTouch_Config.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

#### 📝 Pro_en.yaml
- **路径**: `Pro_en.yaml` | **大小**: 14.9 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/666OS/Pro_en.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (37个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 GUARD | `select` |
| 👆 SPEEDTEST | `select` |
| 👆 TM | `select` |
| 👆 SOCIAL | `select` |
| 👆 AI | `select` |
| 👆 DEV | `select` |
| 👆 EMBY | `select` |
| 👆 STREAMING | `select` |
| 👆 GAMES | `select` |
| 👆 CRYPTO | `select` |
| 👆 GOOGLE | `select` |
| 👆 FACEBOOK | `select` |
| 👆 MICROSOFT | `select` |
| 👆 APPLE | `select` |
| 👆 OUTCN | `select` |
| 👆 CN | `select` |
| 👆 MATCH | `select` |
| 🔧 FALLBACK | `fallback` |
| 👆 MANUAL | `select` |
| 👆 HK | `select` |
| ... | 还有 17 个 |
</details>

#### 📝 MihomoPro_Config.yaml
- **路径**: `MihomoPro_Config.yaml` | **大小**: 22.3 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/666OS/MihomoPro_Config.yaml)
- **模式**: 解析失败 | **TUN**: ❌ | **IPv6**: ❌

#### 📝 Mini_en.yaml
- **路径**: `Mini_en.yaml` | **大小**: 4.8 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/666OS/Mini_en.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (3个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 OUTCN | `select` |
| 👆 CN | `select` |
| 👆 MATCH | `select` |
</details>

#### 📝 Lite_en.yaml
- **路径**: `Lite_en.yaml` | **大小**: 10.0 KB | [查看源码](https://github.com/gog-xie/MIHOMO_YAMLS/blob/main/THEYAMLS/General_Config/666OS/Lite_en.yaml)
- **模式**: rule | **TUN**: 🚫 | **IPv6**: 🚫
<details>
<summary>🔍 策略组 (17个)</summary>

| 名称 | 类型 |
| :--- | :--- |
| 👆 TM | `select` |
| 👆 SOCIAL | `select` |
| 👆 AI | `select` |
| 👆 DEV | `select` |
| 👆 STREAMING | `select` |
| 👆 APPLE | `select` |
| 👆 OUTCN | `select` |
| 👆 CN | `select` |
| 👆 MATCH | `select` |
| 🔧 FALLBACK | `fallback` |
| 👆 MANUAL | `select` |
| ♻️ HK | `url-test` |
| ♻️ TW | `url-test` |
| ♻️ JP | `url-test` |
| ♻️ SG | `url-test` |
| ♻️ KR | `url-test` |
| ♻️ US | `url-test` |
</details>
