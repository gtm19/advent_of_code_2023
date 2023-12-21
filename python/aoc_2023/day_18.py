"""
https://adventofcode.com/2023/day/18
"""
from aoc_2023.base import Day
import re

DIG_DIRECTIONS = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


def trace(lines: list[str], hex: bool = False):
    row, col = (0, 0)
    points = []
    perimiter = 0

    for line in lines:
        direction, steps, colour = line.split(" ")
        colour = colour.replace("(", "").replace(")", "").replace("#", "")
        if hex:
            steps = int(colour[:-1], 16)
            direction = DIG_DIRECTIONS.get(colour[-1])
        else:
            steps = int(steps)
        perimiter += steps
        match direction:
            case "R":
                col += steps
            case "L":
                col -= steps
            case "D":
                row += steps
            case "U":
                row -= steps
            case other:
                raise ValueError(f"No case {other}")
        points.append((row, col, colour))

    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0.5 * sum(
        (p_1[0] + p_2[0]) * (p_1[1] - p_2[1])
        for p_1, p_2 in zip(points[:-1], points[1:])
    )

    return int(area + (perimiter / 2) + 1)


class Solution(Day):
    def part_1(self):
        return trace(self.lines)

    def part_2(self):
        return trace(self.lines, hex=True)


def main():
    day = Solution("./aoc_2023/data/day_18.txt")
    day.run()


if __name__ == "__main__":
    main()
