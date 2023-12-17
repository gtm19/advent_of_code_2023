"""
https://adventofcode.com/2023/day/15
"""
from aoc_2023.base import Day


class Solution(Day):
    def _get_lines(self) -> list[str]:
        with open(self.file_path, "r", encoding="utf-8") as f:
            return f.read().strip().split(",")

    def part_1(self):
        pass

    def part_2(self):
        pass


def main():
    day = Solution("./aoc_2023/data/day_15.txt")
    day.run()


if __name__ == "__main__":
    main()
