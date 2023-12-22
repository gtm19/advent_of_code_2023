import aoc_2023.day_19 as day_19
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_19.txt")


@pytest.fixture
def solution():
    return day_19.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 19114


def test_part_2(solution):
    assert solution.part_2() == 167409079868000


if __name__ == "__main__":
    pytest.main([__file__])
