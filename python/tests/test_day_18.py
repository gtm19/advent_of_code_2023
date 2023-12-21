import aoc_2023.day_18 as day_18
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_18.txt")


@pytest.fixture
def solution():
    return day_18.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 62


def test_part_2(solution):
    assert solution.part_2() == 952408144115


if __name__ == "__main__":
    pytest.main([__file__])
