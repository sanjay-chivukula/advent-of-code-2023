from pathlib import Path
from typing import List


def parse_input(filepath: Path) -> List[str]:
    data = []
    with open(filepath, 'r') as f_obj:
        while line := f_obj.readline():
            data.append(line.strip())

    return data


def parse_line(line: str):
    game_str, _, data_str = line.partition(":")

    _, _, game_num = game_str.strip().rpartition(" ")
    game_num = int(game_num)

    data_str = data_str.strip()
    game_data = []
    for turn_str in data_str.split(";"):
        turn_data = {}
        for dice_str in turn_str.strip().split(","):
            dice_str = dice_str.strip()
            count, color = dice_str.split(" ")
            turn_data[color] = int(count)
        game_data.append(turn_data)

    return game_num, game_data
