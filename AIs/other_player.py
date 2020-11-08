from cell import Cell
from random import randint

class Player():

    def preprocessing(self, board):
        """
        This function allows you to have time to preprocess stuff before the game starts
        :param board: 2D array of cells
        :return: None
        """
        return

    def turn(self, board):
        """
        This is the turn function
        You should return one value which will either be a kill or a spawn of a cell depending on what the board contains at the index
        :param board: 2D array of cells
        :return: (x, y) tuple with the coordinates of the cell to change
        """
        x = randint(0, len(board) - 1)
        y = randint(0, len(board[0]) - 1)
        return (0, 0)
