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


def _get_neighbors(matrix, i, j):
    if i == 0 and j == 0:
        pass  # top left
    elif i == 0 and j == len(matrix[0]):
        pass  # top right
    elif i == len(matrix) and j == 0:
        pass  # left bottom
    elif i == len(matrix) and j == len(matrix[0]):
        pass  # right bottom
    elif i == 0:
        pass  # top
    elif i == len(matrix):
        pass  # bottom
    elif j == 0:
        pass  # left
    elif j == len(matrix[0]):
        pass  # right
    else:
        pass 
    diag_top_left_neighbor = matrix[i-1][j-1]
    print(diag_top_left_neighbor)
    top_neighbor = matrix[i-1][j]
    print(top_neighbor)
    diag_top_right_neighbor = matrix[i-1][j+1]
    print(diag_top_right_neighbor)
    right_neighbor = matrix[i][j+1]
    print(right_neighbor)
    diag_bottom_right_neighbor = matrix[i+1][j+1]
    print(diag_bottom_right_neighbor)
    bottom_neighbor = matrix[i+1][j]
    print(bottom_neighbor)
    diag_bottom_left_neighbor = matrix[i+1][j-1]
    print(diag_bottom_left_neighbor)
    left_neighbor = matrix[i][j-1]
    print(left_neighbor)


def conway_rules(starting_matrix):
    for i in range(0, len(starting_matrix)):
        for j in range(0, len(starting_matrix[0])):
            pass


_get_neighbors(matrix=TEST_START_MATRIX, i=0, j=0)
# print(TEST_START_MATRIX[3][3+1]) # right
# print(TEST_START_MATRIX[3+1][3]) # bottom
# print(TEST_START_MATRIX[3+1][3+1]) # diagonal bottom right
# print(TEST_START_MATRIX[3][3-1]) # left
# print(TEST_START_MATRIX[3-1][3]) # top
# print(TEST_START_MATRIX[3+1][3-1]) # diagonal bottom left
# print(TEST_START_MATRIX[3-1][3-1]) # diagonal top left
# print(TEST_START_MATRIX[3-1][3+1]) # diagonal top right