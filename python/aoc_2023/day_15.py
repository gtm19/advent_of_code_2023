"""
https://adventofcode.com/2023/day/15
"""
from aoc_2023.base import Day
import re
from collections import defaultdict


def hash_int(n: int) -> int:
    return (17 * n) % 256


def hash(step: str) -> int:
    ints = [ord(char) for char in step]

    start = 0
    for n in ints:
        start += n
        start = hash_int(start)

    return start % 256


def slots_score(input: dict) -> int:
    if len(input) == 0:
        return 0
    return sum((i + 1) * focal_length for i, focal_length in enumerate(input.values()))


class Solution(Day):
    def _get_lines(self) -> list[str]:
        with open(self.file_path, "r", encoding="utf-8") as f:
            return f.read().strip().split(",")

    def part_1(self):
        return sum(hash(step) for step in self.lines)

    def part_2(self):
        storage = defaultdict(dict)
        # storage = {key: {} for key in range(256)}
        for step in self.lines:
            regex = re.match(r"^([a-z]+)([=-])(\d)?$", step)
            label = regex.group(1)
            key = hash(label)

            if "=" in regex.groups():
                storage[key][label] = int(regex.group(3))
            else:
                for storage_key in storage:
                    if label in storage[storage_key]:
                        del storage[storage_key][label]
                        break
        return sum((i + 1) * slots_score(slots) for i, slots in storage.items())


def main():
    day = Solution("./aoc_2023/data/day_15.txt")
    day.run()


if __name__ == "__main__":
    main()
    # print(hash("pc=6"))
