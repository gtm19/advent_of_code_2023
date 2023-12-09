#!/bin/zsh

set -e

# print help if no args, or if first arg is -h or --help
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    echo "Usage: setup_day.sh <day>"
    echo "day: the day to set up - must be greater than 0, and will be padded with 0 if less than 10"
    echo "e.g. setup_day.sh 1 -> sets up day01"
    exit 0
fi

# get arg being the day to set up
if [ $# -eq 0 ]; then
    echo "No arguments supplied, defaulting to current day"
    DAY=$(date +"%d")
    DAY=$(expr $DAY + 0)
else
    DAY=$1
fi
echo "Setting up day $DAY"
YEAR=2023
DIR=./aoc_$YEAR
DATA_DIR="$DIR/data"

# exit if day is not greater than 0
if [ $DAY -lt 1 ]; then
    echo "Day must be greater than 0"
    exit 1
fi

# pad with 0 if less than 10
DAY_PADDED=$(printf "%02d" $DAY)
echo "Setting up Python project for day $DAY"

# Initialise data file
DATA_FILE="$DATA_DIR/day_$DAY_PADDED.txt"
if [ ! -f $DATA_FILE ]; then
    echo "Creating $DATA_FILE"
    echo "INPUT DATA GOES HERE" > $DATA_FILE
fi

# Initialise module file
PY_FILE="$DIR/day_$DAY_PADDED.py"
if [ ! -f $PY_FILE ]; then
    echo "Creating $PY_FILE"
    cat << EOF > $PY_FILE
"""
https://adventofcode.com/$YEAR/day/$DAY
"""
from aoc_$YEAR.base import Day

class Solution(Day):
    def part_1(self):
        pass

    def part_2(self):
        pass


def main():
    day = Solution("$DATA_FILE")
    day.run()


if __name__ == "__main__":
    main()
EOF
fi

# Initialise test data file
TEST_DIR="./tests"
TEST_DATA_DIR="$TEST_DIR/data"

TEST_DATA_FILE="$TEST_DATA_DIR/day_$DAY_PADDED.txt"

if [ ! -f $TEST_DATA_FILE ]; then
    echo "Creating $TEST_DATA_FILE"
    echo "INPUT DATA GOES HERE" > $TEST_DATA_FILE
fi

# Initialise test script
TEST_FILE="$TEST_DIR/test_day_$DAY_PADDED.py"
if [ ! -f $TEST_FILE ]; then
    echo "Creating $TEST_FILE"
    cat << EOF > $TEST_FILE
import aoc_$YEAR.day_$DAY_PADDED as day_$DAY_PADDED
import os
import pytest

test_input = os.path.join(os.path.dirname(__file__), "data/day_$DAY_PADDED.txt")


@pytest.fixture
def solution():
    return day_$DAY_PADDED.Solution(test_input)


def test_part_1(solution):
    assert solution.part_1() == -9999 # TODO: add expected result

def test_part_2(solution):
    assert solution.part_2() == -9999 # TODO: add expected result


if __name__ == "__main__":
    pytest.main([__file__])
EOF
fi

echo "All necessary files created"
