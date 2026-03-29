---
description: 基于现有项目文件或参考模板生成新的 PPT 布局模板
---

# 创建新模板工作流

> **调用角色**: [模板设计师](../references/template-designer.md)

为**全局模板库**生成一套完整的可复用 PPT 布局模板。

> 此工作流用于**库资源创建**，而非项目级一次性定制。输出必须可被未来的 PPT 项目复用，并能从 `templates/layouts/layouts_index.json` 中被发现。

## 流程概览

```
收集需求 -> 创建目录 -> 调用模板设计师 -> 验证资源 -> 注册索引 -> 输出确认
```

---

## 步骤1：收集模板信息

与用户确认以下内容：

| 项目 | 必填 | 描述 |
|------|------|------|
| 新模板 ID | 是 | 模板目录名 / 索引键。建议使用 ASCII 格式如 `my_company`；如使用中文品牌名，必须文件系统安全且与 `layouts_index.json` 完全匹配 |
| 模板显示名称 | 是 | 用于文档的人类可读名称 |
| 分类 | 是 | 属于以下之一：`brand` / `general` / `scenario` / `government` / `special` |
| 适用场景 | 是 | 典型用例，如年度报告 / 答辩 / 政府简报 |
| 风格概述 | 是 | 简短风格描述用于推荐，如 `现代、克制、数据驱动` |
| 主题模式 | 是 | 用于推荐的风格描述，如 `浅色主题（白色背景 + 蓝色强调）` |
| 画布格式 | 是 | 默认 `ppt169`；如需其他格式需在生成前明确指定 |
| 参考来源 | 可选 | 现有项目或模板路径 |
| 主题色 | 可选 | 主色 HEX 值（可从参考中自动提取） |
| 设计风格 | 可选 | 额外的风格说明、装饰语言、品牌特征 |
| 资源列表 | 可选 | 模板包中包含的 Logo / 背景纹理 / 参考图片 |
| 快速查找标签 | 可选 | 用于 `layouts_index.json > quickLookup` 的标签，如 `technology`、`finance`、`academic` |

**步骤1的预期产出**：

- 模板被明确定位为**全局库模板**
- 画布格式在 SVG 生成前已固定
- 模板元数据完整到可以注册到 `layouts_index.json`

**如果提供了参考来源**，首先分析其结构：

```bash
ls -la "<参考来源路径>"
```

---

## 步骤2：创建模板目录

```bash
mkdir -p "skills/ppt-master/templates/layouts/<模板ID>"
```

> **输出位置**：全局模板到 `skills/ppt-master/templates/layouts/`；项目模板到 `projects/<项目>/templates/`
>
> 生成的目录名必须与 `layouts_index.json` 中使用的最终模板 ID 一致。

---

## 步骤3：调用模板设计师角色

**切换到 Template_Designer 角色**并按角色定义生成。角色输入的是步骤1中定稿的模板需求，而非项目设计规范。

1. **design_spec.md** — 设计规范文档
2. **4 个核心模板** — 封面、章节、内容、结束页
3. **目录页（可选）** — `02_toc.svg`
4. **模板资源（可选）** — 模板包所需的 Logo / PNG / JPG / 参考 SVG

> **角色详情**：参见 [template-designer.md](../references/template-designer.md)

**新模板占位符约定（新建库模板的强制要求）**：

- 封面：`{{TITLE}}`、`{{SUBTITLE}}`、`{{DATE}}`、`{{AUTHOR}}`
- 章节页：`{{CHAPTER_NUM}}`、`{{CHAPTER_TITLE}}`
- 内容页：`{{PAGE_TITLE}}`、`{{CONTENT_AREA}}`、`{{PAGE_NUM}}`
- 结束页：`{{THANK_YOU}}`、`{{CONTACT_INFO}}`
- 目录页：使用索引式占位符如 `{{TOC_ITEM_1_TITLE}}` 和可选的 `{{TOC_ITEM_1_DESC}}`

**避免**为新模板引入一次性占位符系列如 `{{CHAPTER_01_TITLE}}`。如果确实需要扩展占位符，请在 `design_spec.md` 中明确定义并保持命名模式一致。

---

## 步骤4：验证模板资源

```bash
ls -la "skills/ppt-master/templates/layouts/<模板ID>"
```

对模板目录运行 SVG 验证：

```bash
python3 skills/ppt-master/scripts/svg_quality_checker.py "skills/ppt-master/templates/layouts/<模板ID>" --format <画布格式>
```

**检查清单**：

- [ ] SVG可以正常显示，没有语法错误
- [ ] `design_spec.md` 包含完整的设计规范
- [ ] 4 个核心模板全部存在
- [ ] 如存在目录页，占位符模式使用规范的索引形式
- [ ] SVG viewBox 与所选画布格式匹配（`ppt169` 为 `0 0 1280 720`）
- [ ] 占位符名称与新模板约定和 `design_spec.md` 一致
- [ ] SVG 引用的资源文件实际存在于模板包中

此步骤是**硬性门槛**。验证通过前不要将模板注册到库索引。

---

## 步骤5：在库索引中注册模板

更新 `skills/ppt-master/templates/layouts/layouts_index.json`：

- `meta.total`
- `meta.updated`
- 正确的 `categories.<分类>.layouts` 条目
- 适当的 `quickLookup` 条目
- 新的 `layouts.<模板ID>` 元数据块

`layouts_index.json` 是模板发现的事实来源，主 PPT 生成工作流依赖于此。一个未在此注册的模板目录被认为是未完成的。

如果存在手动维护的人类可读的 `templates/layouts/README.md` 摘要表，请在更新 JSON 索引后同步。JSON 索引优先。

---

## 步骤6：输出确认

```markdown
## 模板创建完成

**模板名称**: <模板ID> (<显示名称>)
**模板路径**: `skills/ppt-master/templates/layouts/<模板ID>/`
**分类**: <分类>
**画布格式**: <画布格式>
**索引注册**: 已完成

### 包含文件

| 文件 | 状态 |
|------|------|
| `design_spec.md` | 已完成 |
| `01_cover.svg` | 已完成 |
| `02_chapter.svg` | 已完成 |
| `03_content.svg` | 已完成 |
| `04_ending.svg` | 已完成 |
| `02_toc.svg` | 可选 |
```

---

## 配色方案快速参考

| 风格 | 主色 | 用例 |
|------|------|------|
| 科技蓝 | `#004098` | 认证、评估 |
| 麦肯锡蓝 | `#005587` | 战略咨询 |
| 政府蓝 | `#003366` | 政府项目 |
| 商务灰 | `#2C3E50` | 通用商务 |

---

## 注意事项

1. **SVG 技术约束**：参见 [template-designer.md](../references/template-designer.md) 中的技术约束部分
2. **色彩一致性**：所有 SVG 文件必须使用相同的配色方案
3. **占位符约定**：使用 `{{}}` 格式和上述规范的新模板占位符约定
4. **发现要求**：新模板必须添加到 `layouts_index.json`，否则主工作流无法推荐

> **详细规范**：参见 [template-designer.md](../references/template-designer.md)
