import aoc_2023.day_08 as day_08
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_08.txt")


@pytest.fixture
def solution():
    return day_08.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 6


def test_part_2(solution):
    assert solution.part_2() == 6


if __name__ == "__main__":
    pytest.main([__file__])
