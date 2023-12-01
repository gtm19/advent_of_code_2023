from aoc_2023.base import Day
import re

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_digits(
    input: str | list[str], swap_digits: bool = False
) -> int | list[int]:
    if isinstance(input, list):
        return [extract_digits(i, swap_digits) for i in input]
    if swap_digits:
        word_digits = re.findall("|".join(DIGITS), input)
        for word in word_digits:
            input = re.sub(word, str(DIGITS[word]), input)
    digits = re.sub(r"\D", "", input)
    return int(digits[0] + digits[-1])


class Solution(Day):
    def part_1(self):
        digits = extract_digits(self.lines)
        return sum(digits)

    def part_2(self):
        digits = extract_digits(self.lines, swap_digits=True)
        return sum(digits)


def main():
    day = Solution("aoc_2023/data/day_01.txt")
    day.run()


if __name__ == "__main__":
    main()
