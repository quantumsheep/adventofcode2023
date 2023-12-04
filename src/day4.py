from utils.input import read_day_input
from utils.lo import intersect, split_strip


class Card:
    def __init__(self, line: str):
        _, numbers = line.split(": ")
        winning_numbers, my_numbers = numbers.split(" | ")
        self.winning_numbers = [int(n) for n in split_strip(winning_numbers, " ")]
        self.my_numbers = [int(n) for n in split_strip(my_numbers, " ")]

        self.matching_numbers = len(intersect(self.winning_numbers, self.my_numbers))
        self.count = 1


def part1(data: str) -> int:
    lines = data.splitlines()

    total = 0

    for line in lines:
        card = Card(line)
        if card.matching_numbers == 0:
            continue

        total += pow(2, card.matching_numbers - 1)

    return total


def part2(data: str) -> int:
    lines = data.splitlines()
    cards = [Card(line) for line in lines]

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
