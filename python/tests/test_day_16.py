import aoc_2023.day_16 as day_16
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_16.txt")


@pytest.fixture
def solution():
    return day_16.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 46


def test_part_2(solution):
    assert solution.part_2() == 51


if __name__ == "__main__":
    pytest.main([__file__])
