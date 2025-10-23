"""
终端显示模块 - 处理彩色输出和UI渲染
"""
import os
import sys
import time
from colorama import init, Fore, Back, Style

init(autoreset=True)


class Terminal:
    """终端显示类，处理所有视觉输出"""

    @staticmethod
    def clear():
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_slow(text, delay=0.03, color=Fore.GREEN):
        """逐字符打印文本（打字机效果）"""
        for char in text:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(delay)
        print(Style.RESET_ALL)

    @staticmethod
    def print_header():
        """打印游戏头部"""
        Terminal.clear()
        header = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              {Fore.RED}█▀▀█ █░░█ █▀▀▄ █▀▀ █▀▀█ ░░{Fore.CYAN}                     ║
║              {Fore.RED}█░░░ █▄▄█ █▀▀▄ █▀▀ █▄▄▀ ░░{Fore.CYAN}                     ║
║              {Fore.RED}█▄▄█ ▄▄▄█ ▀▀▀░ ▀▀▀ ▀░▀▀ ▀▀{Fore.CYAN}                     ║
║                                                              ║
║         {Fore.YELLOW}T E R M I N A L   I N F I L T R A T O R{Fore.CYAN}         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
        print(header)

    @staticmethod
    def print_success(message):
        """打印成功信息"""
        print(f"{Fore.GREEN}[✓] {message}{Style.RESET_ALL}")

    @staticmethod
    def print_error(message):
        """打印错误信息"""
        print(f"{Fore.RED}[✗] {message}{Style.RESET_ALL}")

    @staticmethod
    def print_warning(message):
        """打印警告信息"""
        print(f"{Fore.YELLOW}[!] {message}{Style.RESET_ALL}")

    @staticmethod
    def print_info(message):
        """打印信息"""
        print(f"{Fore.CYAN}[i] {message}{Style.RESET_ALL}")

    @staticmethod
    def print_system(message):
        """打印系统消息"""
        print(f"{Fore.MAGENTA}[SYSTEM] {message}{Style.RESET_ALL}")

    @staticmethod
    def print_prompt():
        """打印命令提示符"""
        return input(f"{Fore.GREEN}cyber@terminal{Fore.WHITE}:{Fore.BLUE}~${Style.RESET_ALL} ")

    @staticmethod
    def print_box(title, content, width=60):
        """打印带边框的内容框"""
        print(f"\n{Fore.CYAN}╔{'═' * (width - 2)}╗")
        print(f"║ {Fore.YELLOW}{title.center(width - 4)}{Fore.CYAN} ║")
        print(f"╠{'═' * (width - 2)}╣")

        for line in content.split('\n'):
            if line.strip():
                padding = width - len(line) - 4
                print(f"║ {Fore.WHITE}{line}{' ' * padding}{Fore.CYAN} ║")

        print(f"╚{'═' * (width - 2)}╝{Style.RESET_ALL}\n")

    @staticmethod
    def print_loading(message="Loading", duration=2):
        """显示加载动画"""
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            sys.stdout.write(f'\r{Fore.CYAN}{frames[i % len(frames)]} {message}...{Style.RESET_ALL}')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write('\r' + ' ' * 50 + '\r')
        sys.stdout.flush()

    @staticmethod
    def print_ascii_art(art_type="welcome"):
        """打印ASCII艺术"""
        arts = {
            "welcome": f"""{Fore.GREEN}
    ╔═══════════════════════════════════════╗
    ║   欢迎来到终端渗透者               ║
    ║   你的任务：破解系统，找到真相     ║
    ╚═══════════════════════════════════════╝{Style.RESET_ALL}
            """,
            "skull": f"""{Fore.RED}
        ▄▄▄▄▄▄▄▄▄▄
      ▄▀░░░░░░░░░░░▀▄
     █░░░░░░░░░░░░░░█
    █░░░░██░░░░██░░░░█
    █░░░░░░░░░░░░░░░░█
    █░░░██████████░░░█
     █░░░░░░░░░░░░░░█
      ▀▄▄▄▄▄▄▄▄▄▄▄▄▀{Style.RESET_ALL}
            """,
            "lock": f"""{Fore.YELLOW}
         ██████
        ██░░░░██
       ██░░░░░░██
       ██░░░░░░██
      ████████████
     ██░░░░░░░░░░██
     ██░░░░██░░░░██
     ██░░░░██░░░░██
      ████████████{Style.RESET_ALL}
            """
        }
        print(arts.get(art_type, arts["welcome"]))
