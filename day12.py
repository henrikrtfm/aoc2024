from collections import deque
from collections import defaultdict
from utils.readinput import read_input_as_list

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def parse_day12_input():
    #day12_input = read_input_as_list('input/day12_sample.txt')
    day12_input = read_input_as_list('input/day12.txt')
    garden_map = defaultdict()
    for row in range(len(day12_input)):
        for col in range(len(day12_input[0])):
            garden_map[(row, col)] = day12_input[row][col]

    return garden_map


def get_neighbors(coordinate, garden_map):
    neighbors = [(coordinate[0] + dx, coordinate[1] + dy) for dx, dy in DIRECTIONS]
    valid_coordinates = [neighbor for neighbor in neighbors if neighbor in garden_map]
    return valid_coordinates


def find_regions(garden_map):
    visited = set()
    regions = []

    for plot, plant in garden_map.items():
        if plot not in visited:
            queue = deque([plot])
            region = set()

            while queue:
                current = queue.popleft()
                if current in visited:
                    continue
                visited.add(current)
                region.add(current)
                neighbors = get_neighbors(current, garden_map)
                [queue.append(neighbor) for neighbor in neighbors if neighbor not in visited and garden_map[neighbor] == plant]

            regions.append(region)

    return regions


def get_area_and_perimeter(region, garden_map):
    perimeter = 0
    for plot in region:
        perimeter += 4
        neighbors = get_neighbors(plot, garden_map)
        for neighbor in neighbors:
            if neighbor in region:
                perimeter -= 1

    return len(region), perimeter


def get_area_and_corners(region):
    left = set()
    right = set()
    up = set()
    down = set()

    for (row, col) in region:
        if (row - 1, col) not in region:
            up.add((row, col))
        if (row + 1, col) not in region:
            down.add((row, col))
        if (row, col + 1) not in region:
            right.add((row, col))
        if (row, col - 1) not in region:
            left.add((row, col))

    corners = 0

    for (row, col) in region:
        match (row, col):
            case (row, col) if (row, col) in up and (row, col) in left:
                corners += 1
            case (row, col) if (row, col) in up and (row, col) in right:
                corners += 1
            case (row, col) if (row - 1, col - 1) in right and (row, col) not in left:
                corners += 1
            case (row, col) if (row - 1, col + 1) in left and (row, col) not in right:
                corners += 1
            case (row, col) if (row, col) in down and (row, col) in left:
                corners += 1
            case (row, col) if (row, col) in down and (row, col) in right:
                corners += 1
            case (row, col) if (row + 1, col - 1) in right and (row, col) not in left:
                corners += 1
            case (row, col) if (row + 1, col + 1) in left and (row, col) not in right:
                corners += 1

    return len(region), corners


def solve_part_1(garden_map):
    regions = find_regions(garden_map)
    results = [get_area_and_perimeter(region, garden_map) for region in regions]
    return sum([area*perimeter for area, perimeter in results])


def solve_part_2(garden_map):
    regions = find_regions(garden_map)
    results = [get_area_and_corners(region) for region in regions]
    return sum([area*corners for area, corners in results])


if __name__ == '__main__':
    garden_map = parse_day12_input()
    print("Answer to part 1: {}".format(solve_part_1(garden_map)))
    print("Answer to part 2: {}".format(solve_part_2(garden_map)))
