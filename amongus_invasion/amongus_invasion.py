import sys
import pygame
from os import path
from settings import Settings
from aub import AmongUsBlue

class AmongusInvasion():#класс для управления поведением игры и ресурсами
    def __init__(self):#инициализация игры и ресурсов
        pygame.init()
        self.img_dir = path.join(path.dirname(__file__), 'img')#определение папки с изображениями

        self.settings = Settings()#экземпляр настроек

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#размер окна
        pygame.display.set_caption('Among Us вторжение')

        self.aub = AmongUsBlue(self.screen)#экземпляр амонга

        self.background = pygame.image.load(path.join(self.img_dir, 'sky.png')).convert()#путь к фону
        self.background_rect = self.background.get_rect()#загрузка фона
  
    def run_game(self):#запуск игры
        while True:
            self._check_events()
            self.aub.update()
            self._update_screen()

            

    def _check_events(self):#отслеживание клавиатуры и мыши
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:#ПРОВЕРКА НАЖАТИЯ КЛАВИШИ
                    if event.key == pygame.K_RIGHT:
                        #перемещение вправо-влево
                        self.aub.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.aub.moving_left = True
                elif event.type == pygame.KEYUP:#проверка отпускания
                    if event.key == pygame.K_RIGHT:
                        #остановка
                        self.aub.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.aub.moving_left = False

    def _update_screen(self):
        #self.screen.fill('BLACK')#цвет фона
        self.screen.blit(self.background, self.background_rect)#наложение фона
        self.aub.blitme()#вывод амонга на экран
        #all_sprites.draw(self.screen)

        pygame.display.flip()#отображение прорисованного экрана


if __name__ == '__main__':#создание экземпляра и запуск игры
    ai = AmongusInvasion()
    ai.run_game()
