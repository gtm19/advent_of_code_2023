import aoc_2023.day_09 as day_09
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_09.txt")


@pytest.fixture
def solution():
    return day_09.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 114


def test_part_2(solution):
    assert solution.part_2() == 2


if __name__ == "__main__":
    pytest.main([__file__])
