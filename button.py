import pygame.font          # 能够将文本渲染到屏幕上


class Button:

    def __init__(self, ai_settings, screen, msg):          # msg是要显示的文本内容
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)                # 按钮颜色
        self.text_color = (255, 255, 255)              # 文本颜色
        self.font = pygame.font.SysFont(None, 48)     # 文本使用默认字体， 字号48

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self.prep_msg(msg)                              # 将要显示的字符串渲染为图像来处理文本

    def prep_msg(self, msg):
        """将msg渲染为图像， 并使其在按钮上居中"""
        self.msg_image = self.font.render(msg,  True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮， 再绘制文本
        self.screen.fill(self.button_color, self.rect)         # 绘制矩形按钮
        self.screen.blit(self.msg_image, self.msg_image_rect)        # 传递图像及和图像关联的矩形对象
