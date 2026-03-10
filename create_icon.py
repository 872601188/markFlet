#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
创建多尺寸 Windows ICO 图标
"""

from PIL import Image
import struct
import io

def create_ico():
    # 读取原始图片
    img = Image.open('assets/icon.png')
    
    # 确保是 RGBA 模式
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # 正方形裁剪
    size = min(img.size)
    left = (img.width - size) // 2
    top = (img.height - size) // 2
    img = img.crop((left, top, left + size, top + size))
    
    # 尺寸列表
    icon_sizes = [256, 128, 64, 48, 32, 16]
    
    # 准备每个尺寸的数据
    icon_data = []
    for s in icon_sizes:
        resized = img.resize((s, s), Image.Resampling.LANCZOS)
        
        # 保存为 PNG 格式（Windows Vista+ 支持）
        png_buffer = io.BytesIO()
        resized.save(png_buffer, format='PNG')
        png_bytes = png_buffer.getvalue()
        
        icon_data.append({
            'width': s if s < 256 else 0,
            'height': s if s < 256 else 0,
            'size': len(png_bytes),
            'data': png_bytes
        })
    
    # 写入 ICO 文件
    with open('assets/icon.ico', 'wb') as f:
        # ICO 头部
        f.write(struct.pack('<HHH', 0, 1, len(icon_data)))  # 保留、类型、数量
        
        # 图标条目头部
        offset = 6 + len(icon_data) * 16
        for icon in icon_data:
            f.write(struct.pack('<BBBBHHII',
                icon['width'],      # 宽度
                icon['height'],     # 高度
                0,                  # 颜色数
                0,                  # 保留
                1,                  # 颜色平面数
                32,                 # 位深度
                icon['size'],       # 数据大小
                offset              # 偏移量
            ))
            offset += icon['size']
        
        # 写入图标数据
        for icon in icon_data:
            f.write(icon['data'])
    
    print('[OK] Multi-size ICO created successfully')
    print(f'[INFO] Sizes: {icon_sizes}')

if __name__ == '__main__':
    create_ico()
