import sys
from time import sleep
import pygame
from os import path
from settings import Settings
from aub import AmongUsBlue
from pygame.sprite import Sprite
from bullet import Bullet
from traitor import Traitor
from game_stats import GameStats
from button import Button

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

        self.stats = GameStats(self)#экземпляр игровой статистики

        self.aub = AmongUsBlue(self.screen)#экземпляр амонга
        self.bullets = pygame.sprite.Group()#экземпляр снаряда
        self.traitors = pygame.sprite.Group()#экземпляр предателя

        self._create_fleet()

        self.background = pygame.image.load(path.join(self.img_dir, 'sky.png')).convert()#путь к фону
        self.background_rect = self.background.get_rect()#загрузка фона

        #Создание кнопки
        self.play_button = Button(self, 'Play')
  
    def run_game(self):#запуск игры
        while True:
            self._check_events()
            if self.stats.game_active:
                self.aub.update()
                self.bullets.update()#обновление снаряда
                self._update_bullets()
                self._update_traitors()#обновление позиции предателя
            self._update_screen()

    def _aub_hit(self):#обработка столкновения амонга с предателем
        if self.stats.aubs_left > 0:
            #уменьшение кол-ва амонгов
            self.stats.aubs_left -= 1

            #очистка списка предателей и снарядов
            self.traitors.empty()
            self.bullets.empty()

            #создание нового флота и размещение амонга в центре
            self._create_fleet()
            self.aub.center_aub()

            #пауза
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_bullets(self):#проверка позиции и удаление снарядов
        #удаление снарядов
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))проверка удаления снарядов

        self._check_bullet_traitor_collisions()

    def _check_bullet_traitor_collisions(self):
        #Проверка поподание снарядом
        #удаление предателя
        collisions = pygame.sprite.groupcollide(self.bullets, self.traitors, True, True)
        if not self.traitors:
            #уничтожение снарядов и создание нового флота
            self.bullets.empty()
            self._create_fleet()

    def _check_traitors_bottom(self):
        #проверка достижения нижнего края экрана предателем
        screen_rect = self.screen.get_rect()
        for traitor in self.traitors.sprites():
            if traitor.rect.bottom >= screen_rect.bottom:
                #аналогия со столкновением с амогом
                self._aub_hit()
                break

    def _update_traitors(self):#проверка достижения края
        #обновление позиций всех предателей
        self._check_fleet_edges()
        self.traitors.update()

        #проверка коллизии "придатель - амонг"
        if pygame.sprite.spritecollideany(self.aub, self.traitors):
            self._aub_hit()

        #проверка, достижения предателями нижнего края экрана
        self._check_traitors_bottom()

    def _check_events(self):#отслеживание клавиатуры и мыши
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:#ПРОВЕРКА НАЖАТИЯ КЛАВИШИ
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:#проверка отпускания
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        #Запуск новой игры при нажатии на Play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #сброс игровой статистики
            self.stats.reset_stats()
            self.stats.game_active = True

            #очистка списка предателей и снарядов
            self.traitors.empty()
            self.bullets.empty()

            #создание нового флота и ...
            self._create_fleet()
            self.aub.center_aub()


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

    def _create_fleet(self):#создание флота предателей
        # Создание предателя и вычисление количества предателя в ряду
        # Интервал между соседними предателями равен ширине предателя
        traitor = Traitor(self)
        traitor_width, traitor_height = traitor.rect.size
        avialable_space_x = self.settings.screen_width - (2 * traitor_width)
        number_traitors_x = avialable_space_x // (2 * traitor_width)

        #кол-во радов на экран
        aub_height = self.aub.rect.height
        avialable_space_y = (self.settings.screen_height - (3 * traitor_height) - aub_height)
        number_rows = avialable_space_y // (2 * traitor_height)

        #создание флот предателей
        for row_number in range(number_rows):
            for traitor_number in range(number_traitors_x):
                self._create_traitor(traitor_number, row_number)

    def _create_traitor(self, traitor_number, row_number):
        #создание предателя и размещения его в ряду
        traitor = Traitor(self)
        traitor_width, traitor_height = traitor.rect.size
        traitor.x = traitor_width + 2 * traitor_width * traitor_number
        traitor.rect.x = traitor.x
        traitor.rect.y = traitor.rect.height + 2 * traitor.rect.height * row_number
        self.traitors.add(traitor)

    def _check_fleet_edges(self):#реагирует на достижение края экрана предателем
        for traitor in self.traitors.sprites():
            if traitor.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):#снижение и смена направления флота
        for traitor in self.traitors.sprites():
            traitor.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        #self.screen.fill('BLACK')#цвет фона
        self.screen.blit(self.background, self.background_rect)#наложение фона
        self.aub.blitme()#вывод амонга на экран
        #all_sprites.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.traitors.draw(self.screen)#отображение пришельца на экране

        #Кнопка play отображается если игра не активна
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()#отображение прорисованного экрана


if __name__ == '__main__':#создание экземпляра и запуск игры
    ai = AmongusInvasion()
    ai.run_game()
