# 图片工具

图片工具涵盖基于提示的生成、图片检查和Gemini水印去除。

## `image_gen.py`

统一图片生成入口。

```bash
python3 scripts/image_gen.py "A modern futuristic workspace"
python3 scripts/image_gen.py "Abstract tech background" --aspect_ratio 16:9 --image_size 4K
python3 scripts/image_gen.py "Concept car" -o projects/demo/images
python3 scripts/image_gen.py "Beautiful landscape" -n "low quality, blurry, watermark"
python3 scripts/image_gen.py --list-backends
```

支持层级：
- 核心：`gemini`、`openai`、`qwen`、`zhipu`、`volcengine`
- 扩展：`stability`、`bfl`、`ideogram`
- 实验：`siliconflow`、`fal`、`replicate`

后端选择：

```bash
python3 scripts/image_gen.py "A cat" --backend openai
python3 scripts/image_gen.py "A product launch hero image" --backend qwen
python3 scripts/image_gen.py "科技感背景图" --backend zhipu
python3 scripts/image_gen.py "A product KV in cinematic style" --backend volcengine
```

配置来源：

1. 当前进程环境变量
2. 仓库根目录 `.env` 作为备选

必须始终通过 `IMAGE_BACKEND` 明确选择活动后端。

示例 `.env`：

```env
IMAGE_BACKEND=gemini
GEMINI_API_KEY=your-api-key
GEMINI_BASE_URL=https://your-proxy-url.com/v1beta
GEMINI_MODEL=gemini-3.1-flash-image-preview
```

示例进程环境：

```bash
export IMAGE_BACKEND=gemini
export GEMINI_API_KEY=your-api-key
export GEMINI_MODEL=gemini-3.1-flash-image-preview
```

当前进程环境优先于 `.env`。

仅使用提供商特定的密钥，如 `GEMINI_API_KEY`、`OPENAI_API_KEY`、`QWEN_API_KEY`、`ZHIPU_API_KEY`、`VOLCENGINE_API_KEY`、`FAL_KEY` 或 `REPLICATE_API_TOKEN`。

`IMAGE_API_KEY`、`IMAGE_MODEL` 和 `IMAGE_BASE_URL` 故意不支持。

建议：
- 日常PPT工作默认使用核心层级
- 仅当需要特定模型风格时使用扩展层级
- 将实验层级视为选择性加入

## `analyze_images.py`

在编写设计规范或组合幻灯片布局前分析项目目录中的图片。

```bash
python3 scripts/analyze_images.py <project_path>/images
```

遵循项目工作流时使用此工具而非直接打开图片文件。

## `gemini_watermark_remover.py`

手动下载后去除Gemini水印资产。

```bash
python3 scripts/gemini_watermark_remover.py <image_path>
python3 scripts/gemini_watermark_remover.py <image_path> -o output_path.png
python3 scripts/gemini_watermark_remover.py <image_path> -q
```

注意事项：
- 需要 `scripts/assets/bg_48.png` 和 `scripts/assets/bg_96.png`
- 最佳用于下载"全尺寸"Gemini图片后

依赖：

```bash
pip install Pillow numpy
```
