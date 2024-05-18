import pygame

class Mark(pygame.sprite.Sprite):
    """класс меток"""

    def __init__(self, screen, row, col):
        """инициализируем метку (пока что пустую)"""
        super(Mark, self).__init__()
        self.screen = screen
        self.image_none = pygame.image.load("images/empty_image.png")
        self.image_zero = pygame.image.load("images/zero.png")
        self.image_cross = pygame.image.load("images/cross.png")
        self.image = self.image_none
        self.rect = self.image.get_rect()
        self.row_pos = [175, 286, 398]
        self.col_pos = [180, 286, 394]
        self.rect.x, self.rect.y = self.row_pos[col], self.col_pos[row]

    def draw(self):
        """вывод метки на экран"""
        self.screen.blit(self.image, self.rect)
