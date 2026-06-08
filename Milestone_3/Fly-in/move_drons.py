
from configuration import Hub
from typing import Any
from solutions import costs_solutions
import copy


class Movement:

    def __init__(self, name_hubs: list[str], name_links: list[str]):
        self.hubs: dict[str, int] = {name: 0 for name in name_hubs}
        self.links: dict[str, int] = {name: 0 for name in name_links}
        self.moves: list[str] = []


class MovementProcessor:

    def __init__(self, max_links: dict[str, int],
                 max_drons: dict[str, int],
                 zone_hub: dict[str, str]):
        self.max_links = max_links
        self.max_drons = max_drons
        self.zone_hub = zone_hub
        self.movements: list[Movement] = []

    def move_dron(self, num_movement: int,
                  initial_hub: str,
                  final_hub: str,
                  dron_name: str):
        next_move_index = num_movement - 1
        number_moves = len(self.movements)
        if num_movement > number_moves:
            self.add_movement()
        if self.possible_to_move(num_movement,  initial_hub, final_hub):
            if self.zone_hub[final_hub] == 'restricted':
                link = initial_hub + '-' + final_hub
                self.movements[next_move_index].links[link] += 1
                self.movements[next_move_index].moves.append(dron_name + link)
                if number_moves < num_movement + 1:
                    self.add_movement()
                self.movements[next_move_index + 1].hubs[final_hub] += 1
                self.movements[next_move_index + 1].moves.append(dron_name + final_hub)
            else:
                self.movements[next_move_index].hubs[final_hub] += 1
                self.movements[next_move_index].moves.append(dron_name + final_hub)
            return 1
        else:
            return 0

    def add_movement(self):
        movement = Movement(self.max_drons.keys(), self.max_links.keys())
        movement.moves = []
        self.movements.append(movement)

    def possible_to_move(self, num_movement: int, initial_hub: str,
                         final_hub: str):
        number_moves = len(self.movements)
        next_move_index = num_movement - 1
        if (number_moves + 1) < num_movement < 0:
            raise ValueError('The movement number cant be superior to the '
                             'actual movements')
        if self.zone_hub[final_hub] == 'blocked':
            return False
        elif self.zone_hub[final_hub] == 'restricted':
            link = initial_hub + '-' + final_hub
            if (
                self.movements[next_move_index].links[link] <
                self.max_links[link]
            ):
                if number_moves < num_movement + 1:
                    return True
                if (
                    self.movements[next_move_index].hubs[final_hub] <
                    self.max_drons[final_hub]
                ):
                    return True
            else:
                return False
        else:
            if (
                self.movements[next_move_index].hubs[final_hub] <
                self.max_drons[final_hub]
            ):
                return True
            else:
                return False


def simulate_path(movements: MovementProcessor,
                  path: list[str],
                  dron_name: str):
    turn = 1
    for index, hub in enumerate(path):
        move = False
        if index >= len(path) - 1:
            break
        while not move:
            move = movements.move_dron(turn, hub, path[index + 1], dron_name)
            turn += 1
    return turn


def algorithim_movements(data_map: dict[str, Any], solutions: list[list[str]]):
    # cost_path = costs_solutions(solutions, data_map['hub'])
    num_drons = data_map['nb_drones']
    max_drons = {key: data_map['hub'][key].max_drones for key in data_map['hub'].keys()}
    zone_hub = {key: data_map['hub'][key].zone for key in data_map['hub'].keys()}
    movements = MovementProcessor(data_map['max_links'], max_drons, zone_hub)
    for dron in range(num_drons):
        dron_name = f"D{dron}"
        copy_movements = copy.deepcopy(movements)
        path_number = 0
        first_path = simulate_path(copy_movements,
                                   solutions[path_number], dron_name)
        second_path = simulate_path(copy_movements,
                                    solutions[path_number + 1], dron_name)
        while first_path > second_path:
            copy_movements = movements
            path_number += 1
            first_path = second_path
            second_path = simulate_path(copy_movements,
                                        solutions[path_number + 1], dron_name)
        simulate_path(movements, solutions[path_number], dron_name)
    return movements.movements
