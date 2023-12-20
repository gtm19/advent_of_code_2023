"""
https://adventofcode.com/2023/day/17
"""
from aoc_2023.base import Day
from queue import PriorityQueue


def run(lines: list[str], min_steps: int = 1, max_steps: int = 3):
    queue = PriorityQueue()
    width = len(lines[0])
    height = len(lines)
    goal = (height - 1, width - 1)

    # initialise the set of visited points
    visited = set()

    # add the current point in both directions (horizontal / vertical) to the queue
    queue.put((0, (0, 0, 1)))
    queue.put((0, (0, 0, 0)))

    while True:
        # grab closest point by distance
        incoming_cost, (y, x, hor_or_ver) = queue.get()

        # if this point is our goal, return the cost to get there
        if (y, x) == goal:
            return incoming_cost

        # if the point has already been visited, we don't need to do it again
        if (y, x, hor_or_ver) in visited:
            continue

        # add the point to our visited set
        visited.add((y, x, hor_or_ver))

        # look at forwards and backwards separately
        for forwards_backwards in (-1, 1):
            # start with the cost which we got from getting to the point itself
            cost = incoming_cost
            # for 1 ... n steps:
            for i in range(1, max_steps + 1):
                # figure out where our new point is
                if hor_or_ver == 1:
                    new_x = x + (i * forwards_backwards)
                    new_y = y
                else:
                    new_x = x
                    new_y = y + (i * forwards_backwards)
                # if it is off grid, we can ignore that forwards/backwards direction
                if new_x < 0 or new_y < 0 or new_x >= width or new_y >= height:
                    break
                # otherwise add the cost of getting there to our running total for
                # this forwards/backwards direction
                cost += int(lines[new_y][new_x])
                # put together our new location, with cost
                new_location = (cost, (new_y, new_x, 1 - hor_or_ver))
                # if we have gone the minimum required number of steps, we can add this
                # location to the queue
                if i >= min_steps:
                    queue.put(new_location)


class Solution(Day):
    def part_1(self):
        return run(self.lines)

    def part_2(self):
        return run(self.lines, min_steps=4, max_steps=10)


def main():
    day = Solution("./aoc_2023/data/day_17.txt")
    day.run()


if __name__ == "__main__":
    main()
