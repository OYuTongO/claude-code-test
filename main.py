#!/usr/bin/env python3
"""
Terminal Infiltrator - 终端渗透者
一个创新的命令行黑客模拟游戏

运行: python main.py
"""
import sys
from game.engine import GameEngine
from game.commands import CommandSystem
from game.terminal import Terminal


def main():
    """主函数"""
    # 创建游戏引擎
    engine = GameEngine()
    commands = CommandSystem(engine)

    # 显示主菜单
    while True:
        choice = engine.show_main_menu()
        if engine.handle_menu_choice(choice):
            break

    # 主游戏循环
    try:
        while engine.game_running:
            # 获取用户输入
            command = Terminal.print_prompt()

            # 执行命令
            commands.execute(command)

            # 检查是否完成游戏
            if not engine.game_running:
                break

    except KeyboardInterrupt:
        print("\n")
        Terminal.print_warning("检测到中断信号")
        Terminal.print_info("是否保存游戏? (y/n): ")
        try:
            save_choice = input().strip().lower()
            if save_choice == 'y':
                engine.save_game()
                Terminal.print_success("游戏已保存")
        except:
            pass
        Terminal.print_info("再见!")
        sys.exit(0)
    except Exception as e:
        Terminal.print_error(f"发生错误: {e}")
        Terminal.print_info("游戏将自动保存...")
        engine.save_game()
        sys.exit(1)


if __name__ == "__main__":
    main()
