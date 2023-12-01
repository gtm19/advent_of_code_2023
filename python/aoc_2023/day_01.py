from aoc_2023.base import Day
import re

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def word_to_digit(word: str) -> str:
    return DIGITS.get(word, word)


def extract_digits(
    input: str | list[str], swap_digits: bool = False
) -> int | list[int]:
    if isinstance(input, list):
        return [extract_digits(i, swap_digits) for i in input]
    regex = r"\d"
    if swap_digits:
        regex += "|" + "|".join(DIGITS)
    digits = re.findall(regex, input)
    return int(word_to_digit(digits[0]) + word_to_digit(digits[-1]))


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
