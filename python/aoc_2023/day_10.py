"""
https://adventofcode.com/2023/day/10
"""
from aoc_2023.base import Day

VALID_STEPS = {
    (0, -1): "|F7",
    (1, 0): "-7J",
    (0, 1): "|JL",
    (-1, 0): "-FL",
}


class Solution(Day):
    def part_1(self):
        self.n_rows = len(self.lines)
        self.n_cols = len(self.lines[0])
        current_value = "S"
        start_row = [current_value in line for line in self.lines].index(True)
        start_col = self.lines[start_row].index(current_value)
        current_location = (start_row, start_col)
        path = [current_location]

        direction = None

        for step in VALID_STEPS:
            new_location = (
                path[-1][0] + step[0],
                path[-1][1] + step[1],
            )
            if (
                0 <= new_location[0] < self.n_rows
                and 0 <= new_location[1] < self.n_cols
            ):
                new_value = self.lines[new_location[0]][new_location[1]]
                if new_value in VALID_STEPS.get(step):
                    current_value = new_value
                    direction = step
                    path.append(new_location)
                    break

        while current_value != "S":
            match current_value:
                case "F" | "J":
                    direction = (-1 * direction[1], -1 * direction[0])
                case "7" | "L":
                    direction = (direction[1], direction[0])
            new_location = (
                path[-1][0] + direction[0],
                path[-1][1] + direction[1],
            )
            path.append(new_location)
            current_value = self.lines[new_location[0]][new_location[1]]

        self.path = path

        return int((len(path) - 1) / 2)

    def part_2(self):
        trapped_points = 0

        for row_i in range(self.n_rows):
            trapped_this_row = 0
            n_crossings = 0
            for col_i in range(self.n_cols):
                if (row_i, col_i) in self.path:
                    # can safely add 'S' here because it is a "|" in my input
                    if self.lines[row_i][col_i] in "|JLS":
                        n_crossings += 1
                else:
                    trapped_this_row += n_crossings % 2
            trapped_points += trapped_this_row

        return trapped_points


def main():
    day = Solution("./aoc_2023/data/day_10.txt")
    day.run()


if __name__ == "__main__":
    main()
