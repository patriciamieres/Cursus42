from typing import Any
import numpy as np
from move_drons import MovementProcessor, Movement
import sys
from colorama import init, Fore, Back, Style


def get_matrix_position(map: dict[str, Any]):
    map['hub'][map['end_hub'].name] = map['end_hub']
    map['hub'][map['start_hub'].name] = map['start_hub']
    cols = max([map['hub'][x].coordinate[0] for x in map['hub']]) + 1
    rows = max([map['hub'][x].coordinate[1] for x in map['hub']]) + 1
    matrix = np.zeros((rows, cols))
    for hub in map['hub'].values():
        col, row = hub.coordinate
        matrix[row, col] = 1
    return matrix


def get_matrix_colors(map: dict[str, Any]):
    map['hub'][map['end_hub'].name] = map['end_hub']
    map['hub'][map['start_hub'].name] = map['start_hub']
    cols = max([map['hub'][x].coordinate[0] for x in map['hub']]) + 1
    rows = max([map['hub'][x].coordinate[1] for x in map['hub']]) + 1
    matrix = np.empty((rows, cols), dtype=object)
    for hub in map['hub'].values():
        col, row = hub.coordinate
        color = hub.color
        matrix[row, col] = color
    return matrix


def base_map(matrix, matrix_color):
    '''
        Reeturns a matrix with the hubs in each
    '''
    hub = '╚════╝'
    blank = "      "
    colors = {
        'black': "\033[30m",
        'red': "\033[31m",
        'green': "\033[32m",
        'yellow': "\033[33m",
        'blue': "\033[34m",
        'magenta': "\033[35m",
        'cyan': "\033[36m",
        'white': "\033[37m",
        'orange': "\033[38;5;208m",
        'gold': "\033[38;5;220m",
        'brown': "\033[38;5;130m",
        'purple': "\033[38;5;141m",
        'lime': "\033[38;5;154m"
    }
    reset = "\033[0m"
    new_matrix = [[blank] * len(matrix[0]) for _ in range(len(matrix))]
    for num_row, row in enumerate(matrix):
        for num_col, cell in enumerate(row):
            if cell:
                print(1)
                if matrix_color[num_row][num_col]:
                    color = colors[matrix_color[num_row][num_col].lower()]
                else:
                    color = colors['white']
                new_matrix[num_row][num_col] = f"{color}{hub}{reset}"
    return new_matrix


def rows_to_string(matrix):
    mat = []
    for row in matrix:
        mat.append("      ".join(row))
    return (mat)


def print_move(movement: Movement, map_draw: list[list[str]], hubs: dict[str, Any]):
    copy_map = []
    blank = "      "
    rows = len(map_draw)
    cols = len(map_draw[0])
    new_matrix = [[blank] * cols for _ in range(rows)]
    for key, value in movement.hubs.items():
        if value:
            col, row = hubs[key].coordinate
            new_matrix[row][col] = '  --  '
    for num, line in enumerate(map_draw):
        copy_map.append(new_matrix[num])
        # print(new_matrix[num])
        copy_map.append(line)
    return rows_to_string(copy_map)


def print_description_moves(movements: list[Movement], data_map: dict[str, Any]):
    colors = {
        'black': "\033[30m",
        'red': "\033[31m",
        'green': "\033[32m",
        'yellow': "\033[33m",
        'blue': "\033[34m",
        'magenta': "\033[35m",
        'cyan': "\033[36m",
        'white': "\033[37m",
        'orange': "\033[38;5;208m",
        'gold': "\033[38;5;220m",
        'brown': "\033[38;5;130m",
        'purple': "\033[38;5;141m",
        'lime': "\033[38;5;154m"
    }
    reset = "\033[0m"
    for move in movements:
        for dron in move.moves:
            if data_map['hub'][dron[2 :]].color:
                color = colors[data_map['hub'][dron[2:]].color.lower()]
            else:
                color = colors['white']
            print(f"{color}{dron}{reset}")
