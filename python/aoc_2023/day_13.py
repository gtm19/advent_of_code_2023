"""
https://adventofcode.com/2023/day/13
"""
from aoc_2023.base import Day
import numpy as np


def make_folds(n: int) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    lengths = (min(i + 1, n - i - 1) for i in range(n - 1))
    return tuple(
        tuple([tuple(range(i, i - length, -1)), tuple(range(i + 1, i + length + 1))])
        for i, length in enumerate(lengths)
    )


def get_symmetry(
    cluster: np.ndarray, fix_smudge: bool = False, axis: int = 0
) -> int | None:
    if axis == 1:
        cluster = cluster.T

    folds = make_folds(len(cluster))

    for i, (top, bottom) in enumerate(folds):
        if fix_smudge:
            if (cluster[top, :] != cluster[bottom, :]).sum() == 1:
                break
        else:
            if not (cluster[top, :] != cluster[bottom, :]).any():
                break
    else:
        return None

    return i + 1


def solve(lines: list, fix_smudge: bool = False) -> int:
    rows = [get_symmetry(cluster, fix_smudge, 0) for cluster in lines]
    cols = [get_symmetry(cluster, fix_smudge, 1) for cluster in lines]
    return sum(col for col in cols if col is not None) + 100 * sum(
        row for row in rows if row is not None
    )


class Solution(Day):
    def _get_lines(self) -> list[str]:
        with open(self.file_path, "r", encoding="UTF-8") as f:
            clusters = f.read().strip().split("\n\n")
            return [
                np.array([list(row) for row in cluster.split("\n")])
                for cluster in clusters
            ]

    def part_1(self) -> int:
        return solve(self.lines, False)

    def part_2(self) -> int:
        return solve(self.lines, True)


def main():
    day = Solution("./aoc_2023/data/day_13.txt")
    day.run()


if __name__ == "__main__":
    main()
