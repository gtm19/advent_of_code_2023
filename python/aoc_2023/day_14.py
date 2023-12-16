"""
https://adventofcode.com/2023/day/14
"""
from typing import Sequence
from aoc_2023.base import Day


def transpose(input: list[list]) -> list[list]:
    return [list(i) for i in zip(*input)]


def slide(input: list) -> list:
    for i in range(1, len(input)):
        if input[i] == "O":
            j = i
            while j > 0 and input[j - 1] == ".":
                input[j], input[j - 1] = input[j - 1], input[j]
                j -= 1
    return input


def score_line(line: str) -> int:
    return sum(
        (char == "O") * (score + 1) for char, score in zip(line, range(len(line))[::-1])
    )


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        super().__init__(file_path)
        self.lines = [list(line) for line in self.lines]

    def part_1(self):
        lines = transpose(self.lines)
        lines = [slide(line) for line in lines]
        return sum(score_line(line) for line in lines)

    def part_2(self):
        pass


def main():
    day = Solution("./aoc_2023/data/day_14.txt")
    day.run()


if __name__ == "__main__":
    main()
