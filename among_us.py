import sys

import pygame

from amongus import AmongUs

def run_game():
    #Инициализация игры и создание объекта
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    #Назначение цвета фона
    bg_color = (230,230,230)
    umngus = AmongUs(screen)

    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(bg_color)
            umngus.blitme()

        #Отображение последнего прорисованного экрана
        pygame.display.flip()
run_game()
