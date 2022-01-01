import random

MATRIX_VALUES = (0, 1)


def build_2d_array(width, height):
    matrix = [[random.choice(MATRIX_VALUES) for x in range(width)] for y in range(height)]
    return matrix


"""
Example Matrix:
[
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