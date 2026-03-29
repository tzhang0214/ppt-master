#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成智能眼镜PPT所有SVG页面 - 华为暖色版"""

import os

project_path = r"d:\projects\aiprojects\ppt-master\projects\smart-glasses_ppt169_20260329"
svg_output = os.path.join(project_path, "svg_output")
os.makedirs(svg_output, exist_ok=True)

def write_svg(filename, content):
    filepath = os.path.join(svg_output, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {filepath}")

# Huawei Logo SVG path for bottom right
huawei_logo_light = '''<g transform="translate(1180, 660) scale(1.5)">
  <path d="M10.341 17.042s.062-.061 0-.061C7.516 10.902 3.646 6.22 3.646 6.22S1.557 8.168 1.68 10.174c.061 1.52 1.228 2.37 1.228 2.37 1.843 1.763 6.266 4.012 7.31 4.499h.123zm-.737 1.52c0-.061-.123-.061-.123-.061l-7.371.243c.798 1.398 2.15 2.492 3.563 2.188.983-.243 3.194-1.763 3.87-2.25.123-.12.061-.12.061-.12zm.123-.67c.062-.06 0-.12 0-.12C6.471 15.581.206 12.3.206 12.3c-.553 1.763.184 3.161.184 3.161.798 1.702 2.334 2.189 2.334 2.189.676.303 1.413.303 1.413.303h5.529c.061 0 .061-.06.061-.06zm.492-14.831c-.308 0-1.168.243-1.168.243-1.965.486-2.395 2.249-2.395 2.249-.369 1.094 0 2.31 0 2.31.675 2.857 3.87 7.598 4.545 8.57l.062.062c.061 0 .061-.061.061-.061C12.43 5.796 10.22 3.06 10.22 3.06zm2.457 13.373c.061 0 .123-.061.123-.061.737-1.033 3.87-5.714 4.545-8.57 0 0 .369-1.399 0-2.31 0 0-.491-1.764-2.457-2.25 0 0-.553-.121-1.167-.243 0 0-2.211 2.796-1.106 13.312 0 .122.062.122.062.122zm1.72 2.067s-.062 0-.062.06v.122c.738.486 2.826 2.006 3.87 2.249 0 0 1.905.669 3.563-2.188l-7.371-.243zm9.398-6.261s-6.265 3.343-9.521 5.531c0 0-.062.06-.062.122 0 0 0 .06.062.06h5.651s.553 0 1.29-.303c0 0 1.536-.487 2.396-2.25 0-.06.737-1.458.184-3.16zM13.66 17.042s.061.06.122 0c1.045-.547 5.468-2.736 7.31-4.499 0 0 1.168-.911 1.23-2.37.122-2.067-1.967-3.951-1.967-3.951s-3.87 4.559-6.695 10.698c0 0-.062.06 0 .122z" fill="#C04000"/>
</g>'''

huawei_logo_dark = '''<g transform="translate(1180, 660) scale(1.5)">
  <path d="M10.341 17.042s.062-.061 0-.061C7.516 10.902 3.646 6.22 3.646 6.22S1.557 8.168 1.68 10.174c.061 1.52 1.228 2.37 1.228 2.37 1.843 1.763 6.266 4.012 7.31 4.499h.123zm-.737 1.52c0-.061-.123-.061-.123-.061l-7.371.243c.798 1.398 2.15 2.492 3.563 2.188.983-.243 3.194-1.763 3.87-2.25.123-.12.061-.12.061-.12zm.123-.67c.062-.06 0-.12 0-.12C6.471 15.581.206 12.3.206 12.3c-.553 1.763.184 3.161.184 3.161.798 1.702 2.334 2.189 2.334 2.189.676.303 1.413.303 1.413.303h5.529c.061 0 .061-.06.061-.06zm.492-14.831c-.308 0-1.168.243-1.168.243-1.965.486-2.395 2.249-2.395 2.249-.369 1.094 0 2.31 0 2.31.675 2.857 3.87 7.598 4.545 8.57l.062.062c.061 0 .061-.061.061-.061C12.43 5.796 10.22 3.06 10.22 3.06zm2.457 13.373c.061 0 .123-.061.123-.061.737-1.033 3.87-5.714 4.545-8.57 0 0 .369-1.399 0-2.31 0 0-.491-1.764-2.457-2.25 0 0-.553-.121-1.167-.243 0 0-2.211 2.796-1.106 13.312 0 .122.062.122.062.122zm1.72 2.067s-.062 0-.062.06v.122c.738.486 2.826 2.006 3.87 2.249 0 0 1.905.669 3.563-2.188l-7.371-.243zm9.398-6.261s-6.265 3.343-9.521 5.531c0 0-.062.06-.062.122 0 0 0 .06.062.06h5.651s.553 0 1.29-.303c0 0 1.536-.487 2.396-2.25 0-.06.737-1.458.184-3.16zM13.66 17.042s.061.06.122 0c1.045-.547 5.468-2.736 7.31-4.499 0 0 1.168-.911 1.23-2.37.122-2.067-1.967-3.951-1.967-3.951s-3.87 4.559-6.695 10.698c0 0-.062.06 0 .122z" fill="#FFFFFF"/>
</g>'''

# ==================== 第1页: 封面 (无华为logo) ====================
cover_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FFF5F0;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="circleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF6B35;stop-opacity:0.12" />
      <stop offset="100%" style="stop-color:#F7931E;stop-opacity:0.08" />
    </linearGradient>
    <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#B71C1C;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#C04000;stop-opacity:0.8" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="url(#bgGradient)" />

  <!-- Right Side Geometric Decoration -->
  <circle cx="1100" cy="200" r="280" fill="url(#circleGradient)" />
  <circle cx="1150" cy="280" r="180" fill="#FF6B35" fill-opacity="0.06" />
  <circle cx="1200" cy="150" r="120" fill="#F7931E" fill-opacity="0.08" />
  <circle cx="1050" cy="400" r="100" fill="#FFD23F" fill-opacity="0.1" />

  <!-- Top Accent Bar -->
  <rect x="0" y="0" width="1280" height="6" fill="url(#accentGradient)" />

  <!-- Left Side Decorative Element -->
  <rect x="60" y="180" width="6" height="80" fill="#B71C1C" />

  <!-- Main Title -->
  <text x="90" y="250" font-family="Microsoft YaHei" font-size="52" font-weight="bold" fill="#B71C1C">智享视界·境启新生</text>

  <!-- Accent Line under title -->
  <rect x="90" y="275" width="160" height="4" fill="url(#accentGradient)" />

  <!-- Subtitle -->
  <text x="90" y="340" font-family="Microsoft YaHei" font-size="26" fill="#666666">打破边界，重构智能生活新体验</text>

  <!-- Divider Line -->
  <line x1="90" y1="400" x2="600" y2="400" stroke="#FFE5DC" stroke-width="1" />

  <!-- Product Name -->
  <text x="90" y="460" font-family="Microsoft YaHei" font-size="22" fill="#333333">XX智能眼镜新品发布</text>

  <!-- Date -->
  <text x="90" y="500" font-family="Microsoft YaHei" font-size="18" fill="#999999">2026年3月</text>

  <!-- Bottom Decorative Bar -->
  <rect x="0" y="680" width="1280" height="40" fill="#FFF5F0" />
  <rect x="0" y="680" width="200" height="40" fill="url(#accentGradient)" />

  <!-- Logo Area -->
  <rect x="1100" y="50" width="140" height="50" fill="#FFF5F0" rx="4" />
  <text x="1170" y="82" font-family="Microsoft YaHei" font-size="16" fill="#B71C1C" text-anchor="middle">Smart Glasses</text>

  <!-- Small geometric accents -->
  <rect x="1200" y="620" width="40" height="40" fill="none" stroke="#B71C1C" stroke-width="2" stroke-opacity="0.3" />
  <rect x="1210" y="630" width="20" height="20" fill="#B71C1C" fill-opacity="0.2" />
</svg>'''
write_svg("01_封面.svg", cover_svg)

# ==================== 第2页: 目录 ====================
toc_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <defs>
    <linearGradient id="sidebarGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#B71C1C;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#C04000;stop-opacity:1" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#FFFFFF" />

  <!-- Left Sidebar -->
  <rect x="0" y="0" width="320" height="720" fill="url(#sidebarGradient)" />

  <!-- White Accent on Sidebar -->
  <rect x="0" y="0" width="8" height="720" fill="#FFFFFF" fill-opacity="0.3" />

  <!-- Sidebar Content -->
  <text x="60" y="100" font-family="Arial" font-size="18" font-weight="bold" fill="#FFFFFF" letter-spacing="4">CONTENTS</text>
  <text x="60" y="140" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" fill-opacity="0.8">目录</text>

  <!-- Decorative Line -->
  <rect x="60" y="165" width="80" height="3" fill="#FFD23F" />

  <!-- Geometric Pattern on Sidebar -->
  <circle cx="260" cy="600" r="150" fill="#FFFFFF" fill-opacity="0.1" />
  <circle cx="280" cy="650" r="100" fill="#FFD23F" fill-opacity="0.08" />

  <!-- Right Side - TOC Items -->
  <!-- Item 1 -->
  <rect x="380" y="120" width="50" height="50" fill="#FFF5F0" rx="4" />
  <text x="405" y="155" font-family="Arial" font-size="22" font-weight="bold" fill="#B71C1C" text-anchor="middle">01</text>
  <text x="460" y="140" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">产品概述与核心定位</text>
  <line x1="380" y1="185" x2="900" y2="185" stroke="#FFE5DC" stroke-width="1" />

  <!-- Item 2 -->
  <rect x="380" y="215" width="50" height="50" fill="#FFF5F0" rx="4" />
  <text x="405" y="250" font-family="Arial" font-size="22" font-weight="bold" fill="#B71C1C" text-anchor="middle">02</text>
  <text x="460" y="235" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">核心硬件配置解析</text>
  <line x1="380" y1="280" x2="900" y2="280" stroke="#FFE5DC" stroke-width="1" />

  <!-- Item 3 -->
  <rect x="380" y="310" width="50" height="50" fill="#FFF5F0" rx="4" />
  <text x="405" y="345" font-family="Arial" font-size="22" font-weight="bold" fill="#B71C1C" text-anchor="middle">03</text>
  <text x="460" y="330" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">核心功能与场景应用</text>
  <line x1="380" y1="375" x2="900" y2="375" stroke="#FFE5DC" stroke-width="1" />

  <!-- Item 4 -->
  <rect x="380" y="405" width="50" height="50" fill="#FFF5F0" rx="4" />
  <text x="405" y="440" font-family="Arial" font-size="22" font-weight="bold" fill="#B71C1C" text-anchor="middle">04</text>
  <text x="460" y="425" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">与同类产品差异化优势</text>
  <line x1="380" y1="470" x2="900" y2="470" stroke="#FFE5DC" stroke-width="1" />

  <!-- Item 5 -->
  <rect x="380" y="500" width="50" height="50" fill="#FFF5F0" rx="4" />
  <text x="405" y="535" font-family="Arial" font-size="22" font-weight="bold" fill="#B71C1C" text-anchor="middle">05</text>
  <text x="460" y="520" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">用户体验反馈与案例</text>
  <line x1="380" y1="565" x2="900" y2="565" stroke="#FFE5DC" stroke-width="1" />

  <!-- Item 6 -->
  <rect x="380" y="595" width="50" height="50" fill="#FFF5F0" rx="4" />
  <text x="405" y="630" font-family="Arial" font-size="22" font-weight="bold" fill="#B71C1C" text-anchor="middle">06</text>
  <text x="460" y="615" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">未来规划与总结</text>

  <!-- Footer -->
  <rect x="0" y="690" width="1280" height="30" fill="#FFF8F5" />
  <text x="40" y="710" font-family="Microsoft YaHei" font-size="12" fill="#999999">Smart Glasses</text>
  <text x="1240" y="710" font-family="Arial" font-size="12" fill="#666666" text-anchor="end">02</text>

  <!-- Huawei Logo in bottom right -->
  {huawei_logo_light}
</svg>'''
write_svg("02_目录.svg", toc_svg)

# ==================== 第3页: 产品概述与核心定位 ====================
content3_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#FFFFFF" />

  <!-- Top Header Bar -->
  <rect x="0" y="0" width="1280" height="100" fill="#FFF8F5" />

  <!-- Red Accent Bar on Left -->
  <rect x="0" y="0" width="8" height="100" fill="#B71C1C" />

  <!-- Page Title -->
  <rect x="40" y="35" width="8" height="35" fill="#B71C1C" />
  <text x="65" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#B71C1C">产品概述与核心定位</text>

  <!-- Title Underline -->
  <line x1="65" y1="85" x2="800" y2="85" stroke="#FFE5DC" stroke-width="1" />

  <!-- Right Side Header Info -->
  <text x="1240" y="60" font-family="Microsoft YaHei" font-size="14" fill="#999999" text-anchor="end">01</text>

  <!-- Main Content Area -->
  <!-- Product positioning card -->
  <rect x="60" y="140" width="560" height="260" fill="#FFF5F0" rx="8" />
  <rect x="60" y="140" width="8" height="260" fill="#B71C1C" rx="4" />
  <text x="95" y="180" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#B71C1C">产品定位</text>
  <text x="95" y="220" font-family="Microsoft YaHei" font-size="16" fill="#333333">一款融合科技与便捷的穿戴设备</text>
  <text x="95" y="260" font-family="Microsoft YaHei" font-size="16" fill="#333333">主打"轻量便携、智能交互、多场景适配"</text>
  <text x="95" y="320" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#C04000">核心价值</text>
  <text x="95" y="360" font-family="Microsoft YaHei" font-size="16" fill="#333333">解放双手 · 拓展视觉体验</text>
  <text x="95" y="385" font-family="Microsoft YaHei" font-size="16" fill="#333333">辅助办公 · 运动监测 · 智能互联</text>

  <!-- Target users card -->
  <rect x="660" y="140" width="560" height="260" fill="#FFF5F0" rx="8" />
  <rect x="660" y="140" width="8" height="260" fill="#C04000" rx="4" />
  <text x="695" y="180" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#B71C1C">目标用户群体</text>

  <!-- User group 1 -->
  <circle cx="740" cy="250" r="30" fill="#B71C1C" fill-opacity="0.15" />
  <text x="740" y="256" font-family="Microsoft YaHei" font-size="24" font-weight="bold" fill="#B71C1C" text-anchor="middle">01</text>
  <text x="790" y="245" font-family="Microsoft YaHei" font-size="16" font-weight="bold" fill="#B71C1C">职场人士</text>
  <text x="790" y="270" font-family="Microsoft YaHei" font-size="14" fill="#666666">办公会议、文档预览</text>

  <!-- User group 2 -->
  <circle cx="960" cy="250" r="30" fill="#C04000" fill-opacity="0.15" />
  <text x="960" y="256" font-family="Microsoft YaHei" font-size="24" font-weight="bold" fill="#C04000" text-anchor="middle">02</text>
  <text x="1010" y="245" font-family="Microsoft YaHei" font-size="16" font-weight="bold" fill="#B71C1C">运动爱好者</text>
  <text x="1010" y="270" font-family="Microsoft YaHei" font-size="14" fill="#666666">跑步健身、数据监测</text>

  <!-- User group 3 -->
  <circle cx="740" cy="340" r="30" fill="#D2691E" fill-opacity="0.15" />
  <text x="740" y="346" font-family="Microsoft YaHei" font-size="24" font-weight="bold" fill="#D2691E" text-anchor="middle">03</text>
  <text x="790" y="335" font-family="Microsoft YaHei" font-size="16" font-weight="bold" fill="#B71C1C">日常通勤族</text>
  <text x="790" y="360" font-family="Microsoft YaHei" font-size="14" fill="#666666">导航、通话、音乐</text>

  <!-- Bottom description -->
  <rect x="60" y="430" width="1160" height="200" fill="#FFF5F0" rx="8" />
  <rect x="60" y="430" width="8" height="200" fill="#B71C1C" rx="4" />
  <text x="100" y="480" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">随身智能终端</text>
  <text x="100" y="520" font-family="Microsoft YaHei" font-size="16" fill="#333333">集辅助办公、运动监测、智能互联于一体的随身智能终端</text>
  <text x="100" y="560" font-family="Microsoft YaHei" font-size="16" fill="#333333">打造随时随地的智能生活体验</text>

  <!-- Footer -->
  <rect x="0" y="690" width="1280" height="30" fill="#FFF8F5" />
  <text x="40" y="710" font-family="Microsoft YaHei" font-size="12" fill="#999999">Smart Glasses</text>
  <text x="1240" y="710" font-family="Arial" font-size="14" fill="#666666" text-anchor="end">03</text>

  <!-- Huawei Logo in bottom right -->
  {huawei_logo_light}
</svg>'''
write_svg("03_产品概述.svg", content3_svg)

# ==================== 第4页: 核心硬件配置解析 ====================
content4_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#FFFFFF" />

  <!-- Top Header Bar -->
  <rect x="0" y="0" width="1280" height="100" fill="#FFF8F5" />

  <!-- Red Accent Bar on Left -->
  <rect x="0" y="0" width="8" height="100" fill="#B71C1C" />

  <!-- Page Title -->
  <rect x="40" y="35" width="8" height="35" fill="#B71C1C" />
  <text x="65" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#B71C1C">核心硬件配置解析</text>

  <!-- Title Underline -->
  <line x1="65" y1="85" x2="800" y2="85" stroke="#FFE5DC" stroke-width="1" />

  <!-- Right Side Header Info -->
  <text x="1240" y="60" font-family="Microsoft YaHei" font-size="14" fill="#999999" text-anchor="end">02</text>

  <!-- Hardware Spec Cards - Row 1 -->
  <!-- Card 1: Display -->
  <rect x="60" y="130" width="360" height="160" fill="#FFF5F0" rx="8" />
  <rect x="60" y="130" width="8" height="160" fill="#B71C1C" rx="4" />
  <text x="95" y="170" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">高清显示屏</text>
  <text x="95" y="205" font-family="Microsoft YaHei" font-size="14" fill="#333333">Micro OLED显示屏</text>
  <text x="95" y="230" font-family="Microsoft YaHei" font-size="14" fill="#333333">视觉清晰无眩晕</text>
  <text x="95" y="265" font-family="Microsoft YaHei" font-size="24" font-weight="bold" fill="#B71C1C">OLED</text>

  <!-- Card 2: Processor -->
  <rect x="460" y="130" width="360" height="160" fill="#FFF5F0" rx="8" />
  <rect x="460" y="130" width="8" height="160" fill="#C04000" rx="4" />
  <text x="495" y="170" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">低功耗处理器</text>
  <text x="495" y="205" font-family="Microsoft YaHei" font-size="14" fill="#333333">高效能低功耗芯片</text>
  <text x="495" y="230" font-family="Microsoft YaHei" font-size="14" fill="#333333">续航可达8小时以上</text>
  <text x="495" y="265" font-family="Microsoft YaHei" font-size="24" font-weight="bold" fill="#C04000">8H+</text>

  <!-- Card 3: Camera -->
  <rect x="860" y="130" width="360" height="160" fill="#FFF5F0" rx="8" />
  <rect x="860" y="130" width="8" height="160" fill="#D2691E" rx="4" />
  <text x="895" y="170" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">高清摄像头</text>
  <text x="895" y="205" font-family="Microsoft YaHei" font-size="14" fill="#333333">高清摄像头+降噪麦克风</text>
  <text x="895" y="230" font-family="Microsoft YaHei" font-size="14" fill="#333333">支持语音交互与实时拍摄</text>
  <text x="895" y="265" font-family="Microsoft YaHei" font-size="24" font-weight="bold" fill="#D2691E">1080P</text>

  <!-- Hardware Spec Cards - Row 2 -->
  <!-- Card 4: Material -->
  <rect x="60" y="320" width="560" height="160" fill="#FFF5F0" rx="8" />
  <rect x="60" y="320" width="8" height="160" fill="#A0522D" rx="4" />
  <text x="95" y="360" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">亲肤轻量化材质</text>
  <text x="95" y="395" font-family="Microsoft YaHei" font-size="14" fill="#333333">采用亲肤轻量化材质</text>
  <text x="95" y="420" font-family="Microsoft YaHei" font-size="14" fill="#333333">镜架可调节，佩戴舒适不压鼻</text>
  <text x="95" y="455" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#B71C1C">轻至30g</text>

  <!-- Card 5: Connectivity -->
  <rect x="660" y="320" width="560" height="160" fill="#FFF5F0" rx="8" />
  <rect x="660" y="320" width="8" height="160" fill="#B71C1C" rx="4" />
  <text x="695" y="360" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">双模连接</text>
  <text x="695" y="395" font-family="Microsoft YaHei" font-size="14" fill="#333333">蓝牙5.3 + WiFi双模连接</text>
  <text x="695" y="420" font-family="Microsoft YaHei" font-size="14" fill="#333333">传输稳定流畅</text>
  <text x="695" y="455" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#B71C1C">BT5.3</text>

  <!-- Bottom highlight bar -->
  <rect x="60" y="510" width="1160" height="120" fill="#FFF5F0" rx="8" />
  <rect x="60" y="510" width="8" height="120" fill="#C04000" rx="4" />
  <text x="100" y="555" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">顶级硬件配置 · 打造极致体验</text>
  <text x="100" y="595" font-family="Microsoft YaHei" font-size="16" fill="#333333">每一项配置都经过精心挑选，只为给您带来最佳使用体验</text>

  <!-- Footer -->
  <rect x="0" y="690" width="1280" height="30" fill="#FFF8F5" />
  <text x="40" y="710" font-family="Microsoft YaHei" font-size="12" fill="#999999">Smart Glasses</text>
  <text x="1240" y="710" font-family="Arial" font-size="14" fill="#666666" text-anchor="end">04</text>

  <!-- Huawei Logo in bottom right -->
  {huawei_logo_light}
</svg>'''
write_svg("04_硬件配置.svg", content4_svg)

# ==================== 第5页: 核心功能与场景应用 ====================
content5_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#FFFFFF" />

  <!-- Top Header Bar -->
  <rect x="0" y="0" width="1280" height="100" fill="#FFF8F5" />

  <!-- Red Accent Bar on Left -->
  <rect x="0" y="0" width="8" height="100" fill="#B71C1C" />

  <!-- Page Title -->
  <rect x="40" y="35" width="8" height="35" fill="#B71C1C" />
  <text x="65" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#B71C1C">核心功能与场景应用</text>

  <!-- Title Underline -->
  <line x1="65" y1="85" x2="800" y2="85" stroke="#FFE5DC" stroke-width="1" />

  <!-- Right Side Header Info -->
  <text x="1240" y="60" font-family="Microsoft YaHei" font-size="14" fill="#999999" text-anchor="end">03</text>

  <!-- Functions Row -->
  <!-- Function 1 -->
  <rect x="60" y="130" width="185" height="130" fill="#B71C1C" rx="8" />
  <text x="152" y="175" font-family="Microsoft YaHei" font-size="32" fill="#FFFFFF" text-anchor="middle">🎙</text>
  <text x="152" y="220" font-family="Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">语音控制</text>

  <!-- Function 2 -->
  <rect x="265" y="130" width="185" height="130" fill="#C04000" rx="8" />
  <text x="357" y="175" font-family="Microsoft YaHei" font-size="32" fill="#FFFFFF" text-anchor="middle">🗺</text>
  <text x="357" y="220" font-family="Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">实时导航</text>

  <!-- Function 3 -->
  <rect x="470" y="130" width="185" height="130" fill="#D2691E" rx="8" />
  <text x="562" y="175" font-family="Microsoft YaHei" font-size="32" fill="#FFFFFF" text-anchor="middle">📊</text>
  <text x="562" y="220" font-family="Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">运动监测</text>

  <!-- Function 4 -->
  <rect x="675" y="130" width="185" height="130" fill="#A0522D" rx="8" />
  <text x="767" y="175" font-family="Microsoft YaHei" font-size="32" fill="#FFFFFF" text-anchor="middle">💼</text>
  <text x="767" y="220" font-family="Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">办公辅助</text>

  <!-- Function 5 -->
  <rect x="880" y="130" width="185" height="130" fill="#8B4513" rx="8" />
  <text x="972" y="175" font-family="Microsoft YaHei" font-size="32" fill="#FFFFFF" text-anchor="middle">📷</text>
  <text x="972" y="220" font-family="Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">拍照录像</text>

  <!-- Function 6 -->
  <rect x="1085" y="130" width="135" height="130" fill="#B71C1C" fill-opacity="0.8" rx="8" />
  <text x="1152" y="175" font-family="Microsoft YaHei" font-size="32" fill="#FFFFFF" text-anchor="middle">🎵</text>
  <text x="1152" y="220" font-family="Microsoft YaHei" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">蓝牙音乐</text>

  <!-- Function Details -->
  <rect x="60" y="280" width="560" height="160" fill="#FFF5F0" rx="8" />
  <rect x="60" y="280" width="8" height="160" fill="#B71C1C" rx="4" />
  <text x="95" y="320" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">语音控制功能</text>
  <text x="95" y="355" font-family="Microsoft YaHei" font-size="14" fill="#333333">• 拨打电话</text>
  <text x="95" y="385" font-family="Microsoft YaHei" font-size="14" fill="#333333">• 查询信息</text>
  <text x="95" y="415" font-family="Microsoft YaHei" font-size="14" fill="#333333">• 语音指令控制设备</text>

  <rect x="660" y="280" width="560" height="160" fill="#FFF5F0" rx="8" />
  <rect x="660" y="280" width="8" height="160" fill="#C04000" rx="4" />
  <text x="695" y="320" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">运动数据监测</text>
  <text x="695" y="355" font-family="Microsoft YaHei" font-size="14" fill="#333333">• 步数统计</text>
  <text x="695" y="385" font-family="Microsoft YaHei" font-size="14" fill="#333333">• 心率监测</text>
  <text x="695" y="415" font-family="Microsoft YaHei" font-size="14" fill="#333333">• 卡路里消耗</text>

  <!-- Usage Scenarios -->
  <rect x="60" y="460" width="1160" height="170" fill="#FFF5F0" rx="8" />
  <rect x="60" y="460" width="8" height="170" fill="#B71C1C" rx="4" />
  <text x="100" y="510" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">适用场景</text>

  <!-- Scenario tags -->
  <rect x="100" y="535" width="100" height="36" fill="#B71C1C" rx="18" />
  <text x="150" y="559" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">职场办公</text>

  <rect x="220" y="535" width="100" height="36" fill="#C04000" rx="18" />
  <text x="270" y="559" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">户外跑步</text>

  <rect x="340" y="535" width="100" height="36" fill="#D2691E" rx="18" />
  <text x="390" y="559" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">日常通勤</text>

  <rect x="460" y="535" width="100" height="36" fill="#FF7F50" rx="18" />
  <text x="510" y="559" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">驾驶出行</text>

  <rect x="580" y="535" width="100" height="36" fill="#B87333" rx="18" />
  <text x="630" y="559" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" text-anchor="middle">休闲娱乐</text>

  <text x="100" y="600" font-family="Microsoft YaHei" font-size="16" fill="#333333">满足不同用户的多样化需求，一机多用</text>

  <!-- Footer -->
  <rect x="0" y="690" width="1280" height="30" fill="#FFF8F5" />
  <text x="40" y="710" font-family="Microsoft YaHei" font-size="12" fill="#999999">Smart Glasses</text>
  <text x="1240" y="710" font-family="Arial" font-size="14" fill="#666666" text-anchor="end">05</text>

  <!-- Huawei Logo in bottom right -->
  {huawei_logo_light}
</svg>'''
write_svg("05_功能应用.svg", content5_svg)

# ==================== 第6页: 与同类产品差异化优势 ====================
content6_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#FFFFFF" />

  <!-- Top Header Bar -->
  <rect x="0" y="0" width="1280" height="100" fill="#FFF8F5" />

  <!-- Red Accent Bar on Left -->
  <rect x="0" y="0" width="8" height="100" fill="#B71C1C" />

  <!-- Page Title -->
  <rect x="40" y="35" width="8" height="35" fill="#B71C1C" />
  <text x="65" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#B71C1C">与同类产品差异化优势</text>

  <!-- Title Underline -->
  <line x1="65" y1="85" x2="800" y2="85" stroke="#FFE5DC" stroke-width="1" />

  <!-- Right Side Header Info -->
  <text x="1240" y="60" font-family="Microsoft YaHei" font-size="14" fill="#999999" text-anchor="end">04</text>

  <!-- Advantage 1 -->
  <rect x="60" y="130" width="280" height="280" fill="#FFF5F0" rx="8" />
  <rect x="60" y="130" width="280" height="8" fill="#B71C1C" rx="4" />
  <circle cx="200" cy="210" r="50" fill="#B71C1C" fill-opacity="0.15" />
  <text x="200" y="220" font-family="Arial" font-size="36" font-weight="bold" fill="#B71C1C" text-anchor="middle">01</text>
  <text x="140" y="290" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C" text-anchor="middle">轻量化设计</text>
  <text x="140" y="330" font-family="Microsoft YaHei" font-size="36" font-weight="bold" fill="#B71C1C" text-anchor="middle">-20%</text>
  <text x="140" y="360" font-family="Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">比行业平均重量</text>
  <text x="140" y="385" font-family="Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">长期佩戴无负担</text>

  <!-- Advantage 2 -->
  <rect x="360" y="130" width="280" height="280" fill="#FFF5F0" rx="8" />
  <rect x="360" y="130" width="280" height="8" fill="#C04000" rx="4" />
  <circle cx="500" cy="210" r="50" fill="#C04000" fill-opacity="0.15" />
  <text x="500" y="220" font-family="Arial" font-size="36" font-weight="bold" fill="#C04000" text-anchor="middle">02</text>
  <text x="440" y="290" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C" text-anchor="middle">超长续航</text>
  <text x="440" y="330" font-family="Microsoft YaHei" font-size="36" font-weight="bold" fill="#C04000" text-anchor="middle">30min</text>
  <text x="440" y="360" font-family="Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">快充30分钟可用4小时</text>
  <text x="440" y="385" font-family="Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">支持快充技术</text>

  <!-- Advantage 3 -->
  <rect x="660" y="130" width="280" height="280" fill="#FFF5F0" rx="8" />
  <rect x="660" y="130" width="280" height="8" fill="#D2691E" rx="4" />
  <circle cx="800" cy="210" r="50" fill="#D2691E" fill-opacity="0.15" />
  <text x="800" y="220" font-family="Arial" font-size="36" font-weight="bold" fill="#D2691E" text-anchor="middle">03</text>
  <text x="740" y="290" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C" text-anchor="middle">智能交互</text>
  <text x="740" y="330" font-family="Microsoft YaHei" font-size="36" font-weight="bold" fill="#D2691E" text-anchor="middle">98%+</text>
  <text x="740" y="360" font-family="Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">语音识别准确率</text>
  <text x="740" y="385" font-family="Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">交互流畅自然</text>

  <!-- Advantage 4 -->
  <rect x="960" y="130" width="260" height="280" fill="#FFF5F0" rx="8" />
  <rect x="960" y="130" width="260" height="8" fill="#A0522D" rx="4" />
  <circle cx="1090" cy="210" r="50" fill="#A0522D" fill-opacity="0.15" />
  <text x="1090" y="220" font-family="Arial" font-size="36" font-weight="bold" fill="#A0522D" text-anchor="middle">04</text>
  <text x="1030" y="290" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C" text-anchor="middle">多场景适配</text>
  <text x="1030" y="330" font-family="Microsoft YaHei" font-size="36" font-weight="bold" fill="#A0522D" text-anchor="middle">∞</text>
  <text x="1030" y="360" font-family="Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">兼顾办公与运动</text>
  <text x="1030" y="385" font-family="Microsoft YaHei" font-size="14" fill="#666666" text-anchor="middle">性价比更高</text>

  <!-- Bottom Summary -->
  <rect x="60" y="440" width="1160" height="190" fill="#FFF5F0" rx="8" />
  <rect x="60" y="440" width="8" height="190" fill="#B71C1C" rx="4" />
  <text x="100" y="490" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#B71C1C">四大核心优势 · 全面领先</text>
  <text x="100" y="530" font-family="Microsoft YaHei" font-size="16" fill="#333333">• 轻量化设计 — 佩戴舒适无负担</text>
  <text x="100" y="560" font-family="Microsoft YaHei" font-size="16" fill="#333333">• 超长续航 — 30分钟快充可用4小时</text>
  <text x="100" y="590" font-family="Microsoft YaHei" font-size="16" fill="#333333">• 智能交互 — 语音识别准确率98%+</text>
  <text x="640" y="530" font-family="Microsoft YaHei" font-size="16" fill="#333333">• 多场景适配 — 办公运动两相宜</text>

  <!-- Footer -->
  <rect x="0" y="690" width="1280" height="30" fill="#FFF8F5" />
  <text x="40" y="710" font-family="Microsoft YaHei" font-size="12" fill="#999999">Smart Glasses</text>
  <text x="1240" y="710" font-family="Arial" font-size="14" fill="#666666" text-anchor="end">06</text>

  <!-- Huawei Logo in bottom right -->
  {huawei_logo_light}
</svg>'''
write_svg("06_差异化优势.svg", content6_svg)

# ==================== 第7页: 用户体验反馈与案例 ====================
content7_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#FFFFFF" />

  <!-- Top Header Bar -->
  <rect x="0" y="0" width="1280" height="100" fill="#FFF8F5" />

  <!-- Red Accent Bar on Left -->
  <rect x="0" y="0" width="8" height="100" fill="#B71C1C" />

  <!-- Page Title -->
  <rect x="40" y="35" width="8" height="35" fill="#B71C1C" />
  <text x="65" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#B71C1C">用户体验反馈与案例</text>

  <!-- Title Underline -->
  <line x1="65" y1="85" x2="800" y2="85" stroke="#FFE5DC" stroke-width="1" />

  <!-- Right Side Header Info -->
  <text x="1240" y="60" font-family="Microsoft YaHei" font-size="14" fill="#999999" text-anchor="end">05</text>

  <!-- Stats Section -->
  <rect x="60" y="130" width="380" height="180" fill="#B71C1C" rx="8" />
  <text x="250" y="190" font-family="Arial" font-size="64" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1000+</text>
  <text x="250" y="235" font-family="Microsoft YaHei" font-size="18" fill="#FFFFFF" text-anchor="middle">用户实测</text>
  <text x="250" y="275" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" fill-opacity="0.8" text-anchor="middle">经过大规模真实用户测试</text>

  <rect x="460" y="130" width="380" height="180" fill="#C04000" rx="8" />
  <text x="650" y="190" font-family="Arial" font-size="64" font-weight="bold" fill="#FFFFFF" text-anchor="middle">95%</text>
  <text x="650" y="235" font-family="Microsoft YaHei" font-size="18" fill="#FFFFFF" text-anchor="middle">用户满意度</text>
  <text x="650" y="275" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" fill-opacity="0.8" text-anchor="middle">远超行业平均水平</text>

  <rect x="860" y="130" width="360" height="180" fill="#D2691E" rx="8" />
  <text x="1040" y="190" font-family="Arial" font-size="64" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4.8</text>
  <text x="1040" y="235" font-family="Microsoft YaHei" font-size="18" fill="#FFFFFF" text-anchor="middle">综合评分</text>
  <text x="1040" y="275" font-family="Microsoft YaHei" font-size="14" fill="#FFFFFF" fill-opacity="0.8" text-anchor="middle">应用商店用户评价</text>

  <!-- User Feedback -->
  <rect x="60" y="340" width="560" height="200" fill="#FFF5F0" rx="8" />
  <rect x="60" y="340" width="8" height="200" fill="#B71C1C" rx="4" />
  <text x="95" y="380" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">用户好评</text>
  <text x="95" y="420" font-family="Microsoft YaHei" font-size="14" fill="#333333">"佩戴非常舒适，长时间使用也不觉得累"</text>
  <text x="95" y="450" font-family="Microsoft YaHei" font-size="14" fill="#333333">"操作便捷，语音控制反应很快"</text>
  <text x="95" y="480" font-family="Microsoft YaHei" font-size="14" fill="#333333">"导航和办公辅助功能特别实用"</text>
  <text x="95" y="515" font-family="Microsoft YaHei" font-size="12" fill="#666666">— 来自应用商店用户评价</text>

  <!-- Case Studies -->
  <rect x="660" y="340" width="560" height="200" fill="#FFF5F0" rx="8" />
  <rect x="660" y="340" width="8" height="200" fill="#C04000" rx="4" />
  <text x="695" y="380" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">典型案例</text>
  <text x="695" y="420" font-family="Microsoft YaHei" font-size="14" fill="#333333">🏢 职场用户通过眼镜快速预览会议文档</text>
  <text x="695" y="450" font-family="Microsoft YaHei" font-size="14" fill="#333333">🏃 运动爱好者实时查看心率数据</text>
  <text x="695" y="480" font-family="Microsoft YaHei" font-size="14" fill="#333333">🚗 通勤族利用导航功能安全出行</text>
  <text x="695" y="515" font-family="Microsoft YaHei" font-size="12" fill="#666666">有效提升使用效率与体验感</text>

  <!-- Bottom Quote -->
  <rect x="60" y="560" width="1160" height="100" fill="#FFF5F0" rx="8" />
  <rect x="60" y="560" width="8" height="100" fill="#D2691E" rx="4" />
  <text x="100" y="605" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#B71C1C">口碑反响良好</text>
  <text x="100" y="635" font-family="Microsoft YaHei" font-size="14" fill="#333333">用户体验反馈与案例充分证明了产品的实用性和可靠性</text>

  <!-- Footer -->
  <rect x="0" y="690" width="1280" height="30" fill="#FFF8F5" />
  <text x="40" y="710" font-family="Microsoft YaHei" font-size="12" fill="#999999">Smart Glasses</text>
  <text x="1240" y="710" font-family="Arial" font-size="14" fill="#666666" text-anchor="end">07</text>

  <!-- Huawei Logo in bottom right -->
  {huawei_logo_light}
</svg>'''
write_svg("07_用户体验.svg", content7_svg)

# ==================== 第8页: 未来规划与总结 ====================
content8_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="#FFFFFF" />

  <!-- Top Header Bar -->
  <rect x="0" y="0" width="1280" height="100" fill="#FFF8F5" />

  <!-- Red Accent Bar on Left -->
  <rect x="0" y="0" width="8" height="100" fill="#B71C1C" />

  <!-- Page Title -->
  <rect x="40" y="35" width="8" height="35" fill="#B71C1C" />
  <text x="65" y="65" font-family="Microsoft YaHei" font-size="32" font-weight="bold" fill="#B71C1C">未来规划与总结</text>

  <!-- Title Underline -->
  <line x1="65" y1="85" x2="800" y2="85" stroke="#FFE5DC" stroke-width="1" />

  <!-- Right Side Header Info -->
  <text x="1240" y="60" font-family="Microsoft YaHei" font-size="14" fill="#999999" text-anchor="end">06</text>

  <!-- Summary Section -->
  <rect x="60" y="130" width="560" height="260" fill="#FFF5F0" rx="8" />
  <rect x="60" y="130" width="8" height="260" fill="#B71C1C" rx="4" />
  <text x="95" y="175" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#B71C1C">产品总结</text>
  <text x="95" y="220" font-family="Microsoft YaHei" font-size="16" fill="#333333">以优质硬件、丰富功能、高适配性</text>
  <text x="95" y="255" font-family="Microsoft YaHei" font-size="16" fill="#333333">打破传统穿戴设备局限</text>
  <text x="95" y="290" font-family="Microsoft YaHei" font-size="16" fill="#333333">为用户提供更便捷、智能的生活方式</text>
  <text x="95" y="340" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#C04000">核心竞争力</text>
  <text x="95" y="375" font-family="Microsoft YaHei" font-size="14" fill="#333333">✓ 优质硬件配置</text>
  <text x="95" y="400" font-family="Microsoft YaHei" font-size="14" fill="#333333">✓ 丰富功能应用</text>

  <!-- Future Plans -->
  <rect x="660" y="130" width="560" height="260" fill="#FFF5F0" rx="8" />
  <rect x="660" y="130" width="8" height="260" fill="#C04000" rx="4" />
  <text x="695" y="175" font-family="Microsoft YaHei" font-size="22" font-weight="bold" fill="#B71C1C">未来规划</text>
  <text x="695" y="220" font-family="Microsoft YaHei" font-size="16" fill="#333333">持续优化交互体验</text>
  <text x="695" y="255" font-family="Microsoft YaHei" font-size="16" fill="#333333">新增健康监测功能</text>
  <text x="695" y="290" font-family="Microsoft YaHei" font-size="16" fill="#333333">引入AR增强现实技术</text>
  <text x="695" y="325" font-family="Microsoft YaHei" font-size="16" fill="#333333">拓展更多行业应用场景</text>
  <text x="695" y="365" font-family="Microsoft YaHei" font-size="18" font-weight="bold" fill="#C04000">愿景目标</text>
  <text x="695" y="395" font-family="Microsoft YaHei" font-size="14" fill="#333333">打造最具竞争力的智能穿戴产品</text>

  <!-- Roadmap -->
  <rect x="60" y="420" width="1160" height="200" fill="#FFF5F0" rx="8" />
  <rect x="60" y="420" width="8" height="200" fill="#B71C1C" rx="4" />
  <text x="100" y="470" font-family="Microsoft YaHei" font-size="20" font-weight="bold" fill="#B71C1C">发展路线图</text>

  <!-- Timeline -->
  <line x1="150" y1="540" x2="1130" y2="540" stroke="#FFE5DC" stroke-width="2" />

  <!-- Point 1 -->
  <circle cx="250" cy="540" r="12" fill="#B71C1C" />
  <text x="250" y="580" font-family="Microsoft YaHei" font-size="14" fill="#B71C1C" text-anchor="middle">2026 Q2</text>
  <text x="250" y="600" font-family="Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">健康监测</text>

  <!-- Point 2 -->
  <circle cx="500" cy="540" r="12" fill="#C04000" />
  <text x="500" y="580" font-family="Microsoft YaHei" font-size="14" fill="#C04000" text-anchor="middle">2026 Q3</text>
  <text x="500" y="600" font-family="Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">AR增强</text>

  <!-- Point 3 -->
  <circle cx="750" cy="540" r="12" fill="#D2691E" />
  <text x="750" y="580" font-family="Microsoft YaHei" font-size="14" fill="#D2691E" text-anchor="middle">2026 Q4</text>
  <text x="750" y="600" font-family="Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">行业应用</text>

  <!-- Point 4 -->
  <circle cx="1000" cy="540" r="12" fill="#A0522D" />
  <text x="1000" y="580" font-family="Microsoft YaHei" font-size="14" fill="#A0522D" text-anchor="middle">2027</text>
  <text x="1000" y="600" font-family="Microsoft YaHei" font-size="12" fill="#666666" text-anchor="middle">生态完善</text>

  <!-- Footer -->
  <rect x="0" y="690" width="1280" height="30" fill="#FFF8F5" />
  <text x="40" y="710" font-family="Microsoft YaHei" font-size="12" fill="#999999">Smart Glasses</text>
  <text x="1240" y="710" font-family="Arial" font-size="14" fill="#666666" text-anchor="end">08</text>

  <!-- Huawei Logo in bottom right -->
  {huawei_logo_light}
</svg>'''
write_svg("08_未来规划.svg", content8_svg)

# ==================== 第9页: 结束页 ====================
ending_svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
  <defs>
    <linearGradient id="endingGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#B71C1C;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#C04000;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#FFD23F;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FFDB58;stop-opacity:0.8" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect x="0" y="0" width="1280" height="720" fill="url(#endingGradient)" />

  <!-- Top White Accent Line -->
  <rect x="0" y="0" width="1280" height="6" fill="#FFFFFF" />

  <!-- Geometric Decorations -->
  <circle cx="-150" cy="750" r="450" fill="#FFFFFF" fill-opacity="0.1" />
  <circle cx="1350" cy="-50" r="300" fill="#FFFFFF" fill-opacity="0.1" />
  <circle cx="200" cy="100" r="100" fill="#FFD23F" fill-opacity="0.15" />
  <circle cx="1100" cy="650" r="150" fill="#FF7F50" fill-opacity="0.1" />
  <circle cx="300" cy="600" r="80" fill="#D2691E" fill-opacity="0.08" />

  <!-- Thank You Text -->
  <text x="640" y="260" font-family="Microsoft YaHei" font-size="64" font-weight="bold" fill="#FFFFFF" text-anchor="middle">感谢观看</text>

  <!-- Accent Line -->
  <rect x="520" y="295" width="240" height="4" fill="url(#accentGradient)" />

  <!-- Main Slogan -->
  <text x="640" y="370" font-family="Microsoft YaHei" font-size="28" fill="#FFFFFF" fill-opacity="0.95" text-anchor="middle">智启未来，镜观世界</text>

  <!-- Product Name -->
  <text x="640" y="420" font-family="Microsoft YaHei" font-size="22" fill="#FFD23F" text-anchor="middle">XX智能眼镜，伴你每一步</text>

  <!-- Divider Line -->
  <line x1="440" y1="470" x2="840" y2="470" stroke="#FFFFFF" stroke-width="1" stroke-opacity="0.3" />

  <!-- Contact Information -->
  <text x="640" y="520" font-family="Microsoft YaHei" font-size="16" fill="#FFFFFF" fill-opacity="0.9" text-anchor="middle">咨询电话：400-XXX-XXXX</text>
  <text x="640" y="550" font-family="Microsoft YaHei" font-size="16" fill="#FFFFFF" fill-opacity="0.9" text-anchor="middle">官方网站：www.example.com</text>

  <!-- Bottom Decorative Elements -->
  <rect x="0" y="640" width="1280" height="80" fill="#FFFFFF" fill-opacity="0.1" />
  <rect x="0" y="680" width="1280" height="40" fill="#FFFFFF" fill-opacity="0.2" />
  <rect x="0" y="680" width="200" height="40" fill="#FFD23F" fill-opacity="0.6" />

  <!-- Geometric Accent -->
  <rect x="1080" y="600" width="80" height="80" fill="none" stroke="#FFFFFF" stroke-width="1" stroke-opacity="0.2" rx="4" />
  <rect x="1100" y="620" width="40" height="40" fill="#FFD23F" fill-opacity="0.4" />

  <rect x="120" y="600" width="80" height="80" fill="none" stroke="#FFFFFF" stroke-width="1" stroke-opacity="0.2" rx="4" />
  <rect x="140" y="620" width="40" height="40" fill="#FFD23F" fill-opacity="0.4" />

  <!-- Huawei Logo in bottom right (white for dark background) -->
  {huawei_logo_dark}
</svg>'''
write_svg("09_结束页.svg", ending_svg)

print("\nAll 9 SVG pages created with Huawei warm color scheme and logo!")
