"""
https://adventofcode.com/2023/day/12
"""
from aoc_2023.base import Day
import re
from functools import cache


@cache
def count_possibilities(clue: str, groups: tuple[int, ...]) -> int:
    # get the length of the first damaged spring
    group = groups[0]

    # save the rest for later
    groups = groups[1:]

    # total length of the row
    total_length = len(clue)

    # initialise number of possibilities
    possibilities = 0

    # the range of values from which our first group of damaged springs can start
    # takes into account:
    #  - the total length of the row
    #  - less the space needed for the remaining groups
    #  - less 1 space of padding for each of the remaining groups
    #  - less the space that the group itself would take up
    #  - plus 1 because the first element of the group would start on the first value
    start_values = range(total_length - sum(groups) - len(groups) - group + 1)

    for start in start_values:
        # get the possible match e.g. "?##"
        possible_match = clue[start : start + group]
        # get the remaining characters of the clue e.g. "#????????"
        remaining_chars = clue[start + group :]

        # if none of the characters are a ., then this could be our chain of damaged springs
        if not any(char == "." for char in possible_match):
            # if we are not in our last group
            if len(groups) > 0:
                # and if the next character is not a "#" (since this would make the group
                # length n+1)
                if remaining_chars[0] != "#":
                    # then we *keep this as a possibility*, but defer its counting
                    # to when we get to the last group. e.g. if there are 2 possible start
                    # values, the next line will create 2 paths towards the finish
                    possibilities += count_possibilities(remaining_chars[1:], groups)
            else:
                # if we are in the last group and there are no more #s beween our
                # possible match and the end of the string, it is time to count it
                if not any(char == "#" for char in remaining_chars):
                    possibilities += 1

        # if the first character of our possible match is #, we must have
        # found the chain - no need to try other start values
        if possible_match[0] == "#":
            break

    return possibilities


class Solution(Day):
    def _get_lines(self) -> list[str]:
        lines = super()._get_lines()
        return [
            (
                re.match(r"[\.\?#]+", line).group(),
                tuple(int(digit) for digit in re.findall(r"\d+", line)),
            )
            for line in lines
        ]

    def part_1(self):
        return sum(count_possibilities(*line) for line in self.lines)

    def part_2(self):
        lines = [
            ("?".join([line[0]] * 5), tuple(list(line[1]) * 5)) for line in self.lines
        ]
        return sum(count_possibilities(*line) for line in lines)


def main():
    day = Solution("./aoc_2023/data/day_12.txt")
    day.run()


if __name__ == "__main__":
    main()
