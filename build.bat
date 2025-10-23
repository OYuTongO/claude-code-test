@echo off
REM Terminal Infiltrator - Windows 打包脚本

echo ==================================
echo Terminal Infiltrator - 打包工具
echo ==================================
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python
    pause
    exit /b 1
)

echo [√] Python 已安装

REM 安装依赖
echo.
echo [信息] 安装依赖...
pip install -r requirements.txt
pip install pyinstaller

REM 清理旧文件
echo.
echo [信息] 清理旧文件...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__
if exist TerminalInfiltrator.spec del TerminalInfiltrator.spec

REM 打包
echo.
echo [信息] 开始打包...
pyinstaller --onefile ^
  --name=TerminalInfiltrator ^
  --clean ^
  --noconfirm ^
  --hidden-import=colorama ^
  main.py

REM 检查结果
if exist dist\TerminalInfiltrator.exe (
    echo.
    echo [√] 打包成功！
    echo.
    echo 可执行文件位置: dist\TerminalInfiltrator.exe

    REM 创建发布包
    echo.
    echo [信息] 创建发布包...
    if exist release-1.0.0 rmdir /s /q release-1.0.0
    mkdir release-1.0.0
    copy dist\TerminalInfiltrator.exe release-1.0.0\
    copy README.md release-1.0.0\ 2>nul
    copy WALKTHROUGH.md release-1.0.0\ 2>nul
    copy LICENSE release-1.0.0\ 2>nul
    copy BUILD_GUIDE.md release-1.0.0\ 2>nul

    echo [√] 发布包已创建: release-1.0.0\
    echo.
    echo 测试运行：
    echo   cd dist
    echo   TerminalInfiltrator.exe
) else (
    echo.
    echo [错误] 打包失败
    pause
    exit /b 1
)

echo.
pause
