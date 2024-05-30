import pygame, controls
from bg import Background
from pygame.sprite import Group
from turn_indicator import Turn_indicator
from text import Turn_text


def run():
    """основная функция, запускающая игру"""
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Крестики-нолики")
    bg = Background(screen)
    marks = Group()
    controls.create_marks(screen, marks)
    sc = controls.create_scores(screen)
    turn_indicator = Turn_indicator(screen)
    turn_text = Turn_text(screen)

    while True:
        """основной цикл"""
        controls.events(marks, sc, turn_indicator)
        controls.update(bg, screen, marks, sc, turn_indicator, turn_text)

run()