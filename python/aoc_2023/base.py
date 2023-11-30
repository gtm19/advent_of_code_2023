from abc import ABC, abstractmethod
from typing import Any


def get_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        return f.readlines()


class Day(ABC):
    def __init__(self, file_path: str | None = None) -> None:
        print(__file__)
        if file_path is not None:
            self.lines = get_lines(file_path)

    @abstractmethod
    def part_1(self) -> Any:
        pass

    @abstractmethod
    def part_2(self) -> Any:
        pass

    def run(self) -> None:
        print(f"Part 1: {self.part_1()}")
        print(f"Part 2: {self.part_2()}")
