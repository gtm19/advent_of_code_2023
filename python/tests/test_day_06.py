import aoc_2023.day_06 as day_06
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_06.txt")


@pytest.fixture
def solution():
    return day_06.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 288


def test_part_2(solution):
    assert solution.part_2() == 71503


if __name__ == "__main__":
    pytest.main([__file__])
