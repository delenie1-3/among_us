class GameStats():
    #статистика игры
    def __init__(self, au_game):
        #инициализация статистики
        self.settings = au_game.settings
        self.reset_stats()
        self.game_active = False#Запуск игры в активном режиме

    def reset_stats(self):
        #инициализация
        self.aubs_left = self.settings.aub_limit
        self.score = 0