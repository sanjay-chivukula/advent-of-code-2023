from pathlib import Path
from typing import List

from advent.calibration import process_calib_values, parse_by_digit
from advent.utils import read_inputs


def compute_calib_values(calib_doc_lines: List) -> List:
    calib_values = []

    for line in calib_doc_lines:
        calib_value = parse_by_digit(line)
        calib_values.append(calib_value)

    return calib_values


def driver_main():
    inputs_path = Path("../inputs/aoc-2023-d1-p1-input.txt")
    calib_doc_lines = read_inputs(inputs_path)
    calib_values = compute_calib_values(calib_doc_lines)
    output_data = process_calib_values(calib_values)
    print(output_data)


if __name__ == "__main__":
    driver_main()
