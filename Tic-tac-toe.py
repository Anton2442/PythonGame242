import pygame, controls
from bg import Background
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Крестики-нолики")
    bg = Background(screen)
    marks = Group()
    controls.create_marks(screen, marks)
    sc = controls.create_scores(screen)

    while True:
        controls.events(marks)
        controls.update(bg, screen, marks, sc)


run()