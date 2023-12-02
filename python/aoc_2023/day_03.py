from aoc_2023.base import Day
import re


def match_intersects(t1: re.Match, t2: re.Match):
    t1_set = set(range(t1.span()[0], t1.span()[1] + 1))
    t2_set = set(range(t2.span()[0], t2.span()[1] + 1))

    return bool(t1_set.intersection(t2_set))


class Solution(Day):
    def get_surrounding(
        self, line: int, start: int | None = None, end: int | None = None, n: int = 1
    ) -> str:
        safe_start = max(0, start - n)
        safe_end = min(end + n, len(self.lines[0]))

        line_start = max(0, line - n)
        line_end = min(line + n + 1, len(self.lines))
        return "\n".join(
            [line[safe_start:safe_end] for line in self.lines[line_start:line_end]]
        )

    @property
    def numbers_in_lines(self) -> int:
        number_matches = [re.finditer(r"\d+", line) for line in self.lines]
        total = 0
        for line, matches in enumerate(number_matches):
            for match in matches:
                surrounding = self.get_surrounding(line, match.start(), match.end())
                if re.findall(r"[^\d\.\n]", surrounding):
                    total += int(match.group())
        return total

    @property
    def gears(self) -> int:
        potential_gears = [list(re.finditer(r"\*", line)) for line in self.lines]
        number_matches = [list(re.finditer(r"\d+", line)) for line in self.lines]
        total = 0
        for line, gears in enumerate(potential_gears):
            near_numbers = number_matches[
                max(0, line - 1) : min(len(self.lines), line + 1) + 1
            ]
            near_numbers = [num for line in near_numbers for num in line]
            for gear in gears:
                adj_numbers = [
                    num for num in near_numbers if match_intersects(num, gear)
                ]
                if len(adj_numbers) == 2:
                    total += int(adj_numbers[0].group()) * int(adj_numbers[1].group())

        return total

    def part_1(self):
        return self.numbers_in_lines

    def part_2(self):
        return self.gears


def main():
    day = Solution("./aoc_2023/data/day_03.txt")
    day.run()


if __name__ == "__main__":
    main()
