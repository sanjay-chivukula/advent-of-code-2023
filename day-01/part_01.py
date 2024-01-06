from pathlib import Path
from typing import List

from common import parse_input
from common import first_digit


def process_data(data: List[str]):
    digits = [str(x) for x in "0123456789"]
    digits_rev = [x[::-1] for x in digits]

    total = 0
    for line in data:
        start_digit = first_digit(line, digits)
        end_digit = first_digit(line[::-1], digits_rev)
        total += int(start_digit + end_digit)

    return total


def driver_main():
    filepath = Path("../inputs/d01-main.txt")
    data = parse_input(filepath)
    total = process_data(data)
    print(total)


if __name__ == "__main__":
    driver_main()
