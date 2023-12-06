import aoc_2023.day_05 as day_05
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_05.txt")


@pytest.fixture
def solution():
    return day_05.Solution(test_input)


@pytest.fixture
def mapper():
    return day_05.Func(((50, 98, 2), (52, 50, 48)))


@pytest.mark.parametrize(
    "n_in, n_out", zip((5, 51, 80, 99, 1000), (5, 53, 82, 51, 1000))
)
def test_func(mapper, n_in, n_out):
    assert mapper(n_in) == n_out


def test_part_1(solution):
    assert solution.part_1() == 35  # TODO: add expected result


def test_part_2(solution):
    assert solution.part_2() == 46  # TODO: add expected result


if __name__ == "__main__":
    pytest.main([__file__])
