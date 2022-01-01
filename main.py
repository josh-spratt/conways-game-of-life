from src.build_matrix import build_2d_array

START_MATRIX = build_2d_array(9, 9)

TEST_START_MATRIX = [
    [0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1]
]

"""
Conway's Rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""


def _get_neighbors(i, j):
    pass


def conway_rules(starting_matrix):
    for i in range(0, len(starting_matrix)):
        for j in range(0, len(starting_matrix[0])):
            print(starting_matrix[i][j])


conway_rules(TEST_START_MATRIX)
