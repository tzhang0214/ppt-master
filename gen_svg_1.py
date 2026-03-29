# -*- coding: utf-8 -*-
import os

project_path = r'd:/projects/aiprojects/ppt-master/projects/ai_glasses_ppt/svg_output'
os.makedirs(project_path, exist_ok=True)

# Page 1: Cover
svg1 = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <defs>
        <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0D1117"/>
            <stop offset="50%" stop-color="#16213E"/>
            <stop offset="100%" stop-color="#0F0F1A"/>
        </linearGradient>
        <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#1565C0"/>
            <stop offset="100%" stop-color="#00D4FF"/>
        </linearGradient>
        <radialGradient id="glowBlue" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.2"/>
            <stop offset="100%" stop-color="#00D4FF" stop-opacity="0"/>
        </radialGradient>
        <radialGradient id="glowCyan" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#1565C0" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#1565C0" stop-opacity="0"/>
        </radialGradient>
    </defs>
    <rect width="1280" height="720" fill="url(#bgGradient)"/>
    <g stroke="#FFFFFF" stroke-opacity="0.03" stroke-width="1">
        <line x1="0" y1="180" x2="1280" y2="180"/>
        <line x1="0" y1="360" x2="1280" y2="360"/>
        <line x1="0" y1="540" x2="1280" y2="540"/>
        <line x1="320" y1="0" x2="320" y2="720"/>
        <line x1="640" y1="0" x2="640" y2="720"/>
        <line x1="960" y1="0" x2="960" y2="720"/>
    </g>
    <ellipse cx="1000" cy="200" rx="350" ry="250" fill="url(#glowBlue)"/>
    <ellipse cx="280" cy="500" rx="300" ry="200" fill="url(#glowCyan)"/>
    <g stroke="#00D4FF" stroke-opacity="0.4" stroke-width="1" fill="none">
        <path d="M100,200 Q250,150 350,220"/>
        <path d="M350,220 Q450,280 500,200"/>
        <path d="M800,500 Q900,450 1000,500"/>
        <path d="M1000,500 Q1100,550 1150,480"/>
    </g>
    <g fill="#00D4FF" fill-opacity="0.6">
        <circle cx="100" cy="200" r="4"/>
        <circle cx="350" cy="220" r="6"/>
        <circle cx="500" cy="200" r="4"/>
        <circle cx="800" cy="500" r="5"/>
        <circle cx="1000" cy="500" r="7"/>
    </g>
    <g fill="#1565C0" fill-opacity="0.7">
        <circle cx="950" cy="180" r="8"/>
        <circle cx="1150" cy="130" r="5"/>
        <circle cx="180" cy="500" r="6"/>
    </g>
    <rect x="60" y="60" width="80" height="4" fill="url(#accentGradient)" rx="2"/>
    <text x="640" y="280" font-family="Microsoft YaHei, Arial, sans-serif" font-size="52" font-weight="bold" fill="#FFFFFF" text-anchor="middle">AI 智能眼镜：开启未来视界</text>
    <text x="640" y="350" font-family="Microsoft YaHei, Arial, sans-serif" font-size="26" fill="#FFFFFF" fill-opacity="0.85" text-anchor="middle">科技与生活的无缝融合</text>
    <rect x="520" y="390" width="240" height="3" fill="url(#accentGradient)" rx="1.5"/>
    <text x="60" y="680" font-family="Arial, sans-serif" font-size="14" fill="#64748B">2026-03-29</text>
    <text x="1220" y="680" text-anchor="end" font-family="Arial, sans-serif" font-size="14" fill="#64748B">PPT Master</text>
