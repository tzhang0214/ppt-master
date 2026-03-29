# SVG流水线工具

这些工具涵盖后处理、SVG验证、演讲备注和PPTX导出。

## 推荐流水线

按顺序运行这些步骤：

```bash
python3 scripts/total_md_split.py <project_path>
python3 scripts/finalize_svg.py <project_path>
python3 scripts/svg_to_pptx.py <project_path> -s final
```

## `finalize_svg.py`

统一后处理入口。这是运行SVG清理的首选方式。

它聚合了：
- `embed_icons.py`
- `crop_images.py`
- `fix_image_aspect.py`
- `embed_images.py`
- `flatten_tspan.py`
- `svg_rect_to_path.py`

典型用法：

```bash
python3 scripts/finalize_svg.py <project_path>
```

仅在需要高级调试或一次性修复时才使用独立子工具。

## `svg_to_pptx.py`

将项目SVG转换为PPTX。

```bash
python3 scripts/svg_to_pptx.py <project_path> -s final
python3 scripts/svg_to_pptx.py <project_path> -s final --only native
python3 scripts/svg_to_pptx.py <project_path> -s final --only legacy
python3 scripts/svg_to_pptx.py <project_path> -s final --no-notes
python3 scripts/svg_to_pptx.py <project_path> -t none
python3 scripts/svg_to_pptx.py <project_path> -s final --auto-advance 3
```

行为：
- 默认输出：原生可编辑PPTX + SVG参考PPTX
- 推荐源目录：`svg_final/`
- 默认自动嵌入演讲备注，除非使用 `--no-notes`

依赖：

```bash
pip install python-pptx
```

## `total_md_split.py`

将 `total.md` 拆分为每页备注文件。

```bash
python3 scripts/total_md_split.py <project_path>
python3 scripts/total_md_split.py <project_path> -o <output_directory>
python3 scripts/total_md_split.py <project_path> -q
```

要求：
- 每个部分以 `# ` 开头
- 标题文字与SVG文件名匹配
- 部分之间用 `---` 分隔

## `svg_quality_checker.py`

验证SVG技术合规性。

```bash
python3 scripts/svg_quality_checker.py examples/project/svg_output/01_cover.svg
python3 scripts/svg_quality_checker.py examples/project/svg_output
python3 scripts/svg_quality_checker.py examples/project
python3 scripts/svg_quality_checker.py examples/project --format ppt169
python3 scripts/svg_quality_checker.py --all examples
python3 scripts/svg_quality_checker.py examples/project --export
```

检查包括：
- `viewBox`
- 禁止元素
- 宽度/高度一致性
- 换行结构

## `svg_position_calculator.py`

分析或预计算图表坐标。

常用命令：

```bash
python3 scripts/svg_position_calculator.py analyze <svg_file>
python3 scripts/svg_position_calculator.py interactive
python3 scripts/svg_position_calculator.py calc bar --data "East:185,South:142"
python3 scripts/svg_position_calculator.py calc pie --data "A:35,B:25,C:20"
python3 scripts/svg_position_calculator.py from-json config.json
```

AI生成前后验证图表几何时使用此工具。

## 高级独立工具

### `flatten_tspan.py`

```bash
python3 scripts/svg_finalize/flatten_tspan.py examples/<project>/svg_output
python3 scripts/svg_finalize/flatten_tspan.py path/to/input.svg path/to/output.svg
```

### `svg_rect_to_path.py`

```bash
python3 scripts/svg_finalize/svg_rect_to_path.py <project_path>
python3 scripts/svg_finalize/svg_rect_to_path.py <project_path> -s final
python3 scripts/svg_finalize/svg_rect_to_path.py path/to/file.svg
```

当圆角必须保留以通过PowerPoint形状转换时使用。

### `fix_image_aspect.py`

```bash
python3 scripts/svg_finalize/fix_image_aspect.py path/to/slide.svg
python3 scripts/svg_finalize/fix_image_aspect.py 01_cover.svg 02_toc.svg
python3 scripts/svg_finalize/fix_image_aspect.py --dry-run path/to/slide.svg
```

当嵌入图片在PowerPoint形状转换后拉伸时使用。

### `embed_icons.py`

```bash
python3 scripts/svg_finalize/embed_icons.py output.svg
python3 scripts/svg_finalize/embed_icons.py svg_output/*.svg
python3 scripts/svg_finalize/embed_icons.py --dry-run svg_output/*.svg
```

在 `finalize_svg.py` 之外手动检查图标嵌入时使用。

## PPT兼容性规则

使用PowerPoint安全的透明度语法：

| 避免 | 使用 |
|------|------|
| `fill=\"rgba(...)\"` | `fill=\"#hex\"` + `fill-opacity` |
| `<g opacity=\"...\">` | 在每个子元素上设置透明度 |
| `<image opacity=\"...\">` | 用遮罩层叠加 |

PowerPoint还有以下问题：
- 基于marker的箭头
- 不支持的滤镜
- 未映射到DrawingML的直接SVG特性
