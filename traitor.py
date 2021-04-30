import pygame
from pygame.sprite import Sprite

class Traitor(Sprite):#
    #Класс, представляющий одного предателя

    def __init__(self,au_settings,screen):
        #Инициализация одного предателя и задаёт его начальную позицию
        super(Traitor,self).__init__()
        self.screen = screen
        self.au_settings = au_settings

        #Загрузка изображения предателя и назначение атрибута rect.
        self.image = pygame.image.load('images/aur.png')
        self.rect = self.image.get_rect()

        #Каждый новый предатель появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохранение точной позиции прищельца
        self.x = float(self.rect.x)
        
    def blitme(self):
        #Выводит предателя в текущем положении
        self.screen.blit(self.image,self.rect)
        
