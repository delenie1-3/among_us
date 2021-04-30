import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, au_settings, screen, amongus):
        #Создаёт пули в текущей позиции персонажа
        super(Bullet,self).__init__()
        self.screen = screen

        #Создание пули в позиции (0,0) и назначает
        #правильные позиции
        self.rect = pygame.Rect(0,0,au_settings.bullet_width,au_settings.bullet_height)
        self.rect.centerx = amongus.rect.centerx
        self.rect.top = amongus.rect.top

        #Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        self.color = au_settings.bullet_color
        self.speed_factor = au_settings.bullet_speed_factor

    def update(self):
        #Перемещает пулю вверх по экрану
        self.y -= self.speed_factor
        #Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        #Вывод пули на экран
        pygame.draw.rect(self.screen,self.color,self.rect)

        
        
        
