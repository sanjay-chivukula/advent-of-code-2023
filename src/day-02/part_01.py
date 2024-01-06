from pathlib import Path
from typing import List

from common import parse_input
from common import parse_line

DICE_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_valid_game(game_data):
    for turn in game_data:
        for color, count in turn.items():
            if count > DICE_LIMITS[color]:
                return False
    return True


def compute_valid_game_sum(doc_lines: List[str]):
    parsed_games = map(lambda line: parse_line(line), doc_lines)
    filtered_games = filter(lambda x: is_valid_game(x[1]), parsed_games)
    game_num_sum = sum((game_num for game_num, _ in filtered_games))
    return game_num_sum


def driver_main():
    filepath = Path("../../inputs/d02-main.txt")
    doc_lines = parse_input(filepath)

    valid_game_sum = compute_valid_game_sum(doc_lines)
    print(valid_game_sum)


if __name__ == "__main__":
    driver_main()