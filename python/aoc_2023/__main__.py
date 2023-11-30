from aoc_2023 import day_01

DAYS = {
    1: day_01,
}


def main():
    for i, day in DAYS.items():
        print(f"Day {i}")
        day.main()


if __name__ == "__main__":
    main()
