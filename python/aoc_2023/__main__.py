import aoc_2023


def main():
    for day in aoc_2023.__all__:
        print(f"Day {day}")
        day = getattr(aoc_2023, day)
        day.main()


if __name__ == "__main__":
    main()
