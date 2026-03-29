# 故障排除

## 验证失败

1. 运行：

```bash
python3 scripts/project_manager.py validate <project_path>
```

2. 修复验证器报告的缺失文件或无效目录。
3. 后处理或导出前重新运行验证。

## SVG预览有问题

1. 检查文件路径和文件名。
2. 确认命名约定一致。
3. 如浏览器文件加载不一致，通过本地服务器预览：

```bash
python3 -m http.server --directory <svg_output_path> 8000
```

## 演讲备注未拆分

检查 `total.md`：
- 标题必须以 `# ` 开头
- 标题文字必须与SVG文件名匹配
- 部分之间必须用 `---` 分隔

然后重新运行：

```bash
python3 scripts/total_md_split.py <project_path>
```

## PPT导出质量问题

首选顺序：

```bash
python3 scripts/total_md_split.py <project_path>
python3 scripts/finalize_svg.py <project_path>
python3 scripts/svg_to_pptx.py <project_path> -s final
```

当 `svg_final/` 存在时不要直接从 `svg_output/` 导出。

## 依赖检查清单

大多数工具使用标准库。仅在需要时安装额外依赖：

```bash
pip install -r requirements.txt
```

重要的可选包：
- `python-pptx` 用于PPTX导出
- `Pillow` 用于图片工具
- `numpy` 用于水印去除
- `PyMuPDF` 用于PDF转换
- `google-genai` / `openai` 用于图片生成后端
