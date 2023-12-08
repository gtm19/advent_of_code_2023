"""
https://adventofcode.com/2023/day/8
"""
from aoc_2023.base import Day
import re
import math


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        super().__init__(file_path)
        self.directions = self.lines[0]
        self.paths = {}
        for line in self.lines[2:]:
            start, left, right = re.findall(r"[A-Z]+", line)
            self.paths[start] = tuple([left, right])

    def part_1(self):
        current = "AAA"
        n_steps = 0
        while current != "ZZZ":
            current = self.paths[current][
                self.directions[n_steps % len(self.directions)] == "R"
            ]
            n_steps += 1

        return n_steps

    def part_2(self):
        currents = [node for node in list(self.paths.keys()) if node[-1] == "A"]
        currents_steps = []

        for current in currents:
            n_steps = 0

            while current[-1] != "Z":
                current = self.paths[current][
                    self.directions[n_steps % len(self.directions)] == "R"
                ]
                n_steps += 1
            currents_steps.append(n_steps)

        return math.lcm(*currents_steps)


def main():
    day = Solution("./aoc_2023/data/day_08.txt")
    day.run()


if __name__ == "__main__":
    main()
