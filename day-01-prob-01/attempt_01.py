from pathlib import Path
from typing import List


def read_inputs(filepath: Path) -> List:
    pass


def line_to_calib(doc_line: str) -> int:
    pass


def compute_calib_values(calib_doc_lines: List) -> List:
    pass


def process_calib_values(calib_values: List) -> int:
    pass


def driver_main():
    inputs_path = Path("inputs/aoc-2023-d1-p1-input.txt")
    calib_doc_lines = read_inputs(inputs_path)


if __name__ == "__main__":
    driver_main()
