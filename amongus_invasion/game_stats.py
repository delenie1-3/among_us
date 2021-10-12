class GameStats():
    #статистика игры
    def __init__(self, au_game):
        #инициализация статистики
        self.settings = au_game.settings
        self.reset_stats()

    def reset_stats(self):
        #инициализация
        self.aubs_left = self.settings.aub_limit