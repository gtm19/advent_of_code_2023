"""
https://adventofcode.com/2023/day/5
"""
from __future__ import annotations
from aoc_2023.base import Day
from dataclasses import dataclass, field
import re
from typing import Optional


@dataclass
class Func:
    maps: tuple[tuple[int, int, int], ...]
    ranges: Optional[tuple[tuple[range, range], ...]] = None

    def __post_init__(self):
        self.ranges = tuple(
            tuple([range(map[1], map[1] + map[2]), range(map[0], map[0] + map[2])])
            for map in self.maps
        )

    def call_int(self, input: int) -> int:
        for source, dest in self.ranges:
            if input in source:
                return dest[source.index(input)]
        return input

    def call_range(self, input: list[range]) -> list[range]:
        pass

    def __call__(self, input: int | range) -> int | list[range]:
        if isinstance(input, int):
            return self.call_int(input)
        if isinstance(input, (range, list)):
            return self.call_range(input)


@dataclass
class Almanac:
    seeds: list[int] | list[range]
    funcs: list[Func] = field(default_factory=list)

    @classmethod
    def from_lines(cls, lines: list[str], use_range: bool = False) -> Almanac:
        seeds = list(map(int, re.findall(r"\d+", lines[0])))
        if use_range:
            new_seeds = []
            for i in range(0, len(seeds), 2):
                new_seeds.append(range(seeds[i], seeds[i] + seeds[i + 1]))
            seeds = new_seeds
        funcs = []
        for line in lines[1:]:
            map_str = re.match(r".+([\d\s\n]+)", line).group(1).strip().split("\n")
            maps = tuple(tuple(map(int, string.split(" "))) for string in map_str)
            funcs.append(Func(maps))

        return cls(seeds, funcs)

    def map_int(self):
        seeds = self.seeds.copy()
        for i, func in enumerate(self.funcs):
            seeds = list(func(seed) for seed in seeds)
        return seeds

    def map_range(self):
        pass


class Solution(Day):
    def _get_lines(self) -> list[str]:
        if self.file_path is None:
            raise ValueError("No file path provided")
        with open(self.file_path, "r", encoding="UTF-8") as f:
            return f.read().split("\n\n")

    def part_1(self):
        almanac = Almanac.from_lines(self.lines)
        return min(almanac.map_int())

    def part_2(self):
        almanac = Almanac.from_lines(self.lines, use_range=True)
        return


def main():
    day = Solution("./aoc_2023/data/day_05.txt")
    day.run()


if __name__ == "__main__":
    main()
