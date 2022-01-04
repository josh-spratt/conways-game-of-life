from src.build_matrix import build_2d_array, initiate_tmp_matrix
from src.get_neighbors import get_neighbors
from matplotlib import pyplot

# Configuration
PLOT_GAME = True #Set this to true if you want to plot each frame as heatmap
FRAMES_TO_COMPUTE = 50 #Total number of frames to compute

# Matrix info
START_MATRIX = build_2d_array(9, 9)

# TEST_START_MATRIX = [
#     [0, 1, 0, 0, 1, 1, 0, 1, 0],
#     [1, 1, 1, 0, 1, 1, 0, 0, 1],
#     [0, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 0, 1, 1, 1, 1],
#     [0, 0, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 0, 1, 1, 1, 1],
#     [0, 0, 1, 1, 0, 0, 1, 0, 0],
#     [1, 1, 0, 0, 1, 0, 0, 1, 1],
#     [1, 0, 0, 1, 0, 1, 1, 1, 1]
# ]

GLIDER_TEST = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

"""
Conway's Rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""


def conway_rules(starting_matrix):
    tmp_matrix = initiate_tmp_matrix(width=len(starting_matrix[0]), height=len(starting_matrix))
    for i in range(0, len(starting_matrix)):
        for j in range(0, len(starting_matrix[0])):
            neighbors = get_neighbors(matrix=starting_matrix, i=i, j=j)
            if starting_matrix[i][j] == 1 and sum(neighbors) < 2:
                tmp_matrix[i][j] = 0
            elif starting_matrix[i][j] == 1 and 2 <= sum(neighbors) <= 3:
                tmp_matrix[i][j] = 1
            elif starting_matrix[i][j] == 1 and sum(neighbors) > 3:
                tmp_matrix[i][j] = 0
            elif starting_matrix[i][j] == 0 and sum(neighbors) == 3:
                tmp_matrix[i][j] = 1
            else:
                tmp_matrix[i][j] = starting_matrix[i][j]
    return tmp_matrix


# TODO: how to set this up in a while loop so that the function runs with the input parameter being the output of the function's last iteration (see below)
def main():
    current_matrix = GLIDER_TEST
    for i in range(0, FRAMES_TO_COMPUTE):
        if PLOT_GAME:
            pyplot.imshow(current_matrix)
            pyplot.show(block=False)
            pyplot.pause(0.125)
            pyplot.close('all')
        current_matrix = conway_rules(current_matrix)

            
if __name__ == "__main__":
    main()
