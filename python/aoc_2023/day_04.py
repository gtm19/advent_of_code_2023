from __future__ import annotations
from aoc_2023.base import Day
from dataclasses import dataclass
from typing import Optional
import re
from collections import Counter


@dataclass
class Ticket:
    id: int
    winning_numbers: set[str]
    numbers: set[str]
    score: Optional[int] = None
    matching_nums: Optional[int] = None

    def __post_init__(self):
        self._set_score()

    def _set_score(self):
        self.matching_nums = len(self.winning_numbers.intersection(self.numbers))
        if self.matching_nums == 0:
            self.score = 0
            return
        self.score = 2 ** (self.matching_nums - 1)

    @classmethod
    def from_string(cls, input: str) -> Ticket:
        regex = r"^Card\s+(\d+):\s([\d\s]+)\s[\D]\s([\d\s]+)$"
        search = re.search(regex, input)
        ticket = cls(
            id=int(search.group(1)),
            winning_numbers=set(re.findall(r"\d+", search.group(2))),
            numbers=set(re.findall(r"\d+", search.group(3))),
        )
        return ticket


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        super().__init__(file_path)
        self.tickets = tuple(Ticket.from_string(line) for line in self.lines)

    def part_1(self):
        return sum(ticket.score for ticket in self.tickets)

    def part_2(self):
        counts = Counter([ticket.id for ticket in self.tickets])

        for ticket in self.tickets:
            new_tickets = self.tickets[ticket.id : ticket.id + ticket.matching_nums]
            for new_ticket in new_tickets:
                counts[new_ticket.id] += counts[ticket.id]

        return sum(counts.values())


def main():
    day = Solution("./aoc_2023/data/day_04.txt")
    day.run()


if __name__ == "__main__":
    main()
