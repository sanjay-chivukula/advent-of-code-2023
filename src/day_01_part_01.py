from pathlib import Path

from advent.calibration import process_calib_values, parse_by_digit
from advent.utils import read_inputs


def solve_calibration(input_pathstr: str):
    calib_doc_path = Path(input_pathstr)
    calib_doc_lines = read_inputs(calib_doc_path)
    calib_values = [parse_by_digit(line) for line in calib_doc_lines]
    calib_output_data = process_calib_values(calib_values)
    print(calib_output_data)


if __name__ == "__main__":
    solve_calibration("../inputs/aoc-2023-d1-p1-input.txt")
