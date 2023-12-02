from typing import Dict, List

from utils.input import read_day_input


def get_game_sets_colors(sets: List[str]) -> List[Dict[str, int]]:
    colors: List[Dict[str, int]] = []

    for set in sets:
        set_colors = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        cubes = set.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")

            set_colors[color] += int(count)

        colors.append(set_colors)

    return colors


def part1(data: str) -> List[int]:
    output: List[int] = []

    lines = data.splitlines()
    for line in lines:
        game, sets = line.split(": ")
        game_id = int(game.split(" ")[1])

        sets = sets.split("; ")
        sets_colors = get_game_sets_colors(sets)

        if all(
            [
                colors["red"] <= 12 and colors["green"] <= 13 and colors["blue"] <= 14
                for colors in sets_colors
            ]
        ):
            output.append(game_id)

    return output


def part2(data: str) -> List[int]:
    output: List[int] = []

    lines = data.splitlines()
    for line in lines:
        _, sets = line.split(": ")

        sets = sets.split("; ")
        sets_colors = get_game_sets_colors(sets)

        max_red = max([colors["red"] for colors in sets_colors])
        max_green = max([colors["green"] for colors in sets_colors])
        max_blue = max([colors["blue"] for colors in sets_colors])

        output.append(max_red * max_green * max_blue)

    return output


if __name__ == "__main__":
    day_input = read_day_input(2)

    lines = part1(day_input)
    print("Part 1: ", sum(lines))

    lines = part2(day_input)
    print("Part 2: ", sum(lines))
