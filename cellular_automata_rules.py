from cell import Cell

def next_step_cell(neighborhood):
    """
    Specifies the algorithm to update a cell at each step
    :param neighborhood: 3 * 3 array of cells constituing the neighborhood of the cell to update
    :return: cell in the state it will be after the step
    """
    neighbors = get_neighbors(neighborhood)
    nb_neighbors = neighbors[Cell.ALIVE] + neighbors[Cell.PLAYER1] + neighbors[Cell.PLAYER2]
    if nb_neighbors == 2:
        if neighborhood[1][1] == Cell.DEAD:
            return Cell.DEAD
        if neighbors[Cell.PLAYER1] == 2:
            if neighborhood[1][1] in [Cell.ALIVE, Cell.PLAYER1]:
                return Cell.PLAYER1
            return Cell.DEAD
        if neighbors[Cell.PLAYER2] == 2:
            if neighborhood[1][1] in [Cell.ALIVE, Cell.PLAYER2]:
                return Cell.PLAYER2
            return Cell.DEAD
        return neighborhood[1][1]
    if nb_neighbors < 2:
        return Cell.DEAD
    if nb_neighbors == 3:
        if (neighbors[Cell.PLAYER1] >= 2 and neighborhood[1][1] == Cell.PLAYER2):
            return Cell.DEAD
        if (neighbors[Cell.PLAYER2] >= 2 and neighborhood[1][1] == Cell.PLAYER1):
            return Cell.DEAD
        if (neighbors[Cell.PLAYER1] > neighbors[Cell.PLAYER2]):
            return Cell.PLAYER1
        if (neighbors[Cell.PLAYER2] > neighbors[Cell.PLAYER1]):
            return Cell.PLAYER2
        return Cell.ALIVE
    if nb_neighbors > 3:
        # if (neighborhood[1][1] == Cell.PLAYER1):
        #     if (neighbors[Cell.PLAYER1] - neighbors[Cell.PLAYER2] >= 2):
        #         return Cell.PLAYER1
        #     if (neighbors[Cell.PLAYER2] - neighbors[Cell.PLAYER1] >= 2):
        #         return Cell.PLAYER2
        # if (neighborhood[1][1] == Cell.PLAYER2):
        #     if (neighbors[Cell.PLAYER2] - neighbors[Cell.PLAYER1] >= 2):
        #         return Cell.PLAYER2
        #     if (neighbors[Cell.PLAYER1] - neighbors[Cell.PLAYER2] >= 2):
        #         return Cell.PLAYER1
        return Cell.DEAD

def get_neighbors(neighborhood):
    d = {Cell.DEAD: 0, Cell.ALIVE: 0, Cell.PLAYER1: 0, Cell.PLAYER2: 0}
    for i in range(len(neighborhood)):
        for j in range(len(neighborhood[0])):
            if (i != 1 or j != 1):
                d[neighborhood[i][j]] += 1
    return d
