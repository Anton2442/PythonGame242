import pygame, sys

def events(screen):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update(bg, screen):
    """обновление экрана"""
    screen.blit(bg, (0 ,0))
    pygame.display.flip()