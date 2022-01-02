from src.build_matrix import build_2d_array, initiate_tmp_matrix
from src.get_neighbors import get_neighbors
from matplotlib import pyplot
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


# TODO: how to dynamically render the pyplot so that you can see the changes in realtime instead of open/close?
# TODO: how to set this up in a while loop so that the function runs with the input parameter being the output of the function's last iteration (see below)
def main():
    first_iteration = conway_rules(GLIDER_TEST)
    pyplot.imshow(first_iteration)
    pyplot.show()
    pyplot.clf()
    second_iteration = conway_rules(first_iteration)
    pyplot.imshow(second_iteration)
    pyplot.show()
    pyplot.clf()
    third_iteration = conway_rules(second_iteration)
    pyplot.imshow(third_iteration)
    pyplot.show()
    pyplot.clf()
    fourth_iteration = conway_rules(third_iteration)
    pyplot.imshow(fourth_iteration)
    pyplot.show()
    pyplot.clf()
    fifth_iteration = conway_rules(fourth_iteration)
    pyplot.imshow(fifth_iteration)
    pyplot.show()
    pyplot.clf()
    sixth_iteration = conway_rules(fifth_iteration)
    pyplot.imshow(sixth_iteration)
    pyplot.show()
    pyplot.clf()


if __name__ == "__main__":
    main()
