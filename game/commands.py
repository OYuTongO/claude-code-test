"""
命令系统 - 处理所有游戏内命令
"""
import random
import time
from colorama import Fore, Style
from game.terminal import Terminal


class CommandSystem:
    """命令处理系统"""

    def __init__(self, game_engine):
        self.engine = game_engine
        self.commands = {
            'help': self.cmd_help,
            'scan': self.cmd_scan,
            'hack': self.cmd_hack,
            'decrypt': self.cmd_decrypt,
            'read': self.cmd_read,
            'execute': self.cmd_execute,
            'status': self.cmd_status,
            'save': self.cmd_save,
            'exit': self.cmd_exit,
            'clear': self.cmd_clear,
            'hint': self.cmd_hint,
        }

    def execute(self, command_str):
        """执行命令"""
        if not command_str.strip():
            return

        parts = command_str.strip().split()
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []

        if cmd in self.commands:
            self.commands[cmd](args)
        else:
            Terminal.print_error(f"未知命令: {cmd}. 输入 'help' 查看可用命令。")

    def cmd_help(self, args):
        """显示帮助信息"""
        help_text = """
scan [target]    - 扫描目标系统或文件
hack [target]    - 尝试破解目标
decrypt [file]   - 解密加密文件
read [file]      - 读取文件内容
execute [cmd]    - 执行系统命令
status           - 查看当前状态
hint             - 获取当前关卡提示
save             - 保存游戏进度
clear            - 清屏
exit             - 退出游戏
        """
        Terminal.print_box("可用命令", help_text, 62)

    def cmd_scan(self, args):
        """扫描命令"""
        current_level = self.engine.get_current_level()

        if not args:
            Terminal.print_info("扫描当前系统...")
            Terminal.print_loading("扫描中", 1.5)

            if 'files' in current_level:
                Terminal.print_success("发现以下文件:")
                for file in current_level['files']:
                    status = "🔒" if file.get('encrypted', False) else "📄"
                    print(f"  {status} {file['name']}")

            if 'targets' in current_level:
                Terminal.print_success("\n发现以下目标:")
                for target in current_level['targets']:
                    status = "🔐" if target.get('locked', True) else "✅"
                    print(f"  {status} {target['name']}")
        else:
            target_name = ' '.join(args)
            Terminal.print_info(f"扫描目标: {target_name}")
            Terminal.print_loading("分析中", 1)

            # 查找目标
            if 'targets' in current_level:
                for target in current_level['targets']:
                    if target['name'].lower() == target_name.lower():
                        Terminal.print_success(f"目标信息:")
                        print(f"  名称: {target['name']}")
                        print(f"  描述: {target.get('description', '未知')}")
                        print(f"  状态: {'已锁定' if target.get('locked', True) else '已解锁'}")
                        if 'hint' in target:
                            print(f"  提示: {target['hint']}")
                        return

            Terminal.print_error("未找到目标")

    def cmd_hack(self, args):
        """破解命令"""
        if not args:
            Terminal.print_error("用法: hack [target]")
            return

        target_name = ' '.join(args)
        current_level = self.engine.get_current_level()

        Terminal.print_info(f"尝试破解: {target_name}")
        Terminal.print_loading("破解中", 2)

        # 查找并破解目标
        if 'targets' in current_level:
            for target in current_level['targets']:
                if target['name'].lower() == target_name.lower():
                    if target.get('locked', True):
                        # 检查是否需要密码
                        if 'password' in target:
                            Terminal.print_warning("目标受密码保护")
                            Terminal.print_info("提示: 需要使用正确的访问命令和密码")
                            Terminal.print_info("尝试使用 decrypt 命令解密文件获取密码，然后使用 execute 命令访问")
                            if self.engine.current_level == 0:
                                Terminal.print_info(f"示例: {Fore.YELLOW}execute access database [密码]{Style.RESET_ALL}")
                            return
                        else:
                            # 模拟破解过程
                            success_rate = random.randint(60, 95)
                            print(f"\n破解进度: {success_rate}%")
                            target['locked'] = False
                            Terminal.print_success(f"成功破解 {target_name}!")

                            # 检查是否完成关卡
                            if target.get('is_objective', False):
                                self.engine.complete_level()
                            return
                    else:
                        Terminal.print_info("目标已经被破解")
                        return

        Terminal.print_error("未找到目标或无法破解")

    def cmd_decrypt(self, args):
        """解密命令"""
        if not args:
            Terminal.print_error("用法: decrypt [file]")
            return

        filename = ' '.join(args)
        current_level = self.engine.get_current_level()

        Terminal.print_info(f"解密文件: {filename}")
        Terminal.print_loading("解密中", 1.5)

        if 'files' in current_level:
            for file in current_level['files']:
                if file['name'].lower() == filename.lower():
                    if file.get('encrypted', False):
                        # 显示解密挑战
                        if 'puzzle' in file:
                            puzzle = file['puzzle']
                            Terminal.print_box("解密挑战", puzzle['question'])
                            answer = input(f"你的答案: ").strip()

                            if answer.lower() == puzzle['answer'].lower():
                                file['encrypted'] = False
                                Terminal.print_success("解密成功!")
                                if 'content' in file:
                                    print(f"\n文件内容:\n{file['content']}\n")

                                # 检查是否解锁了某个目标
                                if 'unlocks' in file:
                                    self.engine.unlock_target(file['unlocks'])
                                    # 给出更明确的提示
                                    if file['name'].lower() == 'note.txt' and self.engine.current_level == 0:
                                        Terminal.print_info("💡 提示: 现在你知道了密码，可以使用以下命令访问数据库:")
                                        print(f"   {Fore.YELLOW}execute access database 2024{Style.RESET_ALL}\n")
                                return
                            else:
                                Terminal.print_error("答案错误，解密失败")
                                return
                        else:
                            file['encrypted'] = False
                            Terminal.print_success("解密成功!")
                            if 'content' in file:
                                print(f"\n{file['content']}\n")
                            return
                    else:
                        Terminal.print_info("文件未加密，使用 'read' 命令查看")
                        return

        Terminal.print_error("文件不存在")

    def cmd_read(self, args):
        """读取文件"""
        if not args:
            Terminal.print_error("用法: read [file]")
            return

        filename = ' '.join(args)
        current_level = self.engine.get_current_level()

        if 'files' in current_level:
            for file in current_level['files']:
                if file['name'].lower() == filename.lower():
                    if file.get('encrypted', False):
                        Terminal.print_error("文件已加密，请先使用 decrypt 命令解密")
                        return
                    else:
                        Terminal.print_success(f"读取文件: {filename}")
                        if 'content' in file:
                            print(f"\n{file['content']}\n")
                        return

        Terminal.print_error("文件不存在")

    def cmd_execute(self, args):
        """执行命令"""
        if not args:
            Terminal.print_error("用法: execute [command]")
            return

        command = ' '.join(args)
        current_level = self.engine.get_current_level()

        Terminal.print_info(f"执行: {command}")
        Terminal.print_loading("执行中", 1)

        # 检查是否有可执行命令
        if 'executable_commands' in current_level:
            for cmd in current_level['executable_commands']:
                if cmd['command'].lower() == command.lower():
                    Terminal.print_success("执行成功!")
                    print(f"\n{cmd['output']}\n")

                    if cmd.get('completes_level', False):
                        self.engine.complete_level()
                    return

        Terminal.print_error("命令执行失败或权限不足")

    def cmd_status(self, args):
        """显示状态"""
        status_info = f"""
当前关卡: {self.engine.current_level + 1} / {len(self.engine.levels)}
关卡名称: {self.engine.get_current_level()['name']}
完成进度: {self.engine.current_level} 关已完成
        """
        Terminal.print_box("系统状态", status_info)

    def cmd_save(self, args):
        """保存游戏"""
        self.engine.save_game()
        Terminal.print_success("游戏已保存")

    def cmd_exit(self, args):
        """退出游戏"""
        Terminal.print_warning("确定要退出吗? (y/n): ")
        confirm = input().strip().lower()
        if confirm == 'y':
            Terminal.print_info("感谢游玩!")
            exit(0)

    def cmd_clear(self, args):
        """清屏"""
        Terminal.clear()
        Terminal.print_header()

    def cmd_hint(self, args):
        """获取提示"""
        current_level = self.engine.get_current_level()
        if 'hint' in current_level:
            Terminal.print_box("提示", current_level['hint'])
        else:
            Terminal.print_info("当前关卡没有可用提示")
