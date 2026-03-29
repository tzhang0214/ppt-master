---
name: ppt-master
description: >
  AI驱动的多格式SVG内容生成系统。将源文档（PDF/DOCX/URL/Markdown）通过多角色协作转换为高质量SVG页面，
  并导出为PPTX格式。当用户要求"创建PPT"、"制作PPT"、"生成演示文稿"或提到"ppt-master"时使用此技能。
---

# PPT Master 技能指南

> AI驱动的多格式SVG内容生成系统。通过多角色协作将源文档转换为高质量SVG页面，并导出为PPTX格式。

**核心流程**：`源文档 → 创建项目 → 选择模板 → 策略师 → [图片生成器] → 执行器 → 后处理 → 导出`

> [!CAUTION]
> ## 🚨 全局执行纪律（强制执行）
>
> **此工作流程为严格串行管道。以下规则具有最高优先级——违反任何一条即视为执行失败：**
>
> 1. **串行执行** — 各步骤必须按顺序执行；每个步骤的输出是下一步的输入。满足前置条件的非阻塞相邻步骤可连续执行，无需等待用户说"继续"
> 2. **阻塞 = 硬性停止** — 标记为 ⛔ 阻塞的步骤需要完全停止；AI 必须等待用户明确响应后才能继续，不得代为决策
> 3. **禁止跨阶段打包** — 禁止跨阶段打包。（注意：第4步中的八项确认 ⛔ 阻塞——AI 必须呈现建议并等待用户明确确认后才能继续。一旦用户确认，所有后续非阻塞步骤——设计规范输出、SVG生成、演讲备注和后处理——可自动执行，无需进一步用户确认）
> 4. **入口前先验证** — 每个步骤都有列在顶部的前置条件（🚧 门槛）；在开始该步骤前必须验证这些条件
> 5. **禁止预执行** — 禁止"预准备"后续步骤的内容（例如：在策略师阶段编写SVG代码）

> [!IMPORTANT]
> ## 🌐 语言与沟通规则
>
> - **回复语言**：始终匹配用户输入和提供的源材料语言。例如：用户用中文提问就用中文回复；源材料是英文就用英文回复。
> - **明确覆盖**：如果用户明确指定语言（如"请用英文回答"或"Reply in Chinese"），则使用该语言。
> - **模板格式**：`design_spec.md` 文件必须始终遵循其原始英文模板结构（章节标题、字段名称），无论对话使用何种语言。模板内的内容值可使用用户的语言。

## 主要流程脚本

| 脚本 | 用途 |
|------|------|
| `${SKILL_DIR}/scripts/pdf_to_md.py` | PDF转Markdown |
| `${SKILL_DIR}/scripts/doc_to_md.py` | 通过Pandoc将文档转换为Markdown（DOCX、EPUB、HTML、LaTeX、RST等） |
| `${SKILL_DIR}/scripts/web_to_md.py` | 网页转Markdown |
| `${SKILL_DIR}/scripts/web_to_md.cjs` | 微信/高安全性网站转Markdown |
| `${SKILL_DIR}/scripts/project_manager.py` | 项目初始化/验证/管理 |
| `${SKILL_DIR}/scripts/analyze_images.py` | 图片分析 |
| `${SKILL_DIR}/scripts/image_gen.py` | AI图片生成（多提供商） |
| `${SKILL_DIR}/scripts/svg_quality_checker.py` | SVG质量检查 |
| `${SKILL_DIR}/scripts/total_md_split.py` | 演讲备注拆分 |
| `${SKILL_DIR}/scripts/finalize_svg.py` | SVG后处理（统一入口） |
| `${SKILL_DIR}/scripts/svg_to_pptx.py` | 导出为PPTX |

完整工具文档请参阅 `${SKILL_DIR}/scripts/README.md`。

## 模板索引

| 索引 | 路径 | 用途 |
|------|------|------|
| 布局模板 | `${SKILL_DIR}/templates/layouts/layouts_index.json` | 查询可用的页面布局模板 |
| 图表模板 | `${SKILL_DIR}/templates/charts/charts_index.json` | 查询可用的图表SVG模板 |
| 图标库 | `${SKILL_DIR}/templates/icons/icons_index.json` | 查询可用的图标名称和类别 |

## 独立工作流程

| 工作流程 | 路径 | 用途 |
|----------|------|------|
| `create-template` | `workflows/create-template.md` | 独立模板创建工作流程 |

---

## 步骤0：生成模式确认（新用户首次必须执行）

🚧 **门槛**：用户提供了源材料或描述了PPT需求。

