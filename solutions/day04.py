from utils.readinput import read_input_as_list


def parse_day04_input():
    #day04_input = read_input_as_list('input/day04_sample.txt')
    day04_input = read_input_as_list('../input/day04.txt')
    grid_dict = {}
    for row in range(len(day04_input)):
        for col in range(len(day04_input[0])):
            grid_dict[(row, col)] = day04_input[row][col]
    return grid_dict


def get_neighbors(coordinate, grid_dict, length, filter_self):
    row, col = coordinate
    directions = {
        "right": [(row, col + i) for i in range(length)],
        "left": [(row, col - i) for i in range(length)],
        "down": [(row + i, col) for i in range(length)],
        "up": [(row - i, col) for i in range(length)],
        "diag-right-down": [(row + i, col + i) for i in range(length)],
        "diag-left-up": [(row - i, col - i) for i in range(length)],
        "diag-right-up": [(row - i, col + i) for i in range(length)],
        "diag-left-down": [(row + i, col - i) for i in range(length)],
    }

    valid_neighbors = {}
    for direction, cells in directions.items():
        if filter_self:
            filtered_cells = [
                cell for cell in cells if cell in grid_dict and cell != coordinate
            ]
            if filtered_cells:
                valid_neighbors[direction] = filtered_cells
        else:
            if all(cell in grid_dict for cell in cells):
                valid_neighbors[direction] = cells
    return valid_neighbors


def solve_part_1(grid):
    found_patterns = set()
    pattern_length = 4
    patterns = {"XMAS", "SAMX"}

    for coordinate in grid:
        neighbors = get_neighbors(coordinate, grid, pattern_length, False)
        for direction, coordinates in neighbors.items():
            pattern = "".join(grid[coordinate] for coordinate in coordinates)
            if pattern in patterns:
                found_patterns.add(frozenset(coordinates))
    return len(found_patterns)


def solve_part_2(grid):
    found_patterns = set()
    pattern_length = 2
    patterns = {"MAS", "SAM"}
    a_grid = {key: value for key, value in grid.items() if value == 'A'}
    for coordinate in a_grid:
        neighbors = get_neighbors(coordinate, grid, pattern_length, True)
        x_neighbors = {key: value for key, value in neighbors.items() if 'diag' in key and len(neighbors) == 8}

        if len(x_neighbors) != 0:
            diag_pattern_down = "".join([grid[x_neighbors['diag-left-up'][0]], grid[coordinate], grid[x_neighbors['diag-right-down'][0]]])
            diag_pattern_up = "".join([grid[x_neighbors['diag-left-down'][0]], grid[coordinate], grid[x_neighbors['diag-right-up'][0]]])
            if diag_pattern_down in patterns and diag_pattern_up in patterns:
                coordinates = [coord for coords in x_neighbors.values() for coord in coords]
                found_patterns.add(frozenset(coordinates))
    return len(found_patterns)


if __name__ == '__main__':
    parsed_input = parse_day04_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))

