from collections import OrderedDict
from typing import List

from utils.input import read_day_input
from utils.tokenizer import Tokenizer

NUMBERS = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

PATTERNS: OrderedDict[str, List[str]] = OrderedDict(
    {
        "number": sorted(
            [
                *list(NUMBERS.keys()),
            ],
            key=len,
            reverse=True,
        ),
        "any": ["."],
    }
)

tokenizer = Tokenizer(patterns=PATTERNS, ignore_patterns=["any"])


def part1(data: str) -> List[int]:
    output: List[int] = []

    lines = data.splitlines()
    for line in lines:
        tokens = tokenizer.to_tokens_simple(line)
        tokens = list(filter(lambda a: a.isnumeric(), tokens))

        first = NUMBERS[tokens[0]]
        last = NUMBERS[tokens[-1]]

        output.append(first * 10 + last)

    return output


def part2(data: str) -> List[int]:
    output: List[int] = []

    lines = data.splitlines()
    for line in lines:
        tokens = tokenizer.to_tokens_simple(line, with_collisions=True)

        first = NUMBERS[tokens[0]]
        last = NUMBERS[tokens[-1]]

        output.append(first * 10 + last)

    return output


if __name__ == "__main__":
    day_input = read_day_input(1)

    lines = part1(day_input)
    print("Part 1: ", sum(lines))

    lines = part2(day_input)
    print("Part 2: ", sum(lines))
