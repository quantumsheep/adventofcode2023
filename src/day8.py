import math
from typing import Dict, List

from utils.bench import bench
from utils.input import read_day_input


@bench
def part1(data: str) -> int:
    lines = data.splitlines()

    directions = [0 if d == "L" else 1 for d in lines[0]]

    nodes: Dict[str, (str, str)] = {}
    for line in lines[2:]:
        name, destinations = line.split(" = ")
        left, right = destinations[1:-1].split(", ")

        nodes[name] = (left, right)

    current_node = "AAA"
    current_direction_cursor = 0
    moves = 0

    while True:
        if current_node == "ZZZ":
            break

        current_node = nodes[current_node][directions[current_direction_cursor]]
        current_direction_cursor = (current_direction_cursor + 1) % len(directions)
        moves += 1

    return moves


@bench
def part2(data: str) -> int:
    lines = data.splitlines()

    directions = [0 if d == "L" else 1 for d in lines[0]]

    nodes: Dict[str, (str, str)] = {}
    for line in lines[2:]:
        name, destinations = line.split(" = ")
        left, right = destinations[1:-1].split(", ")

        nodes[name] = (left, right)

    moves: List[int] = []
    start_nodes = [name for name in nodes if name[-1] == "A"]

    for current_node in start_nodes:
        current_direction_cursor = 0
        move_counts = 0

        while True:
            if current_node[-1] == "Z":
                break

            current_node = nodes[current_node][directions[current_direction_cursor]]
            current_direction_cursor = (current_direction_cursor + 1) % len(directions)
            move_counts += 1

        moves.append(move_counts)

    return math.lcm(*moves)


if __name__ == "__main__":
    day_input = read_day_input(8)

    result = part1(day_input)
    print("Part 1: ", result)

    result = part2(day_input)
    print("Part 2: ", result)
