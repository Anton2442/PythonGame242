import pygame

class Background(pygame.sprite.Sprite):
    """Задний фон"""

    def __init__(self, screen):
        """инициализируем задний фон"""
        super(Background, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/bg_game.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw(self):
        """вывод заднего фона на экран"""
        self.screen.blit(self.image, self.rect)
