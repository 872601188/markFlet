# markFlet

> 📝 一个基于 Python Flet 的 Markdown 阅读器，支持导出 Word 文档

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flet](https://img.shields.io/badge/Flet-0.20+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ 功能特性

- 📝 **Markdown 编辑** - 支持实时预览的 Markdown 编辑器
- 👁️ **实时预览** - 左右分栏，编辑与预览同步
- 📂 **文件操作** - 打开、保存 Markdown 文件
- 📄 **Word 导出** - 支持图片、表格、代码块、链接等元素
- 🌐 **HTML 导出** - 导出带样式的 HTML 文件
- 📄 **PDF 导出** - 支持图片和格式化的 PDF 导出
- 🎨 **主题切换** - 支持亮色/暗色主题
- 💾 **SQLite 存储** - 保存最近打开的文件历史
- 🖼️ **图片粘贴支持** - 从剪贴板粘贴图片并自动保存

---

## 📸 界面预览

```
┌─────────────────────────────────────────────────────────────┐
│  markFlet                                      [打开] [保存] │
├──────────────────┬──────────────────────────────────────────┤
│                  │                                          │
│  # Hello World   │  Hello World                             │
│                  │  ==========                              │
│  This is a       │                                          │
│  **markdown**    │  This is a markdown editor               │
│  editor.         │                                          │
│                  │                                          │
│                  │                                          │
│  [编辑区]         │  [预览区]                                 │
│                  │                                          │
├──────────────────┴──────────────────────────────────────────┤
│  [导出 Word]                    状态: 就绪                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
python main.py
```

---

## 📦 依赖说明

| 包名 | 版本 | 用途 |
|------|------|------|
| flet | >=0.20.0 | UI 框架 |
| markdown | >=3.5.0 | Markdown 解析 |
| python-docx | >=1.1.0 | Word 文档生成 |
| pymdown-extensions | >=10.0 | Markdown 扩展 |
| Pillow | >=10.0.0 | 图片处理 |
| beautifulsoup4 | >=4.12.0 | HTML 解析 |
| weasyprint | >=60.0 | PDF 导出（可选）|

---

## 🛠️ 开发计划

- [x] 基础 Markdown 编辑器
- [x] 实时预览功能
- [x] 文件打开/保存
- [x] Word 导出（改进版）
- [x] HTML 导出
- [x] PDF 导出
- [x] SQLite 历史记录
- [x] 图片粘贴支持
- [ ] 数学公式渲染
- [ ] 代码高亮优化
- [ ] 多标签页支持

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

*Made with ❤️ by 贾维斯 (Jarvis)*