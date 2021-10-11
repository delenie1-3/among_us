import sys
import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img')#определение папки с изображениями


class AmongusInvasion:#класс для управления поведением игры и ресурсами
    def __init__(self):#инициализация игры и ресурсов
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 750))
        pygame.display.set_caption('Among Us вторжение')

        self.background = pygame.image.load(path.join(img_dir, 'sky.png')).convert()#путь к фону
        self.background_rect = self.background.get_rect()#загрузка фона

    def run_game(self):#запуск игры
        while True:#отслеживание клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill('BLACK')#цвет фона
            self.screen.blit(self.background, self.background_rect)#наложение фона
            #all_sprites.draw(self.screen)

            pygame.display.flip()#отображение прорисованного экрана

if __name__ == '__main__':#создание экземпляра и запуск игры
    ai = AmongusInvasion()
    ai.run_game()
