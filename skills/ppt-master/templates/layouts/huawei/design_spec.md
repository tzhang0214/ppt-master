# Huawei Warm Template (华为暖色PPT模板) - Design Specification

> 适用于温暖风格的企业汇报、产品介绍、解决方案演示等场景。风格：温暖活力、简洁大气、科技感。

---

## I. Template Overview

| Property         | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| **Template Name**| Huawei Warm (华为暖色 / huawei)                                 |
| **Use Cases**    | Corporate reports, product introductions, solution presentations, annual meetings, training materials |
| **Design Tone**  | Warm, energetic, clean, professional, tech-forward             |
| **Theme Mode**   | Light theme (white background + warm coral/red accents)          |

---

## II. Canvas Specification

| Property           | Value                         |
| ------------------ | ----------------------------- |
| **Format**         | Standard 16:9                 |
| **Dimensions**     | 1280 × 720 px                |
| **viewBox**        | `0 0 1280 720`               |
| **Safe Margins**   | 60px (left/right), 50px (top/bottom) |
| **Content Area**   | x: 60-1220, y: 140-640       |
| **Title Area**     | y: 40-100                    |
| **Grid Baseline**  | 40px                         |

---

## III. Color Scheme

### Primary Colors (主色 - 所有页面主标题使用)

| Role               | Value       | Notes                                    |
| ------------------ | ----------- | ---------------------------------------- |
| **Deep Red**       | `#B71C1C`   | Primary headings, main titles (MANDATORY) |
| **Burnt Orange**   | `#C04000`   | Secondary accents, CTAs                  |
| **Chocolate**      | `#D2691E`   | Tertiary accents, highlights             |
| **Sienna**         | `#A0522D`   | Additional warm accent                   |
| **Saddle Brown**   | `#8B4513`   | Decorative elements                     |
| **Coral**          | `#FF7F50`   | Bright accent, highlights                |
| **Gold**           | `#FFDB58`   | Emphasis, decorative lines               |
| **Copper**         | `#B87333`   | Secondary metallic accent               |
| **Maroon**         | `#800000`   | Dark accent, depth                      |

### Supporting Colors

| Role               | Value       | Notes                                    |
| ------------------ | ----------- | ---------------------------------------- |
| **Primary Orange** | `#FF6B35`   | Warm brand color                        |
| **Secondary Orange`| `#F7931E`   | Secondary warm color                    |
| **Accent Yellow**  | `#FFD23F`   | Decorative accents                       |

### Neutral Colors

| Role               | Value       | Usage                          |
| ------------------ | ----------- | ------------------------------ |
| **Background White**| `#FFFFFF`  | Main page background           |
| **Light Warm BG**  | `#FFF8F5`   | Subtle section backgrounds     |
| **Card Background**| `#FFF5F0`   | Content card backgrounds       |
| **Border Warm**    | `#FFE5DC`   | Dividers, borders              |
| **Body Text**      | `#333333`   | Standard body text              |
| **Subtitle**       | `#666666`   | Subtitles, secondary text       |
| **Caption Gray**   | `#999999`   | Annotations, timestamps         |
| **Dark Gray**      | `#2D2D2D`   | Alternative headings            |

---

## IV. Typography System

### Font Stack

**Font Stack**: `"Microsoft YaHei", "PingFang SC", "Helvetica Neue", Arial, sans-serif`

### Font Size Hierarchy

| Level    | Usage              | Size    | Weight  | Color    |
| -------- | ------------------ | ------- | ------- | -------- |
| H1       | Cover main title   | 52-64px | Bold    | #B71C1C |
| H2       | Page title         | 32-40px | Bold    | #B71C1C |
| H3       | Section/card title | 22-28px | Bold    | #B71C1C |
| P        | Body content       | 16-22px | Regular | #333333 |
| Caption  | Supplementary text | 14-16px | Regular | #666666 |

> **IMPORTANT**: All primary headings and titles MUST use color `#B71C1C` for brand consistency.

---

## V. Core Design Principles

### Huawei Warm Style

1. **Deep Red Titles**: Primary headings use `#B71C1C` for strong brand identity
2. **Warm Gradients**: Subtle gradients from `#B71C1C` to `#C04000` for backgrounds
3. **Color Blocking**: Strategic use of warm accent blocks as visual anchors
4. **Geometric Patterns**: Subtle geometric shapes (circles, rectangles) in warm tones
5. **Generous Whitespace**: Ample white space creates breathing room and clarity

### Advanced Styling Features

1. **Gradient Application**: Deep red to burnt orange gradients for cover/chapter backgrounds
2. **Icon Integration**: Clean, geometric icons aligned with warm aesthetic
3. **Card Layouts**: Rounded corner cards (`rx="8"`) with warm-toned accents
4. **Data Visualization**: Clean chart styles with warm brand colors

---

## VI. Page Structure

### General Layout

| Area         | Position/Height | Description                            |
| ------------ | --------------- | -------------------------------------- |
| **Top**      | y=0-120         | Title area, logo placement             |
| **Content**  | y=140-640       | Main content area                      |
| **Footer**   | y=680-720       | Page number, copyright, Huawei logo    |

### Decorative Design

- **Deep Red Accent Bar**: `#B71C1C` horizontal bar at the top or as a title prefix
- **Geometric Icons**: Small geometric shapes as section indicators
- **Huawei Logo**: Located in bottom right corner of all pages except cover
- **Subtle Lines**: Light warm-colored dividers for content organization

---

## VII. Page Types

### 1. Cover Page (01_cover.svg)

