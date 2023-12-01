from typing import List


def process_calib_values(calib_values: List) -> int:
    return sum(calib_values)


def get_first_digit(line: str, range_gen) -> [int, None]:
    digits = "0123456789"

    for idx in range_gen:
        if line[idx] in digits:
            return line[idx]

    # Warn: This return value can cause issues if the input data does not have digits.
    return 0
