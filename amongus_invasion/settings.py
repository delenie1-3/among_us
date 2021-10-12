class Settings():#класс настроек игры
    def __init__(self):#иницализация статических настроек
        #параметры экрана
        self.screen_width = 1000
        self.screen_height = 750
        self.bg_color = ('BLACK')
        
        #настройки амонга
        self.aub_speed = 0.5
        self.aub_limit = 3

        #Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = ('red')
        self.bullets_allowed = 3

        #настройка предателей
        self.traitor_speed = 0.1#скорость флота
        self.fleet_drop_speed = 10

        #Темп ускорения игры
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #Инициализация настроек, изменяющихся в ходе игры
        self.aub_speed = 1.5
        self.bullet_speed = 3.0
        self.traitor_speed = 0.1
        #fleet_direction = 1 вправо, -1 влево
        self.fleet_direction = 1

    def increase_speed(self):
        #Увилечение настройки скорости
        self.aub_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.traitor_speed *= self.speedup_scale
