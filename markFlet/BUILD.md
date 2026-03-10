# 构建和运行

## 开发环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

## 运行应用

```bash
python main.py
```

## 打包为可执行文件

```bash
# 安装打包工具
pip install pyinstaller

# 打包
pyinstaller --onefile --windowed main.py
```

## 项目结构

```
markFlet/
├── main.py           # 主程序
├── requirements.txt  # 依赖列表
├── README.md         # 项目说明
├── LICENSE           # 许可证
├── .gitignore        # Git 忽略文件
└── markflet.db       # SQLite 数据库（自动创建）
```