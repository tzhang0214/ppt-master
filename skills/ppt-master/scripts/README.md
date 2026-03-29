# PPT Master 工具集

本目录包含用于转换、项目设置、SVG处理、导出和图片生成的用户级脚本。

## 目录结构

- `scripts/` 顶层：可运行的入口脚本
- `scripts/image_backends/`：内部提供商实现，被 `image_gen.py` 使用
- `scripts/svg_finalize/`：内部后处理辅助工具，被 `finalize_svg.py` 使用
- `scripts/docs/`：主题聚焦的脚本文档
- `scripts/assets/`：脚本消耗的静态资产

## 快速开始

典型端到端工作流：

```bash
python3 scripts/pdf_to_md.py <file.pdf>
python3 scripts/project_manager.py init <project_name> --format ppt169
python3 scripts/project_manager.py import-sources <project_path> <source_files...> --move
python3 scripts/total_md_split.py <project_path>
python3 scripts/finalize_svg.py <project_path>
python3 scripts/svg_to_pptx.py <project_path> -s final
```

## 脚本索引

| 领域 | 主要脚本 | 文档 |
|------|---------|------|
| 转换 | `pdf_to_md.py`、`doc_to_md.py`、`web_to_md.py`、`web_to_md.cjs` | [docs/conversion.md](./docs/conversion.md) |
| 项目管理 | `project_manager.py`、`batch_validate.py`、`generate_examples_index.py`、`error_helper.py` | [docs/project.md](./docs/project.md) |
| SVG流水线 | `finalize_svg.py`、`svg_to_pptx.py`、`total_md_split.py`、`svg_quality_checker.py` | [docs/svg-pipeline.md](./docs/svg-pipeline.md) |
| 图片工具 | `image_gen.py`、`analyze_images.py`、`gemini_watermark_remover.py` | [docs/image.md](./docs/image.md) |
| 故障排除 | 验证、预览、导出、依赖问题 | [docs/troubleshooting.md](./docs/troubleshooting.md) |

## 高频命令

项目设置：

```bash
python3 scripts/project_manager.py init <project_name> --format ppt169
python3 scripts/project_manager.py import-sources <project_path> <source_files...> --move
python3 scripts/project_manager.py validate <project_path>
```

后处理与导出：

```bash
python3 scripts/total_md_split.py <project_path>
python3 scripts/finalize_svg.py <project_path>
python3 scripts/svg_to_pptx.py <project_path> -s final
```

图片生成：

```bash
python3 scripts/image_gen.py "A modern futuristic workspace"
python3 scripts/image_gen.py --list-backends
python3 scripts/analyze_images.py <project_path>/images
```

## 建议

- 新增可运行脚本放在 `scripts/` 顶层
- 将提供商特定或辅助内部工具移入子目录
- 优先使用统一入口 `project_manager.py`、`finalize_svg.py` 和 `image_gen.py`
- 导出时优先使用 `svg_final/` 而非 `svg_output/`

## 相关文档

- [转换工具](./docs/conversion.md)
- [项目工具](./docs/project.md)
- [SVG流水线工具](./docs/svg-pipeline.md)
- [图片工具](./docs/image.md)
- [故障排除](./docs/troubleshooting.md)
- [AGENTS指南](../../../AGENTS.md)

_最后更新: 2026-03-26_
