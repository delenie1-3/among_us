import sys

import pygame
from pygame.sprite import Group

from pers import AmongUs
from settings import Settings
import game_functions as fg

def run_game():
    #Инициализация игры и создание объекта
    pygame.init()
    au_settings = Settings()
    screen = pygame.display.set_mode((au_settings.screen_width, au_settings.screen_height))
    pygame.display.set_caption("Amon Us для Илюши!!!")
    #Назначение цвета фона
    amongus = AmongUs(screen)#au_settings
    bullets = Group()
    #Создание персонажа
    #among_us_blue = AmongUs(au_settings,screen)

    #Запуск основного цикла игры
    while True:
        fg.check_events(au_settings,screen,amongus,bullets)
        amongus.update()
        bullets.update()
        fg.update_bullets(bullets)
        fg.update_screen(au_settings,screen,amongus,bullets)
      
run_game()
