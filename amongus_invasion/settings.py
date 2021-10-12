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