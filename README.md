# game-of-life-battle
A game based on Conway's Game of Life, made into a 1v1 game. The idea is that players will code an ia for it, not play it by themselves

The rules are slightly different from the base game of life

First of, a cell can be alive, dead or be alive and be of the color of a player. A player can "convert" alive cells to their color (by having several cells of their color around other cells, or just more than their opponent)
Second, each turn, each player can either kill a cell, or spawn one of their cells anywhere on the field. If both players play on the same spot, the turn is skipped.

After a certain amount of moves (defaults to 250), the game is over, the winner is the one with the most cells fo their color
