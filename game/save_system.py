"""
存档系统 - 处理游戏进度保存和加载
"""
import json
import os
from datetime import datetime


class SaveSystem:
    """游戏存档管理"""

    def __init__(self, save_dir="saves"):
        self.save_dir = save_dir
        self.save_file = os.path.join(save_dir, "save.json")

        # 确保存档目录存在
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

    def save_game(self, game_state):
        """保存游戏状态"""
        save_data = {
            "current_level": game_state["current_level"],
            "levels": game_state["levels"],
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0"
        }

        try:
            with open(self.save_file, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"保存失败: {e}")
            return False

    def load_game(self):
        """加载游戏状态"""
        if not os.path.exists(self.save_file):
            return None

        try:
            with open(self.save_file, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            return save_data
        except Exception as e:
            print(f"加载失败: {e}")
            return None

    def has_save(self):
        """检查是否存在存档"""
        return os.path.exists(self.save_file)

    def delete_save(self):
        """删除存档"""
        if os.path.exists(self.save_file):
            try:
                os.remove(self.save_file)
                return True
            except Exception as e:
                print(f"删除失败: {e}")
                return False
        return False

    def get_save_info(self):
        """获取存档信息"""
        if not self.has_save():
            return None

        save_data = self.load_game()
        if save_data:
            return {
                "level": save_data.get("current_level", 0) + 1,
                "timestamp": save_data.get("timestamp", "未知"),
                "version": save_data.get("version", "未知")
            }
        return None
