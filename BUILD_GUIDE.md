# 打包指南 - 如何将游戏打包成 EXE

本指南介绍如何将 Terminal Infiltrator 打包成可独立运行的可执行文件。

## 📦 打包原理

Python 程序打包成 exe 的原理：
1. **打包器**（如 PyInstaller）分析你的 Python 代码
2. 收集所有依赖的库和模块
3. 将 Python 解释器嵌入到可执行文件中
4. 创建一个启动器，在运行时解压并执行代码
5. 用户可以直接运行 exe，无需安装 Python

## 🛠️ 三种主流打包工具对比

### 1. PyInstaller ⭐ 推荐
- **优点**：最流行，支持多平台，使用简单
- **缺点**：生成文件较大
- **适用**：大多数场景

### 2. cx_Freeze
- **优点**：跨平台，生成文件较小
- **缺点**：配置复杂
- **适用**：需要精细控制

### 3. Nuitka
- **优点**：编译成 C 代码，运行速度快
- **缺点**：编译时间长
- **适用**：对性能要求高的场景

---

## 方法一：使用 PyInstaller（推荐）

### 步骤 1：安装 PyInstaller

```bash
pip install pyinstaller
```

### 步骤 2：基础打包命令

**最简单的方式：**
```bash
pyinstaller main.py
```

这会生成：
- `dist/main/` 目录 - 包含 exe 和所有依赖文件
- 需要整个文件夹才能运行

**打包成单个 exe 文件：**
```bash
pyinstaller --onefile main.py
```

生成单个 `dist/main.exe` 文件，可以独立运行。

### 步骤 3：优化打包配置

**添加图标和窗口配置：**
```bash
pyinstaller --onefile --name="TerminalInfiltrator" --icon=icon.ico main.py
```

**完整配置命令：**
```bash
pyinstaller --onefile \
  --name="TerminalInfiltrator" \
  --clean \
  --noconfirm \
  main.py
```

参数说明：
- `--onefile`: 打包成单个文件
- `--name`: 指定生成的 exe 名称
- `--clean`: 清理临时文件
- `--noconfirm`: 覆盖已有文件不询问
- `--noconsole`: 隐藏控制台窗口（不推荐用于命令行游戏）
- `--icon`: 指定图标文件

### 步骤 4：使用 spec 文件（高级）

运行一次打包后会生成 `.spec` 文件，可以编辑它来精确控制打包：

```python
# TerminalInfiltrator.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['colorama'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='TerminalInfiltrator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 保持控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

使用 spec 文件打包：
```bash
pyinstaller TerminalInfiltrator.spec
```

---

## 方法二：使用 cx_Freeze

### 步骤 1：安装

```bash
pip install cx_Freeze
```

### 步骤 2：创建 setup.py

```python
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["colorama", "game"],
    "include_files": [],
}

setup(
    name="TerminalInfiltrator",
    version="1.0.0",
    description="终端黑客模拟游戏",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=None)]
)
```

### 步骤 3：打包

```bash
python setup.py build
```

生成的文件在 `build/` 目录中。

---

## 方法三：使用 auto-py-to-exe（图形界面）

这是 PyInstaller 的 GUI 版本，适合不熟悉命令行的用户。

### 步骤 1：安装

```bash
pip install auto-py-to-exe
```

### 步骤 2：启动

```bash
auto-py-to-exe
```

### 步骤 3：在图形界面中配置

1. 选择 main.py 文件
2. 选择 "One File" 模式
3. 选择 "Console Based"
4. 点击 "Convert .py to .exe"

---

## 🚀 快速开始 - 推荐配置

对于本游戏，推荐使用这个命令：

```bash
# Windows
pyinstaller --onefile --name="TerminalInfiltrator" --clean main.py

