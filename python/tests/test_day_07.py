import aoc_2023.day_07 as day_07
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_07.txt")


@pytest.fixture
def solution():
    return day_07.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 6440


def test_part_2(solution):
    assert solution.part_2() == 5905


if __name__ == "__main__":
    pytest.main([__file__])
