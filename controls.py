import pygame, sys
from mark import Mark

turn = 1

def events(marks):
    """обработка событий"""
    global turn
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # выход из игры
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # обработка клика мышкой
            mouse_pos = event.pos
            for mark in marks:
                if mark.rect.collidepoint(mouse_pos):
                    if turn == 1:
                        mark.image = mark.image_cross
                        turn = 2
                    else:
                        mark.image = mark.image_zero
                        turn = 1

def create_marks(screen, marks):
    """Создание позиций для крестиков и ноликов"""
    for row in range(3):
        for col in range(3):
            mark = Mark(screen, row, col)
            marks.add(mark)

def update(bg, screen, marks):
    """обновление экрана"""
    bg.draw()
    marks.draw(screen)
    pygame.display.flip()
