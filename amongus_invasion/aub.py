import pygame
from os import path
from settings import Settings

class AmongUsBlue():#класс управления амонгом
    def __init__(self, au_game):
        self.img_dir = path.join(path.dirname(__file__), 'img')#определение папки с изображениями
        #инициализация амонга и его начальной позиции
        self.screen = au_game
        self.screen_rect = au_game.get_rect()
        self.settings = Settings().aub_speed

        #изоборажение амонга
        self.image = pygame.image.load(path.join(self.img_dir, 'aub.bmp')).convert()#путь к амонгу
        self.rect = self.image.get_rect()
        #self.image.set_colorkey('BLACK')#убираю фон
        #точка установки амонга
        self.rect.midbottom = self.screen_rect.midbottom#середина низ

        #преобразование для дробной скорости
        self.x = float(self.rect.x)

        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):#обновление позиции корбля по флагу
        if self.moving_right:
            self.x += self.settings
        if self.moving_left:
            self.x -= self.settings
        self.rect.x = self.x#дробное присвоение
    
    def blitme(self):#прорисовка амонга
        self.screen.blit(self.image, self.rect)