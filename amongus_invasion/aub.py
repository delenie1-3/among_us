import pygame
from os import path

class AmongUsBlue():#класс управления амонгом
    def __init__(self, au_screen):
        self.img_dir = path.join(path.dirname(__file__), 'img')#определение папки с изображениями
        #инициализация амонга и его начальной позиции
        self.screen = au_screen
        self.screen_rect = au_screen.get_rect()

        #изоборажение амонга
        self.image = pygame.image.load(path.join(self.img_dir, 'aub.bmp')).convert()#путь к амонгу
        self.rect = self.image.get_rect()
        #self.image.set_colorkey('BLACK')#убираю фон
        #точка установки амонга
        self.rect.midbottom = self.screen_rect.midbottom#середина низ
    
    def blitme(self):#прорисовка амонга
        self.screen.blit(self.image, self.rect)