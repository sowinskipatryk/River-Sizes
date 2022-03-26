def get_river_coords(matrix):
    coord_list = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                coord_list.append((row, col))
    return coord_list


def check_river_len(x, y, coord_list, river_size=1):
    coord_list.pop(coord_list.index((x, y)))
    if (x + 1, y) in coord_list:
        river_size += 1
        river_size, coord_list = check_river_len(x + 1, y, coord_list, 
                                                 river_size)
    if (x, y + 1) in coord_list:
        river_size += 1
        river_size, coord_list = check_river_len(x, y + 1, coord_list, 
                                                 river_size)
    if (x - 1, y) in coord_list:
        river_size += 1
        river_size, coord_list = check_river_len(x - 1, y, coord_list, 
                                                 river_size)
    if (x, y - 1) in coord_list:
        river_size += 1
        river_size, coord_list = check_river_len(x, y - 1, coord_list, 
                                                 river_size)
    return river_size, coord_list


def get_river_sizes(matrix):
    coord_list = get_river_coords(matrix)
    river_sizes = []
    while coord_list:
        river_size, coord_list = check_river_len(coord_list[0][0], 
                                                 coord_list[0][1], coord_list)
        river_sizes.append(river_size)
    return river_sizes


matrix = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]

print(get_river_sizes(matrix))
