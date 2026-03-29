# 共享技术标准

PPT Master 的通用技术约束，消除跨角色文件重复。

---

## 1. SVG 禁止功能黑名单

生成 SVG 时**绝对禁止**以下功能——使用任何一项都会导致 PPT 导出失败：

| 禁止功能 | 描述 |
|---------|------|
| `clipPath` | 裁剪路径 |
| `mask` | 蒙版 |
| `<style>` | 内嵌样式表 |
| `class` | CSS选择器属性（`<defs>` 内的 `id` 是合法引用，**不被禁止**） |
| 外部CSS | 外部样式表链接 |
| `<foreignObject>` | 内嵌外部内容 |
| `<symbol>` + `<use>` | 符号引用复用 |
| `textPath` | 沿路径文字 |
| `@font-face` | 自定义字体声明 |
| `<animate*>` / `<set>` | SVG动画 |
| `<script>` / 事件属性 | 脚本和交互 |
| `marker` / `marker-end` | 线条端点标记 |
| `<iframe>` | 内嵌框架 |

---

## 2. PPT 兼容性替代方案

| 禁止语法 | 正确替代方案 |
|---------|-------------|
| `fill="rgba(255,255,255,0.1)"` | `fill="#FFFFFF" fill-opacity="0.1"` |
| `<g opacity="0.2">...</g>` | 在每个子元素上单独设置 `fill-opacity` / `stroke-opacity` |
| `<image opacity="0.3"/>` | 在图片后叠加遮罩层 `<rect fill="背景色" opacity="0.7"/>` |
| `marker-end` 箭头 | 用 `<polygon>` 绘制三角形箭头 |

**助记**：PPT 不识别 rgba、组透明度、图片透明度或 markers。

---

## 3. 画布格式快速参考

### 演示文稿

| 格式 | viewBox | 尺寸 | 比例 |
|------|---------|------|------|
| PPT 16:9 | `0 0 1280 720` | 1280x720 | 16:9 |
| PPT 4:3 | `0 0 1024 768` | 1024x768 | 4:3 |

### 社交媒体

| 格式 | viewBox | 尺寸 | 比例 |
|------|---------|------|------|
| 小红书 (RED) | `0 0 1242 1660` | 1242x1660 | 3:4 |
| 微信朋友圈/Instagram | `0 0 1080 1080` | 1080x1080 | 1:1 |
| 故事/TikTok竖版 | `0 0 1080 1920` | 1080x1920 | 9:16 |

### 营销物料

| 格式 | viewBox | 尺寸 | 比例 |
|------|---------|------|------|
| 微信文章封面 | `0 0 900 383` | 900x383 | 2.35:1 |
| 横版Banner | `0 0 1920 1080` | 1920x1080 | 16:9 |
| 竖版海报 | `0 0 1080 1920` | 1080x1920 | 9:16 |
| A4打印 (150dpi) | `0 0 1240 1754` | 1240x1754 | 1:1.414 |

---

## 4. 基础 SVG 规则

- **viewBox** 必须与画布尺寸匹配（`width`/`height` 必须与 `viewBox` 一致）
- **背景**：使用 `<rect>` 定义页面背景色
- **换行**：使用 `<tspan>` 手动换行；**禁止** `<foreignObject>`
- **字体**：仅使用系统字体（Microsoft YaHei、Arial、Calibri 等）；**禁止** `@font-face`
- **样式**：仅使用内联样式（`fill="..."` `font-size="..."`）；**禁止** `<style>` / `class`（`<defs>` 内的 `id` 是合法的）
- **颜色**：使用 HEX 值；透明度使用 `fill-opacity` / `stroke-opacity`
- **图片引用**：`<image href="../images/xxx.png" preserveAspectRatio="xMidYMid slice"/>`
- **图标占位符**：`<use data-icon="icon-name" x="" y="" width="48" height="48" fill="#HEX"/>`（后处理时自动嵌入）

---

## 5. 后处理流水线（3步）

必须按顺序执行——禁止跳过或添加额外参数：

```bash
# 1. 将演讲备注拆分为每页备注文件
python3 scripts/total_md_split.py <项目路径>

# 2. SVG后处理（图标嵌入、图片裁剪/嵌入、文字扁平化、圆角rect转path）
python3 scripts/finalize_svg.py <项目路径>

# 3. 导出PPTX（从svg_final/，默认嵌入演讲备注）
python3 scripts/svg_to_pptx.py <项目路径> -s final
# 默认：生成原生形状(.pptx) + SVG参考(_svg.pptx)
```

**禁止事项**：
- 禁止使用 `cp` 替代 `finalize_svg.py`
- 禁止直接从 `svg_output/` 导出——必须从 `svg_final/` 导出（使用 `-s final`）
- 禁止添加额外参数如 `--only`

**重运行规则**：后处理完成后对 `svg_output/` 的任何修改（包括页面修订、添加或删除）都需要重新运行步骤2和3。仅当 `notes/total.md` 也被修改时才需要重新运行步骤1。

---

## 6. 阴影与叠加技术

> `<mask>` 元素和 `<image opacity="...">` 被禁止。始终使用堆叠 `<rect>` 或渐变叠加代替（见 §2）。

### 阴影

#### 滤镜柔和阴影 — 推荐

适用于：卡片、浮动面板、浮起元素。`svg_to_shapes.py` 自动将 `feGaussianBlur` + `feOffset` 转换为原生 PPTX `<a:outerShdw>`。

