from utils.input import read_day_input
from utils.lo import split_strip


def part1(data: str) -> int:
    lines = data.splitlines()

    times = [int(n) for n in split_strip(lines[0].split(": ")[1], " ")]
    distances = [int(n) for n in split_strip(lines[1].split(": ")[1], " ")]
    ways_of_winning = [0 for _ in range(len(times))]

    for i, t in enumerate(times):
        target_distance = distances[i]

        for hold in range(0, t + 1):
            distance = hold * (t - hold)

            if distance > target_distance:
                ways_of_winning[i] += 1

    result = 1
    for n in ways_of_winning:
        result *= n
    return result


def part2(data: str) -> int:
    lines = data.splitlines()

    max_time = int(lines.pop(0).split(": ")[1].replace(" ", ""))
    target_distance = int(lines.pop(0).split(": ")[1].replace(" ", ""))
    ways_of_winning = 0

    for hold in range(0, max_time + 1):
        distance = hold * (max_time - hold)

        if distance > target_distance:
            ways_of_winning += 1

    return ways_of_winning


if __name__ == "__main__":
    day_input = read_day_input(6)

    result = part1(day_input)
    print("Part 1: ", result)

    result = part2(day_input)
    print("Part 2: ", result)