- **Layout**: Left-aligned content with right-side geometric decoration
- **Background**: Clean white or subtle gradient (white to light warm)
- **Title**: Left-aligned, large deep red (`#B71C1C`) text with gradient accent underline
- **Decoration**: Geometric circles/patterns on the right side in warm colors
- **Logo**: Top-right corner placement
- **NO Huawei logo in bottom right** (logo only appears on non-cover pages)

### 2. Table of Contents (02_toc.svg)

- **Layout**: Clean numbered list with deep red accents
- **Left Side**: "CONTENTS" title in bold with gold accent line
- **Right Side**: Numbered entries with deep red numbers and titles
- **Decoration**: Minimalist warm-colored line dividers
- **Huawei Logo**: Bottom right corner

### 3. Chapter Page (02_chapter.svg)

- **Background**: Deep red gradient (`#B71C1C` -> `#C04000`)
- **Center**: Large chapter number + bold white title
- **Decoration**: Subtle geometric patterns, gold accent lines
- **Style**: Professional, commanding presence with warmth
- **Huawei Logo**: Bottom right corner (white color)

### 4. Content Page (03_content.svg)

- **Top**: Minimalist title bar with deep red rectangle accent in the upper-left
- **Page Title**: Always uses `#B71C1C` color
- **Background**: Pure white
- **Content**: Flexible layout with optional card containers (warm accent colors)
- **Footer**: Small gray text for page number and company name
- **Huawei Logo**: Bottom right corner

### 5. Ending Page (04_ending.svg)

- **Background**: Deep red gradient echoing warm professional theme
- **Center**: "Thank You" message with contact information
- **Decoration**: Gold accents, geometric patterns
- **Style**: Elegant closure matching cover page sophistication
- **Huawei Logo**: Bottom right corner (white color)

---

## VIII. Common Components

### Title Prefix Decoration

```xml
<!-- Deep red rectangle decoration -->
<rect x="40" y="40" width="8" height="36" fill="#B71C1C" />
```

### Card Container

```xml
<!-- Rounded content card with warm accent -->
<rect x="60" y="140" width="500" height="200" fill="#FFF5F0" rx="8" />
<rect x="60" y="140" width="8" height="200" fill="#B71C1C" rx="4" />
```

### Bottom Accent Line

```xml
<!-- Deep red accent underline -->
<rect x="60" y="95" width="120" height="3" fill="#B71C1C" />
```

### Huawei Logo (Bottom Right)

```xml
<!-- Huawei logo for light backgrounds -->
<g transform="translate(1180, 660) scale(1.5)">
  <path d="..." fill="#C04000"/>
</g>

<!-- Huawei logo for dark backgrounds (chapter/ending) -->
<g transform="translate(1180, 660) scale(1.5)">
  <path d="..." fill="#FFFFFF"/>
</g>
```

---

## IX. SVG Technical Constraints

### Mandatory Rules

1. viewBox: `0 0 1280 720`
2. Use `<rect>` elements for backgrounds
3. Use `<tspan>` for text wrapping (**`<foreignObject>` is strictly prohibited**)
4. Use `fill-opacity` / `stroke-opacity` for transparency
5. Prohibited: `clipPath`, `mask`, `<style>`, `class`, `foreignObject`
6. Prohibited: `textPath`, `animate*`, `script`
7. Define gradients in `<defs>`

---

## X. Placeholder Specification

| Placeholder                   | Description                |
| ----------------------------- | -------------------------- |
| `{{TITLE}}`                   | Main title (use #B71C1C)  |
| `{{SUBTITLE}}`                | Subtitle                   |
| `{{AUTHOR}}`                  | Speaker/Author             |
| `{{DATE}}`                    | Date                       |
| `{{PAGE_TITLE}}`              | Page title (use #B71C1C)  |
| `{{CONTENT_AREA}}`            | Content area prompt text   |
| `{{CHAPTER_NUM}}`            | Chapter number (01)        |
| `{{CHAPTER_TITLE}}`          | Chapter title              |
| `{{CHAPTER_DESC}}`           | Chapter description        |
| `{{PAGE_NUM}}`               | Page number                |
| `{{TOC_ITEM_1_TITLE}}`        | TOC item 1 title           |
| `{{TOC_ITEM_1_DESC}}`         | TOC item 1 description     |
| `{{TOC_ITEM_2_TITLE}}`        | TOC item 2 title           |
| `{{TOC_ITEM_2_DESC}}`         | TOC item 2 description     |
| `{{TOC_ITEM_3_TITLE}}`        | TOC item 3 title           |
| `{{TOC_ITEM_3_DESC}}`         | TOC item 3 description     |
| `{{TOC_ITEM_4_TITLE}}`        | TOC item 4 title           |
| `{{TOC_ITEM_4_DESC}}`         | TOC item 4 description     |
| `{{THANK_YOU}}`              | Thank-you message          |
| `{{ENDING_SUBTITLE}}`         | Ending subtitle            |
| `{{CLOSING_MESSAGE}}`         | Closing message            |
| `{{CONTACT_INFO}}`           | Contact information        |
| `{{SECTION_NAME}}`           | Section name (header)      |
| `{{SOURCE}}`                 | Source attribution          |
| `{{LOGO}}`                   | Logo text                  |

---

## XI. Usage Notes

1. This template follows Huawei warm brand guidelines with deep red headings
2. **ALL page titles MUST use `#B71C1C`** for primary headings
3. Content pages maintain maximum flexibility for various content types
4. Deep red accents should be used for titles; other warm colors for decorations
5. Huawei logo appears in bottom right corner of all pages except the cover page
6. Geometric decorations use warm palette colors for visual interest
