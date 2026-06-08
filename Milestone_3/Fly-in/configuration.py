from pydantic import BaseModel
from typing import Any



class Hub(BaseModel):
    name: str
    coordinate: list[int, int]
    zone: str = 'normal'
    color: str | None = None
    max_drones: int = 1

def read_map(file_path: str) -> list[str]:
    try:
        with open(file_path) as file:
            return file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not open the file {file_path}")

def parse_map(lines: list[str]) -> dict[str, list[str]]:
    data_map: dict[str, Any] = {}
    dic_connection: dict[str, list[str]]= {}
    list_hub: list[Hub] = []
    max_links = {}
    for num_line, line in enumerate(lines):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Error in line '{num_line}': invalid format: '{line}'")
        if not data_map and  not line.startswith('nb_drones:'):
                raise ValueError('The first line must define the number of '
                                 'drones using nb_drones: <positive_integer>')
        name, value = line.split(':', 1)
        name = name.strip()
        value = value.strip()
        if name in ['nb_drones', 'start_hub', 'end_hub']:
            if name in data_map:
                raise ValueError(f"Error in line {num_line}: "
                                    f"There is more than one {name}")
            if name in ['start_hub', 'end_hub']:
                try:
                    data_map[name] = valid_hub(value)
                except ValueError as e:
                    raise ValueError (f"Error in line '{num_line}': {e}")
            else:
                try:
                    data_map[name] = int(value)
                except ValueError as e:
                    raise ValueError(f"Error in line {num_line}: {e}")
        elif name == 'hub':
            try:
                list_hub.append(valid_hub(value))
            except ValueError as e:
                raise ValueError(f"Error in line {num_line}: {e}")
        elif name == 'connection':
            hub_names = [hub.name for hub in list_hub] + [data_map['start_hub'].name, data_map['end_hub'].name]
            try:
                list_conection = value.split('-', 1)
                list_conection[1] = list_conection[1].split(' ', 1)
                if list_conection[0] not in hub_names:
                    raise ValueError(f"there is no hub name for {list_conection[0]}")
                if len(list_conection[1]) >= 2:
                    name, link = list_conection[1]
                    if name not in hub_names:
                        raise ValueError(f"there is no hub name for {list_conection[0]}")
                    if link[0] == '[' and link[-1] == ']':
                        link = link[1 : -1]
                    else:
                        raise ValueError(f"Formt error")
                    key, max_link  = link.split('=', 1)
                    if key == 'max_link_capacity' and max_link.isdigit():
                        dic_connection.setdefault(list_conection[0], []).append(name)
                        max_links[value.split(' ', 1)[0]] = int(max_link)

                else:
                    if list_conection[1][0] not in hub_names:
                        raise ValueError(f"there is no hub name for {list_conection[0]}")
                    dic_connection.setdefault(list_conection[0], []).append(list_conection[1][0])
                    max_links[(value.split(' ', 1)[0])] = 1
            except ValueError as e:
                raise ValueError(f"Error in line {num_line}: {e}")
        else:
            raise  ValueError(f"Error in line {num_line}: "
                                f"This line can't sart with  {name}")
    data_map['connection'] = dic_connection
    data_map['max_links'] = max_links
    dic_hub = {hub.name: hub for hub in list_hub}
    data_map['hub'] = dic_hub
    cols = [data_map['hub'][x].coordinate[0] for x in data_map['hub']]
    rows = [data_map['hub'][x].coordinate[1] for x in data_map['hub']]
    minimum = 0
    if not all (num >= 0 for num in cols):
        minimum  = abs(min(cols))
    for hub in data_map['hub'].values():
        hub.coordinate[0] += minimum
    if not all (num >= 0 for num in rows):
        minimum  = abs(min(rows))
    for hub in data_map['hub'].values():
        hub.coordinate[1] += minimum
    return data_map



def valid_hub(hub: str) -> Hub:

    hub_data =  hub.split(' ', 3)
    num_parameters = len(hub_data)
    if  num_parameters < 3:
        raise ValueError('Some parmeeeter i left')
    elif num_parameters > 4:
        raise ValueError('Some parmeeeter i left')
    name = hub_data[0]
    x = hub_data[1]
    y = hub_data[2]
    try:
        coordinate = [int(x), int(y)]
    except ValueError:
        raise ValueError('The coordinates does nort have the format (int, int)')
    parameters_dic: dict[str, Any]= {'name': name, 'coordinate': coordinate}

    if num_parameters == 4:
        properties = hub_data[3]
        properties = properties.strip()
        if not (properties.startswith('[') and properties.endswith(']')):
            raise ValueError("Error")
        properties = properties[1:-1]
        list_prop = properties.split()
        for prop in list_prop:
            if '=' not in prop:
                raise ValueError('Error there is no =')
            key, value = prop.split('=', 1)
            key = key.strip()
            value = value.strip()
            if key not in ['zone', 'color', 'max_drones']:
                raise ValueError('Error the name is invalid')
            if key == 'max_drones':
                parameters_dic[key] = int(value)
            else:
                parameters_dic[key] = value
    return Hub(**parameters_dic)


    
    