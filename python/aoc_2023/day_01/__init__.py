from .solution import Solution


def main():
    import os

    day = Solution(os.path.join(os.path.dirname(__file__), "data/actual.txt"))
    day.run()
