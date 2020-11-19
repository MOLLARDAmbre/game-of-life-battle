"""
This files explicitly exposes utility functions
"""

from cell import Cell
from cellular_automata import next


def other_player(cell_color):
    if (cell_color == Cell.PLAYER1):
        return Cell.PLAYER2
    if (cell_color == Cell.PLAYER2):
        return Cell.PLAYER1
    return None # Should never be reached

def next_board_state(board):
    return next(board)
