import pygame

class AmongUs():

    def __init__(self,screen):
        #Инициализирует персонажа и задаёт его начальную позицию.
        self.screen = screen

        #Загрузка изображения персонажа и получения прямоугольника.
        self.image = pygame.image.load('images/aub.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый персонаж появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        #Рисует персонажа в текущей позиции.
        self.screen.blit(self.image,self.rect)
