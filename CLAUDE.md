# CLAUDE.md

本文件为 Claude Code 提供项目概览。执行PPT生成任务之前，**你必须先阅读 `skills/ppt-master/SKILL.md`** 获取完整工作流程和规则。

## 项目概述

PPT Master 是一个AI驱动的演示文稿生成系统。通过多角色协作（策略师 → 图片生成器 → 执行器），将源文档（PDF/DOCX/URL/Markdown）转换为具有真实PowerPoint形状（DrawingML）的原生可编辑PPTX。

**核心流程**：`源文档 → 创建项目 → 选择模板 → 策略师八项确认 → [图片生成器] → 执行器 → 后处理 → 导出PPTX`

## 常用命令

```bash
# 源文档内容转换
python3 skills/ppt-master/scripts/pdf_to_md.py <PDF文件>
python3 skills/ppt-master/scripts/doc_to_md.py <DOCX或_other文件>   # 需要：pandoc (DOCX/EPUB/HTML/LaTeX/RST等)
python3 skills/ppt-master/scripts/web_to_md.py <URL>
node skills/ppt-master/scripts/web_to_md.cjs <URL>

# 项目管理
python3 skills/ppt-master/scripts/project_manager.py init <项目名称> --format ppt169
python3 skills/ppt-master/scripts/project_manager.py import-sources <项目路径> <源文件或URL...> --move
python3 skills/ppt-master/scripts/project_manager.py validate <项目路径>

# 图片工具
python3 skills/ppt-master/scripts/analyze_images.py <项目路径>/images
python3 skills/ppt-master/scripts/image_gen.py "提示词" --aspect_ratio 16:9 --image_size 1K -o <项目路径>/images

# SVG质量检查
python3 skills/ppt-master/scripts/svg_quality_checker.py <项目路径>

# 后处理流水线（必须按顺序执行，一次一个——禁止批量）
python3 skills/ppt-master/scripts/total_md_split.py <项目路径>
# ✅ 确认无错误后再执行下一条命令
python3 skills/ppt-master/scripts/finalize_svg.py <项目路径>
# ✅ 确认无错误后再执行下一条命令
python3 skills/ppt-master/scripts/svg_to_pptx.py <项目路径> -s final
# 默认：生成两个文件——原生形状(.pptx) + SVG参考(_svg.pptx)
# 使用 --only native 跳过SVG参考版本
# 使用 --only legacy 仅生成SVG图片版本
```

## 架构

- `skills/ppt-master/references/` — AI角色定义和技术规范
- `skills/ppt-master/scripts/` — 可运行工具脚本
- `skills/ppt-master/scripts/docs/` — 主题聚焦的脚本文档
- `skills/ppt-master/templates/` — 布局模板、图表模板、640+矢量图标
- `examples/` — 示例项目
- `projects/` — 用户项目工作空间

## SVG技术约束（不可协商）

**禁止功能**：`clipPath` | `mask` | `<style>` | `class` | 外部CSS | `<foreignObject>` | `textPath` | `@font-face` | `<animate*>` | `<script>` | `marker-end` | `<iframe>` | `<symbol>+<use>`（`<defs>` 内的 `id` 是合法引用，**不被禁止**）

**PPT兼容性替代方案**：

| 禁止 | 替代方案 |
|------|---------|
| `rgba()` | `fill-opacity` / `stroke-opacity` |
| `<g opacity>` | 在每个子元素上单独设置透明度 |
| `<image opacity>` | 用遮罩层叠加 |
| `marker-end` 箭头 | `<polygon>` 三角形 |

## 画布格式快速参考

| 格式 | viewBox |
|------|---------|
| PPT 16:9 | `0 0 1280 720` |
| PPT 4:3 | `0 0 1024 768` |
| 小红书 (RED) | `0 0 1242 1660` |
| 微信朋友圈 | `0 0 1080 1080` |
| 故事 | `0 0 1080 1920` |

## 后处理注意事项

- **禁止**使用 `cp` 替代 `finalize_svg.py`
- **禁止**直接从 `svg_output/` 导出——必须从 `svg_final/` 导出（使用 `-s final`）
- 不要在后处理命令中添加额外参数如 `--only`
- **禁止**将三个后处理步骤放在单个代码块或单个shell调用中执行
