import pygame.font

class Button():
    def __init__(self, au_game, msg):#инициализация атрибутов кнопки
        self.screen = au_game.screen
        self.screen_rect = self.screen.get_rect()

        #размеры и свойства кнопки
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #построение объекта кнопки и выравнивание по центру
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #одно создание кнопки
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        #преобразует сообщение в прямоугольник и выравнивает по центру
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):#отображение кнопки
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)