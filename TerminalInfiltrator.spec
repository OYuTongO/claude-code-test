# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller 配置文件 - Terminal Infiltrator
使用方法: pyinstaller TerminalInfiltrator.spec
"""

block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        # 如果需要打包额外的数据文件，在这里添加
        # ('data', 'data'),  # 打包 data 目录
    ],
    hiddenimports=[
        'colorama',
        'game',
        'game.terminal',
        'game.engine',
        'game.commands',
        'game.levels',
        'game.save_system',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # 排除不需要的模块以减小文件大小
        'tkinter',
        'matplotlib',
        'numpy',
        'pandas',
        'PIL',
        'PyQt5',
        'scipy',
        'IPython',
        'jupyter',
    ],
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
    upx=True,  # 使用 UPX 压缩（如果安装了）
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 保持控制台窗口（游戏需要）
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # 如果有图标文件，在这里指定路径
)
