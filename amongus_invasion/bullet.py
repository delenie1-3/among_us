import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):#класс управления снарядами
    def __init__(self, au_game):#создание объекта снаряда
        super().__init__()
        self.screen = au_game.screen
        self.settings = au_game.settings
        self.color = self.settings.bullet_color

        #создание снаряда в позиции 0,0
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        self.settings.bullet_height)
        self.rect.midtop = au_game.aub.rect.midtop

        self.y = float(self.rect.y)

    def update(self):#перемещение снаряда вверх
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):#вывод снаряда на экран
        pygame.draw.rect(self.screen, self.color, self.rect)