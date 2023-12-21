"""
https://adventofcode.com/2023/day/19
"""
from __future__ import annotations
from aoc_2023.base import Day
from dataclasses import dataclass
import re


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    @classmethod
    def from_str(cls, string: str) -> Part:
        return cls(*map(int, re.findall(r"\d+", string)))


def make_lookup(input: str = "ccr{a<259:A,x>2863:R,m>2689:jpj,xt}"):
    label, rules = re.match(r"^([a-z]+){(.+)}$", input).groups()
    rules = rules.split(",")
    pre_rules, lastly = rules[:-1], rules[-1]

    def lookup(part: Part):
        for rule in pre_rules:
            attr, func, num, outcome = re.match(
                r"^([xmas])([<>])(\d+):([A-z]+)$", rule
            ).groups()
        pass

    return lookup


class Solution(Day):
    def part_1(self):
        pass

    def part_2(self):
        pass


def main():
    day = Solution("./aoc_2023/data/day_19.txt")
    day.run()


if __name__ == "__main__":
    # main()
    print(Part.from_str("{x=1351,m=134,a=1152,s=1764}"))
    lookup = make_lookup()
    lookup(Part.from_str("{x=1351,m=134,a=1152,s=1764}"))