# 生成的文件在 dist/TerminalInfiltrator.exe
```

**完整步骤：**

1. 安装打包工具
   ```bash
   pip install pyinstaller
   ```

2. 进入项目目录
   ```bash
   cd claude-code-test
   ```

3. 执行打包
   ```bash
   pyinstaller --onefile --name="TerminalInfiltrator" main.py
   ```

4. 查找生成的 exe
   ```bash
   cd dist
   # Windows: TerminalInfiltrator.exe
   # Linux: TerminalInfiltrator
   # macOS: TerminalInfiltrator
   ```

5. 运行测试
   ```bash
   ./TerminalInfiltrator  # Linux/macOS
   TerminalInfiltrator.exe  # Windows
   ```

---

## 📋 打包检查清单

打包前确认：
- [ ] 所有依赖都在 requirements.txt 中
- [ ] 游戏在开发环境中正常运行
- [ ] 没有使用绝对路径
- [ ] 没有依赖外部文件（或已配置打包）

打包后测试：
- [ ] 在干净的机器上测试（没有安装 Python）
- [ ] 测试所有游戏功能
- [ ] 检查存档系统是否正常
- [ ] 测试彩色输出是否正常

---

## 🐛 常见问题

### 1. 找不到模块错误

**问题**：运行 exe 时报 `ModuleNotFoundError`

**解决**：在 spec 文件中添加隐藏导入
```python
hiddenimports=['colorama', 'game.terminal', 'game.engine']
```

### 2. 生成的文件太大

**原因**：PyInstaller 打包了整个 Python 环境

**解决**：
- 使用虚拟环境，只安装必要的包
- 使用 `--exclude-module` 排除不需要的模块
- 考虑使用 UPX 压缩（`--upx-dir`）

### 3. 彩色输出不正常

**问题**：Windows 上颜色不显示

**解决**：确保 colorama 被正确打包
```bash
pyinstaller --onefile --hidden-import=colorama main.py
```

### 4. 杀毒软件误报

**原因**：打包的 exe 包含解压代码，可能被误判

**解决**：
- 添加数字签名
- 向杀毒软件提交白名单申请
- 使用 Nuitka 编译（减少误报）

### 5. 存档文件保存位置

**问题**：打包后找不到 saves 目录

**解决**：使用相对于用户目录的路径
```python
import os
save_dir = os.path.join(os.path.expanduser("~"), ".terminal_infiltrator", "saves")
```

---

## 🔧 高级优化

### 减小文件大小

1. **使用虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   pyinstaller --onefile main.py
   ```

2. **排除不需要的模块**
   ```bash
   pyinstaller --onefile --exclude-module pytest --exclude-module IPython main.py
   ```

3. **使用 UPX 压缩**
   ```bash
   # 下载 UPX: https://upx.github.io/
   pyinstaller --onefile --upx-dir=/path/to/upx main.py
   ```

### 加速启动

1. **禁用临时目录解压**（使用 onefile 时）
   - 使用 `--onedir` 代替 `--onefile`
   - 文件会更多但启动更快

2. **预编译 Python 文件**
   ```bash
   python -m compileall game/
   ```

---

## 📦 发布打包好的程序

### 1. 创建发布包

```bash
# 创建发布目录
mkdir release
cp dist/TerminalInfiltrator.exe release/
cp README.md release/
cp WALKTHROUGH.md release/
cp LICENSE release/

# 压缩
zip -r TerminalInfiltrator-v1.0.0-Windows.zip release/
```

### 2. 不同平台打包

- **Windows**：在 Windows 上打包生成 `.exe`
- **Linux**：在 Linux 上打包生成 ELF 可执行文件
- **macOS**：在 macOS 上打包生成 `.app` 或可执行文件

**注意**：不能跨平台打包，需要在目标平台上进行打包。

### 3. 使用 GitHub Actions 自动打包

可以配置 CI/CD 自动为多个平台打包，见项目的 `.github/workflows/` 目录。

---

## 📚 参考资源

- [PyInstaller 官方文档](https://pyinstaller.org/)
- [cx_Freeze 文档](https://cx-freeze.readthedocs.io/)
- [Nuitka 文档](https://nuitka.net/)
- [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe)

---

## 🎯 总结

**推荐方案**：
- 新手：使用 `auto-py-to-exe` 图形界面
- 进阶：使用 `pyinstaller --onefile` 命令
- 高级：编辑 `.spec` 文件精确控制

**最简单的命令**：
```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

打包后的 exe 可以直接在没有安装 Python 的电脑上运行！
