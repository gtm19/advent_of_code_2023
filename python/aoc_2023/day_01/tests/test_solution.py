from aoc_2023.day_01 import Solution
import pytest
import os

file_path = os.path.join(os.path.dirname(__file__), "../data/test.txt")


@pytest.fixture
def day():
    return Solution(file_path)


class TestParts:
    def test_part_1(self, day):
        print(file_path)
        assert day.part_1() == -9999

    def test_part_2(self, day):
        assert day.part_2() == -9999
