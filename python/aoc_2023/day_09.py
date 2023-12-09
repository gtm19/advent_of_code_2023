"""
https://adventofcode.com/2023/day/9
"""
from aoc_2023.base import Day
import numpy as np


def add_n_terms(seq: np.ndarray, n: int = 1):
    if all(seq == 0):
        return np.append(seq, *([0] * n))
    return np.cumsum(np.insert(add_n_terms(np.diff(seq), n), 0, seq[0]))


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        super().__init__(file_path)
        self.sequences = [
            np.array(list(map(int, line.split(" ")))) for line in self.lines
        ]

    def part_1(self):
        return sum(add_n_terms(seq)[-1] for seq in self.sequences)

    def part_2(self):
        return sum(add_n_terms(np.flip(seq))[-1] for seq in self.sequences)


def main():
    day = Solution("./aoc_2023/data/day_09.txt")
    day.run()


if __name__ == "__main__":
    main()
