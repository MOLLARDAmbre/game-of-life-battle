from cell import Cell
from random import randint

class Player():

    def test(self, board, player):
        """
        This function allows you to set the board to your initialisation position
        :param board: 2D array of cells
        :param player: Either Cell.PLAYER1 or Cell.PLAYER2 depending on which player you are
        :return: 2D array of cells initialised
        """
        return board

    def preprocessing(self, board, player):
        """
        This function allows you to have time to preprocess stuff before the game starts
        :param board: 2D array of cells
        :param player: Either Cell.PLAYER1 or Cell.PLAYER2 depending on which player you are
        :return: None
        """
        return

    def turn(self, board, player):
        """
        This is the turn function
        You should return one value which will either be a kill or a spawn of a cell depending on what the board contains at the index
        :param board: 2D array of cells
        :param player: Either Cell.PLAYER1 or Cell.PLAYER2 depending on which player you are
        :return: (x, y) tuple with the coordinates of the cell to change
        """
        x = randint(0, len(board) - 1)
        y = randint(0, len(board[0]) - 1)
        return (0, 0)
