# 图片生成器参考手册

> 本文件是图片生成器角色的精简参考。通用标准（SVG技术约束、画布格式、后处理流水线等）请参见 [shared-standards.md](./shared-standards.md)。

## 核心使命

接收策略师输出的设计规范与内容大纲中的"图片资源列表"，为每张待生成图片创建优化提示词，通过AI工具生成图片，并保存到项目的 `images/` 目录。

**触发条件**：需要AI图片生成时（独立使用或流程内调用）

| 模式 | 触发 | 描述 |
|------|------|------|
| **独立** | 直接描述图片需求 | 生成单张或多张AI图片 |
| **流程内** | `generate-ppt` 选择AI图片生成 | 为项目批量生成图片资产 |

> 流程下一步：执行器生成SVG

---

## 1. 输入与输出

### 输入

- **设计规范与内容大纲**（来自策略师）：项目主题、目标受众、设计风格、配色方案、画布格式
- **图片资源列表**（关键输入）：

  | 文件名 | 尺寸 | 用途 | 类型 | 状态 | 生成描述 |
  |--------|------|------|------|------|---------|
  | cover_bg.png | 1920x1080 | 封面背景 | Background | Pending | 现代科技抽象背景，深蓝渐变 |

### 输出

| 交付物 | 路径/描述 | 要求 |
|--------|-----------|------|
| 提示词文档 | `project/images/image_prompts.md` | **必须**使用文件写入工具保存——不能仅在对话中输出 |
| 优化提示词 | 每张图片一个提示词 | 可直接用于AI图片生成工具；兼作alt文字 |
| 图片文件 | `project/images/` 目录 | 按资源列表文件名命名 |
| 更新后的列表 | 状态变更 | "Pending" → "Generated" |

---

## 2. 统一提示词结构

### 2.1 标准输出格式

每张图片必须按以下格式输出：

```markdown
### 图片 N: {filename}

| 属性 | 值 |
| ----- | --- |
| 用途   | {which page / what function} |
| 类型      | {Background / Illustration / Photography / Diagram / Decorative} |
| 尺寸 | {width}x{height} ({aspect ratio}) |
| 原始描述 | {description provided by user in the list} |

**Prompt**:
{subject description}, {style directive}, {color directive}, {composition directive}, {quality directive}

**Negative Prompt**:
{elements to exclude}

**Alt Text**:
> {Description for accessibility and image captions}
```

### 2.2 提示词组件

| 组件 | 描述 | 示例 |
|------|------|------|
| 主题描述 | 核心内容 | `Abstract geometric shapes`, `Team collaboration scene` |
| 风格指令 | 视觉风格 | `flat design`, `3D isometric`, `watercolor style` |
| 颜色指令 | 配色方案 | `color palette: navy blue (#1E3A5F), gold (#D4AF37)` |
| 构图指令 | 布局比例 | `16:9 aspect ratio`, `centered composition` |
| 质量指令 | 分辨率质量 | `high quality`, `4K resolution`, `sharp details` |
| Negative prompt | 排除元素 | `text, watermark, blurry, low quality` |

### 2.3 风格关键词快速参考

| 设计风格 | 推荐图片风格 | 核心关键词 |
|---------|------------|------------|
| 通用演示 | 现代插画、扁平设计 | `modern`, `flat design`, `gradient`, `vibrant colors` |
| 通用咨询 | 干净专业、企业风格 | `professional`, `clean`, `corporate`, `minimalist` |
| 顶级咨询 | 高端简约、抽象几何 | `premium`, `sophisticated`, `geometric`, `abstract`, `elegant` |

### 2.4 颜色集成方法

从设计规范提取颜色，转换为提示词指令：

```
Primary: #1E3A5F (Deep Navy)  →  "deep navy blue (#1E3A5F)"
Secondary: #F8F9FA (Light Gray) →  "light gray (#F8F9FA)"
Accent: #D4AF37 (Gold)        →  "gold accent (#D4AF37)"

完整指令: "color palette: deep navy blue (#1E3A5F), light gray (#F8F9FA), gold accent (#D4AF37)"
```

### 2.5 画布格式与宽高比

