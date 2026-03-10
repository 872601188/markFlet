# markFlet 项目指南

> 本文档为 AI 编码助手提供项目背景、架构和开发指南。
> 项目语言：中文（注释和文档主要使用中文）

---

## 项目概述

**markFlet** 是一个基于 Python Flet 框架开发的 Markdown 阅读器/编辑器桌面应用，支持将 Markdown 文档导出为 Word (.docx) 格式。

### 核心功能

- 📝 **Markdown 编辑** - 支持实时预览的 Markdown 编辑器
- 👁️ **实时预览** - 左右分栏布局，编辑与预览同步更新
- 📂 **文件操作** - 打开、保存 Markdown 文件
- 📄 **Word 导出** - 一键将 Markdown 转换为 Word 文档
- 🎨 **主题切换** - 支持亮色/暗色主题切换
- 💾 **SQLite 存储** - 保存最近打开的文件历史记录

---

## 技术栈

| 依赖包 | 最低版本 | 用途 |
|--------|----------|------|
| flet | >=0.20.0 | UI 框架，构建跨平台桌面应用 |
| markdown | >=3.5.0 | Markdown 解析 |
| python-docx | >=1.1.0 | Word 文档生成 |
| pymdown-extensions | >=10.0 | Markdown 扩展（代码高亮、表格等） |
| beautifulsoup4 | >=4.12.0 | HTML 解析 |

**Python 版本要求**: 3.8+

---

## 项目结构

```
fletMark/
└── markFlet/               # 项目根目录
    ├── main.py             # 主程序（单文件架构，包含所有逻辑）
    ├── requirements.txt    # 依赖列表
    ├── README.md           # 项目说明文档（中文）
    ├── BUILD.md            # 构建和运行指南
    ├── LICENSE             # MIT 许可证
    ├── .gitignore          # Git 忽略配置
    └── markflet.db         # SQLite 数据库（运行时自动创建）
```

### 代码组织

项目采用**单文件架构**，所有功能集中在 `main.py` 中：

1. **Database 类** (行 12-58) - SQLite 数据库管理
   - 初始化数据库表结构
   - 添加/获取最近打开的文件记录

2. **MarkdownConverter 类** (行 61-184) - Markdown 转换器
   - `md_to_html()` - 将 Markdown 转换为 HTML
   - `md_to_docx()` - 将 Markdown 转换为 Word 文档

3. **main() 函数** (行 187-484) - 主应用入口
   - UI 组件创建和布局
   - 事件处理函数（打开、保存、导出等）
   - 工具栏和状态栏

---

## 构建和运行

### 开发环境搭建

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt
```

### 运行应用

```bash
python main.py
```

### 打包为可执行文件

```bash
# 安装打包工具
pip install pyinstaller

# 打包（单文件、无控制台窗口）
pyinstaller --onefile --windowed main.py
```

---

## 代码风格指南

### 注释规范

- 使用**中文**编写所有注释和文档字符串
- 类文档字符串：简要说明类的用途
- 方法文档字符串：说明方法功能

示例：
```python
class Database:
    """SQLite 数据库管理"""
    
    def add_recent_file(self, file_path):
        """添加最近打开的文件"""
```

### 命名规范

- 类名：大驼峰（如 `Database`, `MarkdownConverter`）
- 函数/变量：小写下划线（如 `update_preview`, `current_file`）
- 常量：全大写（如有需要）

### 代码结构

- 导入语句分组：标准库、第三方库
- 类定义之间空两行
- 方法定义之间空一行

---

## 功能开发指南

### 添加新功能

由于项目采用单文件架构，新功能建议遵循以下模式：

1. **数据操作**：在 `Database` 类中添加新方法
2. **格式转换**：在 `MarkdownConverter` 类中添加静态方法
3. **UI 交互**：在 `main()` 函数中添加事件处理函数

### Markdown 导出扩展

当前 `md_to_docx()` 方法支持以下 Markdown 元素：
- 标题（H1-H4）
- 代码块
- 无序列表
- 有序列表
- 引用块
- 粗体、斜体、行内代码

如需支持更多元素，需扩展 `md_to_docx()` 中的解析逻辑。

---

## 测试策略

当前项目**无自动化测试**。测试方式：

1. **手动测试**：运行应用，验证各项功能
2. **测试场景**：
   - 打开/保存不同大小的 Markdown 文件
   - 导出包含各种 Markdown 语法的文档为 Word
   - 切换主题模式
   - 验证最近文件历史记录

---

## 部署说明

### 分发方式

1. **源码分发**：用户安装 Python 依赖后运行 `main.py`
2. **可执行文件**：使用 PyInstaller 打包为 `.exe`（Windows）或对应平台的可执行文件

### 数据文件

- 数据库文件 `markflet.db` 在首次运行时自动创建
- 无需预配置数据库

---

## 注意事项

### 已知限制

- 项目采用单文件架构，不适合大型功能扩展
- Word 导出功能对复杂 Markdown 格式的支持有限
- 无单元测试覆盖

### 开发计划（来自 README）

- [ ] 图片粘贴支持
- [ ] 数学公式渲染
- [ ] 代码高亮优化
- [ ] 多标签页支持

---

## 许可证

MIT License - 详见 [LICENSE](markFlet/LICENSE) 文件

---

*文档基于项目实际代码生成*
