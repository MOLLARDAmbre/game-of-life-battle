import copy
import random
from cellular_automata_rules import next_step_cell
from cell import Cell

def init_board(density, width, height):
    """
    Initialises a board
    :param density: float between 0 and 1, representing how many cells are alive at the start at most
    :return: 2D array of cells, randomly put on the field
    """
    board = [[Cell.DEAD for i in range(width)] for j in range(height)]
    for i in range(int(width * height * density)):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        board[y][x] = Cell.ALIVE
    return board

def next(board):
    """
    Runs one step of the cellular automata
    :param board: 2D array of cells, representing the initial state of the board
    :return: 2D array of cells, representing the next state
    """
    next_board = copy.deepcopy(board)  # All cells evolve at the same time so we store their next state before updating them all
    for i in range(len(board)):
        for j in range(len(board[0])):
            next_board[i][j] = next_step_cell([[board[(i+k) % len(board)][(j+l) % len(board[0])] for k in range(-1, 2)] for l in range(-1, 2)])  # Gets the neighborhood of the cell, including itself
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = next_board[i][j]  # Updates the initial board
    return board