</svg>'''

with open(os.path.join(project_path, '01_cover.svg'), 'w', encoding='utf-8') as f:
    f.write(svg1)
print('Created 01_cover.svg')

# Page 2: TOC
svg2 = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <defs>
        <linearGradient id="sideAccent" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1565C0"/>
            <stop offset="100%" stop-color="#00D4FF"/>
        </linearGradient>
    </defs>
    <rect width="1280" height="720" fill="#FFFFFF"/>
    <rect x="0" y="0" width="8" height="720" fill="url(#sideAccent)"/>
    <text x="60" y="55" font-family="Arial, sans-serif" font-size="14" font-weight="500" fill="#1565C0" letter-spacing="2">AGENDA</text>
    <text x="60" y="100" font-family="Microsoft YaHei, Arial, sans-serif" font-size="36" font-weight="bold" fill="#1A1A2E">目录</text>
    <line x1="60" y1="130" x2="300" y2="130" stroke="#E2E8F0" stroke-width="2"/>
    <g font-family="Microsoft YaHei, Arial, sans-serif">
        <g>
            <circle cx="90" cy="200" r="24" fill="#1565C0"/>
            <text x="90" y="207" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
            <text x="130" y="195" font-size="20" font-weight="600" fill="#1A1A2E">什么是 AI 智能眼镜？</text>
        </g>
        <g>
            <circle cx="90" cy="285" r="24" fill="#1565C0"/>
            <text x="90" y="292" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2</text>
            <text x="130" y="280" font-size="20" font-weight="600" fill="#1A1A2E">核心技术解析</text>
        </g>
        <g>
            <circle cx="90" cy="370" r="24" fill="#1565C0"/>
            <text x="90" y="377" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3</text>
            <text x="130" y="365" font-size="20" font-weight="600" fill="#1A1A2E">多元应用场景</text>
        </g>
        <g>
            <circle cx="90" cy="455" r="24" fill="#1565C0"/>
            <text x="90" y="462" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4</text>
            <text x="130" y="450" font-size="20" font-weight="600" fill="#1A1A2E">未来发展展望</text>
        </g>
    </g>
    <g transform="translate(850, 220)">
        <rect x="0" y="0" width="350" height="350" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1" rx="16"/>
        <rect x="40" y="40" width="270" height="60" fill="#00D4FF" fill-opacity="0.1" stroke="#00D4FF" stroke-width="2" rx="8"/>
        <text x="175" y="75" font-family="Arial, sans-serif" font-size="16" font-weight="600" fill="#00D4FF" text-anchor="middle">智能眼镜</text>
        <path d="M175,100 L175,130" stroke="#64748B" stroke-width="2" stroke-dasharray="4,2"/>
        <polygon points="175,140 170,130 180,130" fill="#64748B"/>
        <rect x="40" y="145" width="270" height="60" fill="#1565C0" fill-opacity="0.2" stroke="#1565C0" stroke-width="2" rx="8"/>
        <text x="175" y="180" font-family="Arial, sans-serif" font-size="16" font-weight="600" fill="#1565C0" text-anchor="middle">核心技术与AI</text>
        <path d="M175,205 L175,235" stroke="#64748B" stroke-width="2" stroke-dasharray="4,2"/>
        <polygon points="175,245 170,235 180,235" fill="#64748B"/>
        <rect x="40" y="250" width="270" height="60" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="2" rx="8"/>
        <text x="175" y="285" font-family="Arial, sans-serif" font-size="16" font-weight="600" fill="#7C3AED" text-anchor="middle">无限应用可能</text>
    </g>
    <text x="640" y="695" font-family="Arial, sans-serif" font-size="14" fill="#64748B" text-anchor="middle">2 / 7</text>
</svg>'''

with open(os.path.join(project_path, '02_toc.svg'), 'w', encoding='utf-8') as f:
    f.write(svg2)
print('Created 02_toc.svg')

