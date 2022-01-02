def get_neighbors(matrix, i, j):
    neighbors = []
    if i == 0 and j == 0:
        # print("branch 1")
        right_neighbor = matrix[i][j+1]
        diag_bottom_right_neighbor = matrix[i+1][j+1]
        bottom_neighbor = matrix[i+1][j]
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
    elif i == 0 and j == len(matrix[0])-1:
        # print("branch 2")
        bottom_neighbor = matrix[i+1][j]
        left_neighbor = matrix[i][j-1]
        diag_bottom_left_neighbor = matrix[i+1][j-1]
        neighbors.append(bottom_neighbor)
        neighbors.append(left_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
    elif i == len(matrix)-1 and j == 0:
        # print("branch 3")
        top_neighbor = matrix[i-1][j]
        diag_top_right_neighbor = matrix[i-1][j+1]
        right_neighbor = matrix[i][j+1]
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
    elif i == len(matrix)-1 and j == len(matrix[0])-1:
        # print("branch 4")
        top_neighbor = matrix[i-1][j]
        diag_top_left_neighbor = matrix[i-1][j-1]
        left_neighbor = matrix[i][j-1]
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(left_neighbor)
    elif i == 0:
        # print("branch 5")
        right_neighbor = matrix[i][j+1]
        diag_bottom_right_neighbor = matrix[i+1][j+1]
        bottom_neighbor = matrix[i+1][j]
        diag_bottom_left_neighbor = matrix[i+1][j-1]
        left_neighbor = matrix[i][j-1]
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
        neighbors.append(left_neighbor)
    elif i == len(matrix)-1:
        # print("branch 6")
        diag_top_left_neighbor = matrix[i-1][j-1]
        top_neighbor = matrix[i-1][j]
        diag_top_right_neighbor = matrix[i-1][j+1]
        right_neighbor = matrix[i][j+1]
        left_neighbor = matrix[i][j-1]
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(left_neighbor)
    elif j == 0:
        # print("branch 7")
        top_neighbor = matrix[i-1][j]
        bottom_neighbor = matrix[i+1][j]
        right_neighbor = matrix[i][j+1]
        diag_top_right_neighbor = matrix[i-1][j+1]
        diag_bottom_right_neighbor = matrix[i+1][j+1]
        neighbors.append(top_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
    elif j == len(matrix[0])-1:
        # print("branch 8")
        top_neighbor = matrix[i-1][j]
        bottom_neighbor = matrix[i+1][j]
        left_neighbor = matrix[i][j-1]
        diag_top_left_neighbor = matrix[i-1][j-1]
        diag_bottom_left_neighbor = matrix[i+1][j-1]
        neighbors.append(top_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(left_neighbor)
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
    else:
        # print("branch 9")
        diag_top_left_neighbor = matrix[i-1][j-1]
        top_neighbor = matrix[i-1][j]
        diag_top_right_neighbor = matrix[i-1][j+1]
        right_neighbor = matrix[i][j+1]
        diag_bottom_right_neighbor = matrix[i+1][j+1]
        bottom_neighbor = matrix[i+1][j]
        diag_bottom_left_neighbor = matrix[i+1][j-1]
        left_neighbor = matrix[i][j-1]
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
        neighbors.append(left_neighbor)
    return neighbors