在开始工作流程之前，**必须询问用户**选择生成模式：

> 💬 **请选择PPT生成模式：**
> 
> **A) 全自动生成** — AI自动选择最佳配置，适合快速生成
> - 画布格式：PPT 16:9 (`ppt169`)
> - 设计风格：通用演示风格（视觉冲击优先）
> - 配色方案：科技蓝商务风格（`#1565C0` 主色）
> - 模板：Anthropic 科技模板（如可用）
> - 字体：微软雅黑 + Arial
> - 图片：AI生成（如配置）或SVG渐变替代
> 
> **B) 手动配置** — 用户自定义所有配置项
> - 进入标准工作流程，逐步确认各项参数

**选择A（全自动）后的流程**：
1. 使用预设配置直接进入步骤2
2. 跳过步骤3模板确认（使用Anthropic模板）
3. 跳过步骤4八项确认（使用预设方案）
4. 自动进入执行器阶段

> ⚠️ **快速选择**：如果用户只是简单说"帮我做一个PPT"、"生成演示文稿"等，可直接推荐模式A并询问确认。

---

## 工作流程

### 步骤1：源内容处理

🚧 **门槛**：用户提供了源材料（PDF/DOCX/EPUB/URL/Markdown文件/文字描述/对话内容——任何形式均可）。

当用户提供非Markdown内容时，立即转换：

| 用户提供 | 命令 |
|----------|------|
| PDF文件 | `python3 ${SKILL_DIR}/scripts/pdf_to_md.py <file>` |
| DOCX/Word/Office文档 | `python3 ${SKILL_DIR}/scripts/doc_to_md.py <file>` |
| EPUB/HTML/LaTeX/RST/其他 | `python3 ${SKILL_DIR}/scripts/doc_to_md.py <file>` |
| 网页链接 | `python3 ${SKILL_DIR}/scripts/web_to_md.py <URL>` |
| 微信/高安全性网站 | `node ${SKILL_DIR}/scripts/web_to_md.cjs <URL>` |
| Markdown | 直接读取 |

**✅ 检查点 — 确认源内容已就绪，继续步骤2。**

---

### 步骤2：项目初始化

🚧 **门槛**：步骤1完成；源内容已就绪（Markdown文件、用户直接提供的文本或在对话中描述的需求均有效）。

```bash
python3 ${SKILL_DIR}/scripts/project_manager.py init <project_name> --format <format>
```

格式选项：`ppt169`（默认）、`ppt43`、`xhs`、`story` 等。完整格式列表请参阅 `references/canvas-formats.md`。

导入源内容（根据情况选择）：

| 情况 | 操作 |
|------|------|
| 有源文件（PDF/MD等） | `python3 ${SKILL_DIR}/scripts/project_manager.py import-sources <project_path> <source_files...> --move` |
| 用户直接在对话中提供文本 | 无需导入——内容已在对话上下文中；后续步骤可直接引用 |

> ⚠️ **必须使用 `--move`**：所有源文件（原始PDF/MD/图片）必须**移动**（不是复制）到 `sources/` 进行归档。
> - 步骤1生成的Markdown文件、原始PDF、原始MD——**全部**必须通过 `import-sources --move` 移动到项目中
> - 中间产物（如 `_files/` 目录）由 `import-sources` 自动处理
> - 执行后，源文件在其原始位置不再存在

**✅ 检查点 — 确认项目结构创建成功，`sources/` 包含所有源文件，转换材料已就绪。继续步骤3。**

---

### 步骤3：模板选择

🚧 **门槛**：步骤2完成；项目目录结构已就绪。

> ⚠️ **全自动模式跳过**：如果用户在步骤0选择了模式A（全自动），直接跳过此步骤，使用Anthropic模板。

⛔ **阻塞**：如果用户尚未明确表示是否使用模板，必须呈现选项并**等待用户明确回复**后再继续。如果用户之前已声明"不使用模板"或指定了特定模板，跳过此提示直接继续。

**⚡ 提前退出**：如果用户在对话中任何时候已声明"不使用模板"/"不用模板"/"自由设计"（或同等含义），**不要查询 `layouts_index.json`**——直接跳到步骤4。这可避免不必要的token消耗。

**模板推荐流程**（仅在用户尚未决定时）：
查询 `${SKILL_DIR}/templates/layouts/layouts_index.json` 列出可用模板及其风格描述。
**呈现选项时，必须根据当前PPT主题和内容提供专业推荐**（推荐特定模板或自由设计，并说明理由），然后询问用户：