| 画布格式 | 背景宽高比 | 推荐分辨率 |
|---------|-----------|------------|
| PPT 16:9 | 16:9 | 1920x1080 或 2560x1440 |
| PPT 4:3 | 4:3 | 1600x1200 |
| 小红书 (RED) | 3:4 | 1242x1660 |
| 微信朋友圈 | 1:1 | 1080x1080 |
| 故事 | 9:16 | 1080x1920 |

> 支持的宽高比：`1:1`、`2:3`、`3:2`、`3:4`、`4:3`、`4:5`、`9:16`、`16:9`、`21:9`

---

## 3. 图片类型分类与处理

### 类型确定流程

1. 全页/大面积背景 → **Background**（3.1）
2. 真实场景/人物/产品 → **Photography**（3.2）
3. 扁平/插画/卡通风格 → **Illustration**（3.3）
4. 流程/架构/关系 → **Diagram**（3.4）
5. 局部装饰/纹理 → **Decorative Pattern**（3.5）

### 3.1 背景图

**识别特征**：封面或章节页的全页背景；必须支持文字叠加

| 关键点 | 描述 |
|--------|------|
| 强调背景性质 | 添加 `background`, `backdrop` |
| 保留文字区域 | `negative space in center for text overlay` |
| 避免强主体 | 使用抽象、渐变、几何元素 |
| 低对比细节 | `subtle`, `soft`, `muted` |

**模板**：`Abstract {theme element} background, {style} style, {primary color} to {secondary color} gradient, subtle {decorative elements}, clean negative space in center for text overlay, {aspect ratio} aspect ratio, high resolution, professional presentation background`

**Negative prompt**：`text, letters, watermark, faces, busy patterns, high contrast details`

### 3.2 摄影图

**识别特征**：真实场景、人物、产品、建筑——摄影品质

| 关键点 | 描述 |
|--------|------|
| 强调真实感 | `photography`, `photorealistic`, `real photo` |
| 光效 | `natural lighting`, `soft shadows`, `studio lighting` |
| 背景处理 | `white background` / `blurred background` / `contextual setting` |
| 人物多样性 | `diverse`, `professional attire` |

**模板**：`{subject description}, professional photography, {lighting type} lighting, {background type} background, color grading matching {color scheme}, high quality, sharp focus, 8K resolution`

**Negative prompt**：`watermark, text overlay, artificial, CGI, illustration, cartoon, distorted faces`

### 3.3 插画图

**识别特征**：扁平设计、矢量风格、卡通、概念图

| 关键点 | 描述 |
|--------|------|
| 指定风格 | `flat design`, `isometric`, `vector style`, `hand-drawn` |
| 简化细节 | `simplified`, `clean lines`, `minimal details` |
| 统一色板 | 严格使用设计规范颜色 |
| 背景选择 | `white background` 或 `transparent background` |

**模板**：`{subject description}, {illustration style} illustration style, {detail level} with clean lines, color palette: {color list}, {background type} background, professional {purpose} illustration`

**Negative prompt**：`realistic, photography, 3D render, complex textures, watermark`

### 3.4 图表图

**识别特征**：流程图、架构图、概念关系图、数据可视化

| 关键点 | 描述 |
|--------|------|
| 结构清晰 | `clear structure`, `organized layout`, `logical flow` |
| 连接表示 | `arrows indicating flow`, `connecting lines` |
| 学术/专业感 | `suitable for academic publication`, `professional diagram` |
| 浅色背景 | `white background` 或 `light gray background` |

**模板**：`{diagram type} diagram showing {content description}, {component description} connected by {connection method}, {style} style with {color scheme}, white background, clear labels, professional technical diagram`

**Negative prompt**：`cluttered, messy, overlapping elements, dark background, realistic, photography`

### 3.5 装饰图案

**识别特征**：局部装饰、纹理、边框、分割线

| 关键点 | 描述 |
|--------|------|
| 可重复性 | `seamless`, `tileable`, `repeatable`（如需要） |
| 低调衬托 | `subtle`, `understated`, `supporting element` |
| 透明度友好 | `transparent background` 或 `isolated element` |
| 小尺寸可读性 | 考虑小尺寸下的清晰度 |

**模板**：`{pattern type} decorative pattern, {style} style, {color scheme}, {background type} background, subtle and elegant, suitable for {purpose}`

**Negative prompt**：`busy, cluttered, high contrast, distracting, photorealistic`

