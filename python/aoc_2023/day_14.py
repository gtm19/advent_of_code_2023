"""
https://adventofcode.com/2023/day/14
"""
from aoc_2023.base import Day
from copy import deepcopy


def slide_horizontal(input: list[list], reverse: bool = False) -> list[list]:
    """
    reverse = False => left
    reverse = True => right
    """
    for i, row in enumerate(input):
        if reverse:
            row.reverse()
        for j in range(1, len(row)):
            if row[j] == "O":
                k = j
                while k > 0 and row[k - 1] == ".":
                    row[k], row[k - 1] = row[k - 1], row[k]
                    k -= 1
        if reverse:
            row.reverse()
        input[i] = row
    return input


def slide_vertical(input: list[list], reverse: bool = False) -> list[list]:
    """
    reverse = False => up
    reverse = True => down
    """
    if reverse:
        input.reverse()
    for row_i in range(1, len(input)):
        for col_i in range(len(input[row_i])):
            if (char := input[row_i][col_i]) == "O":
                k = row_i
                while k > 0 and input[k - 1][col_i] == ".":
                    input[k][col_i], input[k - 1][col_i] = (
                        input[k - 1][col_i],
                        input[k][col_i],
                    )
                    k -= 1
    if reverse:
        input.reverse()
    return input


def cycle(input: list[list]) -> list[list]:
    # north
    slide_vertical(input)
    # west
    slide_horizontal(input)
    # south
    slide_vertical(input, reverse=True)
    # east
    slide_horizontal(input, reverse=True)
    return input


def run(input: list[list], times: int = 1) -> list[list]:
    results = []
    for i in range(times):
        input = cycle(input)
        cycle_hash = deepcopy(input)
        if cycle_hash in results:
            # where did the existing result occur?
            where = results.index(cycle_hash)
            # What is the cycle length
            cycle_length = i - where
            # after a bunch of cycles, how many short of `times` would 'where' be?
            short = (times - where) % cycle_length
            # Get the result 'short' places along (-1 for 0-index)
            return results[where + short - 1]
        # if it's a new result, append it
        results.append(cycle_hash)
    return input


def score_lines(input: list[list]) -> int:
    line_scores = [
        (len(input) - i) * sum(char == "O" for char in row)
        for i, row in enumerate(input)
    ]

    return sum(line_scores)


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        super().__init__(file_path)
        self.lines = [list(line) for line in self.lines]

    def part_1(self):
        lines = self.lines.copy()
        slide_vertical(lines, reverse=False)
        return score_lines(lines)

    def part_2(self):
        lines = self.lines.copy()
        result = run(lines, 1_000_000_000)
        return score_lines(result)


def main():
    day = Solution("./aoc_2023/data/day_14.txt")
    day.run()


if __name__ == "__main__":
    main()
