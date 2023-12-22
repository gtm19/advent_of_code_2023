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

    def sum(self) -> int:
        return self.x + self.m + self.a + self.s


def make_lookup(input: str = "ccr{a<259:A,x>2863:R,m>2689:jpj,xt}"):
    label, rules = re.match(r"^([a-z]+){(.+)}$", input).groups()
    rules = rules.split(",")
    pre_rules, lastly = rules[:-1], rules[-1]

    def lookup(part: Part):
        for rule in pre_rules:
            attr, func, num, outcome = re.match(
                r"^([xmas])([<>])(\d+):([A-z]+)$", rule
            ).groups()
            value = getattr(part, attr)
            num = int(num)
            if func == ">" and value > num:
                return outcome
            if func == "<" and value < num:
                return outcome
        return lastly

    return label, lookup


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        with open(file_path, "r", encoding="utf-8") as f:
            workflows, parts = f.read().split("\n\n")
            self.parts = [Part.from_str(part) for part in parts.strip().split("\n")]
            self.workflows = {
                label: func
                for label, func in [
                    make_lookup(input) for input in workflows.strip().split("\n")
                ]
            }

    def part_1(self):
        results = {"A": [], "R": []}

        while self.parts:
            part = self.parts.pop()
            workflow = "in"
            while workflow not in ("A", "R"):
                workflow = self.workflows.get(workflow)(part)
            results[workflow].append(part)

        return sum(part.sum() for part in results["A"])

    def part_2(self):
        pass


def main():
    day = Solution("./aoc_2023/data/day_19.txt")
    day.run()


if __name__ == "__main__":
    main()