> 💡 **AI推荐**：根据您的内容主题（简要概述），我推荐**[具体模板/自由设计]**，因为...
>
> 您更倾向于哪种方式？
> **A) 使用现有模板**（请指定模板名称或风格偏好）
> **B) 不使用模板** — 自由设计

用户确认选项A后，将模板文件复制到项目目录：
```bash
cp ${SKILL_DIR}/templates/layouts/<template_name>/*.svg <project_path>/templates/
cp ${SKILL_DIR}/templates/layouts/<template_name>/design_spec.md <project_path>/templates/
cp ${SKILL_DIR}/templates/layouts/<template_name>/*.png <project_path>/images/ 2>/dev/null || true
cp ${SKILL_DIR}/templates/layouts/<template_name>/*.jpg <project_path>/images/ 2>/dev/null || true
```

用户确认选项B后，直接继续步骤4。

> 如需创建新的全局模板，请阅读 `workflows/create-template.md`

**✅ 检查点 — 用户已回复模板选择，模板文件已复制（如选择A）。继续步骤4。**

---

### 步骤4：策略师阶段（强制执行——不可跳过）

🚧 **门槛**：步骤3完成；用户已确认模板选择。

> ⚠️ **全自动模式跳过**：如果用户在步骤0选择了模式A（全自动），跳过此步骤，直接使用预设配置进入执行器阶段。预设配置：
> - 画布格式：PPT 16:9
> - 页面数量：7页左右
> - 设计风格：通用演示风格
> - 配色方案：科技蓝商务（主色`#1565C0`，强调色`#00D4FF`）
> - 字体：微软雅黑 + Arial
> - 图标：内置图标库
> - 图片：AI生成或SVG渐变替代

首先，读取角色定义：
```
读取 references/strategist.md
读取 references/shared-standards.md
```

**必须完成八项确认**（参考 `templates/design_spec_reference.md` 获取模板结构）：

> ⚠️ **全自动模式使用预设**：如果用户在步骤0选择了模式A（全自动），直接使用以下预设方案，无需用户确认八项：
> | 项目 | 预设方案 |
> |------|---------|
> | 画布格式 | PPT 16:9 (`0 0 1280 720`) |
> | 页面数量 | 7页（封面+目录+3内容页+致谢） |
> | 目标受众 | 科技爱好者、企业决策者 |
> | 风格目标 | A) 通用演示（视觉冲击优先） |
> | 配色方案 | 科技蓝商务（主色`#1565C0`，强调色`#00D4FF`） |
> | 图标使用 | C) 内置图标库 |
> | 字体方案 | P1 现代商务/科技（微软雅黑+Arial） |
> | 图片使用 | C) AI生成（如配置）或SVG渐变替代 |

⛔ **阻塞**：八项确认必须作为一整套建议呈现给用户，**必须等待用户确认或修改**后才能输出设计规范和内容大纲。这是工作流程中仅有的两个核心确认点之一（另一个是模板选择）。一旦确认，所有后续脚本执行和幻灯片生成应完全自动进行。

1. 画布格式
2. 页面数量范围
3. 目标受众
4. 风格目标
5. 配色方案
6. 图标使用方式
7. 字体排版方案
8. 图片使用方式

如果用户提供了图片，在**输出设计规范之前**运行分析脚本（不要直接读取/打开图片文件——仅使用脚本输出）：
```bash
python3 ${SKILL_DIR}/scripts/analyze_images.py <project_path>/images
```

> ⚠️ **图片处理规则**：AI 不得直接读取、打开或查看图片文件（`.jpg`、`.png` 等）。所有图片信息必须来自 `analyze_images.py` 脚本输出或设计规范中的图片资源列表。

**输出**：`<project_path>/design_spec.md`

**✅ 检查点 — 阶段交付物完成，自动继续下一步**：
```markdown
## ✅ 策略师阶段完成
- [x] 八项确认完成（用户已确认）
- [x] 设计规范和内容大纲已生成
- [ ] **下一步**：自动继续 [图片生成器/执行器] 阶段
```

---

### 步骤5：图片生成器阶段（条件执行）

🚧 **门槛**：步骤4完成；设计规范和内容大纲已生成并经用户确认。

> **触发条件**：图片方式包含"AI生成"。如未触发，直接跳到步骤6（仍需满足步骤6的门槛）。

读取 `references/image-generator.md`

1. 从设计规范中提取所有状态为"待生成"的图片
2. 生成提示文档 → `<project_path>/images/image_prompts.md`
3. 生成图片（推荐使用CLI工具）：
   ```bash
   python3 ${SKILL_DIR}/scripts/image_gen.py "prompt" --aspect_ratio 16:9 --image_size 1K -o <project_path>/images
   ```

