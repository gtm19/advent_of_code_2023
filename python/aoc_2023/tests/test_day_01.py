import aoc_2023.day_01 as day_01
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_01.txt")


@pytest.fixture
def solution():
    return day_01.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == 0


def test_part_2(solution):
    assert solution.part_2() == 0
