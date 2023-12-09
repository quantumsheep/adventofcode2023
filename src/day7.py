from enum import IntEnum
from typing import Dict, Tuple

from utils.bench import bench
from utils.input import read_day_input


class HandType(IntEnum):
    FiveOfAKind = 0
    FourOfAKind = 1
    FullHouse = 2
    ThreeOfAKind = 3
    TwoPairs = 4
    OnePair = 5
    HighCard = 6


CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
CARDS_WITH_JOKER = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_card_type(cards: str, is_j_joker: bool) -> HandType:
    card_count: Dict[str, int] = {}
    for card in cards:
        if card not in card_count:
            card_count[card] = 0
        card_count[card] += 1

    best = HandType.HighCard

    if len(card_count) == 5:
        best = HandType.HighCard
    elif len(card_count) == 4:
        best = HandType.OnePair
    elif len(card_count) == 3:
        if 3 in card_count.values():
            best = HandType.ThreeOfAKind
        else:
            best = HandType.TwoPairs
    elif len(card_count) == 2:
        if 2 in card_count.values():
            best = HandType.FullHouse
        else:
            best = HandType.FourOfAKind
    else:
        best = HandType.FiveOfAKind

    if is_j_joker:
        if "J" not in card_count or best == HandType.FiveOfAKind:
            return best

        if best == HandType.FourOfAKind:
            if card_count["J"] == 1:
                return HandType.FiveOfAKind
            elif card_count["J"] == 4:
                return HandType.FiveOfAKind

        if best == HandType.FullHouse:
            if card_count["J"] == 2:
                return HandType.FiveOfAKind
            elif card_count["J"] == 3:
                return HandType.FiveOfAKind

        if best == HandType.ThreeOfAKind:
            if card_count["J"] == 1:
                return HandType.FourOfAKind
            elif card_count["J"] == 3:
                return HandType.FourOfAKind

        if best == HandType.TwoPairs:
            if card_count["J"] == 1:
                return HandType.FullHouse
            elif card_count["J"] == 2:
                return HandType.FourOfAKind

        if best == HandType.OnePair:
            if card_count["J"] == 1:
                return HandType.ThreeOfAKind
            elif card_count["J"] == 2:
                return HandType.ThreeOfAKind

        if best == HandType.HighCard:
            if card_count["J"] == 1:
                return HandType.OnePair

    return best


def get_card_score(card: Tuple[str, HandType, int], is_j_joker: bool) -> int:
    cards = CARDS_WITH_JOKER if is_j_joker else CARDS

    return int(card[1]) * 100000000000 + sum(
        cards.index(c) * pow(100, i) for i, c in enumerate(reversed(card[0]))
    )


@bench
def run(data: str, is_j_joker: bool) -> int:
    lines = data.splitlines()

    cards = [line.split(" ") for line in lines]
    cards = [
        (card[0], get_card_type(card[0], is_j_joker), int(card[1])) for card in cards
    ]
    cards.sort(key=lambda card: get_card_score(card, is_j_joker), reverse=True)

    return sum(card[2] * (i + 1) for i, card in enumerate(cards))


if __name__ == "__main__":
    day_input = read_day_input(7)

    result = run(day_input, is_j_joker=False)
    print("Part 1: ", result)

    result = run(day_input, is_j_joker=True)
    print("Part 2: ", result)
