"""
https://adventofcode.com/2023/day/11
"""
from aoc_2023.base import Day
import numpy as np
from itertools import combinations


def dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def expand_and_measure(lines, expansion: int = 2):
    image = np.array([list(line) for line in lines])

    rows, cols = np.where(image == "#")

    missing_rows = np.setdiff1d(np.arange(len(image)), rows)
    missing_cols = np.setdiff1d(np.arange(len(image[0])), cols)

    rows = rows + (expansion - 1) * sum(
        (rows > missing_rows[i]).astype(int) for i in range(len(missing_rows))
    )
    cols = cols + (expansion - 1) * sum(
        (cols > missing_cols[i]).astype(int) for i in range(len(missing_cols))
    )

    galaxies = zip(rows, cols)
    galaxy_pairs = combinations(galaxies, 2)

    return sum(dist(*pair) for pair in galaxy_pairs)


class Solution(Day):
    def part_1(self):
        return expand_and_measure(self.lines, 2)

    def part_2(self):
        return expand_and_measure(self.lines, 1_000_000)


def main():
    day = Solution("./aoc_2023/data/day_11.txt")
    day.run()


if __name__ == "__main__":
    main()