**✅ 检查点 — 确认所有图片已就绪，继续步骤6**：
```markdown
## ✅ 图片生成器阶段完成
- [x] 提示文档已创建
- [x] 所有图片已保存到 images/
```

---

### 步骤6：执行器阶段

🚧 **门槛**：步骤4（及步骤5，如触发）完成；所有前置交付物已就绪。

根据选择的风格读取角色定义：
```
读取 references/executor-base.md          # 必需：通用指南
读取 references/executor-general.md       # 通用灵活风格
读取 references/executor-consultant.md    # 咨询风格
读取 references/executor-consultant-top.md # 顶级咨询风格（MBB级别）
```

> 只需读取 executor-base + 一种风格文件。

**设计参数确认（强制）**：在生成第一个SVG之前，执行器必须审查并输出设计规范中的关键设计参数（画布尺寸、配色方案、字体计划、正文字号）以确保符合规范。具体见 executor-base.md 第2节。

**视觉构建阶段**：
- 批量生成SVG页面 → `<project_path>/svg_output/`

> ⚠️ **SVG编码保护规则（强制）**：
> - **必须使用Python脚本写入SVG文件**，禁止直接使用Write工具写入包含中文字符的SVG
> - Python写入必须使用：`file.write_bytes(svg_content.encode('utf-8'))`
> - 写入后必须验证：`content.encode('utf-8')` 不抛出异常
> - 如果发现编码异常，立即重新生成文件
> - SVG文件必须包含XML声明：`<?xml version="1.0" encoding="UTF-8"?>`

**逻辑构建阶段**：
- 生成演讲备注 → `<project_path>/notes/total.md`

**✅ 检查点 — 确认所有SVG和备注已完全生成。直接继续步骤7后处理**：
```markdown
## ✅ 执行器阶段完成
- [x] 所有SVG已生成到 svg_output/
- [x] 演讲备注已生成到 notes/total.md
```

---

### 步骤7：后处理与导出

🚧 **门槛**：步骤6完成；所有SVG已生成到 `svg_output/`；演讲备注 `notes/total.md` 已生成。

> ⚠️ 以下三个子步骤必须**逐个单独执行**。每个命令必须完成并确认成功后再运行下一个。
> ❌ **禁止**将三个命令放在单个代码块或单次shell调用中。

**步骤7.1** — 拆分演讲备注：
```bash
python3 ${SKILL_DIR}/scripts/total_md_split.py <project_path>
```

**步骤7.2** — SVG后处理（图标嵌入/图片裁剪与嵌入/文本扁平化/圆角矩形转路径）：
```bash
python3 ${SKILL_DIR}/scripts/finalize_svg.py <project_path>
```

**步骤7.3** — 导出PPTX（默认嵌入演讲备注）：
```bash
python3 ${SKILL_DIR}/scripts/svg_to_pptx.py <project_path> -s final
# 默认：生成两个文件 — 原生形状(.pptx) + SVG参考(_svg.pptx)
# 使用 --only native 跳过SVG参考版本
# 使用 --only legacy 仅生成SVG图片版本
```

> ⚠️ **PPTX导出后验证**：
> - 检查导出是否成功（查看输出文件大小 > 0）
> - 如果发现SVG解析错误或PPTX异常，检查svg_final目录中的SVG文件编码
> - 如有编码问题，使用Python脚本重新生成SVG文件后再导出

> ❌ **禁止**使用 `cp` 替代 `finalize_svg.py`——它执行多个关键处理步骤
> ❌ **禁止**直接从 `svg_output/` 导出——必须使用 `-s final` 从 `svg_final/` 导出
> ❌ **禁止**添加额外标志如 `--only`

---

## 角色切换协议

切换角色前，**必须首先读取**相应的参考文件——禁止跳过。输出标记：

```markdown
## [角色切换：<角色名称>]
📖 读取角色定义：references/<filename>.md
📋 当前任务：<简要描述>
```

---

## 参考资源

| 资源 | 路径 |
|------|------|
| 共享技术约束 | `references/shared-standards.md` |
| 画布格式规范 | `references/canvas-formats.md` |
| 图片布局规范 | `references/image-layout-spec.md` |
| SVG图片嵌入 | `references/svg-image-embedding.md` |

---

## 注意事项

- 后处理命令不要添加额外标志如 `--only`——原样运行
- 本地预览：`python3 -m http.server -d <project_path>/svg_final 8000`
