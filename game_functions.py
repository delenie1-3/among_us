import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,au_settings,screen,amongus,bullets):
    #Реагирует на нажатие клавиш.
    if event.key == pygame.K_RIGHT:
        #Переместить персонажа вправо
        amongus.moving_right = True
    elif event.key == pygame.K_LEFT:
        amongus.moving_left = True
    elif event.key == pygame.K_SPACE:
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

def update_screen(au_settings, screen, amongus, bullets):
        screen.fill(au_settings.bg_color)
        #Все пули выводятся позади изображения персонажей
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        amongus.blitme()

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
