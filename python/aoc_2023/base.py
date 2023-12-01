from abc import ABC, abstractmethod
from typing import Any


class Day(ABC):
    def __init__(self, file_path: str | None = None) -> None:
        self.file_path = file_path
        self.lines = self._get_lines()

    @abstractmethod
    def part_1(self) -> Any:
        pass

    @abstractmethod
    def part_2(self) -> Any:
        pass

    def run(self) -> None:
        print(f"Part 1: {self.part_1()}")
        print(f"Part 2: {self.part_2()}")

    def _get_lines(self) -> list[str]:
        if self.file_path is None:
            raise ValueError("No file path provided")
        with open(self.file_path, "r", encoding="UTF-8") as f:
            return f.read().splitlines()
