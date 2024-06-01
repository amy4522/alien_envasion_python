import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        size=(ai_settings.screen_width, ai_settings.screen_height))   # 创建一个显示窗口
    pygame.display.set_caption("Alien Invasion")    # 设置游戏窗口的标题

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)           # 更新屏幕上的图像，并切换到新屏幕


run_game()
