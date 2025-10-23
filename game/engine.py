"""
游戏引擎 - 核心游戏逻辑
"""
import copy
from game.terminal import Terminal
from game.levels import get_game_levels
from game.save_system import SaveSystem


class GameEngine:
    """游戏引擎主类"""

    def __init__(self):
        self.levels = get_game_levels()
        self.current_level = 0
        self.save_system = SaveSystem()
        self.game_running = True

    def start_new_game(self):
        """开始新游戏"""
        self.levels = get_game_levels()
        self.current_level = 0
        Terminal.clear()
        Terminal.print_header()
        Terminal.print_ascii_art("welcome")
        Terminal.print_slow("\n正在初始化系统...", delay=0.02)
        Terminal.print_loading("连接中", 2)
        self.show_level_intro()

    def load_game(self):
        """加载游戏"""
        save_data = self.save_system.load_game()
        if save_data:
            self.current_level = save_data["current_level"]
            self.levels = save_data["levels"]
            Terminal.clear()
            Terminal.print_header()
            Terminal.print_success("游戏加载成功!")
            self.show_level_intro()
            return True
        return False

    def save_game(self):
        """保存游戏"""
        game_state = {
            "current_level": self.current_level,
            "levels": self.levels
        }
        return self.save_system.save_game(game_state)

    def get_current_level(self):
        """获取当前关卡数据"""
        if 0 <= self.current_level < len(self.levels):
            return self.levels[self.current_level]
        return None

    def show_level_intro(self):
        """显示关卡介绍"""
        level = self.get_current_level()
        if level:
            Terminal.print_box(f"第 {level['id']} 关: {level['name']}", level['story'])
            Terminal.print_info("输入 'help' 查看可用命令")
            print()

    def complete_level(self):
        """完成当前关卡"""
        level = self.get_current_level()

        if level['id'] == 3:
            # 第三关特殊处理 - 游戏真正结束
            Terminal.print_success("\n恭喜！你已经完成了所有关卡！")
            Terminal.print_info("\n感谢游玩 Terminal Infiltrator!")
            Terminal.print_warning("\n按 Enter 键退出...")
            input()
            self.game_running = False
            return

        Terminal.print_success(f"\n{'='*60}")
        Terminal.print_success(f"恭喜！你完成了第 {level['id']} 关: {level['name']}")
        Terminal.print_success(f"{'='*60}\n")

        if self.current_level < len(self.levels) - 1:
            Terminal.print_info("准备进入下一关...")
            Terminal.print_loading("加载中", 2)
            self.current_level += 1
            self.save_game()
            Terminal.clear()
            Terminal.print_header()
            self.show_level_intro()
        else:
            Terminal.print_success("\n你已经完成了所有关卡！")
            Terminal.print_info("感谢游玩!")
            self.game_running = False

    def unlock_target(self, target_name):
        """解锁目标"""
        level = self.get_current_level()
        if 'targets' in level:
            for target in level['targets']:
                if target['name'].lower() == target_name.lower():
                    target['locked'] = False
                    Terminal.print_success(f"目标 {target_name} 已解锁!")
                    return True
        return False

    def show_main_menu(self):
        """显示主菜单"""
        Terminal.clear()
        Terminal.print_header()

        menu_text = ""
        if self.save_system.has_save():
            save_info = self.save_system.get_save_info()
            menu_text = f"""
1. 新游戏
2. 继续游戏 (关卡 {save_info['level']})
3. 删除存档
4. 退出

当前存档信息:
  关卡: {save_info['level']}
  时间: {save_info['timestamp'][:19]}
            """
        else:
            menu_text = """
1. 新游戏
4. 退出

(当前没有存档)
            """

        Terminal.print_box("主菜单", menu_text)
        choice = input(f"请选择 [1-4]: ").strip()
        return choice

    def handle_menu_choice(self, choice):
        """处理菜单选择"""
        if choice == '1':
            if self.save_system.has_save():
                Terminal.print_warning("开始新游戏将覆盖当前存档，确定吗? (y/n): ")
                confirm = input().strip().lower()
                if confirm != 'y':
                    return False
            self.start_new_game()
            return True
        elif choice == '2' and self.save_system.has_save():
            if self.load_game():
                return True
            else:
                Terminal.print_error("加载游戏失败")
                input("按 Enter 继续...")
                return False
        elif choice == '3' and self.save_system.has_save():
            Terminal.print_warning("确定要删除存档吗? (y/n): ")
            confirm = input().strip().lower()
            if confirm == 'y':
                if self.save_system.delete_save():
                    Terminal.print_success("存档已删除")
                else:
                    Terminal.print_error("删除失败")
            input("按 Enter 继续...")
            return False
        elif choice == '4':
            Terminal.print_info("再见!")
            exit(0)
        else:
            Terminal.print_error("无效选择")
            input("按 Enter 继续...")
            return False
