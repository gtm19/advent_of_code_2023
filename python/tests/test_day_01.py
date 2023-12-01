import aoc_2023.day_01 as day_01
import os
import pytest

test_input_1 = os.path.join(os.path.dirname(__file__), "data/day_01_1.txt")
test_input_2 = os.path.join(os.path.dirname(__file__), "data/day_01_2.txt")


@pytest.fixture
def solution1():
    return day_01.Solution(test_input_1)


@pytest.fixture
def solution2():
    return day_01.Solution(test_input_2)


def test_part_1(solution1):
    assert solution1.part_1() == 142


def test_part_2(solution2):
    assert solution2.part_2() == 281


if __name__ == "__main__":
    pytest.main([__file__])
