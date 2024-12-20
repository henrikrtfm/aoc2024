from collections import defaultdict
from utils.readinput import read_input_as_list
from itertools import permutations

def parse_day08_input():
    #day08_input = read_input_as_list('input/day08_sample.txt')
    day08_input = read_input_as_list('../input/day08.txt')
    grid = {}
    for i, row in enumerate(day08_input):
        for j, d in enumerate(row):
            grid[(i, j)] = d
    frequencies = defaultdict(list)
    for coord, spot in grid.items():
        if spot != '.':
            frequencies[spot].append(coord)
    return grid, frequencies


def find_antinodes(this, other, grid):
    antinodes = set()

    di = this[0] - other[0]
    dj = this[1] - other[1]

    antinode_this = di + this[0], dj + this[1]
    antinode_other = di + other[0], dj + other[1]
    if antinode_this in grid:
        antinodes.add(antinode_this)
    if antinode_other in grid:
        antinodes.add(antinode_other)
    return antinodes - {this, other}


def find_antinodes_harmonics(this, other, grid):
    antinodes = set()
    di = this[0] - other[0]
    dj = this[1] - other[1]

    i, j = 1, 1
    while True:
        antinode_this = i * di + this[0], i * dj + this[1]
        if antinode_this not in grid:
            break
        antinodes.add(antinode_this)
        i += 1
    while True:
        antinode_other = i * di + this[0], i * dj + this[1]
        if antinode_other not in grid:
            break
        antinodes.add(antinode_other)
        j += 1

    return antinodes | {this, other}


def solve_part_1(grid, frequencies):
    antinodes = set()
    for coordinates in frequencies.values():
        for this, other in permutations(coordinates, 2):
            antinodes |= find_antinodes(this, other, grid)
    return len(antinodes)


def solve_part_2(grid, frequencies):
    antinodes_harmonics = set()
    for coordinates in frequencies.values():
        for this, other in permutations(coordinates, 2):
            antinodes_harmonics |= find_antinodes_harmonics(this, other, grid)
    return len(antinodes_harmonics)


if __name__ == '__main__':
    parsed_input = parse_day08_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input[0], parsed_input[1])))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input[0], parsed_input[1])))

