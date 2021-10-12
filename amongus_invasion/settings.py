class Settings():#класс настроек игры
    def __init__(self):#иницализация настроек
        #параметры экрана
        self.screen_width = 1000
        self.screen_height = 750
        
        #настройки амонга
        self.aub_speed = 0.5

        #Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = ('red')
        self.bullets_allowed = 3

        #настройка предателей
        self.traitor_speed = 0.1#скорость флота
        self.fleet_drop_speed = 100
        #fleet_direction = 1 вправо, -1 влево
        self.fleet_direction = 1