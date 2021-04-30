import sys
import pygame
from bullet import Bullet
from traitor import Traitor

def check_keydown_events(event,au_settings,screen,amongus,bullets):
    #Реагирует на нажатие клавиш.
    if event.key == pygame.K_RIGHT:
        #Переместить персонажа вправо
        amongus.moving_right = True
    elif event.key == pygame.K_LEFT:
        amongus.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(au_settings,screen,amongus,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(au_settings,screen,amongus,bullets):
    #Выпускает пулю, если максимум ещё не достигнут.
    #Создание новыой пули и вкл. её в группу bullets/
    if len(bullets) < au_settings.bullets_allowed:
        new_bullet = Bullet(au_settings,screen,amongus)
        bullets.add(new_bullet)

def check_keyup_events(event,amongus):
    #Реагирует на отпускание клавиш.
    if event.key == pygame.K_RIGHT:
        amongus.moving_right = False
    elif event.key == pygame.K_LEFT:
        amongus.moving_left = False
        
def check_events(au_settings,screen,amongus,bullets):
    #Обрабатывает нажатие клавиш и события мыши
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,au_settings,screen,amongus,bullets)            
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,amongus)

def update_screen(au_settings,screen,amongus,traitors,bullets):
        screen.fill(au_settings.bg_color)
        #Все пули выводятся позади изображения персонажей
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        amongus.blitme()
        traitors.draw(screen)

        #Отображение последнего прорисованного экрана
        pygame.display.flip()

def update_bullets(bullets):
    #Обновление поз.пуль и уничтожение старых
    #Обновление поз.пуль
    #Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets)) Проверка удаления

def create_fleet(au_settings,screen,traitors):
    #Создаёт флот предателей
    #Создёт предателя и вычесляет количество пришельцев в ряду
    #Интервал между соседними предателями равен одной ширине предателя

    traitor = Traitor(au_settings,screen)
    traitor_width = traitor.rect.width
    avialable_space_x = au_settings.screen_width - 2*traitor_width
    number_traitors_x = int(avialable_space_x / (2*traitor_width))

    #Создание первого ряда предателей.
    for traitor_number in range(number_traitors_x):
        #Создание предателя и размещение его вряду.
        traitor = Traitor(au_settings,screen)
        traitor.x = traitor_width + 2*traitor_width*traitor_number
        traitor.rect.x = traitor.x
        traitors.add(traitor)
