from utils.readinput import read_input_as_list
from itertools import cycle

GUARD = '^'
OBJECT = '#'
FLOOR = '.'

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)


def parse_day06_input():
    #day06_input = read_input_as_list('input/day06_sample.txt')
    day06_input = read_input_as_list('input/day06.txt')
    grid = {}
    guard = None
    for i in range(len(day06_input)):
        for j in range(len(day06_input[0])):
            current = day06_input[i][j]
            if current == GUARD:
                guard = (i, j)
                grid[(i, j)] = FLOOR
            else:
                grid[(i, j)] = current
    return guard, grid


def step(guard, direction):
    i, j = guard
    di, dj = direction
    return i + di, j + dj


def is_facing_obstruction(guard, direction, lab_map):
    i, j = guard
    di, dj = direction
    next_spot = (i+di, j+dj)
    if lab_map[next_spot] == OBJECT:
        return True
    return False


def is_out_of_bounds(guard, direction, lab_map):
    i, j = guard
    di, dj = direction
    next_spot = (i+di, j+dj)
    return next_spot in lab_map


def simulate_guard(guard, lab):
    DIRECTIONS = cycle([UP, RIGHT, DOWN, LEFT])
    next_dir = next(DIRECTIONS)
    visited = set()
    visited_cycle = set()
    path_is_cycle = False

    while True:
        visited.add(guard)
        if (guard, next_dir) in visited_cycle:
            path_is_cycle = True
            break
        else:
            visited_cycle.add((guard, next_dir))
        if not is_out_of_bounds(guard, next_dir, lab):
            break
        elif is_facing_obstruction(guard, next_dir, lab):
            next_dir = next(DIRECTIONS)
        else:
            guard = step(guard, next_dir)
    return visited, path_is_cycle


def find_obstructions(guard, lab):
    possible_obstructions, _ = simulate_guard(guard, lab)
    possible_obstructions.remove(guard)

    obstructions = set()
    for candidate in possible_obstructions:
        changed_lab = lab.copy()
        changed_lab[candidate] = OBJECT
        _, is_cycle = simulate_guard(guard, changed_lab)
        if is_cycle:
            obstructions.add(candidate)

    return len(obstructions)


def solve_part_1(guard, grid):
    return len(simulate_guard(guard, grid)[0])


def solve_part_2(guard, grid):
    return find_obstructions(guard, grid)


if __name__ == '__main__':
    parsed_input = parse_day06_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input[0], parsed_input[1])))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input[0], parsed_input[1])))