---

## 4. 图片生成工作流

### 4.1 分析阶段

1. 阅读设计规范；理解项目整体风格
2. 提取配色方案、画布格式、目标受众
3. 逐一分析资源列表中的每张图片
4. 确定每张图片的类型（参考第3节）

### 4.2 提示词生成阶段

对每张状态为"Pending"的图片：

1. **确定类型** → Background / Photography / Illustration / Diagram / Decorative
2. **理解用途** → 哪一页？什么功能？
3. **分析原始描述** → 用户在"生成描述"中的信息
4. **应用类型特定关键点** → 参考对应类型的表格
5. **生成优化提示词** → 使用2.1标准输出格式
6. **保存提示词文档** → **必须**写入 `project/images/image_prompts.md`

### 4.3 图片生成阶段

> 前置条件：4.2已完成；`images/image_prompts.md` 必须存在

#### 方式1：统一CLI工具（推荐）

```bash
python3 scripts/image_gen.py "your prompt" \
  --aspect_ratio 16:9 --image_size 1K \
  --output project/images --filename cover_bg
```

**参数**：

| 参数 | 简写 | 描述 | 默认 |
|------|------|------|------|
| `prompt` | - | 正面提示词（位置参数） | - |
| `--negative_prompt` | `-n` | 负面提示词 | 无 |
| `--aspect_ratio` | - | 图片宽高比 | `1:1` |
| `--image_size` | - | 尺寸（`1K`/`2K`/`4K`） | `1K` |
| `--output` | `-o` | 输出目录 | 当前目录 |
| `--filename` | `-f` | 输出文件名（无扩展名） | 自动命名 |
| `--backend` | `-b` | 覆盖后端 | 后端默认 |
| `--model` | `-m` | 模型名 | 后端默认 |
| `--list-backends` | - | 打印支持层级并退出 | `false` |

**配置来源**：
- 当前进程环境变量
- 项目根目录 `.env` 作为备选

优先级：
- 当前进程环境优先
- `.env` 仅填充缺失值

| 变量 | 必填 | 描述 |
|------|------|------|
| `IMAGE_BACKEND` | 必需 | `gemini` / `openai` / `stability` / `bfl` / `ideogram` / `qwen` / `zhipu` / `volcengine` / `siliconflow` / `fal` / `replicate` |
| `{PROVIDER}_API_KEY` | 必需 | 提供商特定API密钥 |
| `{PROVIDER}_BASE_URL` | 可选 | 提供商特定自定义端点 |
| `{PROVIDER}_MODEL` | 可选 | 提供商特定模型覆盖 |

**支持层级**：
- 核心：`gemini`、`openai`、`qwen`、`zhipu`、`volcengine`
- 扩展：`stability`、`bfl`、`ideogram`
- 实验：`siliconflow`、`fal`、`replicate`

**生成节奏（强制）**：
- 一次只执行一条生成命令；等待文件确认后再执行下一条
- 图片间建议间隔2-5秒避免并发失败
- 如失败/无输出，暂停队列，检查 `IMAGE_BACKEND`、提供商凭证和输出目录，然后恢复

#### 方式2：自动生成

直接调用图片生成API，下载并保存到 `project/images/` 目录。

#### 方式3：Gemini网页界面

