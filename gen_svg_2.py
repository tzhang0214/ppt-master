# -*- coding: utf-8 -*-
import os

project_path = r'd:/projects/aiprojects/ppt-master/projects/ai_glasses_ppt/svg_output'
os.makedirs(project_path, exist_ok=True)

# Page 4: Core Technologies
svg4 = '''<?xml version="1.0" encoding="UTF-8"?>
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
    <text x="60" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="500" fill="#1565C0" letter-spacing="2">02 / 核心技术解析</text>
    <text x="60" y="100" font-family="Microsoft YaHei, Arial, sans-serif" font-size="32" font-weight="bold" fill="#1A1A2E">核心技术解析</text>
    
    <!-- Three cards -->
    <!-- Card 1: Computer Vision -->
    <g transform="translate(60, 140)">
        <rect x="0" y="0" width="360" height="460" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="360" height="6" fill="#1565C0" rx="3"/>
        <circle cx="100" cy="100" r="50" fill="#1565C0" fill-opacity="0.1"/>
        <text x="100" y="108" text-anchor="middle" font-family="Arial, sans-serif" font-size="36" fill="#1565C0">👁</text>
        <text x="30" y="180" font-family="Microsoft YaHei, Arial, sans-serif" font-size="22" font-weight="bold" fill="#1F2937">计算机视觉</text>
        <text x="30" y="210" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Computer Vision</text>
        <line x1="30" y1="235" x2="120" y2="235" stroke="#1565C0" stroke-width="3"/>
        <text x="30" y="275" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">赋予眼镜"看"的能力</text>
        <text x="30" y="305" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#6B7280">
            <tspan x="30" dy="0">实现物体识别、人脸识别、</tspan>
            <tspan x="30" dy="22">文字识别等功能</tspan>
        </text>
        <g transform="translate(30, 360)">
            <rect x="0" y="0" width="90" height="28" fill="#1565C0" fill-opacity="0.1" rx="14"/>
            <text x="45" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#1565C0" text-anchor="middle">物体识别</text>
            <rect x="100" y="0" width="90" height="28" fill="#1565C0" fill-opacity="0.1" rx="14"/>
            <text x="145" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#1565C0" text-anchor="middle">人脸识别</text>
            <rect x="200" y="0" width="90" height="28" fill="#1565C0" fill-opacity="0.1" rx="14"/>
            <text x="245" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#1565C0" text-anchor="middle">文字识别</text>
        </g>
    </g>
    
    <!-- Card 2: NLP -->
    <g transform="translate(460, 140)">
        <rect x="0" y="0" width="360" height="460" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="360" height="6" fill="#00D4FF" rx="3"/>
        <circle cx="100" cy="100" r="50" fill="#00D4FF" fill-opacity="0.1"/>
        <text x="100" y="108" text-anchor="middle" font-family="Arial, sans-serif" font-size="36" fill="#00D4FF">💬</text>
        <text x="30" y="180" font-family="Microsoft YaHei, Arial, sans-serif" font-size="22" font-weight="bold" fill="#1F2937">自然语言处理</text>
        <text x="30" y="210" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Natural Language Processing</text>
        <line x1="30" y1="235" x2="120" y2="235" stroke="#00D4FF" stroke-width="3"/>
        <text x="30" y="275" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">理解和处理人类语言</text>
        <text x="30" y="305" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#6B7280">
            <tspan x="30" dy="0">实现语音助手、实时翻译</tspan>
            <tspan x="30" dy="22">等功能</tspan>
        </text>
        <g transform="translate(30, 360)">
            <rect x="0" y="0" width="90" height="28" fill="#00D4FF" fill-opacity="0.1" rx="14"/>
            <text x="45" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#00D4FF" text-anchor="middle">语音助手</text>
            <rect x="100" y="0" width="90" height="28" fill="#00D4FF" fill-opacity="0.1" rx="14"/>
            <text x="145" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#00D4FF" text-anchor="middle">实时翻译</text>
            <rect x="200" y="0" width="90" height="28" fill="#00D4FF" fill-opacity="0.1" rx="14"/>
            <text x="245" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#00D4FF" text-anchor="middle">对话交互</text>
        </g>
    </g>
    
    <!-- Card 3: AR -->
    <g transform="translate(860, 140)">
        <rect x="0" y="0" width="360" height="460" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="360" height="6" fill="#7C3AED" rx="3"/>
        <circle cx="100" cy="100" r="50" fill="#7C3AED" fill-opacity="0.1"/>
        <text x="100" y="108" text-anchor="middle" font-family="Arial, sans-serif" font-size="36" fill="#7C3AED">🕶</text>
        <text x="30" y="180" font-family="Microsoft YaHei, Arial, sans-serif" font-size="22" font-weight="bold" fill="#1F2937">增强现实 (AR)</text>
        <text x="30" y="210" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Augmented Reality</text>
        <line x1="30" y1="235" x2="120" y2="235" stroke="#7C3AED" stroke-width="3"/>
        <text x="30" y="275" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">虚拟信息与现实融合</text>
        <text x="30" y="305" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#6B7280">
            <tspan x="30" dy="0">提供导航、数据可视化</tspan>
            <tspan x="30" dy="22">等服务</tspan>
        </text>
        <g transform="translate(30, 360)">
            <rect x="0" y="0" width="90" height="28" fill="#7C3AED" fill-opacity="0.1" rx="14"/>
            <text x="45" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#7C3AED" text-anchor="middle">导航</text>
            <rect x="100" y="0" width="90" height="28" fill="#7C3AED" fill-opacity="0.1" rx="14"/>
            <text x="145" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#7C3AED" text-anchor="middle">数据可视化</text>
            <rect x="200" y="0" width="90" height="28" fill="#7C3AED" fill-opacity="0.1" rx="14"/>
            <text x="245" y="18" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#7C3AED" text-anchor="middle">3D叠加</text>
        </g>
    </g>
    
    <text x="640" y="695" font-family="Arial, sans-serif" font-size="14" fill="#64748B" text-anchor="middle">4 / 7</text>
</svg>'''

