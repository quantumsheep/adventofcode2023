from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

from utils.bench import bench
from utils.input import read_day_input


class Map:
    def __init__(self, data: str):
        lines = data.splitlines()
        self.size = (len(lines[0]), len(lines))

        self.start = (0, 0)
        self.rocks = {}

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "S":
                    self.start = (x, y)
                elif c == "#":
                    self.rocks[(x, y)] = True
        if self.start == (0, 0):
            raise Exception("No start found")

    def is_out_of_bounds(self, position: Tuple[int, int]) -> bool:
        return (
            position[0] < 0
            or position[0] >= self.size[0]
            or position[1] < 0
            or position[1] >= self.size[1]
        )

    def is_rock(self, position: Tuple[int, int]) -> bool:
        return self.rocks.get(position, False)

    def display(self, plots: Set[Tuple[int, int]]):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if (x, y) in plots:
                    print("O", end="")
                elif (x, y) == self.start:
                    print("S", end="")
                elif (x, y) in self.rocks:
                    print("#", end="")
                else:
                    print(".", end="")
            print()


DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


@bench
def part1(data: str) -> int:
    m = Map(data)
    goal = 64

    plots: Dict[Tuple[int, int], Set[int]] = {}
    plots[m.start] = set()
    steps = 0

    for _ in range(goal):
        steps += 1

        new_plots: Dict[Tuple[int, int], Set[int]] = {}

        for plot in plots:
            for direction in DIRECTIONS:
                next_position = (
                    plot[0] + direction[0],
                    plot[1] + direction[1],
                )
                if m.is_rock(next_position) or m.is_out_of_bounds(next_position):
                    continue

                new_plots[next_position] = set()
                new_plots[next_position].add(steps)

        plots = new_plots

    m.display(plots.keys())

    return len(plots)


@bench
def part2(data: str) -> int:
    return 0


if __name__ == "__main__":
    day_input = read_day_input(21)

    result = part1(day_input)
    print("Part 1: ", result)

    result = part2(day_input)
    print("Part 2: ", result)
