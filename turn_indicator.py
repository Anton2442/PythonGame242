import pygame

class Turn_indicator(pygame.sprite.Sprite):

    def __init__(self, screen):
        """инициализируем индикатор хода"""
        super(Turn_indicator, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 150, 150)
        self.color_cross = (217, 36, 36)
        self.color_zero = (53, 0, 247)
        self.color = self.color_cross
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom - 20
        self.rect.left = self.screen_rect.left + 20

    def change_turn(self):
        """меняем цвет индикатора"""
        if self.color == self.color_cross:
            self.color = self.color_zero
        else:
            self.color = self.color_cross

    def draw(self):
        """рисуем индикатор на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)