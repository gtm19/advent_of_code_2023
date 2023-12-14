import aoc_2023.day_11 as day_11
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_11.txt")


@pytest.fixture
def solution():
    return day_11.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 374


# def test_part_2(solution):
#     assert solution.part_2() == 1030  # removed because the test n is 10, whilst actual challenge is 1m


if __name__ == "__main__":
    pytest.main([__file__])
