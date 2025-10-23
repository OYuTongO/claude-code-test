# 快速开始指南

## 🎮 运行游戏（三种方式）

### 方式一：Python 直接运行（推荐新手）

这是最简单的方式，适合学习和开发。

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行游戏
python main.py
```

**优点**：
- 简单快速
- 容易调试
- 可以修改代码

**缺点**：
- 需要安装 Python
- 需要安装依赖库

---

### 方式二：打包成可执行文件（推荐分享）

适合分享给没有 Python 环境的朋友。

**Windows 用户：**
```bash
# 双击运行或命令行执行
build.bat
```

**Linux/macOS 用户：**
```bash
# 在终端运行
./build.sh
```

**跨平台（Python 脚本）：**
```bash
python build.py
```

打包完成后：
- 可执行文件在 `dist/` 目录
- 发布包在 `release-1.0.0/` 目录
- 可以复制到任何电脑直接运行

**优点**：
- 无需安装 Python
- 一个文件即可运行
- 方便分享

**缺点**：
- 文件较大（约 10-20 MB）
- 首次打包需要时间

---

### 方式三：开发模式

适合开发者修改和扩展游戏。

```bash
# 1. 创建虚拟环境（推荐）
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# 2. 安装开发依赖
pip install -r requirements.txt

# 3. 运行游戏
python main.py

# 4. 修改代码后直接运行测试
```

---

## 📋 各平台详细说明

### Windows

1. **检查 Python**
   ```cmd
   python --version
   ```
   如果提示找不到命令，请先安装 Python：https://www.python.org/

2. **安装依赖**
   ```cmd
   pip install -r requirements.txt
   ```

3. **运行游戏**
   ```cmd
   python main.py
   ```

4. **打包（可选）**
   ```cmd
   build.bat
   ```

### Linux

1. **检查 Python（通常已安装）**
   ```bash
   python3 --version
   ```

2. **安装依赖**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **运行游戏**
   ```bash
   python3 main.py
   ```

4. **打包（可选）**
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

### macOS

1. **检查 Python**
   ```bash
   python3 --version
   ```

2. **安装依赖**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **运行游戏**
   ```bash
   python3 main.py
   ```

4. **打包（可选）**
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

---

## ⚠️ 常见问题

### Python 版本问题

**问题**：提示 Python 版本太低

**解决**：游戏需要 Python 3.7+，请升级 Python：
- Windows: https://www.python.org/downloads/
- Linux: `sudo apt install python3.9` 或 `sudo yum install python39`
- macOS: `brew install python@3.9`

### 依赖安装失败

**问题**：pip install 失败

**解决**：
```bash
# 升级 pip
python -m pip install --upgrade pip

# 使用国内镜像（中国用户）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 彩色输出不显示

**问题**：Windows 上没有颜色

**解决**：
- 使用 Windows 10+ 的新终端
- 或下载 Windows Terminal：https://aka.ms/terminal

### 打包后运行失败

**问题**：exe 运行报错

**解决**：
1. 检查杀毒软件是否拦截
2. 确保使用命令行运行（游戏需要控制台）
3. 查看 BUILD_GUIDE.md 的故障排除部分

---

## 🎯 推荐流程

**首次体验：**
```bash
pip install -r requirements.txt
python main.py
```

**分享给朋友：**
```bash
python build.py
# 或
build.bat  # Windows
./build.sh # Linux/macOS

# 然后将 release-1.0.0 文件夹打包发送
```

---

## 📚 更多帮助

- **游戏攻略**：查看 [WALKTHROUGH.md](WALKTHROUGH.md)
- **打包详细说明**：查看 [BUILD_GUIDE.md](BUILD_GUIDE.md)
- **项目说明**：查看 [README.md](README.md)

---

## 🎮 游戏快速入门

启动游戏后：

1. **查看帮助**
   ```
   help
   ```

2. **扫描系统**
   ```
   scan
   ```

3. **查看提示**
   ```
   hint
   ```

4. **第一关通关步骤**
   ```
   scan
   decrypt note.txt
   250
   execute access database 2024
   ```

祝你游戏愉快！
