import sys
import pygame

def check_events(amongus):
    #Обрабатывает нажатие клавиш и события мыши
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Переместить персонажа вправо
                    amongus.moving_right = True
                elif event.key == pygame.K_LEFT:
                    amongus.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    amongus.moving_right = False
                elif event.key == pygame.K_LEFT:
                    amongus.moving_left = False

def update_screen(au_settings, screen, amongus):
        screen.fill(au_settings.bg_color)
        amongus.blitme()

        #Отображение последнего прорисованного экрана
        pygame.display.flip()
