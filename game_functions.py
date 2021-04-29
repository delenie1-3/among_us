import sys
import pygame

def check_keydown_events(event,amongus):
    #Реагирует на нажатие клавиш.
    if event.key == pygame.K_RIGHT:
        #Переместить персонажа вправо
        amongus.moving_right = True
    elif event.key == pygame.K_LEFT:
        amongus.moving_left = True

def check_keyup_events(event,amongus):
    #Реагирует на отпускание клавиш.
    if event.key == pygame.K_RIGHT:
        amongus.moving_right = False
    elif event.key == pygame.K_LEFT:
        amongus.moving_left = False
        
def check_events(amongus):
    #Обрабатывает нажатие клавиш и события мыши
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,amongus)            
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,amongus)

def update_screen(au_settings, screen, amongus):
        screen.fill(au_settings.bg_color)
        amongus.blitme()

        #Отображение последнего прорисованного экрана
        pygame.display.flip()
