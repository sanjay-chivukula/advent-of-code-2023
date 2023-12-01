from typing import List


def process_calib_values(calib_values: List) -> int:
    return sum(calib_values)


def parse_by_digit(doc_line: str) -> int:
    l_idx_gen, r_idx_gen = range(0, len(doc_line), 1), range(len(doc_line) - 1, -1, -1)

    l_digit = first_number_digit(doc_line, l_idx_gen)
    r_digit = first_number_digit(doc_line, r_idx_gen)
    calib_value = int(l_digit + r_digit)
    return calib_value


def parse_by_digit_or_word(doc_line: str) -> int:
    pass


def first_number_digit(line: str, range_gen) -> [int, None]:
    digits = "0123456789"

    for idx in range_gen:
        if line[idx] in digits:
            return line[idx]

    # Warn: This return value can cause issues if the input data does not have digits.
    return 0
