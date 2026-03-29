# -*- coding: utf-8 -*-
import os

# Define paths
base_path = r"d:\projects\aiprojects\ppt-master\projects"
project_name = "智能眼镜介绍_ppt169_20260329"
svg_dir = os.path.join(base_path, project_name, "svg_output")
notes_dir = os.path.join(base_path, project_name, "notes")

os.makedirs(svg_dir, exist_ok=True)
os.makedirs(notes_dir, exist_ok=True)

# Color scheme
PRIMARY = "#1565C0"
ACCENT = "#00D4FF"
DARK = "#0D47A1"
LIGHT_BG = "#FAFAFA"
TEXT_DARK = "#424242"
GRAY = "#757575"
LIGHT_BLUE = "#B3E5FC"
MID_BLUE = "#90CAF9"

# Page names in English for filenames, Chinese for content
pages = [
    ("01_cover.svg", "01_封面.svg"),
    ("02_toc.svg", "02_目录.svg"),
    ("03_overview.svg", "03_产品概述.svg"),
    ("04_hardware.svg", "04_硬件配置.svg"),
    ("05_features.svg", "05_功能场景.svg"),
    ("06_advantages.svg", "06_优势对比.svg"),
    ("07_feedback.svg", "07_用户体验.svg"),
    ("08_future.svg", "08_未来规划.svg"),
    ("09_ending.svg", "09_结束页.svg"),
]

# SVG templates
svgs = {}

