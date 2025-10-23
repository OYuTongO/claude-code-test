#!/usr/bin/env python3
"""
自动打包脚本 - Terminal Infiltrator
支持一键打包成可执行文件
"""
import os
import sys
import shutil
import subprocess
import platform


class Builder:
    """打包构建器"""

    def __init__(self):
        self.project_name = "TerminalInfiltrator"
        self.version = "1.0.0"
        self.system = platform.system()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

    def print_info(self, msg):
        """打印信息"""
        print(f"[INFO] {msg}")

    def print_success(self, msg):
        """打印成功信息"""
        print(f"[✓] {msg}")

    def print_error(self, msg):
        """打印错误信息"""
        print(f"[✗] {msg}")

    def check_pyinstaller(self):
        """检查是否安装了 PyInstaller"""
        try:
            import PyInstaller
            self.print_success(f"PyInstaller 已安装 (版本: {PyInstaller.__version__})")
            return True
        except ImportError:
            self.print_error("PyInstaller 未安装")
            return False

    def install_pyinstaller(self):
        """安装 PyInstaller"""
        self.print_info("正在安装 PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            self.print_success("PyInstaller 安装成功")
            return True
        except subprocess.CalledProcessError:
            self.print_error("PyInstaller 安装失败")
            return False

    def clean_build_files(self):
        """清理构建文件"""
        self.print_info("清理旧的构建文件...")
        dirs_to_clean = ['build', 'dist', '__pycache__']
        files_to_clean = [f'{self.project_name}.spec']

        for dir_name in dirs_to_clean:
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)
                self.print_info(f"已删除: {dir_name}/")

        for file_name in files_to_clean:
            if os.path.exists(file_name):
                os.remove(file_name)
                self.print_info(f"已删除: {file_name}")

        self.print_success("清理完成")

    def build_onefile(self):
        """打包成单文件"""
        self.print_info("开始打包（单文件模式）...")

        cmd = [
            "pyinstaller",
            "--onefile",
            "--name", self.project_name,
            "--clean",
            "--noconfirm",
            "--hidden-import", "colorama",
            "main.py"
        ]

        try:
            subprocess.check_call(cmd)
            self.print_success("打包完成！")
            return True
        except subprocess.CalledProcessError as e:
            self.print_error(f"打包失败: {e}")
            return False

    def build_onedir(self):
        """打包成目录"""
        self.print_info("开始打包（目录模式）...")

        cmd = [
            "pyinstaller",
            "--onedir",
            "--name", self.project_name,
            "--clean",
            "--noconfirm",
            "--hidden-import", "colorama",
            "main.py"
        ]

        try:
            subprocess.check_call(cmd)
            self.print_success("打包完成！")
            return True
        except subprocess.CalledProcessError as e:
            self.print_error(f"打包失败: {e}")
            return False

    def create_release(self):
        """创建发布包"""
        self.print_info("创建发布包...")

        release_dir = f"release-{self.version}"
        if os.path.exists(release_dir):
            shutil.rmtree(release_dir)
        os.makedirs(release_dir)

        # 确定可执行文件名称
        if self.system == "Windows":
            exe_name = f"{self.project_name}.exe"
        else:
            exe_name = self.project_name

        exe_path = os.path.join("dist", exe_name)

        if os.path.exists(exe_path):
            # 复制可执行文件
            shutil.copy(exe_path, release_dir)
            self.print_info(f"已复制: {exe_name}")

            # 复制文档
            docs = ["README.md", "WALKTHROUGH.md", "LICENSE", "BUILD_GUIDE.md"]
            for doc in docs:
                if os.path.exists(doc):
                    shutil.copy(doc, release_dir)
                    self.print_info(f"已复制: {doc}")

            self.print_success(f"发布包已创建: {release_dir}/")

            # 显示文件大小
            size = os.path.getsize(os.path.join(release_dir, exe_name))
            size_mb = size / (1024 * 1024)
            self.print_info(f"可执行文件大小: {size_mb:.2f} MB")

            return True
        else:
            self.print_error(f"找不到可执行文件: {exe_path}")
            return False

    def show_menu(self):
        """显示菜单"""
        print("\n" + "="*60)
        print(f"  Terminal Infiltrator - 打包工具")
        print(f"  版本: {self.version}")
        print(f"  系统: {self.system}")
        print("="*60)
        print("\n选择打包方式：")
        print("  1. 单文件模式（推荐，生成单个exe）")
        print("  2. 目录模式（启动更快，但文件较多）")
        print("  3. 清理构建文件")
        print("  4. 退出")
        print()

    def run(self):
        """运行构建器"""
        # 检查并安装 PyInstaller
        if not self.check_pyinstaller():
            choice = input("是否安装 PyInstaller? (y/n): ").strip().lower()
            if choice == 'y':
                if not self.install_pyinstaller():
                    return
            else:
                self.print_error("需要 PyInstaller 才能打包")
                return

        while True:
            self.show_menu()
            choice = input("请选择 [1-4]: ").strip()

            if choice == '1':
                self.clean_build_files()
                if self.build_onefile():
                    self.create_release()
                input("\n按 Enter 继续...")

            elif choice == '2':
                self.clean_build_files()
                if self.build_onedir():
                    self.print_info("目录模式打包完成，文件在 dist/ 目录中")
                input("\n按 Enter 继续...")

            elif choice == '3':
                self.clean_build_files()
                input("\n按 Enter 继续...")

            elif choice == '4':
                print("再见！")
                break

            else:
                print("无效选择，请重试")


if __name__ == "__main__":
    builder = Builder()
    builder.run()
