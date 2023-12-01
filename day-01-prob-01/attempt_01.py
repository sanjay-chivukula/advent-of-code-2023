from pathlib import Path
from typing import List


def read_inputs(filepath: Path) -> List:
    lines = []
    with open(filepath, 'r') as f_handle:
        while line := f_handle.readline():
            lines.append(line.rstrip())

    return lines


def get_first_digit(line: str, range_gen) -> [int, None]:
    digits = "0123456789"

    for idx in range_gen:
        if line[idx] in digits:
            return line[idx]

    # Warn: This return value can cause issues if the input data does not have digits.
    return 0


def line_to_calib(doc_line: str) -> int:
    l_idx_gen, r_idx_gen = range(0, len(doc_line), 1), range(len(doc_line) - 1, -1, -1)

    l_digit = get_first_digit(doc_line, l_idx_gen)
    r_digit = get_first_digit(doc_line, r_idx_gen)
    calib_value = int(l_digit + r_digit)
    return calib_value


def compute_calib_values(calib_doc_lines: List) -> List:
    calib_values = []

    for line in calib_doc_lines:
        calib_value = line_to_calib(line)
        calib_values.append(calib_value)

    return calib_values


def process_calib_values(calib_values: List) -> int:
    return sum(calib_values)


def driver_main():
    inputs_path = Path("inputs/aoc-2023-d1-p1-input.txt")
    calib_doc_lines = read_inputs(inputs_path)
    calib_values = compute_calib_values(calib_doc_lines)
    output_data = process_calib_values(calib_values)
    print(output_data)


if __name__ == "__main__":
    driver_main()