# Page 3: What is AI Smart Glasses
svg3 = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">
    <defs>
        <linearGradient id="cardGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#FFFFFF"/>
            <stop offset="100%" stop-color="#F8FAFC"/>
        </linearGradient>
        <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#1565C0"/>
            <stop offset="100%" stop-color="#00D4FF"/>
        </linearGradient>
    </defs>
    <rect width="1280" height="720" fill="#FFFFFF"/>
    <rect x="0" y="0" width="1280" height="6" fill="url(#accentGradient)"/>
    <text x="60" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="500" fill="#1565C0" letter-spacing="2">01 / 什么是AI智能眼镜</text>
    <text x="60" y="100" font-family="Microsoft YaHei, Arial, sans-serif" font-size="32" font-weight="bold" fill="#1A1A2E">什么是 AI 智能眼镜？</text>
    
    <g transform="translate(60, 150)">
        <rect x="0" y="0" width="500" height="450" fill="#F3F4F6" stroke="#E5E7EB" stroke-width="1" rx="16"/>
        <g transform="translate(100, 80)">
            <ellipse cx="80" cy="100" rx="70" ry="45" fill="#1F2937" stroke="#1565C0" stroke-width="3"/>
            <ellipse cx="240" cy="100" rx="70" ry="45" fill="#1F2937" stroke="#1565C0" stroke-width="3"/>
            <path d="M150,100 L170,100" stroke="#1565C0" stroke-width="3"/>
            <path d="M10,100 L10,80" stroke="#1565C0" stroke-width="3"/>
            <path d="M310,100 L310,80" stroke="#1565C0" stroke-width="3"/>
            <ellipse cx="80" cy="100" rx="50" ry="30" fill="#00D4FF" fill-opacity="0.15"/>
            <ellipse cx="240" cy="100" rx="50" ry="30" fill="#00D4FF" fill-opacity="0.15"/>
            <text x="80" y="105" font-family="Arial, sans-serif" font-size="12" fill="#00D4FF" text-anchor="middle">AR</text>
            <text x="240" y="105" font-family="Arial, sans-serif" font-size="12" fill="#00D4FF" text-anchor="middle">AI</text>
        </g>
        <text x="250" y="280" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280" text-anchor="middle">AI智能眼镜示意图</text>
        <g transform="translate(40, 320)">
            <rect x="0" y="0" width="120" height="30" fill="#1565C0" fill-opacity="0.1" rx="15"/>
            <text x="60" y="20" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#1565C0" text-anchor="middle">实时识别</text>
            <rect x="140" y="0" width="120" height="30" fill="#00D4FF" fill-opacity="0.1" rx="15"/>
            <text x="200" y="20" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#00D4FF" text-anchor="middle">语音交互</text>
            <rect x="280" y="0" width="120" height="30" fill="#7C3AED" fill-opacity="0.1" rx="15"/>
            <text x="340" y="20" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#7C3AED" text-anchor="middle">AR显示</text>
        </g>
    </g>
    
    <g transform="translate(600, 150)">
        <rect x="0" y="0" width="600" height="450" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="16"/>
        <rect x="0" y="0" width="600" height="6" fill="#1565C0" rx="3"/>
        
        <g transform="translate(30, 40)">
            <circle cx="20" cy="20" r="20" fill="#1565C0" fill-opacity="0.1"/>
            <text x="20" y="26" font-family="Arial, sans-serif" font-size="16" fill="#1565C0" text-anchor="middle">1</text>
            <text x="60" y="20" font-family="Microsoft YaHei, Arial, sans-serif" font-size="18" font-weight="bold" fill="#1F2937">定义</text>
            <text x="60" y="50" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#6B7280">集成人工智能技术的可穿戴设备</text>
        </g>
        
        <line x1="30" y1="110" x2="570" y2="110" stroke="#E5E7EB" stroke-width="1"/>
        
        <g transform="translate(30, 130)">
            <circle cx="20" cy="20" r="20" fill="#00D4FF" fill-opacity="0.1"/>
            <text x="20" y="26" font-family="Arial, sans-serif" font-size="16" fill="#00D4FF" text-anchor="middle">2</text>
            <text x="60" y="20" font-family="Microsoft YaHei, Arial, sans-serif" font-size="18" font-weight="bold" fill="#1F2937">核心功能</text>
            <text x="60" y="50" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#6B7280">通过摄像头、传感器和AI芯片，</text>
            <text x="60" y="75" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#6B7280">实时捕捉分析环境信息，</text>
            <text x="60" y="100" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#6B7280">并将信息叠加在用户视野中</text>
        </g>
        
        <line x1="30" y1="250" x2="570" y2="250" stroke="#E5E7EB" stroke-width="1"/>
        
        <g transform="translate(30, 270)">
            <circle cx="20" cy="20" r="20" fill="#7C3AED" fill-opacity="0.1"/>
            <text x="20" y="26" font-family="Arial, sans-serif" font-size="16" fill="#7C3AED" text-anchor="middle">3</text>
            <text x="60" y="20" font-family="Microsoft YaHei, Arial, sans-serif" font-size="18" font-weight="bold" fill="#1F2937">交互方式</text>
            <text x="60" y="50" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#6B7280">支持语音、手势、触摸等多种交互方式</text>
            <g transform="translate(60, 70)">
                <rect x="0" y="0" width="80" height="28" fill="#7C3AED" fill-opacity="0.1" rx="14"/>
                <text x="40" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#7C3AED" text-anchor="middle">语音</text>
                <rect x="95" y="0" width="80" height="28" fill="#7C3AED" fill-opacity="0.1" rx="14"/>
                <text x="135" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#7C3AED" text-anchor="middle">手势</text>
                <rect x="190" y="0" width="80" height="28" fill="#7C3AED" fill-opacity="0.1" rx="14"/>
                <text x="230" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#7C3AED" text-anchor="middle">触摸</text>
            </g>
        </g>
    </g>
    
    <text x="640" y="695" font-family="Arial, sans-serif" font-size="14" fill="#64748B" text-anchor="middle">3 / 7</text>
</svg>'''

with open(os.path.join(project_path, '03_what_is.svg'), 'w', encoding='utf-8') as f:
    f.write(svg3)
print('Created 03_what_is.svg')

print('Pages 1-3 created successfully!')
