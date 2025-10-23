# Terminal Infiltrator - 终端渗透者

![Game Banner](https://img.shields.io/badge/Game-Terminal_Infiltrator-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

一个创新的终端黑客模拟游戏，结合解谜、剧情和编程元素。通过命令行界面体验黑客渗透的刺激！

## 游戏特色

- **沉浸式剧情**：扮演黑客 "Ghost"，揭开 PHANTOM 项目的真相
- **命令行操作**：真实的终端体验，使用 hack、decrypt、scan 等命令
- **解谜挑战**：数学题、逻辑推理、密码学等多样化谜题
- **多重结局**：你的选择将决定故事的走向
- **彩色终端**：精美的 ASCII 艺术和彩色界面
- **存档系统**：随时保存和加载游戏进度
- **三个关卡**：从入门到高级，逐步深入

## 截图预览

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              █▀▀█ █░░█ █▀▀▄ █▀▀ █▀▀█ ░░                     ║
║              █░░░ █▄▄█ █▀▀▄ █▀▀ █▄▄▀ ░░                     ║
║              █▄▄█ ▄▄▄█ ▀▀▀░ ▀▀▀ ▀░▀▀ ▀▀                     ║
║                                                              ║
║         T E R M I N A L   I N F I L T R A T O R             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

## 快速开始

### 系统要求

- Python 3.7 或更高版本
- 支持 ANSI 颜色的终端（Windows 10+、Linux、macOS）

### 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/yourusername/claude-code-test.git
   cd claude-code-test
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **运行游戏**
   ```bash
   python main.py
   ```

### 打包成可执行文件

想要打包成独立运行的 exe 文件？查看详细指南：[BUILD_GUIDE.md](BUILD_GUIDE.md)

**快速打包（推荐）：**
```bash
# Windows
build.bat

# Linux/macOS
./build.sh

# 或使用 Python 脚本（跨平台）
python build.py
```

打包后的文件在 `dist/` 目录，可以在没有 Python 的电脑上直接运行！

## 游戏玩法

### 基础命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `help` | 显示帮助信息 | `help` |
| `scan` | 扫描系统或目标 | `scan` 或 `scan database` |
| `hack` | 破解目标 | `hack database` |
| `decrypt` | 解密文件 | `decrypt note.txt` |
| `read` | 读取文件 | `read welcome.txt` |
| `execute` | 执行命令 | `execute access database 2024` |
| `status` | 查看当前状态 | `status` |
| `hint` | 获取提示 | `hint` |
| `save` | 保存游戏 | `save` |
| `clear` | 清屏 | `clear` |
| `exit` | 退出游戏 | `exit` |

### 游戏流程

1. **探索系统**：使用 `scan` 命令查看可用文件和目标
2. **收集信息**：使用 `read` 命令阅读未加密的文件
3. **解密文件**：使用 `decrypt` 命令解密加密文件（需要解谜）
4. **破解目标**：使用 `hack` 或 `execute` 命令完成关卡目标
5. **推进剧情**：完成当前关卡，进入下一关

### 关卡介绍

#### 第一关：入侵开始
- 难度：⭐ 简单
- 学习基础命令
- 理解游戏机制
- 解锁第一个数据库

#### 第二关：深入探索
- 难度：⭐⭐ 中等
- 更复杂的解谜
- 多个加密文件
- 逻辑推理和密码学挑战

#### 第三关：最终真相
- 难度：⭐⭐⭐ 困难
- 道德抉择
- 多重结局
- 影响故事走向的决定

## 游戏提示

- 仔细阅读所有文件内容，线索可能隐藏其中
- 使用 `hint` 命令在卡关时获取帮助
- 某些命令需要正确的参数格式，注意大小写
- 游戏支持自动保存，可以随时退出
- 第三关有两个不同的结局，基于你的选择

## 项目结构

```
claude-code-test/
├── main.py                 # 游戏入口
├── requirements.txt        # 依赖列表
├── README.md              # 项目说明
├── .gitignore             # Git 忽略文件
├── game/                  # 游戏核心模块
│   ├── __init__.py       # 包初始化
│   ├── engine.py         # 游戏引擎
│   ├── terminal.py       # 终端显示
│   ├── commands.py       # 命令系统
│   ├── levels.py         # 关卡数据
│   └── save_system.py    # 存档系统
├── data/                  # 数据目录（未来扩展）
└── saves/                 # 存档目录
    └── save.json         # 游戏存档
```

## 技术特点

### 核心技术
- **Python 3.7+**：现代 Python 特性
- **Colorama**：跨平台彩色终端输出
- **JSON**：游戏数据和存档管理

### 设计模式
- **命令模式**：灵活的命令系统
- **状态模式**：游戏状态管理
- **MVC 架构**：清晰的代码结构

### 代码特色
- 模块化设计，易于扩展
- 完整的注释和文档字符串
- 支持自定义关卡（修改 levels.py）
- 彩色输出和 ASCII 艺术

## 自定义关卡

你可以通过编辑 `game/levels.py` 来创建自己的关卡：

```python
{
    "id": 4,
    "name": "你的关卡名称",
    "story": "关卡故事描述",
    "hint": "关卡提示",
    "files": [...],
    "targets": [...],
    "executable_commands": [...]
}
```

## 开发路线图

- [x] 核心游戏引擎
- [x] 三个完整关卡
- [x] 存档系统
- [x] 彩色终端 UI
- [ ] 更多关卡
- [ ] 成就系统
- [ ] 难度选择
- [ ] 多语言支持
- [ ] 配置文件支持

## 贡献指南

欢迎贡献代码、报告 bug 或提出新功能建议！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 常见问题

**Q: 游戏在 Windows 上显示乱码？**
A: 确保使用 Windows 10+ 并在新版 Windows Terminal 中运行。

**Q: 如何重置游戏进度？**
A: 在主菜单选择"删除存档"或手动删除 `saves/save.json` 文件。

**Q: 忘记某个谜题的答案怎么办？**
A: 使用 `hint` 命令获取提示，或查看 `game/levels.py` 源代码。

**Q: 可以跳过某个关卡吗？**
A: 可以通过修改存档文件中的 `current_level` 值。

## 致谢

- 感谢 Colorama 提供的跨平台终端颜色支持
- 灵感来源于经典文字冒险游戏和黑客文化
- 本项目使用 Claude Code 创建，用于测试 AI 辅助编程能力

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件

## 联系方式

- 项目地址：[GitHub Repository](https://github.com/yourusername/claude-code-test)
- 问题反馈：[Issues](https://github.com/yourusername/claude-code-test/issues)

---

**享受游戏，探索真相！**

Made with by Claude Code