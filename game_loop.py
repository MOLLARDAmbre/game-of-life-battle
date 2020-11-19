import pygame
import copy
from pygame.locals import *
from board import Board
from time_wrapper import limit_time
from cell import Cell

def sanitize_moves(p1_move, p2_move, board):
    """
    Makes sure the moves sent by the players are in the correct format
    :param p1_move: array with the two coordinates for p2's move
    :param p2_move: array with the two coordinates for p1's move
    :return: p1 and p2 moves, set to None if they are invalid
    """
    try:
        [a, b] = p1_move
        assert (a >= 0 and a < board.height)
        assert (b >= 0 and b < board.width)
    except:
        p1_move = None
    try:
        [a, b] = p2_move
        assert (a >= 0 and a < board.height)
        assert (b >= 0 and b < board.width)
    except:
        p2_move = None
    return p1_move, p2_move

def exit(board):
    pygame.quit()
    return board.get_results()

def game(player1, player2, width, height, col, ui, synchr, nb_moves, density, test):
    if ui:
        pygame.init()
        clock = pygame.time.Clock()
        FPS = 4

    board = Board(width=width, height=height, colors=col, density=density, ui=ui)

    p1 = __import__(player1, globals(), locals(), ['Player'], 0).Player()
    p2 = __import__(player2, globals(), locals(), ['Player'], 0).Player()

    if test:
        board.set_board(p1.test(board.automata, Cell.PLAYER1))

    limit_time(lambda: p1.preprocessing(copy.deepcopy(board.automata), Cell.PLAYER1), 1)
    limit_time(lambda: p2.preprocessing(copy.deepcopy(board.automata), Cell.PLAYER2), 1)

    while True:  # Game loop
        p1_move = limit_time(lambda: p1.turn(copy.deepcopy(board.automata), Cell.PLAYER1), 0.2)
        p2_move = limit_time(lambda: p2.turn(copy.deepcopy(board.automata), Cell.PLAYER2), 0.2)
        p1_move, p2_move = sanitize_moves(p1_move, p2_move, board)
        board.play(p1_move, p2_move)
        if ui:
            board.draw_cells()
            pygame.display.update()
        board.next()
        nb_moves -= 1
        if nb_moves == 0:
            return exit(board)
        if ui:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return exit(board)
        if not synchr and ui:
            clock.tick(FPS)
