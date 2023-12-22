"""
https://adventofcode.com/2023/day/19
"""
from __future__ import annotations
from aoc_2023.base import Day
from dataclasses import dataclass
import re
from typing import Callable
from copy import copy
from math import prod


@dataclass
class PartRange:
    x: range = range(4000)
    m: range = range(4000)
    a: range = range(4000)
    s: range = range(4000)

    def __len__(self) -> int:
        return prod(len(getattr(self, attr)) for attr in ["x", "m", "a", "s"])

    def split(self, attr: str, n: int) -> tuple[PartRange, PartRange]:
        pr_1 = copy(self)
        pr_2 = copy(self)

        setattr(pr_1, attr, range(getattr(pr_1, attr).start, n))
        setattr(pr_2, attr, range(n, getattr(pr_2, attr).stop))

        return pr_1, pr_2


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


@dataclass
class System:
    input: str

    def __post_init__(self):
        self.label, rules = re.match(r"^([a-z]+){(.+)}$", self.input).groups()
        rules = rules.split(",")
        pre_rules, self.lastly = rules[:-1], rules[-1]

        self.pre_rules = tuple(
            re.match(r"^([xmas])([<>])(\d+):([A-z]+)$", rule).groups()
            for rule in pre_rules
        )

    def lookup(self, part: Part) -> str:
        for attr, func, num, outcome in self.pre_rules:
            value = getattr(part, attr)
            num = int(num)
            if func == ">" and value > num:
                return outcome
            if func == "<" and value < num:
                return outcome
        return self.lastly

    def with_label(self):
        return self.label, self

    def split(self, part_range: PartRange):
        destinations = []
        start = part_range
        for attr, func, num, outcome in self.pre_rules:
            num = int(num)
            if func == ">":
                start, part_pr = start.split(attr, num)
            if func == "<":
                part_pr, start = start.split(attr, num - 1)
            destinations.append((outcome, part_pr))
        destinations.append((self.lastly, start))
        return destinations


class Solution(Day):
    def __init__(self, file_path: str | None = None) -> None:
        with open(file_path, "r", encoding="utf-8") as f:
            workflows, parts = f.read().split("\n\n")
            self.parts = [Part.from_str(part) for part in parts.strip().split("\n")]
            self.workflows = dict(
                [System(input).with_label() for input in workflows.strip().split("\n")]
            )

    def part_1(self):
        accepted = []

        while self.parts:
            part = self.parts.pop()
            workflow = "in"
            while workflow not in ("A", "R"):
                workflow = self.workflows.get(workflow).lookup(part)
            if workflow == "A":
                accepted.append(part)

        return sum(part.sum() for part in accepted)

    def part_2(self):
        accepted = []
        ranges = [("in", PartRange())]

        while ranges:
            workflow, pr = ranges.pop()
            if workflow == "A":
                accepted.append(pr)
                continue
            if workflow == "R":
                continue
            ranges.extend(self.workflows.get(workflow).split(pr))

        return sum(len(pr) for pr in accepted)


def main():
    day = Solution("./aoc_2023/data/day_19.txt")
    day.run()


if __name__ == "__main__":
    main()
