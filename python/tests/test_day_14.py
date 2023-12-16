import aoc_2023.day_14 as day_14
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_14.txt")


@pytest.fixture
def solution():
    return day_14.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 136


def test_part_2(solution):
    assert solution.part_2() == 64  # TODO: add expected result


if __name__ == "__main__":
    pytest.main([__file__])
