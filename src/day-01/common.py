from pathlib import Path


def parse_input(filepath: Path):
    data = []
    with open(filepath, "r") as f_obj:
        while line := f_obj.readline():
            line = line.strip()
            data.append(line)

    return data


def first_digit(line: str, digits_list):
    digits_loc_map = {x: line.find(x) for x in digits_list}
    filtered_loc = dict(filter(lambda x: x[1] > -1, digits_loc_map.items()))
    min_digit, min_loc = 0, len(line)
    for digit, loc in filtered_loc.items():
        if loc < min_loc:
            min_digit, min_loc = digit, loc

    return min_digit


def to_digit(word_str, word_map):
    out_digit = word_str
    if out_digit in word_map:
        out_digit = word_map[word_str]
    return out_digit
