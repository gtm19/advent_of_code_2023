import aoc_2023.day_15 as day_15
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_15.txt")


@pytest.fixture
def solution():
    return day_15.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 1320


def test_part_2(solution):
    assert solution.part_2() == -9999  # TODO: add expected result


if __name__ == "__main__":
    pytest.main([__file__])
