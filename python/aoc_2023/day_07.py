"""
https://adventofcode.com/2023/day/7
"""
from __future__ import annotations

import string
from collections import Counter
from dataclasses import dataclass, field

from aoc_2023.base import Day

CARDS = list("AKQJT98765432")[::-1]
WILD_CARDS = list("AKQT98765432J")[::-1]


@dataclass
class Hand:
    cards: str
    bid: int = 0
    jokers_wild: bool = False
    type: list[int] = field(default_factory=list)
    card_scores: str = ""

    def __post_init__(self):
        self.counts = dict(
            sorted(Counter(self.cards).items(), key=lambda item: item[1], reverse=True)
        )

        self.type = self._set_type()

        pack = WILD_CARDS if self.jokers_wild else CARDS
        self.card_scores = "".join(
            [string.hexdigits[pack.index(card)] for card in self.cards]
        )

    def _set_type(self):
        counts = self.counts.copy()
        if self.jokers_wild and "J" in counts and len(counts) > 1:
            n_jokers = counts.pop("J")
            keys = list(counts.keys())
            counts[keys[0]] += n_jokers
        return list(counts.values())

    def __lt__(self, other: Hand):
        if self.type == other.type:
            return self.card_scores < other.card_scores
        return self.type < other.type

    @classmethod
    def from_string(cls, input: str, jokers_wild: bool = False):
        cards, bid = input.split(" ")
        return Hand(cards, int(bid), jokers_wild)


class Solution(Day):
    def part_1(self):
        hands = [Hand.from_string(input) for input in self.lines]
        hands.sort()
        return sum((i + 1) * hand.bid for i, hand in enumerate(hands))

    def part_2(self):
        hands = [Hand.from_string(input, True) for input in self.lines]
        hands.sort()
        return sum((i + 1) * hand.bid for i, hand in enumerate(hands))


def main():
    day = Solution("./aoc_2023/data/day_07.txt")
    day.run()


if __name__ == "__main__":
    main()
