"""
https://adventofcode.com/2023/day/6
"""
from aoc_2023.base import Day
import re
from math import prod, floor, ceil


def solve_poly(a, b, c):
    numerator_bit = (b**2 - 4 * a * c) ** (0.5)
    return (-b - numerator_bit) / 2 * a, (-b + numerator_bit) / 2 * a


def range_to_len(start, stop):
    return floor(stop - 1e-5) - ceil(start + 1e-5) + 1


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        super().__init__(file_path)
        self.races = zip(
            map(int, re.findall(r"\d+", self.lines[0])),
            map(int, re.findall(r"\d+", self.lines[1])),
        )

    def part_1(self):
        return prod(
            range_to_len(*solve_poly(1, -duration, score_to_beat))
            for duration, score_to_beat in self.races
        )

    def part_2(self):
        duration = int("".join(re.findall(r"\d+", self.lines[0])))
        score_to_beat = int("".join(re.findall(r"\d+", self.lines[1])))
        return range_to_len(*solve_poly(1, -duration, score_to_beat))


def main():
    day = Solution("./aoc_2023/data/day_06.txt")
    day.run()


if __name__ == "__main__":
    main()
