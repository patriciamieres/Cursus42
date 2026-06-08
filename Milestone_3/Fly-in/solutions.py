from typing import Any, Deque
from collections import deque



'''
    primero la ruta ms rapida para el primero e ir moviendo el segundo pra la mas rapida teniendo en cuenta 
'''

# def best_option(list_hub: list[str], actul_hub: str):
# 	prior = []
# 	non_prior = []
# 	for hub in list_hub:


# def path(data_map):
# 	num_drons = data_map['nb_drones']
# 	num_hubs = data_map['hub'] + 2
# 	list_hubs = [data_map['start_hub']]
# 	list_hubs.append(data_map['hub'][hub] for hub in data_map)
# 	list_hubs.append(data_map['end_hub'])
# 	position_drons = [data_map['start_hub'].name] * num_drons
# 	ceros = [0] * num_hubs
# 	structure = []
# 	first_dron = 1
# 	while not all (position == data_map['start_hub'].name for position in position_drons):
# 		if first_dron:

def compute_solution(map: dict[str, Any]) -> list[Any]:
    queue: Deque[str, list[str]]= deque([(map['start_hub'].name, [])])
    priority = {
        'goal': 0,
        'priority': 1,
        'normal': 2,
        'restricted':3

    }
    result: list[Any] = []  
    # goal zone = goal
    map['end_hub'].zone = 'goal'
    # goal in hub
    map['hub'][map['end_hub'].name] = map['end_hub']
    while queue:
        position, sol = queue.popleft()
        if position == map['end_hub'].name:
            result.append(sol)
            continue
        if position not in map['connection']:
            continue
        near_hubs = map['connection'][position]
        accesible_hubs =[hub for hub in near_hubs if hub not in sol]
        if  not accesible_hubs:
            accesible_hubs = near_hubs
        if map['end_hub'].name in accesible_hubs:
            queue.append((map['end_hub'].name, sol + [map['end_hub'].name]))
            continue
        order_hubs = sorted(accesible_hubs, key = lambda x: priority[map['hub'][x].zone])
        for hub in order_hubs:
            queue.append((hub, sol + [hub]))
    return result


def costs_solutions(solutions: list[list[str]], hubs: dict[str, Any]):
    costs_path = []
    for solution in solutions:
        total = len(solution)
        for hub in solution:
            if hubs[hub].zone == 'restricted':
                total += 1
        costs_path.append(total)

                