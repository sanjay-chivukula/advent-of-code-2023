from pathlib import Path
from typing import List
from itertools import chain

from common import parse_input
from common import first_digit
from common import to_digit

words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

digits = [x for x in chain(words.keys(), words.values())]
digits_rev = [x[::-1] for x in digits]


def process_data(data: List[str]):
    total = 0
    for line in data:
        start_digit = first_digit(line, digits)
        start_digit = to_digit(start_digit, words)

        end_digit = first_digit(line[::-1], digits_rev)
        end_digit = to_digit(end_digit[::-1], words)
        total += int(start_digit + end_digit)

    return total


def driver_main():
    filepath = Path("../inputs/d01-main.txt")
    data = parse_input(filepath)
    total = process_data(data)
    print(total)


if __name__ == "__main__":
    driver_main()
