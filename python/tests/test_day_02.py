import aoc_2023.day_02 as day_02
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_02.txt")


@pytest.fixture
def solution():
    return day_02.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 8


def test_part_2(solution):
    assert solution.part_2() == 2286


if __name__ == "__main__":
    pytest.main([__file__])
