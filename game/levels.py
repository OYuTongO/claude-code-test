"""
关卡数据和管理
"""


def get_game_levels():
    """返回所有游戏关卡数据"""
    return [
        # 第一关：基础教学
        {
            "id": 1,
            "name": "入侵开始：废弃的服务器",
            "story": """
你是一名独立黑客，代号 "Ghost"。
今天你收到了一条匿名消息，指向一个废弃的公司服务器。
消息说：真相就在其中。

你成功连接到了系统，现在需要找到隐藏的信息。
            """,
            "hint": "1. 使用 scan 查看文件\n2. 使用 decrypt 解密加密文件\n3. 从文件中找到密码\n4. 使用 execute 命令访问数据库",
            "files": [
                {
                    "name": "welcome.txt",
                    "encrypted": False,
                    "content": """
欢迎来到 CYBERCORE 系统
系统版本: 2.3.1
最后登录: 2024-03-15 23:47:12

注意：本系统包含机密信息
所有访问将被记录
                    """
                },
                {
                    "name": "note.txt",
                    "encrypted": True,
                    "puzzle": {
                        "question": "数学题：一个简单的开始\n计算: 100 + 200 - 50 = ?",
                        "answer": "250"
                    },
                    "content": """
内部备忘录:

项目代号: PHANTOM
状态: 已暂停
原因: 发现严重安全漏洞

主数据库密码已更改
新密码提示: 2024年的前4位数字

- 系统管理员
                    """,
                    "unlocks": "database"
                }
            ],
            "targets": [
                {
                    "name": "database",
                    "description": "主数据库",
                    "locked": True,
                    "password": "2024",
                    "hint": "密码可能在某个文件中"
                }
            ],
            "executable_commands": [
                {
                    "command": "access database 2024",
                    "output": """
正在连接数据库...
认证成功!

数据库记录:
- 项目 PHANTOM: 人工智能监控系统
- 状态: 因道德问题被终止
- 备份位置: 服务器 NEXUS-7

看起来还有更多秘密等待发现...
                    """,
                    "completes_level": True
                }
            ]
        },

        # 第二关：进阶挑战
        {
            "id": 2,
            "name": "深入：NEXUS-7 服务器",
            "story": """
你成功找到了 PHANTOM 项目的线索。
现在你已经连接到 NEXUS-7 服务器。
这里的防护更强，需要更高级的技巧。

你注意到系统中有多个加密文件和防火墙保护的目标。
            """,
            "hint": "某些文件可能包含破解其他目标所需的信息",
            "files": [
                {
                    "name": "system.log",
                    "encrypted": False,
                    "content": """
[2024-03-15 10:23:45] 用户 admin 登录
[2024-03-15 10:24:12] 文件 ai_core.dat 被访问
[2024-03-15 10:25:33] 防火墙规则已更新
[2024-03-15 10:26:01] 加密密钥生成: KEY-ALPHA-7
[2024-03-15 10:27:45] 用户 admin 登出
                    """
                },
                {
                    "name": "firewall_config.enc",
                    "encrypted": True,
                    "puzzle": {
                        "question": """
解密挑战：逻辑推理

有三个开关，只有一个是正确的：
A. 这个开关是错的
B. 开关C是对的
C. 开关A是对的

正确答案是哪个开关？(输入 A, B 或 C)
                        """,
                        "answer": "B"
                    },
                    "content": """
防火墙配置文件

受保护目标:
- ai_core (密码: ALPHA-7)
- backup_server (需要双重认证)

注意: 密钥格式为 KEY-[密码]
                    """,
                    "unlocks": "ai_core"
                },
                {
                    "name": "secret_memo.enc",
                    "encrypted": True,
                    "puzzle": {
                        "question": """
密码学挑战：

密文: KHOOR
提示: 凯撒密码，偏移量为3
解密后的明文是什么？(全部大写)
                        """,
                        "answer": "HELLO"
                    },
                    "content": """
绝密备忘录:

PHANTOM 项目实际上是一个大规模监控系统。
它可以监控全球网络流量，识别任何人的活动。

项目被终止是因为内部举报。
但核心代码已经备份到安全位置。

真相就在 ai_core 中。
                    """
                }
            ],
            "targets": [
                {
                    "name": "ai_core",
                    "description": "AI 核心系统",
                    "locked": True,
                    "is_objective": False
                }
            ],
            "executable_commands": [
                {
                    "command": "access ai_core ALPHA-7",
                    "output": """
正在访问 AI 核心...
认证通过！

╔══════════════════════════════════════╗
║        PHANTOM AI CORE v3.0          ║
║      全球监控系统 - 绝密项目        ║
╚══════════════════════════════════════╝

系统功能:
✓ 实时网络流量分析
✓ 个人行为模式识别
✓ 预测性威胁检测
✓ 自动化响应系统

道德评估: ⚠️ 严重侵犯隐私

项目状态: 表面终止，实际转入地下

下一步线索: 查看 backup_server
位置: SECTOR-OMEGA

任务完成！你发现了真相的一部分...
                    """,
                    "completes_level": True
                }
            ]
        },

        # 第三关：最终挑战
        {
            "id": 3,
            "name": "真相：OMEGA 区域",
            "story": """
你已经深入到了核心区域。
SECTOR-OMEGA 是整个系统的大脑。
这里存储着所有的秘密。

但防护也最为严密...
你需要运用所学的一切才能突破。
            """,
            "hint": "有时候答案就在问题本身，仔细观察所有信息",
            "files": [
                {
                    "name": "README.txt",
                    "encrypted": False,
                    "content": """
欢迎来到 OMEGA 区域

这里是真相的终点。

要访问主控制台，你需要：
1. 解密所有加密文件
2. 理解整个系统的运作
3. 做出你的选择

记住: 有些真相一旦知晓，就无法回头。
                    """
                },
                {
                    "name": "whistleblower.enc",
                    "encrypted": True,
                    "puzzle": {
                        "question": """
最终挑战：完成序列

找出规律，填入下一个数字：
2, 4, 8, 16, 32, ?
                        """,
                        "answer": "64"
                    },
                    "content": """
举报人日志 - 最后记录

我是 PHANTOM 项目的首席工程师。
我无法再继续这个项目。

这个系统太强大了，可以监控任何人。
没有隐私，没有自由，只有控制。

我已经在系统中留下了后门。
访问码: FREEDOM

使用它，你可以选择：
1. 关闭整个系统
2. 公开所有证据

我希望你能做出正确的选择。

- Dr. Sarah Chen
                    """,
                    "unlocks": "main_console"
                },
                {
                    "name": "project_truth.enc",
                    "encrypted": True,
                    "puzzle": {
                        "question": """
哲学问题：

如果一个监控系统可以预防所有犯罪，
但代价是每个人都失去隐私，
这样的系统应该存在吗？

回答 YES 或 NO
(提示：没有绝对的对错，但举报人的选择已经告诉你答案)
                        """,
                        "answer": "NO"
                    },
                    "content": """
PHANTOM 项目真相:

这不仅仅是一个监控系统。
它是一个控制系统。

通过AI预测，它可以：
- 在犯罪发生前逮捕嫌疑人
- 在抗议发生前镇压组织
- 在思想形成前修正认知

这是完美的控制，也是绝对的暴政。

现在，选择权在你手中。
                    """
                }
            ],
            "targets": [
                {
                    "name": "main_console",
                    "description": "主控制台",
                    "locked": True,
                    "is_objective": False
                }
            ],
            "executable_commands": [
                {
                    "command": "access main_console FREEDOM",
                    "output": """
╔══════════════════════════════════════════════════╗
║           主控制台访问已授权                   ║
╚══════════════════════════════════════════════════╝

你面前有两个选择：

[1] shutdown_system - 永久关闭 PHANTOM 系统
[2] leak_evidence - 向媒体公开所有证据

两个选择都将结束这个项目。
但方式不同。

输入 'execute shutdown_system' 或 'execute leak_evidence'
                    """,
                    "completes_level": False
                },
                {
                    "command": "shutdown_system",
                    "output": """
正在关闭系统...

[████████████████████████████████] 100%

PHANTOM 系统已完全关闭。
所有数据已删除。
所有监控已停止。

没有人会知道这个系统的存在。
也没有人会知道它的危险。

也许，这就是最好的结局？

════════════════════════════════════
         游戏结束 - 沉默结局
════════════════════════════════════

感谢游玩！你选择了保护世界，代价是真相。
                    """,
                    "completes_level": True
                },
                {
                    "command": "leak_evidence",
                    "output": """
正在编译证据...
正在加密传输...
正在发送到全球媒体网络...

[████████████████████████████████] 100%

证据已发送！

明天，全世界都会知道 PHANTOM 的存在。
会有调查，会有问责。
隐私权将得到更多关注。

但你也暴露了自己...
有些事情，一旦开始，就无法回头。

════════════════════════════════════
         游戏结束 - 真相结局
════════════════════════════════════

感谢游玩！你选择了真相，无论代价如何。
                    """,
                    "completes_level": True
                }
            ]
        }
    ]
