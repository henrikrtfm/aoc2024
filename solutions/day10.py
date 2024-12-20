from utils.readinput import read_input_as_list

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def parse_day10_input():
    #day10_input = read_input_as_list('input/day10_sample.txt')
    day10_input = read_input_as_list('../input/day10.txt')
    topographic_map = {}
    trailheads = []
    for row in range(len(day10_input)):
        for col in range(len(day10_input[0])):
            height = int(day10_input[row][col])
            topographic_map[(row, col)] = height
            if height == 0:
                trailheads.append((row, col))

    return topographic_map, trailheads


def get_neighbors(coordinate, topographic_map):
    neighbors = [(coordinate[0] + dx, coordinate[1] + dy) for dx, dy in DIRECTIONS]
    valid_coordinates = [neighbor for neighbor in neighbors if neighbor in topographic_map]
    return valid_coordinates


def is_safe(this, next, topographic_map):
    if topographic_map[next] - topographic_map[this] == 1:
        return True
    else:
        return False


def find_trails(trailhead, topographic_map):
    visited = set()
    stack = [trailhead]
    trails = 0

    while stack:
        current = stack.pop()
        visited.add(current)
        if topographic_map[current] == 9:
            trails += 1
        neighbors = get_neighbors(current, topographic_map)
        for neighbor in neighbors:
            if neighbor not in visited and is_safe(current, neighbor, topographic_map):
                stack.append(neighbor)
    return trails


def find_trail_rating(trailhead, topographic_map):
    visited = set()
    stack = [trailhead]
    rating = 0

    while stack:
        current = stack.pop()
        visited.add(current)
        neighbors = get_neighbors(current, topographic_map)
        if topographic_map[current] == 9:
            rating += 1
        for neighbor in neighbors:
            if is_safe(current, neighbor, topographic_map):
                stack.append(neighbor)
    return rating


def solve_part_1(topographic_map, trailheads):
    trails = [find_trails(trailhead, topographic_map) for trailhead in trailheads]
    return sum(trails)


def solve_part_2(topographic_map, trailheads):
    ratings = [find_trail_rating(trailhead, topographic_map) for trailhead in trailheads]
    return sum(ratings)


if __name__ == '__main__':
    topographic_map, trailheads = parse_day10_input()
    print("Answer to part 1: {}".format(solve_part_1(topographic_map, trailheads)))
    print("Answer to part 2: {}".format(solve_part_2(topographic_map, trailheads)))
