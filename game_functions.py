import sys
import pygame

def check_events():
    #Обрабатывает нажатие клавиш и события мыши
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def update_screen(au_settings, screen, amongus):
        screen.fill(au_settings.bg_color)
        amongus.blitme()

        #Отображение последнего прорисованного экрана
        pygame.display.flip()
