import pygame, controls

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Крестики-нолики")
    bg = pygame.image.load("images/bg_game.png")

    while True:
        controls.events(screen)
        controls.update(bg, screen)

run()