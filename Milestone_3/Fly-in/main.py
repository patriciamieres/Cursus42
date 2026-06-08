from pydantic import BaseModel
from typing import Any
from solutions import compute_solution
from draw_map import get_matrix_position, base_map, rows_to_string, print_move, get_matrix_colors, print_description_moves
from move_drons import algorithim_movements
from configuration import read_map, parse_map
import time
import sys
import os


if __name__ == '__main__':
    try:
        lines = read_map('maps/hard/03_ultimate_challenge.txt')
        data_map = parse_map(lines)
        for linne in data_map.keys():
            print(f"{linne} : {data_map[linne]}")
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    solutions = compute_solution(data_map)
    # for solution in solutions:
    #     print(solution)

    map_num = get_matrix_position(data_map)
    map_color = get_matrix_colors(data_map)
    map_draw = base_map(map_num, map_color)
    # print('\n')
    # print_map(map_draw)
    m = algorithim_movements(data_map, solutions)
    # for mov in m:
    #     print('--------------------------------------------------')
    #     print ('hub')
    #     for clave, valor in mov.hubs.items():
    #         if valor:
    #             print(f"{clave}: {valor}")
    #     print ('link')
    #     for clave, valor in mov.links.items():
    #         if valor:
    #             print(f"{clave}: {valor}")
    
    for mov in m:
        me = print_move(mov, map_draw, data_map['hub'])
        c = ''
        for e in me:
            c = c + ''.join(e)
            c = c + '\n'
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.stdout.write(f"\033[H{c}")
        sys.stdout.flush() # Fuerza a la terminal a mostrarlo inmediatamente
        time.sleep(0.5)

    print_description_moves(m, data_map)
