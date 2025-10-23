#!/bin/bash
# Terminal Infiltrator - Linux/macOS 打包脚本

echo "=================================="
echo "Terminal Infiltrator - 打包工具"
echo "=================================="
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "[错误] 未找到 Python3"
    exit 1
fi

echo "[✓] Python3 已安装"

# 检查 pip
if ! command -v pip3 &> /dev/null; then
    echo "[错误] 未找到 pip3"
    exit 1
fi

echo "[✓] pip3 已安装"

# 安装依赖
echo ""
echo "[信息] 安装依赖..."
pip3 install -r requirements.txt
pip3 install pyinstaller

# 清理旧文件
echo ""
echo "[信息] 清理旧文件..."
rm -rf build dist __pycache__ TerminalInfiltrator.spec

# 打包
echo ""
echo "[信息] 开始打包..."
pyinstaller --onefile \
  --name="TerminalInfiltrator" \
  --clean \
  --noconfirm \
  --hidden-import=colorama \
  main.py

# 检查结果
if [ -f "dist/TerminalInfiltrator" ]; then
    echo ""
    echo "[✓] 打包成功！"
    echo ""
    echo "可执行文件位置: dist/TerminalInfiltrator"

    # 设置执行权限
    chmod +x dist/TerminalInfiltrator

    # 显示文件大小
    SIZE=$(du -h dist/TerminalInfiltrator | cut -f1)
    echo "文件大小: $SIZE"

    # 创建发布包
    echo ""
    echo "[信息] 创建发布包..."
    mkdir -p release-1.0.0
    cp dist/TerminalInfiltrator release-1.0.0/
    cp README.md WALKTHROUGH.md LICENSE BUILD_GUIDE.md release-1.0.0/ 2>/dev/null

    echo "[✓] 发布包已创建: release-1.0.0/"
    echo ""
    echo "测试运行："
    echo "  cd dist"
    echo "  ./TerminalInfiltrator"
else
    echo ""
    echo "[错误] 打包失败"
    exit 1
fi
