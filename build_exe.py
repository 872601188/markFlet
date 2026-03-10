#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
markFlet Windows EXE 打脚脚本
用于生成 Windows 可执行文件
"""

import os
import sys
import subprocess

def build_exe():
    """打包 markFlet 为 Windows EXE"""
    
    # 基础命令
    cmd = [
        'pyinstaller',
        '--name=markFlet',
        '--onefile',           # 单文件模式
        '--windowed',          # 无控制台窗口
        '--clean',             # 清理缓存
        '--noconfirm',         # 覆盖输出目录
        
        # 隐藏控制台（Windows）
        '--hide-console=hide-early',
        
        # 添加数据文件
        '--add-data=markflet.db;.',
        
        # 图标（如果有的话）
        # '--icon=assets/icon.ico',
        
        # 排除不必要的模块以减小体积
        '--exclude-module=matplotlib',
        '--exclude-module=numpy',
        '--exclude-module=pandas',
        '--exclude-module=scipy',
        '--exclude-module=tkinter',
        '--exclude-module=unittest',
        '--exclude-module=pytest',
        
        # 主程序入口
        'markFlet/main.py'
    ]
    
    print("[INFO] 开始打包 markFlet...")
    print(f"命令: {' '.join(cmd)}")
    print()
    
    # 执行打包
    result = subprocess.run(cmd, capture_output=False, text=True)
    
    if result.returncode == 0:
        print("\n[SUCCESS] 打包成功!")
        print("\n输出文件:")
        print("  - dist/markFlet.exe")
        print("\n使用方法:")
        print("  直接运行 dist/markFlet.exe 即可")
    else:
        print("\n[ERROR] 打包失败!")
        return result.returncode
    
    return 0

if __name__ == '__main__':
    sys.exit(build_exe())
