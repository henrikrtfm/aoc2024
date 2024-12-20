from utils.readinput import read_input_as_list
import numpy as np
from collections import deque, defaultdict

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def parse_day20_input():
    #day20_input = read_input_as_list('../input/day20_sample.txt')
    day20_input = read_input_as_list('../input/day20.txt')
    rows = len(day20_input)
    cols = len(day20_input[0])
    racetrack = np.zeros((rows, cols), dtype=int)
    start = None
    end = None
    for row in range(rows):
        for col in range(cols):
            current = day20_input[row][col]
            if current == 'S':
                start = (row, col)
                racetrack[(row, col)] = 1
            elif current == 'E':
                end = (row, col)
                racetrack[(row, col)] = 1
            elif current == '.':
                racetrack[(row, col)] = 1

    return start, end, racetrack


def get_neighbors(coordinate, racetrack):
    row, col = coordinate
    rows, cols = racetrack.shape
    neighbors = [(row + dx, col + dy) for dx, dy in DIRECTIONS]
    valid_coordinates = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols]
    return valid_coordinates


def is_safe(next, racetrack):
    if racetrack[next] != 0:
        return True
    else:
        return False


def traverse(start, end, racetrack):
    visited = set()
    visited.add(start)
    queue = deque([start])
    parent_map = {}

    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent_map.get(current)
            return path[::-1]

        neighbors = get_neighbors(current, racetrack)
        for neighbor in neighbors:
            if neighbor not in visited and is_safe(neighbor, racetrack):
                queue.append(neighbor)
                visited.add(neighbor)
                parent_map[neighbor] = current
    return None


def find_cheatable_pairs_in_range(path, savings, cheat_moves):
    cheats = 0

    coords_steps = {}
    for i, coord in enumerate(path):
        coords_steps[coord] = i

    possible_ranges = []
    for dy in range(-cheat_moves, cheat_moves + 1):
        for dx in range(-cheat_moves, cheat_moves + 1):
            if dy == 0 and dx == 0:
                continue

            manhattan = abs(dy) + abs(dx)
            if manhattan > cheat_moves:
                continue

            possible_ranges.append((dy, dx, manhattan))

    for y, x in path:
        for dy, dx, manhattan in possible_ranges:
            ny, nx = y + dy, x + dx
            if (ny, nx) in coords_steps:
                if savings <= (coords_steps[(ny, nx)] - coords_steps[(y, x)] - manhattan):
                    cheats += 1
    return cheats


def solve_part_1(start, end, racetrack):
    path = traverse(start, end, racetrack)
    return find_cheatable_pairs_in_range(path, 100, 2)


def solve_part_2(start, end, racetrack):
    path = traverse(start, end, racetrack)
    return find_cheatable_pairs_in_range(path, 100, 20)


if __name__ == '__main__':
    parsed_input = parse_day20_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input[0], parsed_input[1], parsed_input[2])))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input[0], parsed_input[1], parsed_input[2])))
