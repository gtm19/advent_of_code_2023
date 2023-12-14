import aoc_2023.day_03 as day_03
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_03.txt")


@pytest.fixture
def solution():
    return day_03.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 4361


def test_part_2(solution):
    assert solution.part_2() == 467835


if __name__ == "__main__":
    pytest.main([__file__])
