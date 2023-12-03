from collections import OrderedDict
import re
from tokenize import Token
from typing import Dict, List

from utils.input import read_day_input
from utils.tokenizer import Tokenizer

GEAR_REGEX = r"\*"
SYMBOLS_REGEX = r"[#$@/+%&\-=]"

tokenizer = Tokenizer(
    patterns=OrderedDict(
        {
            "number": [r"\d+"],
            "gear": [GEAR_REGEX],
            "symbols": [SYMBOLS_REGEX],
            "ignore": [r"[.\n]"],
        },
    ),
    ignore_patterns=["symbols", "ignore"],
)


def part1(data: str) -> int:
    tokens = tokenizer.to_tokens(data)
    columns = len(data.splitlines()[0]) + 1

    total = 0

    for token in tokens:
        if token.pattern_type != "number":
            continue

        start_line = max(0, token.line - 1)
        start_columns = max(0, token.column - 1)
        end_line = token.line + 1
        end_column = token.column + len(token.value) + 1

        arround = ""
        for i in range(start_line, end_line + 1):
            arround += (
                data[i * columns + start_columns : i * columns + end_column] + "\n"
            )

        # Check if arround has a symbol
        if re.search(GEAR_REGEX, arround) or re.search(SYMBOLS_REGEX, arround):
            total += int(token.value)

    return total


def part2(data: str) -> int:
    tokens = tokenizer.to_tokens(data)
    total = 0

    for token in tokens:
        if token.pattern_type != "gear":
            continue

        numbers_around: List[Token] = []

        for other_token in tokens:
            if other_token.pattern_type != "number":
                continue

            # Should be in the same line, or the line before or after
            if other_token.line > (token.line + 1):
                continue
            if other_token.line < (token.line - 1):
                continue

            # Should be in the same column, or the column before or after
            column_start = other_token.column
            column_end = other_token.column + len(other_token.value) - 1

            if column_end < (token.column - 1):
                continue
            if column_start > (token.column + 1):
                continue

            numbers_around.append(other_token)

        if len(numbers_around) != 2:
            continue

        total += int(numbers_around[0].value) * int(numbers_around[1].value)

    return total


if __name__ == "__main__":
    day_input = read_day_input(3)

    result = part1(day_input)
    print("Part 1: ", result)

    result = part2(day_input)
    print("Part 2: ", result)
