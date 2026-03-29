# 转换工具

源文档转换工具将PDF、文档和网页转换为Markdown格式，然后才能创建项目。

## `pdf_to_md.py`

原生PDF的首选工具。

```bash
python3 scripts/pdf_to_md.py book.pdf
python3 scripts/pdf_to_md.py book.pdf -o output.md
python3 scripts/pdf_to_md.py ./pdfs
python3 scripts/pdf_to_md.py ./pdfs -o ./markdown
```

适用场景：
- 从Word、PowerPoint、LaTeX或类似工具导出的原生PDF
- 隐私敏感文档，应保留在本地
- 在回退到OCR密集工具之前的快速首轮提取

以下情况优先使用MinerU或其他OCR/布局工具：
- PDF是扫描件或图片-based
- 多栏布局解析差
- 编码乱码

依赖：

```bash
pip install PyMuPDF
```

## `doc_to_md.py`

基于Pandoc的转换器，适用于办公和标记格式。

支持的格式包括：
- `.docx`、`.doc`、`.odt`、`.rtf`
- `.epub`、`.html`、`.tex`、`.rst`、`.org`、`.ipynb`、`.typ`

```bash
python3 scripts/doc_to_md.py lecture.docx
python3 scripts/doc_to_md.py lecture.docx -o output.md
python3 scripts/doc_to_md.py notes.epub
python3 scripts/doc_to_md.py paper.tex -o paper.md
```

依赖：

```bash
# macOS
brew install pandoc

# Ubuntu
sudo apt install pandoc
```

## `web_to_md.py` / `web_to_md.cjs`

将网页转换为Markdown并本地下载图片。

Python版本：

```bash
python3 scripts/web_to_md.py https://example.com/article
python3 scripts/web_to_md.py https://url1.com https://url2.com
python3 scripts/web_to_md.py -f urls.txt
python3 scripts/web_to_md.py https://example.com -o output.md
```

Node.js版本适用于微信或反爬虫页面：

```bash
node scripts/web_to_md.cjs https://mp.weixin.qq.com/s/xxxx
node scripts/web_to_md.cjs https://url1.com https://url2.com
```

微信公众平台和类似高安全性站点优先使用Node.js版本。

## `rotate_images.py`

修复下载或导入资产中的图片EXIF方向。

```bash
python3 scripts/rotate_images.py auto projects/xxx_files
python3 scripts/rotate_images.py gen projects/xxx_files
python3 scripts/rotate_images.py fix fixes.json
```

当转换或导入后提取的照片显示为侧向时使用此工具。
