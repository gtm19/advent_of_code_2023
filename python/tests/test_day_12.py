import aoc_2023.day_12 as day_12
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_12.txt")


@pytest.fixture
def solution():
    return day_12.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 21  # TODO: add expected result


def test_part_2(solution):
    assert solution.part_2() == 525152  # TODO: add expected result


if __name__ == "__main__":
    pytest.main([__file__])