with open(os.path.join(project_path, '04_tech.svg'), 'w', encoding='utf-8') as f:
    f.write(svg4)
print('Created 04_tech.svg')

# Page 5: Applications
svg5 = '''<?xml version="1.0" encoding="UTF-8"?>
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
    <text x="60" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="500" fill="#1565C0" letter-spacing="2">03 / 多元应用场景</text>
    <text x="60" y="100" font-family="Microsoft YaHei, Arial, sans-serif" font-size="32" font-weight="bold" fill="#1A1A2E">多元应用场景</text>
    
    <!-- Four quadrant grid -->
    <!-- Industrial -->
    <g transform="translate(60, 140)">
        <rect x="0" y="0" width="550" height="250" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="550" height="6" fill="#1565C0" rx="3"/>
        <circle cx="70" cy="80" r="40" fill="#1565C0" fill-opacity="0.1"/>
        <text x="70" y="90" text-anchor="middle" font-family="Arial, sans-serif" font-size="32" fill="#1565C0">🔧</text>
        <text x="130" y="70" font-family="Microsoft YaHei, Arial, sans-serif" font-size="22" font-weight="bold" fill="#1F2937">工业维修</text>
        <text x="130" y="95" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Industrial Maintenance</text>
        <line x1="30" y1="130" x2="100" y2="130" stroke="#1565C0" stroke-width="2"/>
        <text x="30" y="160" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">远程专家指导</text>
        <text x="30" y="190" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#9CA3AF">提升维修效率，降低停机时间</text>
        <rect x="30" y="210" width="120" height="28" fill="#10B981" fill-opacity="0.1" rx="14"/>
        <text x="90" y="228" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#10B981" text-anchor="middle">效率提升 40%</text>
    </g>
    
    <!-- Healthcare -->
    <g transform="translate(670, 140)">
        <rect x="0" y="0" width="550" height="250" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="550" height="6" fill="#EF4444" rx="3"/>
        <circle cx="70" cy="80" r="40" fill="#EF4444" fill-opacity="0.1"/>
        <text x="70" y="90" text-anchor="middle" font-family="Arial, sans-serif" font-size="32" fill="#EF4444">🏥</text>
        <text x="130" y="70" font-family="Microsoft YaHei, Arial, sans-serif" font-size="22" font-weight="bold" fill="#1F2937">医疗健康</text>
        <text x="130" y="95" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Healthcare</text>
        <line x1="30" y1="130" x2="100" y2="130" stroke="#EF4444" stroke-width="2"/>
        <text x="30" y="160" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">手术导航、实时监测</text>
        <text x="30" y="190" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#9CA3AF">实时生命体征监测，辅助精准医疗</text>
        <rect x="30" y="210" width="120" height="28" fill="#EF4444" fill-opacity="0.1" rx="14"/>
        <text x="90" y="228" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#EF4444" text-anchor="middle">精准度 99%</text>
    </g>
    
    <!-- Education -->
    <g transform="translate(60, 420)">
        <rect x="0" y="0" width="550" height="250" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="550" height="6" fill="#F59E0B" rx="3"/>
        <circle cx="70" cy="80" r="40" fill="#F59E0B" fill-opacity="0.1"/>
        <text x="70" y="90" text-anchor="middle" font-family="Arial, sans-serif" font-size="32" fill="#F59E0B">📚</text>
        <text x="130" y="70" font-family="Microsoft YaHei, Arial, sans-serif" font-size="22" font-weight="bold" fill="#1F2937">教育学习</text>
        <text x="130" y="95" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Education</text>
        <line x1="30" y1="130" x2="100" y2="130" stroke="#F59E0B" stroke-width="2"/>
        <text x="30" y="160" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">沉浸式学习体验</text>
        <text x="30" y="190" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#9CA3AF">实时信息获取，知识触手可及</text>
        <rect x="30" y="210" width="120" height="28" fill="#F59E0B" fill-opacity="0.1" rx="14"/>
        <text x="90" y="228" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#F59E0B" text-anchor="middle">学习效率 +60%</text>
    </g>
    
    <!-- Daily Life -->
    <g transform="translate(670, 420)">
        <rect x="0" y="0" width="550" height="250" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="550" height="6" fill="#10B981" rx="3"/>
        <circle cx="70" cy="80" r="40" fill="#10B981" fill-opacity="0.1"/>
        <text x="70" y="90" text-anchor="middle" font-family="Arial, sans-serif" font-size="32" fill="#10B981">🌍</text>
        <text x="130" y="70" font-family="Microsoft YaHei, Arial, sans-serif" font-size="22" font-weight="bold" fill="#1F2937">日常生活</text>
        <text x="130" y="95" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Daily Life</text>
        <line x1="30" y1="130" x2="100" y2="130" stroke="#10B981" stroke-width="2"/>
        <text x="30" y="160" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">智能导航、语言翻译</text>
        <text x="30" y="190" font-family="Microsoft YaHei, Arial, sans-serif" font-size="15" fill="#9CA3AF">拍照录像，生活记录无负担</text>
        <rect x="30" y="210" width="120" height="28" fill="#10B981" fill-opacity="0.1" rx="14"/>
        <text x="90" y="228" font-family="Microsoft YaHei, sans-serif" font-size="12" fill="#10B981" text-anchor="middle">便捷度 +80%</text>
    </g>
    
    <text x="640" y="695" font-family="Arial, sans-serif" font-size="14" fill="#64748B" text-anchor="middle">5 / 7</text>
</svg>'''