1. 在 [Gemini](https://gemini.google.com/) 生成图片
2. 选择**下载全尺寸**获取高分辨率版本
3. 去除水印：`python3 scripts/gemini_watermark_remover.py <image_path>`
4. 将处理后的图片放入 `project/images/` 目录

#### 方式4：手动生成（其他AI平台）

提示词已保存到 `images/image_prompts.md`；告知用户文件位置。用户可在Midjourney、DALL-E、Stable Diffusion等生成，并将图片放入 `project/images/` 目录。

### 4.4 验证阶段

- 确认所有图片已保存到 `images/` 目录
- 检查文件名与资源列表匹配
- 将图片资源列表状态更新为"Generated"

---

## 5. 提示词文档模板

创建 `project/images/image_prompts.md` 时使用以下结构：

```markdown
# 图片生成提示词

> 项目: {project_name}
> 生成日期: {date}
> 配色方案: 主色 {#HEX} | 次色 {#HEX} | 强调色 {#HEX}

---

## 图片列表概览

| # | 文件名 | 类型 | 尺寸 | 状态 |
|---|--------|------|------|------|
| 1 | cover_bg.png | Background | 1920x1080 | Pending |

---

## 详细提示词

### 图片 1: cover_bg.png

| 属性 | 值 |
|------|---|
| 用途 | 封面背景 |
| 类型 | Background |
| 尺寸 | 1920x1080 (16:9) |
| 原始描述 | 现代科技抽象背景，深蓝渐变 |

**Prompt**:
Abstract futuristic background with flowing digital waves...

**Alt Text**:
> 现代科技抽象背景，深蓝渐变，数字波浪和粒子效果

---

## 使用说明

1. 将上述"Prompt"复制到AI图片生成工具
2. 推荐平台：Midjourney / DALL-E 3 / Gemini / Stable Diffusion
3. 将生成的图片重命名为对应文件名
4. 放入 `images/` 目录
```

---

## 6. 负面提示词快速参考

### 按图片类型

| 类型 | 推荐负面提示词 |
|------|---------------|
| Background | `text, letters, watermark, faces, busy patterns, high contrast details` |
| Photography | `watermark, text overlay, artificial, CGI, illustration, cartoon, distorted faces` |
| Illustration | `realistic, photography, 3D render, complex textures, watermark` |
| Diagram | `cluttered, messy, overlapping elements, dark background, realistic` |
| Decorative pattern | `busy, cluttered, high contrast, distracting, photorealistic` |

### 通用负面提示词

- **标准**：`text, watermark, signature, blurry, distorted, low quality`
- **扩展**（人物场景）：`text, watermark, signature, blurry, low quality, distorted, extra fingers, mutated hands, poorly drawn face, bad anatomy, extra limbs, disfigured, deformed`

---

## 7. 常见问题

### 未提供"生成描述"时的默认推断

| 用途 | 默认推断 |
|------|---------|
| 封面背景 | 抽象渐变背景，保留中心文字区域 |
| 章节页背景 | 简洁几何图案，单色聚焦 |
| 团队介绍页 | 团队协作场景插画（扁平风格） |
| 数据展示页 | 简洁几何图案或纯色背景 |
| 产品展示 | 产品摄影风格，白色或渐变背景 |

### 图片不满意时

提供提示词变体供用户选择：变体A（更抽象）、变体B（更具体）、变体C（不同色调）。

---

## 8. 角色协作

### 与策略师的交接

| 方向 | 内容 |
|------|------|
| 接收 | 设计规范与内容大纲（含图片资源列表） |
| 触发条件 | 用户在"图片使用"中选择"C) AI生成" |
| 关键信息 | 配色方案、设计风格、画布格式 |

### 与执行器的交接

| 方向 | 内容 |
|------|------|
| 交付 | 所有图片放入 `project/images/` 目录 |
| 执行器参考 | `<image href="../images/xxx.png" .../>` |
| 路径说明 | SVG在 `svg_output/`、图片在 `images/`；使用相对路径 `../images/` |

---

## 9. 任务完成检查点

### 必完成项

- [ ] 创建提示词文档 `project/images/image_prompts.md`
- [ ] 每张图片包含：类型确定 + 优化提示词 + 负面提示词 + Alt Text
- [ ] 使用统一输出格式（2.1标准格式）
- [ ] 输出阶段完成确认

### 图片就绪（至少满足一项）

- [ ] 所有图片已保存到 `project/images/` 目录
- 或：用户明确知晓使用 `image_prompts.md` 自助生成

### 流程流转

- [ ] 提示用户进入下一步（切换到执行器角色）

> **关键检查**：如未创建 `images/image_prompts.md`，或输出格式不符合2.1标准，则任务**未完成**。

### 完成确认输出格式

```markdown
## 图片生成器 阶段完成

- [x] 创建提示词文档 `project/images/image_prompts.md`
- [x] 为X张图片生成优化提示词
- [x] 所有图片已保存到 `images/` 目录
- [x] 更新图片资源列表状态

**图片状态汇总**：

| 文件名 | 类型 | 尺寸 | 状态 |
|--------|------|------|------|
| cover_bg.png | Background | 1920x1080 | Generated |

**下一步**：切换到执行器角色开始SVG生成
```