```xml
<defs>
  <filter id="softShadow" x="-15%" y="-15%" width="140%" height="140%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="8"/>
    <feOffset dx="0" dy="4" result="offsetBlur"/>
    <feFlood flood-color="#000000" flood-opacity="0.08" result="shadowColor"/>
    <feComposite in="shadowColor" in2="offsetBlur" operator="in" result="shadow"/>
    <feMerge>
      <feMergeNode in="shadow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>
<rect x="60" y="60" width="400" height="240" rx="12" fill="#FFFFFF" filter="url(#softShadow)"/>
```

推荐参数：
```
stdDeviation:   6–10     （越小越锐利，越大越柔和）
flood-opacity:  0.06–0.12  （保持低位以获得高级质感）
dy:             3–6      （垂直 > 水平，模拟自然顶光）
dx:             0–2
```

#### 彩色阴影

适用于：强调按钮、品牌色卡片。使用元素自身的色系而非黑色。

```xml
<filter id="colorShadow" x="-15%" y="-15%" width="140%" height="140%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="10"/>
  <feOffset dx="0" dy="6" result="offsetBlur"/>
  <feFlood flood-color="#1A73E8" flood-opacity="0.20" result="shadowColor"/>
  <feComposite in="shadowColor" in2="offsetBlur" operator="in" result="shadow"/>
  <feMerge>
    <feMergeNode in="shadow"/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

将 `flood-color` 替换为元素品牌色；保持 `flood-opacity` 在 0.12–0.20 之间。

#### 层叠矩形阴影 — 高兼容性备选

适用于：最大化与旧版 PowerPoint 的兼容性。在主卡片后堆叠2-3个半透明矩形：

```xml
<!-- 阴影层（从后到前，偏移最大优先） -->
<rect x="68" y="72" width="400" height="240" rx="16" fill="#000000" fill-opacity="0.03"/>
<rect x="65" y="69" width="400" height="240" rx="14" fill="#000000" fill-opacity="0.05"/>
<rect x="62" y="66" width="400" height="240" rx="12" fill="#1A73E8" fill-opacity="0.04"/>
<!-- 主卡片 -->
<rect x="60" y="60" width="400" height="240" rx="12" fill="#FFFFFF"/>
```

### 图片叠加

#### 线性渐变叠加 — 最常见

适用于：图文页面。渐变方向应与文字位置匹配（文字在左 → 渐变向左变暗）。

```xml
<image href="..." x="0" y="0" width="1280" height="720" preserveAspectRatio="xMidYMid slice"/>
<defs>
  <linearGradient id="imgOverlay" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="#1A1A2E" stop-opacity="0.85"/>
    <stop offset="55%"  stop-color="#1A1A2E" stop-opacity="0.30"/>
    <stop offset="100%" stop-color="#1A1A2E" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect x="0" y="0" width="1280" height="720" fill="url(#imgOverlay)"/>
```

#### 底部渐变条

适用于：封面幻灯片和底部标题的全图页面。

```xml
<defs>
  <linearGradient id="bottomBar" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#000000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#000000" stop-opacity="0.72"/>
  </linearGradient>
</defs>
<rect x="0" y="380" width="1280" height="340" fill="url(#bottomBar)"/>
```

#### 径向渐变叠加 — 暗角效果

适用于：全屏氛围幻灯片；将注意力引向中心。

```xml
<defs>
  <radialGradient id="vignette" cx="50%" cy="50%" r="70%">
    <stop offset="0%"   stop-color="#000000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#000000" stop-opacity="0.58"/>
  </radialGradient>
</defs>
<rect x="0" y="0" width="1280" height="720" fill="url(#vignette)"/>
```

#### 品牌色叠加

适用于：需要强烈视觉品牌识别的幻灯片。

```xml
<defs>
  <linearGradient id="brandOverlay" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="#005587" stop-opacity="0.80"/>
    <stop offset="100%" stop-color="#005587" stop-opacity="0.10"/>
  </linearGradient>
</defs>
<rect x="0" y="0" width="1280" height="720" fill="url(#brandOverlay)"/>
```

### 快速参考表

| 场景 | 推荐技术 | 避免 |
|------|---------|------|
| 卡片/面板阴影 | 滤镜柔和阴影（`flood-opacity` ≤ 0.12） | 硬黑色阴影 |
| 强调/CTA按钮 | 彩色阴影（同色系） | 通用灰色阴影 |
| 图片上的文字 | 线性渐变叠加（方向与文字侧匹配） | 整张图片均匀透明 |
| 封面/全图幻灯片 | 底部渐变条 + 品牌色 | 纯黑叠加 |
| 氛围/英雄幻灯片 | 径向暗角 | 未处理的原始图片 |
| 需要最大PPT兼容性 | 层叠矩形阴影 | 基于滤镜的阴影 |

---

## 7. 项目目录结构

```
project/
├── svg_output/    # 原始SVG（执行器输出，包含占位符）
├── svg_final/     # 后处理最终SVG（finalize_svg.py输出）
├── images/        # 图片资产（用户提供 + AI生成）
├── notes/         # 演讲备注（与SVG名称匹配的.md文件）
│   └── total.md   # 完整演讲备注文档（拆分前）
├── templates/     # 项目模板（如有）
└── *.pptx         # 导出的PPT文件
```
