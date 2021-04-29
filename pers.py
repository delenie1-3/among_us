import pygame


class AmongUs():

    def __init__(self,screen):#,au_settings
        #Инициализирует персонажа и задаёт его начальную позицию.
        self.screen = screen
        #self.au_settings = au_settings

        #Загрузка изображения персонажа и получения прямоугольника.
        self.image = pygame.image.load('images/aub.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый персонаж появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Сохранение вещественной координаты центра коробля
        #self.center = float(self.rect.centerx)
        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Обновляет позицию персонажа с учетом флага
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1#self.au_settings.amongus_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1#self.au_settings.amongus_speed_factor
        #Обновление атрибута rect на основании self.center
        #self.rect.centerx = self.center
        
    
    def blitme(self):
        #Рисует персонажа в текущей позиции.
        self.screen.blit(self.image,self.rect)
