import pygame.font

class Scoreboard():
    #класс вывода игровой информации
    def __init__(self, au_game):
        self.screen = au_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = au_game.settings
        self.stats = au_game.stats

        #Настройка шрифта
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        #подготовка изображения
        self.prep_score()

    def prep_score(self):#преобразование в изображение
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #вывод счета в правом верхнем углу
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #ввыводит счет на экран
        self.screen.blit(self.score_image, self.score_rect)