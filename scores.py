import pygame.font


class Scores():
    """вывод игровой информации"""
    def __init__(self, screen):
        """инициализируем подсчёт очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.score = 0
        self.x_positions = [279, 389]
        self.y = 66
        self.text_color_cross = (217, 36, 36)
        self.text_color_zero = (53, 0, 247)
        self.text_color = self.text_color_cross
        self.font = pygame.font.SysFont(None, 120)
        self.image_score()

    def image_score(self):
        """преобразовывает текст счёта в графическое изображение"""
        self.score_img = self.font.render(str(self.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        if self.text_color == self.text_color_cross:
            self.score_rect.centerx = self.x_positions[0]
        else:
            self.score_rect.centerx = self.x_positions[1]
        self.score_rect.centery = self.y

    def show_score(self):
        """вывод счёта на экран"""
        self.screen.blit(self.score_img, self.score_rect)

    def add_score(self):
        self.score += 1
        self.image_score()

