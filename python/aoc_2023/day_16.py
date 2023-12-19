"""
https://adventofcode.com/2023/day/16
"""
from aoc_2023.base import Day
from collections import defaultdict

DIRECTIONS = {
    "r": (0, 1),
    "d": (1, 0),
    "l": (0, -1),
    "u": (-1, 0),
}


def run(lines, start) -> int:
    width = len(lines[0])
    height = len(lines)
    starts = [start]
    visited = defaultdict(list)
    while len(starts) > 0:
        location, direction = starts.pop()

        while direction not in visited[location] and (
            0 <= location[0] < height and 0 <= location[1] < width
        ):
            visited[location].append(direction)
            current_value = lines[location[0]][location[1]]

            if direction in ("r", "l"):
                if current_value == "|":
                    starts.append(((location[0] - 1, location[1]), "u"))
                    location = (location[0] + 1, location[1])
                    direction = "d"
                    continue
                elif current_value == "\\":
                    direction = list(DIRECTIONS.keys())[
                        (list(DIRECTIONS.keys()).index(direction) + 1) % len(DIRECTIONS)
                    ]
                    delta = DIRECTIONS.get(direction)
                    location = (location[0] + delta[0], location[1] + delta[1])
                elif current_value == "/":
                    direction = list(DIRECTIONS.keys())[
                        (list(DIRECTIONS.keys()).index(direction) - 1) % len(DIRECTIONS)
                    ]
                    delta = DIRECTIONS.get(direction)
                    location = (location[0] + delta[0], location[1] + delta[1])
                else:
                    delta = DIRECTIONS.get(direction)
                    location = (location[0] + delta[0], location[1] + delta[1])
                continue

            if direction in ("u", "d"):
                if current_value == "-":
                    starts.append(((location[0], location[1] - 1), "l"))
                    location = (location[0], location[1] + 1)
                    direction = "r"
                elif current_value == "\\":
                    direction = list(DIRECTIONS.keys())[
                        (list(DIRECTIONS.keys()).index(direction) - 1) % len(DIRECTIONS)
                    ]
                    delta = DIRECTIONS.get(direction)
                    location = (location[0] + delta[0], location[1] + delta[1])
                elif current_value == "/":
                    direction = list(DIRECTIONS.keys())[
                        (list(DIRECTIONS.keys()).index(direction) + 1) % len(DIRECTIONS)
                    ]
                    delta = DIRECTIONS.get(direction)
                    location = (location[0] + delta[0], location[1] + delta[1])
                else:
                    delta = DIRECTIONS.get(direction)
                    location = (location[0] + delta[0], location[1] + delta[1])
                continue
    return len([position for position, directions in visited.items() if directions])


class Solution(Day):
    def part_1(self):
        return run(self.lines, ((0, 0), "r"))

    def part_2(self):
        tops = tuple(((0, n), "d") for n in range(len(self.lines[0])))
        bottoms = tuple(
            ((len(self.lines[0]) - 1, n), "d") for n in range(len(self.lines[0]))
        )
        lefts = tuple(((n, 0), "r") for n in range(len(self.lines)))
        rights = tuple(((n, len(self.lines) - 1), "l") for n in range(len(self.lines)))
        starts = tops + bottoms + lefts + rights
        return max(run(self.lines, start) for start in starts)


def main():
    day = Solution("./aoc_2023/data/day_16.txt")
    day.run()


if __name__ == "__main__":
    main()
