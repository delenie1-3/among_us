import pygame
from os import path
from pygame.sprite import Sprite

class Traitor(Sprite):#класс предателя
    def __init__(self, au_game):#инициализация и позиционирование
        super().__init__()
        self.img_dir = path.join(path.dirname(__file__), 'img')#определение папки с изображениями
        self.screen = au_game.screen

        #изоборажение предателя
        self.image = pygame.image.load(path.join(self.img_dir, 'aur.png')).convert()#путь к амонгу
        self.rect = self.image.get_rect()
        #появление предателя в вкрхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #сохранение точной позиции
        self.x = float(self.rect.x)

