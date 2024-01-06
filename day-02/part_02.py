from pathlib import Path
from functools import reduce
from typing import List
from typing import Dict

from common import parse_input
from common import parse_line


def min_required_dice(game_data):
    min_dice_limits = {}
    for turn in game_data:
        for color, count in turn.items():
            if color not in min_dice_limits:
                min_dice_limits[color] = count
            else:
                min_dice_limits[color] = max(min_dice_limits[color], count)
    return min_dice_limits


def dice_power(dice_counts: Dict[str, int]):
    return reduce(lambda tot, cur: tot * cur, dice_counts.values(), 1)


def compute_game_power(doc_lines: List[str]):
    parsed_games = map(lambda line: parse_line(line), doc_lines)
    game_min_limits = map(lambda x: min_required_dice(x[1]), parsed_games)
    game_powers = map(lambda x: dice_power(x), game_min_limits)
    total_power = sum(game_powers)
    return total_power


def driver_main():
    filepath = Path("../inputs/d02-main.txt")
    doc_lines = parse_input(filepath)

    game_power_sum = compute_game_power(doc_lines)
    print(game_power_sum)


if __name__ == "__main__":
    driver_main()