# Page 1: Cover
svgs["01_cover.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D47A1"/>
      <stop offset="100%" stop-color="#1565C0"/>
    </linearGradient>
  </defs>
  <rect width="1280" height="720" fill="url(#bgGrad)"/>
  <circle cx="1100" cy="150" r="300" fill="#00D4FF" opacity="0.1"/>
  <circle cx="200" cy="600" r="200" fill="#00D4FF" opacity="0.08"/>
  <rect x="80" y="280" width="8" height="160" fill="#00D4FF"/>
  <text x="110" y="340" font-family="Microsoft YaHei" font-size="48" font-weight="bold" fill="#FFFFFF">智享视界·境启新生</text>
  <text x="110" y="400" font-family="Microsoft YaHei" font-size="28" fill="#00D4FF">XX智能眼镜新品发布</text>
  <text x="110" y="460" font-family="Microsoft YaHei" font-size="20" fill="#B3E5FC">打破边界，重构智能生活新体验</text>
  <text x="110" y="650" font-family="Microsoft YaHei" font-size="16" fill="#90CAF9">2026年3月</text>
  <rect x="0" y="690" width="1280" height="30" fill="#0D47A1"/>
</svg>'''

# Page 2: Table of Contents
svgs["02_toc.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="#FAFAFA"/>
  <rect x="0" y="0" width="1280" height="100" fill="#1565C0"/>
  <text x="80" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#FFFFFF">目录 CONTENTS</text>
  <rect x="80" y="130" width="60" height="4" fill="#00D4FF"/>
  <text x="80" y="180" font-family="Microsoft YaHei" font-size="18" fill="#1565C0">01</text>
  <text x="140" y="180" font-family="Microsoft YaHei" font-size="18" fill="#424242">产品概述与核心定位</text>
  <text x="80" y="230" font-family="Microsoft YaHei" font-size="18" fill="#1565C0">02</text>
  <text x="140" y="230" font-family="Microsoft YaHei" font-size="18" fill="#424242">核心硬件配置解析</text>
  <text x="80" y="280" font-family="Microsoft YaHei" font-size="18" fill="#1565C0">03</text>
  <text x="140" y="280" font-family="Microsoft YaHei" font-size="18" fill="#424242">核心功能与场景应用</text>
  <text x="80" y="330" font-family="Microsoft YaHei" font-size="18" fill="#1565C0">04</text>
  <text x="140" y="330" font-family="Microsoft YaHei" font-size="18" fill="#424242">与同类产品差异化优势</text>
  <text x="80" y="380" font-family="Microsoft YaHei" font-size="18" fill="#1565C0">05</text>
  <text x="140" y="380" font-family="Microsoft YaHei" font-size="18" fill="#424242">用户体验反馈与案例</text>
  <text x="80" y="430" font-family="Microsoft YaHei" font-size="18" fill="#1565C0">06</text>
  <text x="140" y="430" font-family="Microsoft YaHei" font-size="18" fill="#424242">未来规划与总结</text>
  <rect x="0" y="690" width="1280" height="30" fill="#1565C0"/>
</svg>'''

# Page 3: Product Overview
svgs["03_overview.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="#FAFAFA"/>
  <rect x="0" y="0" width="1280" height="100" fill="#1565C0"/>
  <text x="80" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#FFFFFF">01 产品概述与核心定位</text>
  <rect x="80" y="130" width="60" height="4" fill="#00D4FF"/>
  <rect x="80" y="170" width="500" height="200" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <rect x="80" y="170" width="6" height="200" fill="#00D4FF"/>
  <text x="110" y="210" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#1565C0">产品定位</text>
  <text x="110" y="250" font-family="Microsoft YaHei" font-size="16" fill="#424242">XX智能眼镜是一款融合科技与便捷的穿戴设备</text>
  <text x="110" y="290" font-family="Microsoft YaHei" font-size="18" fill="#1565C0" font-weight="bold">核心关键词</text>
  <text x="110" y="325" font-family="Microsoft YaHei" font-size="14" fill="#757575">轻量便携 · 智能交互 · 多场景适配</text>
  <rect x="620" y="170" width="580" height="200" rx="12" fill="#1565C0"/>
  <text x="660" y="220" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#FFFFFF">目标用户群体</text>
  <circle cx="720" cy="290" r="30" fill="#00D4FF"/>
  <text x="720" y="296" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">职场人士</text>
  <circle cx="900" cy="290" r="30" fill="#00D4FF"/>
  <text x="900" y="296" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">运动爱好者</text>
  <circle cx="1080" cy="290" r="30" fill="#00D4FF"/>
  <text x="1080" y="296" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">通勤族</text>
  <rect x="80" y="400" width="1120" height="180" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <text x="110" y="440" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#1565C0">产品愿景</text>
  <text x="110" y="480" font-family="Microsoft YaHei" font-size="15" fill="#424242">以"解放双手、拓展视觉体验"为核心，打造集辅助办公、运动监测、智能互联于一体的随身智能终端</text>
  <rect x="0" y="690" width="1280" height="30" fill="#1565C0"/>
</svg>'''

# Page 4: Hardware
svgs["04_hardware.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="#FAFAFA"/>
  <rect x="0" y="0" width="1280" height="100" fill="#1565C0"/>
  <text x="80" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#FFFFFF">02 核心硬件配置解析</text>
  <rect x="80" y="130" width="60" height="4" fill="#00D4FF"/>
  <rect x="80" y="160" width="260" height="140" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <rect x="80" y="160" width="6" height="140" fill="#00D4FF"/>
  <text x="110" y="200" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#1565C0">Micro OLED</text>
  <text x="110" y="235" font-family="Microsoft YaHei" font-size="14" fill="#757575">高清显示屏</text>
  <text x="110" y="270" font-family="Microsoft YaHei" font-size="13" fill="#424242">视觉清晰无眩晕</text>
  <rect x="360" y="160" width="260" height="140" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <rect x="360" y="160" width="6" height="140" fill="#00D4FF"/>
  <text x="390" y="200" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#1565C0">8h+</text>
  <text x="390" y="235" font-family="Microsoft YaHei" font-size="14" fill="#757575">超长续航</text>
  <text x="390" y="270" font-family="Microsoft YaHei" font-size="13" fill="#424242">低功耗处理器</text>
  <rect x="640" y="160" width="260" height="140" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <rect x="640" y="160" width="6" height="140" fill="#00D4FF"/>
  <text x="670" y="200" font-family="Microsoft YaHei" font-size="28" font-weight="bold" fill="#1565C0">高清双摄</text>
  <text x="670" y="235" font-family="Microsoft YaHei" font-size="14" fill="#757575">摄像头+降噪麦克风</text>
  <text x="670" y="270" font-family="Microsoft YaHei" font-size="13" fill="#424242">语音交互+实时拍摄</text>
  <rect x="920" y="160" width="260" height="140" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <rect x="920" y="160" width="6" height="140" fill="#00D4FF"/>
  <text x="950" y="200" font-family="Microsoft YaHei" font-size="28" font-weight="bold" fill="#1565C0">轻量化</text>
  <text x="950" y="235" font-family="Microsoft YaHei" font-size="14" fill="#757575">亲肤材质+可调节镜架</text>
  <text x="950" y="270" font-family="Microsoft YaHei" font-size="13" fill="#424242">佩戴舒适不压鼻</text>
  <rect x="80" y="320" width="1100" height="120" rx="12" fill="#1565C0"/>
  <text x="120" y="360" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#FFFFFF">双模连接</text>
  <text x="120" y="400" font-family="Microsoft YaHei" font-size="16" fill="#B3E5FC">蓝牙5.3 + WiFi 双模连接 | 传输稳定流畅</text>
  <rect x="0" y="690" width="1280" height="30" fill="#1565C0"/>
</svg>'''

# Page 5: Features
svgs["05_features.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="#FAFAFA"/>
  <rect x="0" y="0" width="1280" height="100" fill="#1565C0"/>
  <text x="80" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#FFFFFF">03 核心功能与场景应用</text>
  <rect x="80" y="130" width="60" height="4" fill="#00D4FF"/>
  <rect x="80" y="160" width="540" height="280" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <text x="110" y="200" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#1565C0">核心功能</text>
  <text x="110" y="240" font-family="Microsoft YaHei" font-size="15" fill="#424242">语音控制（拨打电话、查询信息）</text>
  <text x="110" y="270" font-family="Microsoft YaHei" font-size="15" fill="#424242">实时导航</text>
  <text x="110" y="300" font-family="Microsoft YaHei" font-size="15" fill="#424242">运动数据监测（步数、心率）</text>
  <text x="110" y="330" font-family="Microsoft YaHei" font-size="15" fill="#424242">办公辅助（消息提醒、文档预览）</text>
  <text x="110" y="360" font-family="Microsoft YaHei" font-size="15" fill="#424242">拍照录像、蓝牙听歌</text>
  <rect x="640" y="160" width="540" height="280" rx="12" fill="#1565C0"/>
  <text x="680" y="200" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#FFFFFF">应用场景</text>
  <circle cx="720" cy="260" r="25" fill="#00D4FF"/>
  <text x="760" y="265" font-family="Microsoft YaHei" font-size="16" fill="#FFFFFF">职场办公</text>
  <circle cx="720" cy="310" r="25" fill="#00D4FF"/>
  <text x="760" y="315" font-family="Microsoft YaHei" font-size="16" fill="#FFFFFF">户外跑步</text>
  <circle cx="720" cy="360" r="25" fill="#00D4FF"/>
  <text x="760" y="365" font-family="Microsoft YaHei" font-size="16" fill="#FFFFFF">日常通勤</text>
  <circle cx="1000" cy="260" r="25" fill="#00D4FF"/>
  <text x="1040" y="265" font-family="Microsoft YaHei" font-size="16" fill="#FFFFFF">驾驶出行</text>
  <text x="680" y="410" font-family="Microsoft YaHei" font-size="14" fill="#90CAF9">满足不同用户的多样化需求</text>
  <rect x="0" y="690" width="1280" height="30" fill="#1565C0"/>
</svg>'''

# Page 6: Advantages
svgs["06_advantages.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="#FAFAFA"/>
  <rect x="0" y="0" width="1280" height="100" fill="#1565C0"/>
  <text x="80" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#FFFFFF">04 与同类产品差异化优势</text>
  <rect x="80" y="130" width="60" height="4" fill="#00D4FF"/>
  <rect x="80" y="160" width="540" height="100" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <circle cx="120" cy="210" r="25" fill="#00D4FF"/>
  <text x="120" y="217" font-family="Arial" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
  <text x="160" y="195" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#1565C0">轻量化设计</text>
  <text x="160" y="225" font-family="Microsoft YaHei" font-size="14" fill="#424242">比行业平均重量轻20%，长期佩戴无负担</text>
  <rect x="640" y="160" width="540" height="100" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <circle cx="680" cy="210" r="25" fill="#00D4FF"/>
  <text x="680" y="217" font-family="Arial" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2</text>
  <text x="720" y="195" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#1565C0">超长续航+快充</text>
  <text x="720" y="225" font-family="Microsoft YaHei" font-size="14" fill="#424242">30分钟充电可使用4小时</text>
  <rect x="80" y="280" width="540" height="100" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <circle cx="120" cy="330" r="25" fill="#00D4FF"/>
  <text x="120" y="337" font-family="Arial" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3</text>
  <text x="160" y="315" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#1565C0">智能交互流畅</text>
  <text x="160" y="345" font-family="Microsoft YaHei" font-size="14" fill="#424242">语音识别准确率达98%以上</text>
  <rect x="640" y="280" width="540" height="100" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <circle cx="680" cy="330" r="25" fill="#00D4FF"/>
  <text x="680" y="337" font-family="Arial" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4</text>
  <text x="720" y="315" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#1565C0">高性价比</text>
  <text x="720" y="345" font-family="Microsoft YaHei" font-size="14" fill="#424242">多场景适配，兼顾办公与运动</text>
  <rect x="80" y="400" width="1100" height="150" rx="12" fill="#1565C0"/>
  <text x="120" y="445" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#FFFFFF">综合优势总结</text>
  <text x="120" y="485" font-family="Microsoft YaHei" font-size="16" fill="#B3E5FC">更轻 · 更快 · 更准 · 更实用</text>
  <text x="120" y="520" font-family="Microsoft YaHei" font-size="14" fill="#90CAF9">全方位领先，打造最具竞争力的智能穿戴产品</text>
  <rect x="0" y="690" width="1280" height="30" fill="#1565C0"/>
</svg>'''

# Page 7: User Feedback
svgs["07_feedback.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="#FAFAFA"/>
  <rect x="0" y="0" width="1280" height="100" fill="#1565C0"/>
  <text x="80" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#FFFFFF">05 用户体验反馈与案例</text>
  <rect x="80" y="130" width="60" height="4" fill="#00D4FF"/>
  <rect x="80" y="160" width="360" height="180" rx="12" fill="#1565C0"/>
  <text x="260" y="220" font-family="Arial" font-size="56" font-weight="bold" fill="#00D4FF" text-anchor="middle">1000+</text>
  <text x="260" y="270" font-family="Microsoft YaHei" font-size="18" fill="#FFFFFF" text-anchor="middle">用户实测</text>
  <rect x="460" y="160" width="360" height="180" rx="12" fill="#00D4FF"/>
  <text x="640" y="220" font-family="Arial" font-size="56" font-weight="bold" fill="#FFFFFF" text-anchor="middle">95%+</text>
  <text x="640" y="270" font-family="Microsoft YaHei" font-size="18" fill="#0D47A1" text-anchor="middle">用户满意度</text>
  <rect x="840" y="160" width="360" height="180" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <text x="880" y="200" font-family="Microsoft YaHei" font-size="16" font-weight="bold" fill="#1565C0">典型用户反馈</text>
  <text x="880" y="235" font-family="Microsoft YaHei" font-size="13" fill="#424242">"佩戴舒适、操作便捷，</text>
  <text x="880" y="255" font-family="Microsoft YaHei" font-size="13" fill="#424242">导航与办公辅助功能</text>
  <text x="880" y="275" font-family="Microsoft YaHei" font-size="13" fill="#424242">实用性强"</text>
  <rect x="80" y="360" width="540" height="180" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <text x="110" y="400" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#1565C0">职场用户案例</text>
  <text x="110" y="440" font-family="Microsoft YaHei" font-size="14" fill="#424242">通过眼镜快速预览会议文档，</text>
  <text x="110" y="465" font-family="Microsoft YaHei" font-size="14" fill="#424242">有效提升会议效率和决策速度</text>
  <rect x="640" y="360" width="540" height="180" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <text x="670" y="400" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#1565C0">运动用户案例</text>
  <text x="670" y="440" font-family="Microsoft YaHei" font-size="14" fill="#424242">实时查看心率数据，</text>
  <text x="670" y="465" font-family="Microsoft YaHei" font-size="14" fill="#424242">科学调整运动强度</text>
  <rect x="0" y="690" width="1280" height="30" fill="#1565C0"/>
</svg>'''

# Page 8: Future Plans
svgs["08_future.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <rect width="1280" height="720" fill="#FAFAFA"/>
  <rect x="0" y="0" width="1280" height="100" fill="#1565C0"/>
  <text x="80" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#FFFFFF">06 未来规划与总结</text>
  <rect x="80" y="130" width="60" height="4" fill="#00D4FF"/>
  <rect x="80" y="160" width="540" height="280" rx="12" fill="#1565C0"/>
  <text x="120" y="210" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#FFFFFF">产品总结</text>
  <text x="120" y="255" font-family="Microsoft YaHei" font-size="15" fill="#B3E5FC">以优质硬件、丰富功能、高适配性，</text>
  <text x="120" y="280" font-family="Microsoft YaHei" font-size="15" fill="#B3E5FC">打破传统穿戴设备局限，</text>
  <text x="120" y="305" font-family="Microsoft YaHei" font-size="15" fill="#B3E5FC">为用户提供更便捷、智能的生活方式。</text>
  <rect x="640" y="160" width="540" height="280" rx="12" fill="#FFFFFF" stroke="#E0E0E0"/>
  <text x="680" y="210" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#1565C0">未来规划</text>
  <circle cx="720" cy="270" r="15" fill="#00D4FF"/>
  <text x="750" y="275" font-family="Microsoft YaHei" font-size="15" fill="#424242">持续优化交互体验</text>
  <circle cx="720" cy="320" r="15" fill="#00D4FF"/>
  <text x="750" y="325" font-family="Microsoft YaHei" font-size="15" fill="#424242">新增健康监测功能</text>
  <circle cx="720" cy="370" r="15" fill="#00D4FF"/>
  <text x="750" y="375" font-family="Microsoft YaHei" font-size="15" fill="#424242">AR增强现实功能</text>
  <circle cx="720" cy="420" r="15" fill="#00D4FF"/>
  <text x="750" y="425" font-family="Microsoft YaHei" font-size="15" fill="#424242">拓展更多行业应用场景</text>
  <rect x="80" y="460" width="1100" height="100" rx="12" fill="#00D4FF"/>
  <text x="120" y="510" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#0D47A1">愿景：打造最具竞争力的智能穿戴产品</text>
  <rect x="0" y="690" width="1280" height="30" fill="#1565C0"/>
</svg>'''

# Page 9: Ending
svgs["09_ending.svg"] = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <defs>
    <linearGradient id="bgGradEnd" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D47A1"/>
      <stop offset="100%" stop-color="#1565C0"/>
    </linearGradient>
  </defs>
  <rect width="1280" height="720" fill="url(#bgGradEnd)"/>
  <circle cx="1100" cy="150" r="300" fill="#00D4FF" opacity="0.1"/>
  <circle cx="200" cy="600" r="200" fill="#00D4FF" opacity="0.08"/>
  <text x="640" y="250" font-family="Microsoft YaHei" font-size="48" font-weight="bold" fill="#FFFFFF" text-anchor="middle">智启未来，镜观世界</text>
  <text x="640" y="320" font-family="Microsoft YaHei" font-size="28" fill="#00D4FF" text-anchor="middle">XX智能眼镜，伴你每一步</text>
  <rect x="540" y="380" width="200" height="3" fill="#00D4FF"/>
  <text x="640" y="450" font-family="Microsoft YaHei" font-size="24" fill="#B3E5FC" text-anchor="middle">感谢观看</text>
  <text x="640" y="520" font-family="Microsoft YaHei" font-size="16" fill="#90CAF9" text-anchor="middle">咨询电话：400-XXX-XXXX</text>
  <text x="640" y="550" font-family="Microsoft YaHei" font-size="16" fill="#90CAF9" text-anchor="middle">官方公众号：XX智能科技</text>
  <rect x="0" y="690" width="1280" height="30" fill="#0D47A1"/>
</svg>'''

# Write SVG files
for filename, content in svgs.items():
    filepath = os.path.join(svg_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {filepath}")

# Write notes file
notes_content = """# 01_cover

欢迎各位来到今天的发布会。今天我将为大家介绍一款颠覆性的智能穿戴产品——XX智能眼镜。

[Pause]

它不仅仅是一副眼镜，更是您通往未来智能生活的钥匙。让我们一起探索：如何用一副眼镜，重构您的数字体验？

关键要点: (1) 引入智能眼镜新品 (2) 建立科技感基调 (3) 激发观众好奇心
时长: 1分钟

---

# 02_toc

本次演示将分为六个部分，帮助大家全面了解这款产品。

[Transition] 首先，让我们从产品的整体定位开始——这款眼镜究竟为谁而生？

关键要点: (1) 清晰展示演示结构 (2) 建立逻辑框架 (3) 为后续内容做铺垫
时长: 30秒

---

# 03_overview

XX智能眼镜定位为一款融合科技与便捷的智能穿戴设备，主打三大核心关键词：轻量便携、智能交互、多场景适配。

[Pause]

我们瞄准三大用户群体：职场人士需要高效办公，运动爱好者追求科学运动，通勤族渴望解放双手。

[Transition] 接下来，让我们深入了解这款产品的"硬核"配置。

关键要点: (1) 强调"轻便+智能+多场景"定位 (2) 明确三大目标用户群体 (3) 体现产品愿景
时长: 2分钟

---

# 04_hardware

这款眼镜在硬件配置上毫不妥协。

首先是Micro OLED高清显示屏，带来视觉清晰无眩晕的体验。[Pause]

8小时以上的超长续航，配合低功耗处理器，让您从早到晚无忧使用。

[Pause]

高清双摄像头配合降噪麦克风，支持语音交互与实时拍摄。轻量化亲肤材质，可调节镜架，佩戴一整天也舒适无负担。

最后，蓝牙5.3加WiFi双模连接，传输稳定流畅。

[Transition] 强大的硬件需要丰富的功能来承载。

关键要点: (1) Micro OLED显示屏 (2) 8h+超长续航 (3) 高清双摄+降噪麦克风 (4) 双模连接
时长: 2分钟

---

# 05_features

这款眼镜的功能覆盖生活方方面面：语音控制拨打电话、实时导航、运动数据监测、办公辅助、拍照录像、蓝牙听歌……

[Pause]

应用场景包括：职场办公、户外跑步、日常通勤、驾驶出行——真正实现一镜多用。

[Transition] 说了这么多，它和市面上的同类产品相比，究竟有哪些过人之处？

关键要点: (1) 六大核心功能 (2) 四大应用场景 (3) 一镜多用的理念
时长: 2分钟

---

# 06_advantages

这是我们最引以为傲的部分。四大核心优势：

一、轻量化设计，比行业平均重量轻20%，长期佩戴零负担。[Pause]

二、超长续航加快充，充电30分钟就能使用4小时。[Pause]

三、智能交互更流畅，语音识别准确率高达98%以上。[Pause]

四、极高性价比，兼顾办公与运动场景。

[Transition] 这些优势不仅仅是参数，更是真实用户反馈的结晶。

关键要点: (1) 四大差异化优势 (2) 量化数据支撑 (3) 强调综合竞争力
时长: 2分钟

---

# 07_feedback

产品经过1000多位真实用户测试，满意度高达95%以上。

[Pause]

用户反馈最集中的两点：佩戴舒适、操作便捷。特别是导航和办公辅助功能，被用户评价为"用了就回不去"。

[Interactive] 各位想象一下——职场用户通过眼镜快速预览会议文档，无需掏出手机；运动爱好者实时查看心率数据，科学调整运动强度。这是效率的提升，更是生活方式的改变。

关键要点: (1) 1000+用户验证 (2) 95%满意度 (3) 职场+运动典型案例
时长: 2分钟

---

# 08_future

让我们回顾总结：以优质硬件、丰富功能、高适配性，这款眼镜正在打破传统穿戴设备的局限。

[Pause]

展望未来，我们将持续优化交互体验，新增健康监测功能，引入AR增强现实技术，并拓展更多行业应用场景。

[Pause]

我们的愿景是：打造最具竞争力的智能穿戴产品，让科技真正服务每一个人。

[Transition] 最后，让我们用一句话总结今天的主题。

关键要点: (1) 产品核心价值 (2) 四大未来方向 (3) 愿景宣言
时长: 2分钟

---

# 09_ending

智启未来，镜观世界。XX智能眼镜，伴你每一步。

感谢各位的聆听。如有任何问题，欢迎扫码或拨打我们的客服热线。

期待与您共同开启智能穿戴新时代！

关键要点: (1) 强化品牌理念 (2) 提供联系方式 (3) 完美收尾
时长: 1分钟
"""

notes_path = os.path.join(notes_dir, "total.md")
with open(notes_path, 'w', encoding='utf-8') as f:
    f.write(notes_content)
print(f"Created: {notes_path}")

print(f"\\nAll 9 SVG pages and notes created successfully!")
