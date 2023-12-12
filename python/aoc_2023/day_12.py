"""
https://adventofcode.com/2023/day/12
"""
from aoc_2023.base import Day
import re
from itertools import combinations


def rows_from_tuple(groups: tuple[int, ...], length: int):
    n_blanks = length - sum(groups) - len(groups) + 1
    options = combinations(range(len(groups) + n_blanks), len(groups))
    for option in options:
        row = ""
        blanks_so_far = 0
        for group, blank_val in zip(groups, option):
            row += "." * (blank_val - blanks_so_far)
            blanks_so_far += blank_val - blanks_so_far
            row += "#" * group
        row += "." * (length - len(row))
        yield row


def valid_options(clue: str, groups: tuple[int, ...]) -> list[str]:
    rows = rows_from_tuple(groups, len(clue))
    regex = re.compile(f"{clue.replace('.', r'\.').replace('?', r'[\.#]')}")
    return len([row for row in rows if regex.match(row)])


class Solution(Day):
    def _get_lines(self) -> list[str]:
        lines = super()._get_lines()
        return [
            (
                re.match(r"[\.\?#]+", line).group(),
                tuple(int(digit) for digit in re.findall(r"\d+", line)),
            )
            for line in lines
        ]

    def part_1(self):
        return sum(valid_options(*line) for line in self.lines)

    def part_2(self):
        # lines = [(line[0] * 5, tuple(list(line[1]) * 5)) for line in self.lines]
        # return sum(valid_options(*line) for line in lines)
        pass


def main():
    day = Solution("./aoc_2023/data/day_12.txt")
    day.run()


if __name__ == "__main__":
    main()
