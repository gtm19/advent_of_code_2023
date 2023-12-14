import aoc_2023.day_13 as day_13
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_13.txt")


@pytest.fixture
def solution():
    return day_13.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 405


def test_part_2(solution):
    assert solution.part_2() == 400


if __name__ == "__main__":
    pytest.main([__file__])
