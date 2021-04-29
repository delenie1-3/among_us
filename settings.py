import sys
import pygame

class Settings():
    #Класс для хранения всех настроек игры

    def __init__(self):#,amongus_speed_factor
        #Инициализирует настройки игры
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230,230,230)#(77,143,172)
        #Настройки каробля
        #self.amongus_speed_factor = 1.5
