import aoc_2023.day_10 as day_10
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_10.txt")


@pytest.fixture
def solution():
    return day_10.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 8  # TODO: add expected result


# def test_part_2(solution):
#     assert True  # didn't need this in the end


if __name__ == "__main__":
    pytest.main([__file__])
