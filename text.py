import pygame.font


class Turn_text():
    """класс для текстовой подписи над индикатором"""
    def __init__(self, screen):
        """инициализируем текст"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Calibri", 30)
        self.text = "Сейчас ходит:"
        self.image_text()

    def image_text(self):
        """преобразовывает текст в графическое изображение"""
        self.text_img = self.font.render(self.text, True, self.text_color, (0, 0, 0))
        self.text_rect = self.text_img.get_rect()
        self.text_rect.left = self.text_rect.left + 10
        self.text_rect.bottom = self.screen_rect.bottom - 180

    def show_text(self):
        """вывод надписи на экран"""
        self.screen.blit(self.text_img, self.text_rect)
