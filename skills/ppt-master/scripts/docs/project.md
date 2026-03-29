# 项目工具

项目工具创建、验证和检查标准PPT Master工作空间。

## `project_manager.py`

项目设置和验证的主要入口。

```bash
python3 scripts/project_manager.py init <project_name> --format ppt169
python3 scripts/project_manager.py import-sources <project_path> <source1> [<source2> ...]
python3 scripts/project_manager.py validate <project_path>
python3 scripts/project_manager.py info <project_path>
```

注意事项：
- 工作区外的文件默认复制到 `sources/`
- 使用 `--move` 时，工作区外的文件移动到 `sources/`
- 工作区内的文件直接移动

常用格式：
- `ppt169`
- `ppt43`
- `xiaohongshu`
- `moments`
- `story`
- `banner`
- `a4`

示例：

```bash
python3 scripts/project_manager.py init my_presentation --format ppt169
python3 scripts/project_manager.py validate projects/my_presentation_ppt169_20251116
python3 scripts/project_manager.py info projects/my_presentation_ppt169_20251116
```

## `project_utils.py`

其他脚本使用的共享辅助模块。

常用方式：

```python
from project_utils import get_project_info, validate_project_structure
```

也可以直接运行进行快速检查：

```bash
python3 scripts/project_utils.py <project_path>
```

## `batch_validate.py`

批量检查项目结构和合规性。

```bash
python3 scripts/batch_validate.py examples
python3 scripts/batch_validate.py examples projects
python3 scripts/batch_validate.py --all
python3 scripts/batch_validate.py examples --export
```

发布前或清理前使用此工具进行仓库级健康检查。

## `generate_examples_index.py`

自动重建 `examples/README.md`。

```bash
python3 scripts/generate_examples_index.py
python3 scripts/generate_examples_index.py examples
```

## `error_helper.py`

显示常见项目错误的标准修复。

```bash
python3 scripts/error_helper.py
python3 scripts/error_helper.py missing_readme
python3 scripts/error_helper.py missing_readme project_path=my_project
```
