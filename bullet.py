import pygame
from pygame.sprite import Sprite          # 通过使用精灵，可以将游戏中相关的元素编组，进而同时操作编组中的所有元素


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()         # 调用super()来继承Sprite
        self.screen = screen

        # 在（0， 0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,  # 提供矩形左上角的x坐标和y坐标，以及矩形的宽度和高度
                                ai_settings.bullet_height)      # 子弹并非基于图像，使用pygame.Rect类从空白开始创建一个矩形
        self.rect.centerx = ship.rect.centerx                   # 子弹的初始位置取决于飞船当前的位置
        self.rect.top = ship.rect.top                           # 子弹应该从飞船顶部射出

        # 存储用小数表示的子弹位置，以便微调子弹的速度
        self.y = float(self.rect.y)

        # 存储子弹的颜色和速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor

        # 更新表示子弹位置的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
