import pygame
from os import path
from pygame.sprite import Sprite
from settings import Settings

class Traitor(Sprite):#класс предателя
    def __init__(self, au_game):#инициализация и позиционирование
        super().__init__()
        self.img_dir = path.join(path.dirname(__file__), 'img')#определение папки с изображениями
        self.screen = au_game.screen
        self.settings = au_game.settings

        #изоборажение предателя
        self.image = pygame.image.load(path.join(self.img_dir, 'aur.png')).convert()#путь к амонгу
        self.rect = self.image.get_rect()
        #появление предателя в вкрхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #сохранение точной позиции
        self.x = float(self.rect.x)

    def check_edges(self):#провкерка края экрана и возвращение Turue
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):#перемещение предателей вправо и влево
        self.x += (self.settings.traitor_speed * self.settings.fleet_direction)
        self.rect.x = self.x