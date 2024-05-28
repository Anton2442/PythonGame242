import pygame

class Mark(pygame.sprite.Sprite):
    """класс меток"""

    def __init__(self, screen, row, col):
        """инициализируем метку (пока что пустую)"""
        super(Mark, self).__init__()
        self.lifes = 3
        self.player = 0
        self.screen = screen
        self.image_empty = pygame.image.load("images/empty_image.png")
        self.image_zero = pygame.image.load("images/zero.png")
        self.image_cross = pygame.image.load("images/cross.png")
        self.image_zero_transparent = pygame.image.load("images/zero_transparent.png")
        self.image_cross_transparent = pygame.image.load("images/cross_transparent.png")
        self.image = self.image_empty
        self.rect = self.image.get_rect()
        self.row = row
        self.col = col
        self.row_pos = [175, 286, 398]
        self.col_pos = [180, 286, 394]
        self.rect.x, self.rect.y = self.row_pos[col], self.col_pos[row]

    def draw(self):
        """вывод метки на экран"""
        self.screen.blit(self.image, self.rect)
