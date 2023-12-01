from pathlib import Path
from typing import List


def read_inputs(filepath: Path) -> List:
    lines = []
    with open(filepath, 'r') as f_handle:
        while line := f_handle.readline():
            lines.append(line.rstrip())

    return lines
