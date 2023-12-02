from aoc_2023.base import Day
from dataclasses import dataclass, field
import re


@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __le__(self, other):
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )

    @classmethod
    def from_string(cls, string: str):
        colors = re.findall(r"(\d+) (\w+)", string)
        return cls(**{color: int(amount) for amount, color in colors})

    @property
    def power(self):
        return self.red * self.green * self.blue


# Just an alias for the Round class really - to make code more readable
Bag = Round


@dataclass
class Game:
    id: int
    rounds: list[Round] = field(default_factory=list)

    def __iadd__(self, other):
        self.rounds.append(other)
        return self

    def __le__(self, other: Round):
        return all(round_ <= other for round_ in self.rounds)

    @property
    def min_bag(self):
        return Round(
            red=max(r.red for r in self.rounds),
            green=max(r.green for r in self.rounds),
            blue=max(r.blue for r in self.rounds),
        )

    @property
    def power(self):
        return self.min_bag.power


def parse_game(line: str | list[str]) -> list[Game]:
    if isinstance(line, list):
        return [parse_game(l) for l in line]
    game_split = re.match(r"^Game (\d+)\D+(.+)$", line).groups()
    id = int(game_split[0])
    game = Game(id)
    rounds = re.split(r";\s*", game_split[1])
    for round in rounds:
        game += Round.from_string(round)
    return game


class Solution(Day):
    def part_1(self):
        games = parse_game(self.lines)
        return sum(game.id for game in games if game <= Bag(12, 13, 14))

    def part_2(self):
        games = parse_game(self.lines)
        return sum(game.power for game in games)


def main():
    day = Solution("./aoc_2023/data/day_02.txt")
    day.run()


if __name__ == "__main__":
    main()
