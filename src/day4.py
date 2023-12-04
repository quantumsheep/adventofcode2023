from dataclasses import dataclass
from typing import List

from utils.input import read_day_input
from utils.lo import intersect, split_strip


@dataclass
class Card:
    id: int
    winning_numbers: List[int]
    my_numbers: List[int]
    matching_numbers: int

    count: int = 1

    def parse(line: str) -> "Card":
        card, numbers = line.split(": ")
        card_id = card.split(" ")[-1]
        winning_numbers, my_numbers = numbers.split(" | ")
        winning_numbers = [int(n) for n in split_strip(winning_numbers, " ")]
        my_numbers = [int(n) for n in split_strip(my_numbers, " ")]

        matching_numbers = intersect(winning_numbers, my_numbers)

        return Card(
            id=int(card_id),
            winning_numbers=winning_numbers,
            my_numbers=my_numbers,
            matching_numbers=len(matching_numbers),
        )


def part1(data: str) -> int:
    lines = data.splitlines()

    total = 0

    for line in lines:
        card = Card.parse(line)
        if card.matching_numbers == 0:
            continue

        total += pow(2, card.matching_numbers - 1)

    return total


def part2(data: str) -> int:
    lines = data.splitlines()
    cards = [Card.parse(line) for line in lines]

    for i, card in enumerate(cards):
        if card.matching_numbers == 0:
            continue

        for j in range(i + 1, i + 1 + card.matching_numbers):
            cards[j].count += card.count

    return sum([card.count for card in cards])


if __name__ == "__main__":
    day_input = read_day_input(4)

    result = part1(day_input)
    print("Part 1: ", result)

    result = part2(day_input)
    print("Part 2: ", result)
