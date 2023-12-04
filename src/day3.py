import re
from collections import OrderedDict
from typing import List

from utils.input import read_day_input
from utils.lo import uniq
from utils.tokenizer import Token, Tokenizer

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
    tokenized_text = tokenizer.tokenize(data)
    columns = len(data.splitlines()[0]) + 1

    total = 0

    for token in tokenized_text.tokens:
        if token.pattern_type != "number":
            continue

        start_line = max(0, token.line - 1)
        start_columns = max(0, token.column - 1)
        end_line = token.line + 1
        end_column = token.column + len(token.value) + 1

        arround = ""
        for i in range(start_line, end_line + 1):
            arround += data[i * columns + start_columns : i * columns + end_column] + "\n"

        # Check if arround has a symbol
        if re.search(GEAR_REGEX, arround) or re.search(SYMBOLS_REGEX, arround):
            total += int(token.value)

    return total


def part2(data: str) -> int:
    tokenized_text = tokenizer.tokenize(data)
    total = 0

    positions_to_check = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for token in tokenized_text.tokens:
        if token.pattern_type != "gear":
            continue

        tokens_around = [
            tokenized_text.what_is_at(token.line + y, token.column + x)
            for x, y in positions_to_check
        ]
        numbers_around = filter(
            lambda a: a is not None and a.pattern_type == "number",
            tokens_around,
        )
        numbers_around: List[Token] = uniq(list(numbers_around))

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
