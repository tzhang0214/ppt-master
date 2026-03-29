> 通用技术约束请参见 shared-standards.md。

# SVG图片嵌入指南

向SVG文件添加图片的技术规范和推荐工作流。

---

## 图片资源列表格式

在设计规范与内容大纲中定义；每张图片有状态标注。如果图片方式包含"B) 用户提供"，必须在策略师完成八项确认后立即运行 `analyze_images.py`，并在输出设计规范前完成列表。

```markdown
| 文件名 | 尺寸 | 用途 | 状态 | 生成描述 |
|--------|------|------|------|---------|
| cover_bg.png | 1280x720 | 封面背景 | Pending | 现代科技抽象背景，深蓝渐变 |
| product.png | 600x400 | 第3页 | Existing | - |
| team.png | 600x400 | 第5页 | Placeholder | 团队协作场景（稍后添加） |
```

### 三种状态类型

| 状态 | 含义 | 执行器处理 |
|------|------|---------|
| **Pending** | 需要AI生成，有描述 | 先生成图片到 `images/`，然后用 `<image>` 引用 |
| **Existing** | 用户已有图片 | 放入 `images/`，用 `<image>` 引用 |
| **Placeholder** | 尚未处理 | 使用虚线边框占位符；稍后替换 |

---

## 工作流

```
1. 策略师定义图片需求 → 添加图片资源列表，标注每张状态
2. 图片准备（待生成/已有） → 放入 project/images/
3. 执行器生成SVG（svg_output/）
   ├── 已有/待生成 → <image href="../images/xxx.png" .../>
   └── 占位符 → 虚线边框 + 描述文字
4. 预览: python3 -m http.server -d <项目路径> 8000 → /svg_output/<filename>.svg
5. 后处理与导出
   ├── python3 scripts/finalize_svg.py <项目路径>
   └── python3 scripts/svg_to_pptx.py <项目路径> -s final
```

> 推荐：在生成阶段保持外部引用在 `svg_output/`。后处理通过 `finalize_svg.py` 自动将图片嵌入 `svg_final/`，然后从 `svg_final/` 导出PPTX。

---

## 外部引用 vs Base64嵌入

| 方式 | 优点 | 缺点 | 适用 |
|------|------|------|------|
| **外部引用** | 文件小，迭代快，易替换 | 预览需要从项目根目录启动HTTP服务器 | `svg_output/` 开发阶段 |
| **Base64嵌入** | 文件自包含，导出稳定 | 文件大 | `svg_final/` 交付阶段 |

---

## 方式1：外部引用（推荐用于生成阶段）

### 语法

```xml
<image href="../images/image.png" x="0" y="0" width="1280" height="720"
       preserveAspectRatio="xMidYMid slice"/>
```

### 关键属性

| 属性 | 描述 | 示例 |
|------|------|------|
| `href` | 图片路径（相对或绝对） | `"../images/cover.png"` |
| `x`, `y` | 图片左上角位置 | `x="0" y="0"` |
| `width`, `height` | 图片显示尺寸 | `width="1280" height="720"` |
| `preserveAspectRatio` | 缩放模式 | `"xMidYMid slice"` |

### preserveAspectRatio 常用值

| 值 | 效果 |
|------|------|
| `xMidYMid slice` | 居中裁剪（类似CSS `cover`） |
| `xMidYMid meet` | 完整显示（类似CSS `contain`） |
| `none` | 拉伸填充，不保持比例 |

### 预览方式

浏览器安全限制阻止直接打开SVG时加载外部图片。从项目根目录启动HTTP服务器：

```bash
python3 -m http.server -d <项目路径> 8000
# 访问 http://localhost:8000/svg_output/your_file.svg
```

---

## 方式2：Base64嵌入（推荐用于交付阶段）

### 语法

```xml
<image href="data:image/png;base64,iVBORw0KGgo..." x="0" y="0" width="1280" height="720"/>
```

### MIME类型

| MIME类型 | 文件格式 |
|---------|---------|
| `image/png` | PNG |
| `image/jpeg` | JPG/JPEG |
| `image/gif` | GIF |
| `image/webp` | WebP |
| `image/svg+xml` | SVG |

---

## 转换过程

### 推荐：使用 finalize_svg.py（统一流水线）

```bash
python3 scripts/finalize_svg.py <项目路径>         # 图标、图片、文字、圆角rect——一气呵成
python3 scripts/svg_to_pptx.py <项目路径> -s final  # 从最终版导出PPTX
```

### 独立使用：embed_images.py（高级用法）

处理特定SVG而不运行完整流水线：

```bash
python3 scripts/svg_finalize/embed_images.py <svg文件>                         # 单文件
python3 scripts/svg_finalize/embed_images.py <项目路径>/svg_output/*.svg    # 批量
python3 scripts/svg_finalize/embed_images.py --dry-run <项目路径>/svg_output/*.svg  # 预览
```

---

## 最佳实践

### 图片优化

嵌入前压缩图片以减小文件大小：

```bash
convert input.png -quality 85 -resize 1920x1080\> output.png  # ImageMagick
pngquant --quality=65-80 input.png -o output.png               # pngquant（推荐）
```

### 文件组织

```
project/
├── images/            # 图片资产
├── sources/           # 源文件及其附带图片
│   └── article_files/
├── svg_output/        # 原始版本（外部引用）
└── svg_final/         # 最终版本（图片嵌入）
```

### 圆角处理（禁止clipPath）

由于 `clipPath` 与PPT不兼容，图片圆角的裁剪路径是**禁止**的。替代方案：
- 在图片生成时处理圆角（导出带圆角的PNG）
- 或在边缘叠加等尺寸圆角矩形（视觉模拟）

---

## 常见问题

**Q: 直接打开SVG时看不到图片？**
浏览器安全策略阻止跨目录请求。从项目根目录启动HTTP服务器，或先运行 `finalize_svg.py` 再从 `svg_final/` 查看。

**Q: Base64文件太大？**
压缩原始图片，使用JPEG格式，减小分辨率（匹配实际显示尺寸）。

**Q: 如何反向提取Base64图片？**
```bash
base64 -d image.b64 > image.png
```