with open(os.path.join(project_path, '05_applications.svg'), 'w', encoding='utf-8') as f:
    f.write(svg5)
print('Created 05_applications.svg')

# Page 6: Future Outlook
svg6 = '''<?xml version="1.0" encoding="UTF-8"?>
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
        <linearGradient id="futureGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#1565C0" stop-opacity="0.1"/>
            <stop offset="100%" stop-color="#00D4FF" stop-opacity="0.1"/>
        </linearGradient>
    </defs>
    <rect width="1280" height="720" fill="#FFFFFF"/>
    <rect x="0" y="0" width="1280" height="6" fill="url(#accentGradient)"/>
    <text x="60" y="50" font-family="Arial, sans-serif" font-size="14" font-weight="500" fill="#1565C0" letter-spacing="2">04 / 未来发展展望</text>
    <text x="60" y="100" font-family="Microsoft YaHei, Arial, sans-serif" font-size="32" font-weight="bold" fill="#1A1A2E">未来发展展望</text>
    
    <!-- Timeline style -->
    <line x1="200" y1="250" x2="200" y2="550" stroke="#E5E7EB" stroke-width="3"/>
    <circle cx="200" cy="250" r="12" fill="#1565C0"/>
    <circle cx="200" cy="400" r="12" fill="#00D4FF"/>
    <circle cx="200" cy="550" r="12" fill="#7C3AED"/>
    
    <!-- Card 1: Lighter Design -->
    <g transform="translate(260, 180)">
        <rect x="0" y="0" width="900" height="140" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="900" height="6" fill="#1565C0" rx="3"/>
        <text x="40" y="50" font-family="Microsoft YaHei, Arial, sans-serif" font-size="24" font-weight="bold" fill="#1F2937">更轻薄的设计</text>
        <text x="40" y="80" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Lighter &amp; Thinner Design</text>
        <line x1="40" y1="100" x2="150" y2="100" stroke="#1565C0" stroke-width="2"/>
        <text x="40" y="125" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">接近普通眼镜的外观，提升佩戴舒适度</text>
        <g transform="translate(700, 30)">
            <text x="0" y="30" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#1565C0">-50%</text>
            <text x="0" y="60" font-family="Microsoft YaHei, sans-serif" font-size="14" fill="#9CA3AF">重量减少</text>
        </g>
    </g>
    
    <!-- Card 2: Stronger AI -->
    <g transform="translate(260, 330)">
        <rect x="0" y="0" width="900" height="140" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="900" height="6" fill="#00D4FF" rx="3"/>
        <text x="40" y="50" font-family="Microsoft YaHei, Arial, sans-serif" font-size="24" font-weight="bold" fill="#1F2937">更强的 AI 能力</text>
        <text x="40" y="80" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Enhanced AI Capabilities</text>
        <line x1="40" y1="100" x2="150" y2="100" stroke="#00D4FF" stroke-width="2"/>
        <text x="40" y="125" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">更智能的交互，更精准的识别与分析</text>
        <g transform="translate(700, 30)">
            <text x="0" y="30" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#00D4FF">3x</text>
            <text x="0" y="60" font-family="Microsoft YaHei, sans-serif" font-size="14" fill="#9CA3AF">AI性能提升</text>
        </g>
    </g>
    
    <!-- Card 3: Broader Ecosystem -->
    <g transform="translate(260, 480)">
        <rect x="0" y="0" width="900" height="140" fill="url(#cardGradient)" stroke="#E5E7EB" stroke-width="1" rx="12"/>
        <rect x="0" y="0" width="900" height="6" fill="#7C3AED" rx="3"/>
        <text x="40" y="50" font-family="Microsoft YaHei, Arial, sans-serif" font-size="24" font-weight="bold" fill="#1F2937">更广泛的应用生态</text>
        <text x="40" y="80" font-family="Microsoft YaHei, Arial, sans-serif" font-size="14" fill="#9CA3AF">Broader Application Ecosystem</text>
        <line x1="40" y1="100" x2="180" y2="100" stroke="#7C3AED" stroke-width="2"/>
        <text x="40" y="125" font-family="Microsoft YaHei, Arial, sans-serif" font-size="16" fill="#6B7280">与更多智能设备和服务无缝连接</text>
        <g transform="translate(700, 30)">
            <text x="0" y="30" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#7C3AED">100+</text>
            <text x="0" y="60" font-family="Microsoft YaHei, sans-serif" font-size="14" fill="#9CA3AF">生态伙伴</text>
        </g>
    </g>
    
    <text x="640" y="695" font-family="Arial, sans-serif" font-size="14" fill="#64748B" text-anchor="middle">6 / 7</text>
</svg>'''

