import sys
import pygame
from os import path
from settings import Settings
from aub import AmongUsBlue
from pygame.sprite import Sprite
from bullet import Bullet

class AmongusInvasion():#класс для управления поведением игры и ресурсами
    def __init__(self):#инициализация игры и ресурсов
        pygame.init()
        self.img_dir = path.join(path.dirname(__file__), 'img')#определение папки с изображениями

        self.settings = Settings()#экземпляр настроек
        '''полнооконный режим. требует дороботки
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        '''
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#размер окна
        pygame.display.set_caption('Among Us вторжение')

        self.aub = AmongUsBlue(self.screen)#экземпляр амонга
        self.bullets = pygame.sprite.Group()#экземпляр снаряда

        self.background = pygame.image.load(path.join(self.img_dir, 'sky.png')).convert()#путь к фону
        self.background_rect = self.background.get_rect()#загрузка фона
  
    def run_game(self):#запуск игры
        while True:
            self._check_events()
            self.aub.update()
            self.bullets.update()#обновление снаряда
            #удаление снарядов
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            #print(len(self.bullets))проверка удаления снарядов
            self._update_screen()

            

    def _check_events(self):#отслеживание клавиатуры и мыши
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:#ПРОВЕРКА НАЖАТИЯ КЛАВИШИ
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:#проверка отпускания
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            #перемещение вправо-влево
            self.aub.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.aub.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:#выстрел пробелом
            self._fire_bullet()

    def _fire_bullet(self):#новый снаряд
        if len(self.bullets) < self.settings.bullets_allowed:#проверка количества одновременных снарядов
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _check_keyup_events(self, event):
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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()#отображение прорисованного экрана


if __name__ == '__main__':#создание экземпляра и запуск игры
    ai = AmongusInvasion()
    ai.run_game()
