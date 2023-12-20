import aoc_2023.day_17 as day_17
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_17.txt")


@pytest.fixture
def solution():
    return day_17.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 102


def test_part_2(solution):
    assert solution.part_2() == 94


if __name__ == "__main__":
    pytest.main([__file__])