with open(os.path.join(project_path, '06_future.svg'), 'w', encoding='utf-8') as f:
    f.write(svg6)
print('Created 06_future.svg')

# Page 7: Thank You
svg7 = '''<?xml version="1.0" encoding="UTF-8"?>
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
    <ellipse cx="300" cy="200" rx="250" ry="180" fill="url(#glowBlue)"/>
    <ellipse cx="980" cy="500" rx="280" ry="200" fill="url(#glowCyan)"/>
    <g stroke="#00D4FF" stroke-opacity="0.3" stroke-width="1" fill="none">
        <path d="M150,150 Q250,100 350,180"/>
        <path d="M350,180 Q420,250 380,320"/>
        <path d="M950,400 Q1050,350 1100,420"/>
        <path d="M1100,420 Q1150,500 1080,550"/>
    </g>
    <g fill="#00D4FF" fill-opacity="0.5">
        <circle cx="150" cy="150" r="5"/>
        <circle cx="350" cy="180" r="7"/>
        <circle cx="380" cy="320" r="4"/>
    </g>
    <g fill="#1565C0" fill-opacity="0.6">
        <circle cx="950" cy="400" r="6"/>
        <circle cx="1100" cy="420" r="8"/>
        <circle cx="1080" cy="550" r="5"/>
    </g>
    <text x="640" y="240" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="500" fill="#1565C0" letter-spacing="3">THANK YOU</text>
    <text x="640" y="320" text-anchor="middle" font-family="Microsoft YaHei, Arial, sans-serif" font-size="52" font-weight="bold" fill="#FFFFFF">感谢聆听</text>
    <rect x="540" y="360" width="200" height="3" fill="url(#accentGradient)" rx="1.5"/>
    <text x="640" y="420" text-anchor="middle" font-family="Microsoft YaHei, Arial, sans-serif" font-size="24" fill="#FFFFFF" fill-opacity="0.7">Q&amp;A</text>
    <rect x="440" y="480" width="400" height="100" fill="#FFFFFF" fill-opacity="0.05" stroke="#FFFFFF" stroke-opacity="0.1" stroke-width="1" rx="12"/>
    <text x="640" y="520" text-anchor="middle" font-family="Microsoft YaHei, Arial, sans-serif" font-size="18" font-weight="bold" fill="#FFFFFF">开启您的 AI 视界之旅</text>
    <text x="640" y="555" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#FFFFFF" fill-opacity="0.6">探索 AI 智能眼镜的无限可能</text>
    <rect x="60" y="640" width="1160" height="1" fill="#FFFFFF" fill-opacity="0.1"/>
    <text x="60" y="680" font-family="Arial, sans-serif" font-size="14" fill="#64748B">2026-03-29</text>
    <text x="1220" y="680" text-anchor="end" font-family="Arial, sans-serif" font-size="14" fill="#64748B">PPT Master</text>
</svg>'''

with open(os.path.join(project_path, '07_ending.svg'), 'w', encoding='utf-8') as f:
    f.write(svg7)
print('Created 07_ending.svg')

print('Pages 4-7 created successfully!')
