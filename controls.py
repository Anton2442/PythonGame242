import pygame, sys
from mark import Mark
from scores import Scores
turn = 1
def events(marks, sc, turn_indicator):
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
                if mark.rect.collidepoint(mouse_pos) and mark.player == 0:
                    if turn == 1:
                        mark.image = mark.image_cross
                        mark.player = 1
                        change_marks_lifes(marks, mark.player)
                        turn = 2
                        turn_indicator.change_turn()
                    else:
                        mark.image = mark.image_zero
                        mark.player = 2
                        change_marks_lifes(marks, mark.player)
                        turn = 1
                        turn_indicator.change_turn()
                    check_win(marks, sc)
def update(bg, screen, marks, sc, turn_indicator, turn_text):
    """обновление экрана"""
    bg.draw()
    marks.draw(screen)
    for score in sc:
        score.show_score()
    turn_indicator.draw()
    turn_text.show_text()
    pygame.display.flip()

def create_marks(screen, marks):
    """Создание позиций для крестиков и ноликов"""
    for row in range(3):
        for col in range(3):
            mark = Mark(screen, row, col)
            marks.add(mark)

def create_scores(screen):
    """Создание счёта"""
    red_score = Scores(screen)
    blue_score = Scores(screen)
    blue_score.text_color = blue_score.text_color_zero
    blue_score.score_rect.centerx = blue_score.x_positions[1]
    blue_score.image_score()
    sc = [red_score, blue_score]
    return sc

def check_win(marks, sc):
    """Проверка на победу"""
    winner = None

    # Преобразование marks в матрицу для удобства проверки
    grid = [[None for _ in range(3)] for _ in range(3)]
    for mark in marks:
        grid[mark.row][mark.col] = mark.player

    # Проверка горизонтальных линий
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] != 0:
            winner = grid[row][0]

    # Проверка вертикальных линий
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != 0:
            winner = grid[0][col]

    # Проверка диагоналей
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != 0:
        winner = grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != 0:
        winner = grid[0][2]

    if winner and winner == 1:
        sc[0].add_score()
        clear_marks(marks)
    elif winner and winner == 2:
        sc[1].add_score()
        clear_marks(marks)

def clear_marks(marks):
    """очистка поля"""
    for mark in marks:
        mark.lifes = 3
        mark.player = 0
        mark.image = mark.image_empty

def change_marks_lifes(marks, player):
    """уменьшение жизней отметкам"""
    for mark in marks:
        if mark.player == player:
            mark.lifes -= 1
    check_marks_lifes(marks)

def check_marks_lifes(marks):
    """удаление отметок у которых не осталось жизней"""
    for mark in marks:
        if mark.lifes < 0:
            mark.lifes = 3
            mark.player = 0
            mark.image = mark.image_empty
        elif mark.lifes == 0:
            if mark.player == 1:
                mark.image = mark.image_cross_transparent
            else:
                mark.image = mark.image_zero_transparent


