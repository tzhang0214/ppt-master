# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil

# Find project directory
base = r'd:/projects/aiprojects/ppt-master/projects'
skill_dir = r'd:/projects/aiprojects/ppt-master/skills/ppt-master'
project_path = None

for d in os.listdir(base):
    if 'ppt169_20260329' in d:
        svg_dir = os.path.join(base, d, 'svg_output')
        if os.path.exists(svg_dir) and len([f for f in os.listdir(svg_dir) if f.endswith('.svg')]) == 9:
            project_path = os.path.join(base, d)
            break

if not project_path:
    print("Error: Project not found")
    sys.exit(1)

print(f"Project path: {project_path}")

# Run post-processing steps
scripts = [
    ('total_md_split.py', 'Splitting notes'),
    ('finalize_svg.py', 'Finalizing SVG'),
    ('svg_to_pptx.py', 'Exporting to PPTX'),
]

for script_name, desc in scripts:
    script_path = os.path.join(skill_dir, 'scripts', script_name)
    cmd = ['python', script_path, project_path]
    if script_name == 'svg_to_pptx.py':
        cmd.extend(['-s', 'final'])
    
    print(f"\n{desc}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{desc} - SUCCESS")
        if result.stdout:
            print(result.stdout[:500])
    else:
        print(f"{desc} - ERROR")
        print(result.stderr[:500])

print("\nDone!")
