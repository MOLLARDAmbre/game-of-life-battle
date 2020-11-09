import pygame
from colors import Colors
import cellular_automata
from cell import Cell


class Board():

    def __init__(self, colors=Colors(), density=0.2, ui=True, width = 15, height = 15, width_mul = 20, height_mul = 20):
        self.colors = colors
        self.width = width  # Width of the board
        self.height = height  # Height of the board
        self.width_mul = width_mul  # Horizontal lenght of a cell
        self.height_mul = height_mul  # Vertical length of a cell
        self.automata = cellular_automata.init_board(density, self.width, self.height)
        self.ui = ui
        if self.ui:
            self.display_surface = pygame.display.set_mode((width * width_mul, height * height_mul))
            self.display_surface.fill(self.colors.WHITE)
            self.draw_grid()

    def draw_grid(self):
        for i in range(self.width):
            pygame.draw.line(self.display_surface, self.colors.BLACK, (i * self.width_mul, 0), (i * self.width_mul, self.height * self.height_mul))
        for i in range(self.height):
            pygame.draw.line(self.display_surface, self.colors.BLACK, (0, i * self.height_mul), (self.width * self.width_mul, i * self.height_mul))

    def draw_cells(self):
        for i in range(len(self.automata)):
            for j in range(len(self.automata[0])):
                cell = self.automata[i][j]
                if cell == Cell.DEAD:
                    col = self.colors.WHITE
                if cell == Cell.ALIVE:
                    col = self.colors.BLACK
                if cell == Cell.PLAYER1:
                    col = self.colors.PLAYER1
                if cell == Cell.PLAYER2:
                    col = self.colors.PLAYER2
                pygame.draw.rect(self.display_surface, col, (j * self.width_mul + 1, i * self.height_mul + 1, self.width_mul - 1, self.height_mul - 1))

    def next(self):  # Update the cellular automata beneath
        self.automata = cellular_automata.next(self.automata)

    def play(self, p1, p2):
        """
        Adds the move played by the players to the grid
        """
        if (p1 == p2):
            return
        if (p1 != None):
            if (self.automata[p1[0]][p1[1]] == Cell.DEAD):
                self.automata[p1[0]][p1[1]] = Cell.PLAYER1
            else:
                self.automata[p1[0]][p1[1]] = Cell.DEAD
        if (p2 != None):
            if (self.automata[p2[0]][p2[1]] == Cell.DEAD):
                self.automata[p2[0]][p2[1]] = Cell.PLAYER2
            else:
                self.automata[p2[0]][p2[1]] = Cell.DEAD

    def get_results(self):
        points = {"p1": 0, "p2": 0}
        for i in range(len(self.automata)):
            for j in range(len(self.automata[0])):
                if (self.automata[i][j] == Cell.PLAYER1):
                    points["p1"] += 1
                if (self.automata[i][j] == Cell.PLAYER2):
                    points["p2"] += 1
        return points
