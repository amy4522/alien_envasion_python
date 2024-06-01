import json


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """"初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 在任何情况下都不应重置最高得分,从文件加载或设置为0
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """将当前最高分写入文件"""
        with open('high_score.json', 'w') as file:
            data = {'high_score': self.high_score}
            json.dump(data, file)

    def load_high_score(self):
        """从文件中加载最高分"""
        try:
            with open('high_score.json', 'r') as file:
                data = json.load(file)
                return data.get('high_score', 0)
        except FileNotFoundError:
            return 0
