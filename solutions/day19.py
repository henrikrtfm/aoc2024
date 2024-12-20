from utils.readinput import read_input
from functools import lru_cache

towel_patterns = []
designs = []

def parse_day19_input():
    #day19_input = read_input('input/day19_sample.txt').split("\n\n")
    day19_input = read_input('input/day19.txt').split("\n\n")
    [towel_patterns.append(towel) for towel in day19_input[0].split(', ')]
    [designs.append(design) for design in day19_input[1].splitlines()]


@lru_cache(None)
def is_constructible(design):
    if design == "":
        return True

    for pattern in towel_patterns:
        if design.startswith(pattern):
            if is_constructible(design[len(pattern):]):
                return True
    return False


@lru_cache(None)
def count_ways(design):
    if design == "":
        return 1

    total_ways = 0
    for pattern in towel_patterns:
        if design.startswith(pattern):
            total_ways += count_ways(design[len(pattern):])
    return total_ways


def solve_part_1():
    return sum(is_constructible(design) for design in designs)


def solve_part_2():
    return sum(count_ways(design) for design in designs)


if __name__ == '__main__':
    parse_day19_input()
    print("Answer to part 1: {}".format(solve_part_1()))
    print("Answer to part 2: {}".format(solve_part_2()))