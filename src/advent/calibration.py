from typing import List


def parse_by_digit(doc_line: str) -> int:
    digits = "0123456789"
    l_digit, r_digit = None, None

    for char in doc_line:
        if char in digits:
            if l_digit is None:
                l_digit = char
            if r_digit is None:
                r_digit = char

    if l_digit is None:
        # Warning: input doesn't have digits, will set value to zero as default.
        l_digit, r_digit = "0", "0"

    calib_value = int(l_digit + r_digit)
    return calib_value


def parse_by_digit_or_word(doc_line: str) -> int:
    pass


def process_calib_values(calib_values: List) -> int:
    return sum(calib_values)
