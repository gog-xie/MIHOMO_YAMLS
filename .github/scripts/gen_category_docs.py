import os
import urllib.parse
import yaml
from yaml import SafeLoader

# ================= 配置部分 =================
REPO_URL_BASE = os.getenv("GITHUB_REPOSITORY", "")
REPO_URL = f"https://github.com/{REPO_URL_BASE}/blob/main"

# 定义主分类
CATEGORIES = {
    "THEYAMLS/Official_Examples": "Mihomo 官方示例 (Official)",
    "THEYAMLS/General_Config": "通用进阶配置 (General Config)",
    "THEYAMLS/Smart_Mode": "Smart 模式 / 路由专用 (Smart Mode)",
    "THEYAMLS/Mobile_Modules": "Android 手机模块 (Mobile Modules)"
}

IGNORE_FILES = ["README.md", "LICENSE", "release_body.md"]
# ===========================================

# 忽略所有 !自定义tag，不中断解析
def ignore_unknown_tag(loader, suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node, deep=False)
    elif isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node, deep=False)
    else:
        return loader.construct_scalar(node)

yaml.add_multi_constructor("!", ignore_unknown_tag, Loader=SafeLoader)

# 关闭锚点、别名严格校验，允许残缺&/*语法
SafeLoader.yaml_implicit_resolvers.pop('&', None)
SafeLoader.yaml_implicit_resolvers.pop('*', None)

def clean_cell(text):
    if text is None: return "N/A"
    return str(text).replace("|", "&#124;").replace("\n", " ").strip() or "N/A"

def get_size(path):
    try:
        size = os.path.getsize(path)
        return f"{size} B" if size < 1024 else f"{size/1024:.1f} KB"
    except:
        return "Unknown"

def analyze(path):
    """解析单个YAML，仅读取顶层基础参数，遇到畸形语法直接兜底"""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read().replace("\t", "  ")
        
        # 仅补充文档头，不修改内部锚点/流式代码
        stripped = content.lstrip()
        if not stripped.startswith("---"):
            content = "---\n" + content
        
        # 浅加载，不递归解析<<: *别名合并块，避免合并语法报错
        data = yaml.safe_load(content)
        if not isinstance(data, dict):
            raise ValueError("根节点非字典")
        
        # 只读取顶层独立字段，不进入锚点合并子块
        info = {
            "mode": data.get("mode", "rule"),
            "ipv6": "✅" if str(data.get("ipv6", False)).lower() == "true" else "🚫",
            "tun": "✅" if data.get("tun", {}).get("enable") else "🚫",
            "mixed_port": data.get("mixed-port", "-"),
            "ext_ctrl": data.get("external-controller", "-"),
            "group_count": 0,
            "rule_count": 0,
            "groups": []
        }

        # 单独捕获proxy-groups、rules读取错误，就算子块畸形也不整体失败
        try:
            groups = data.get("proxy-groups", [])
            if isinstance(groups, list):
                info["group_count"] = len(groups)
                for g in groups[:20]:
                    if isinstance(g, dict):
                        name = clean_cell(g.get("name", "Unknown"))
                        gtype = g.get("type", "select")
                        icon = {"url-test": "♻️", "fallback": "🔧", "load-balance": "⚖️"}.get(gtype, "👆")
                        info["groups"].append(f"| {icon} {name} | `{gtype}` |")
        except Exception:
            pass
        
        try:
            rules = data.get("rules", [])
            if isinstance(rules, list):
                info["rule_count"] = len(rules)
        except Exception:
            pass

        return info

    except Exception as e:
        print(f"⚠️ Parse error {path}: {e}")
        # 解析失败兜底，文件正常计入统计表格
        return {
            "mode": "解析失败",
            "ipv6": "❌",
            "tun": "❌",
            "mixed_port": "N/A",
            "ext_ctrl": "N/A",
            "group_count": 0,
            "rule_count": 0,
            "groups": []
        }

def scan_folder(folder):
    files = []
    if not os.path.isdir(folder): return files
    for root, dirs, filenames in os.walk(folder):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in filenames:
            if f.endswith(('.yaml', '.yml')) and f not in IGNORE_FILES:
                full = os.path.join(root, f)
                files.append((os.path.relpath(full, folder), full))
    return files

def make_readme(folder, title, files, back_link_text, back_link_url):
    if not files: return
    data_map = {}
    for rel, full in files:
        parsed = analyze(full)
        data_map[rel] = {"size": get_size(full), "info": parsed}
    if not data_map: return

    lines = [f"# 📂 {title}", "", f"[{back_link_text}]({back_link_url})", "", f"> 🤖 自动技术分析 | {len(data_map)} 个配置文件", ""]
    if len(data_map) > 1:
        lines.extend(["## ⚔️ 配置横向对比", ""])
        headers = ["特性"] + [f"`{os.path.basename(k)}`" for k in data_map.keys()]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| :--- " + "| :--- " * len(data_map) + "|")
        lines.append("| **大小** | " + " | ".join([v["size"] for v in data_map.values()]) + " |")
        configs = [("mixed_port", "混合端口"), ("ext_ctrl", "面板地址"), ("mode", "运行模式"), 
                   ("tun", "TUN"), ("group_count", "策略组"), ("rule_count", "规则数")]
        for key, label in configs:
            row = [f"**{label}**"]
            for v in data_map.values():
                val = v["info"].get(key, "-")
                row.append(f"**{val}**" if "count" in key else clean_cell(val))
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")
    lines.extend(["## 📄 配置详情", ""])
    by_author = {}
    for rel, data in data_map.items():
        author = rel.split(os.sep)[0] if os.sep in rel else "Root"
        by_author.setdefault(author, []).append((rel, data))
    for author, items in sorted(by_author.items()):
        if author != "Root":
            lines.extend([f"### 👤 {author}", ""])
        for rel, data in items:
            info = data["info"]
            url_path = os.path.join(folder, rel).replace(os.sep, '/')
            url = f"{REPO_URL}/{urllib.parse.quote(url_path)}"
            lines.append(f"#### 📝 {os.path.basename(rel)}")
            lines.append(f"- **路径**: `{rel}` | **大小**: {data['size']} | [查看源码]({url})")
            lines.append(f"- **模式**: {info['mode']} | **TUN**: {info['tun']} | **IPv6**: {info['ipv6']}")
            if info["groups"]:
                lines.extend(["<details>", f"<summary>🔍 策略组 ({info['group_count']}个)</summary>", "", 
                              "| 名称 | 类型 |", "| :--- | :--- |"] + info["groups"])
                if info["group_count"] > 20: lines.append(f"| ... | 还有 {info['group_count']-20} 个 |")
                lines.append("</details>")
            lines.append("")
        if author != "Root":
            lines.append("---")
    out_path = os.path.join(folder, "README.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Generated: {out_path}")

def process_category(folder, title):
    if not os.path.isdir(folder): return
    all_files = scan_folder(folder)
    make_readme(folder, title, all_files, "🔙 返回主页", "../../README.md")
    try:
        sub_dirs = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d)) and not d.startswith('.')]
    except OSError:
        sub_dirs = []
    for sub_dir in sub_dirs:
        sub_path = os.path.join(folder, sub_dir)
        sub_files = scan_folder(sub_path)
        if sub_files:
            sub_title = f"{sub_dir} ({title.split(' ')[0]})"
            make_readme(sub_path, sub_title, sub_files, "🔙 返回上一级", "../README.md")

if __name__ == "__main__":
    for folder, title in CATEGORIES.items():
        process_category(folder, title)
