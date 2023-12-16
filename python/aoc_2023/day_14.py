"""
https://adventofcode.com/2023/day/14
"""
from typing import Sequence
from aoc_2023.base import Day


def transpose(input: list[str]) -> list[str]:
    return [
        "".join([input[j][i] for j in range(len(input))]) for i in range(len(input[0]))
    ]


def slide(points: tuple[int], anchors: tuple[int]):
    anchors = (-999,) + anchors + (float("inf"),)

    new_points = []
    for left, right in zip(anchors[:-1], anchors[1:]):
        start = max(-1, left)
        new_points.extend(
            range(
                start + 1,
                start
                + 1
                + len([point for point in points if point > left and point < right]),
            )
        )

    return tuple(new_points)


def score_line(line: str) -> int:
    noughts = tuple(i for i, char in enumerate(line) if char == "O")
    hashes = tuple(i for i, char in enumerate(line) if char == "#")

    return sum(len(line) - nought for nought in slide(noughts, hashes))


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        super().__init__(file_path)
        self.noughts = self.find("O")
        self.hashes = self.find("#")

    def find(self, char: str = "O"):
        points = []
        for row_i, row in enumerate(self.lines):
            for col_i, item in enumerate(row):
                if item == char:
                    points.append(
                        (
                            row_i,
                            col_i,
                        )
                    )
        return points

    def part_1(self):
        lines = transpose(self.lines)
        return sum(score_line(line) for line in lines)

    def part_2(self):
        pass


def main():
    day = Solution("./aoc_2023/data/day_14.txt")
    day.run()


if __name__ == "__main__":
    main()
    # print(slide((0, 4, 5, 9), (2, 6, 7)))
    # print(slide((3, 4, 5, 6, 7, 8, 6, 5, 4), ()))
    # expect (0, 3, 4, 8)
