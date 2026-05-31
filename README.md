<div align="center">

# ⚡ QuickBin

**A lightweight CLI tool for sharing code snippets instantly**

[English](#english) | [简体中文](#简体中文) | [繁體中文](#繁體中文)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-Coming%20Soon-orange.svg)](https://pypi.org/)

</div>

---

## 🌍 Language Selection / 语言选择

- [English](#english)
- [简体中文](#简体中文)
- [繁體中文](#繁體中文)

---

<a name="english"></a>
# 🇺🇸 English

## 🎉 Introduction

QuickBin is a **lightweight, fast, and elegant** command-line tool that allows developers to instantly share code snippets from their terminal. No more switching between browser tabs or copying code to web interfaces - just a simple command and your code is shared!

### ✨ Why QuickBin?

- 🚀 **Instant Sharing** - Upload and get a shareable link in seconds
- 🎨 **Syntax Highlighting** - Automatic language detection with beautiful formatting
- 📋 **Clipboard Integration** - URLs automatically copied to clipboard
- 📜 **History Management** - Keep track of all your shared snippets
- 🔒 **Privacy First** - Private by default, public option available
- 🌐 **Fallback Support** - Multiple upload backends for reliability

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📤 **Quick Upload** | Upload files or stdin content instantly |
| 🔍 **Auto Language Detection** | Supports 50+ programming languages |
| 📚 **History Tracking** | Browse and manage your snippet history |
| ⚙️ **Configurable** | Customize default behaviors |
| 👁️ **Snippet Viewer** | Preview snippets directly in terminal |
| 📋 **Auto Copy** | URLs copied to clipboard automatically |

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI (coming soon)
pip install quickbin-cli

# Or install from source
git clone https://github.com/gitstq/QuickBin.git
cd QuickBin
pip install -e .
```

### Basic Usage

```bash
# Upload a file
quickbin upload myscript.py

# Upload with description
quickbin upload myscript.py -d "My Python script"

# Upload from stdin
echo "print('Hello World')" | quickbin upload -

# View upload history
quickbin history

# View a snippet
quickbin view https://gist.github.com/xxx/xxx
```

### Supported Languages

QuickBin automatically detects language from file extension. Supported languages include:

- **Python** (.py)
- **JavaScript/TypeScript** (.js, .ts, .jsx, .tsx)
- **Java** (.java)
- **C/C++** (.c, .cpp, .h)
- **Go** (.go)
- **Rust** (.rs)
- **Ruby** (.rb)
- **PHP** (.php)
- **Swift** (.swift)
- **Kotlin** (.kt)
- **And 40+ more!**

## 📖 Detailed Usage

### Upload Command

```bash
# Basic upload
quickbin upload script.py

# With options
quickbin upload script.py \
  --description "My awesome script" \
  --language python \
  --public \
  --copy

# Using short options
qb upload script.py -d "My script" -l python -p -c
```

### History Command

```bash
# Show recent uploads (default 20)
quickbin history

# Show specific number
quickbin history --limit 50

# Clear history
quickbin clear
```

### Configuration

```bash
# List all settings
quickbin config --list

# Set a value
quickbin config --key auto_copy --value false

# Get a value
quickbin config --key default_language
```

### View Command

```bash
# View a gist
quickbin view https://gist.github.com/user/gist_id

# View any raw URL
quickbin view https://example.com/code.py
```

## 💡 Design Philosophy

QuickBin was designed with these principles:

1. **Simplicity** - Minimal commands, maximum utility
2. **Speed** - No waiting, instant uploads
3. **Reliability** - Multiple fallback options
4. **Developer-Friendly** - Rich terminal output with syntax highlighting

## 📦 Development

```bash
# Clone repository
git clone https://github.com/gitstq/QuickBin.git
cd QuickBin

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

<a name="简体中文"></a>
# 🇨🇳 简体中文

## 🎉 项目介绍

QuickBin 是一款**轻量、快速、优雅**的命令行工具，让开发者能够从终端即时分享代码片段。无需在浏览器标签页之间切换，也无需将代码复制到网页界面 - 只需一个简单的命令，您的代码就能被分享！

### ✨ 为什么选择 QuickBin？

- 🚀 **即时分享** - 几秒钟内上传并获取可分享链接
- 🎨 **语法高亮** - 自动语言检测，美观的格式化显示
- 📋 **剪贴板集成** - URL 自动复制到剪贴板
- 📜 **历史管理** - 追踪所有分享过的代码片段
- 🔒 **隐私优先** - 默认为私有，可选择公开
- 🌐 **备用支持** - 多个上传后端确保可靠性

## ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 📤 **快速上传** | 即时上传文件或标准输入内容 |
| 🔍 **自动语言检测** | 支持 50+ 种编程语言 |
| 📚 **历史追踪** | 浏览和管理您的代码片段历史 |
| ⚙️ **可配置** | 自定义默认行为 |
| 👁️ **片段查看器** | 直接在终端预览代码片段 |
| 📋 **自动复制** | URL 自动复制到剪贴板 |

## 🚀 快速开始

### 安装

```bash
# 从 PyPI 安装（即将推出）
pip install quickbin-cli

# 或从源码安装
git clone https://github.com/gitstq/QuickBin.git
cd QuickBin
pip install -e .
```

### 基本用法

```bash
# 上传文件
quickbin upload myscript.py

# 带描述上传
quickbin upload myscript.py -d "我的 Python 脚本"

# 从标准输入上传
echo "print('Hello World')" | quickbin upload -

# 查看上传历史
quickbin history

# 查看代码片段
quickbin view https://gist.github.com/xxx/xxx
```

### 支持的语言

QuickBin 自动从文件扩展名检测语言。支持的语言包括：

- **Python** (.py)
- **JavaScript/TypeScript** (.js, .ts, .jsx, .tsx)
- **Java** (.java)
- **C/C++** (.c, .cpp, .h)
- **Go** (.go)
- **Rust** (.rs)
- **Ruby** (.rb)
- **PHP** (.php)
- **Swift** (.swift)
- **Kotlin** (.kt)
- **以及 40+ 更多语言！**

## 📖 详细使用指南

### 上传命令

```bash
# 基本上传
quickbin upload script.py

# 带选项上传
quickbin upload script.py \
  --description "我的超棒脚本" \
  --language python \
  --public \
  --copy

# 使用短选项
qb upload script.py -d "我的脚本" -l python -p -c
```

### 历史命令

```bash
# 显示最近上传（默认 20 条）
quickbin history

# 显示指定数量
quickbin history --limit 50

# 清空历史
quickbin clear
```

### 配置

```bash
# 列出所有设置
quickbin config --list

# 设置值
quickbin config --key auto_copy --value false

# 获取值
quickbin config --key default_language
```

### 查看命令

```bash
# 查看 gist
quickbin view https://gist.github.com/user/gist_id

# 查看任意原始 URL
quickbin view https://example.com/code.py
```

## 💡 设计思路

QuickBin 遵循以下设计原则：

1. **简洁性** - 最少命令，最大效用
2. **速度** - 无需等待，即时上传
3. **可靠性** - 多个备用选项
4. **开发者友好** - 丰富的终端输出，支持语法高亮

## 📦 开发与部署

```bash
# 克隆仓库
git clone https://github.com/gitstq/QuickBin.git
cd QuickBin

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest
```

## 🤝 贡献指南

我们欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南。

## 📄 开源协议

本项目采用 MIT 协议 - 详见 [LICENSE](LICENSE) 文件。

---

<a name="繁體中文"></a>
# 🇹🇼 繁體中文

## 🎉 專案介紹

QuickBin 是一款**輕量、快速、優雅**的命令列工具，讓開發者能夠從終端即時分享程式碼片段。無需在瀏覽器分頁之間切換，也無需將程式碼複製到網頁介面 - 只需一個簡單的命令，您的程式碼就能被分享！

### ✨ 為什麼選擇 QuickBin？

- 🚀 **即時分享** - 幾秒鐘內上傳並獲取可分享連結
- 🎨 **語法高亮** - 自動語言檢測，美觀的格式化顯示
- 📋 **剪貼簿整合** - URL 自動複製到剪貼簿
- 📜 **歷史管理** - 追蹤所有分享過的程式碼片段
- 🔒 **隱私優先** - 預設為私有，可選擇公開
- 🌐 **備援支援** - 多個上傳後端確保可靠性

## ✨ 核心特性

| 特性 | 描述 |
|------|------|
| 📤 **快速上傳** | 即時上傳檔案或標準輸入內容 |
| 🔍 **自動語言檢測** | 支援 50+ 種程式語言 |
| 📚 **歷史追蹤** | 瀏覽和管理您的程式碼片段歷史 |
| ⚙️ **可設定** | 自訂預設行為 |
| 👁️ **片段檢視器** | 直接在終端預覽程式碼片段 |
| 📋 **自動複製** | URL 自動複製到剪貼簿 |

## 🚀 快速開始

### 安裝

```bash
# 從 PyPI 安裝（即將推出）
pip install quickbin-cli

# 或從原始碼安裝
git clone https://github.com/gitstq/QuickBin.git
cd QuickBin
pip install -e .
```

### 基本用法

```bash
# 上傳檔案
quickbin upload myscript.py

# 帶描述上傳
quickbin upload myscript.py -d "我的 Python 腳本"

# 從標準輸入上傳
echo "print('Hello World')" | quickbin upload -

# 查看上傳歷史
quickbin history

# 查看程式碼片段
quickbin view https://gist.github.com/xxx/xxx
```

### 支援的語言

QuickBin 自動從檔案副檔名檢測語言。支援的語言包括：

- **Python** (.py)
- **JavaScript/TypeScript** (.js, .ts, .jsx, .tsx)
- **Java** (.java)
- **C/C++** (.c, .cpp, .h)
- **Go** (.go)
- **Rust** (.rs)
- **Ruby** (.rb)
- **PHP** (.php)
- **Swift** (.swift)
- **Kotlin** (.kt)
- **以及 40+ 更多語言！**

## 📖 詳細使用指南

### 上傳命令

```bash
# 基本上傳
quickbin upload script.py

# 帶選項上傳
quickbin upload script.py \
  --description "我的超棒腳本" \
  --language python \
  --public \
  --copy

# 使用短選項
qb upload script.py -d "我的腳本" -l python -p -c
```

### 歷史命令

```bash
# 顯示最近上傳（預設 20 條）
quickbin history

# 顯示指定數量
quickbin history --limit 50

# 清空歷史
quickbin clear
```

### 設定

```bash
# 列出所有設定
quickbin config --list

# 設定值
quickbin config --key auto_copy --value false

# 獲取值
quickbin config --key default_language
```

### 檢視命令

```bash
# 檢視 gist
quickbin view https://gist.github.com/user/gist_id

# 檢視任意原始 URL
quickbin view https://example.com/code.py
```

## 💡 設計理念

QuickBin 遵循以下設計原則：

1. **簡潔性** - 最少命令，最大效用
2. **速度** - 無需等待，即時上傳
3. **可靠性** - 多個備援選項
4. **開發者友善** - 豐富的終端輸出，支援語法高亮

## 📦 開發與部署

```bash
# 複製倉庫
git clone https://github.com/gitstq/QuickBin.git
cd QuickBin

# 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝開發依賴
pip install -e ".[dev]"

# 執行測試
pytest
```

## 🤝 貢獻指南

我們歡迎貢獻！請查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南。

## 📄 開源授權

本專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案。

---

<div align="center">

**Made with ❤️ for developers worldwide**

[⭐ Star us on GitHub](https://github.com/gitstq/QuickBin) |
[🐛 Report Bug](https://github.com/gitstq/QuickBin/issues) |
[💡 Request Feature](https://github.com/gitstq/QuickBin/issues)

</div>
