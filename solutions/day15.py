from utils.readinput import read_input


ROBOT = '@'
WALL = '#'
OBJECT = 'O'
LEFT_BOX = '['
RIGHT_BOX = ']'
FLOOR = '.'
DIRECTIONS = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}


def parse_day15_input():
    #day15_input = read_input('input/day15_sample.txt').split("\n\n")
    day15_input = read_input('../input/day15.txt').split("\n\n")
    raw_warehouse = day15_input[0].splitlines()
    moves = day15_input[1].replace('\n', '')
    warehouse = {}
    robot = None
    for row in range(len(raw_warehouse)):
        for col in range(len(raw_warehouse[0])):
            current = raw_warehouse[row][col]
            if current == ROBOT:
                robot = (row, col)
                warehouse[(row, col)] = ROBOT
            else:
                warehouse[(row, col)] = current
    return robot, warehouse, moves


def parse_and_resize_day15_input():
    day15_input = read_input('../input/day15_sample.txt').split("\n\n")
    #day15_input = read_input('input/day15.txt').split("\n\n")
    initial_warehouse = day15_input[0].splitlines()
    moves = day15_input[1].replace('\n', '')
    expanded_warehouse = []

    for row in initial_warehouse:
        row = row.replace('#', '##')
        row = row.replace('O', '[]')
        row = row.replace('.', '..')
        row = row.replace('@', '@.')
        expanded_warehouse.append(row)

    warehouse = {}
    robot = None
    for row in range(len(expanded_warehouse)):
        for col in range(len(expanded_warehouse[0])):
            current = expanded_warehouse[row][col]
            if current == ROBOT:
                robot = (row, col)
                warehouse[(row, col)] = ROBOT
            else:
                warehouse[(row, col)] = current
    return robot, warehouse, moves


def show(grid):
    max_i = max([pos[0] for pos in grid.keys()])
    max_j = max([pos[1] for pos in grid.keys()])

    pic = [[None for h in range(max_j+1)] for w in range(max_i+1)]

    for i, row in enumerate(pic):
        for j, _ in enumerate(row):
            pic[i][j] = grid[(i, j)]

    for line in pic:
        print(''.join(line))
    print()


def get_next(current, direction):
    row, col = current
    d_row, d_col = direction
    return row+d_row, col+d_col


def update_positions(positions, warehouse):
    robot = (0, 0)
    values = [warehouse[position] for position in positions]
    rotated_values = [values[-1]] + values[:-1]
    for position, new_value in zip(positions, rotated_values):
        if new_value == ROBOT:
            robot = position
        warehouse[position] = new_value
    return robot, warehouse


def find_positions(start, move, warehouse):
    positions = []
    current = start
    while True:
        positions.append(current)
        next_pos = get_next(current, DIRECTIONS[move])
        value = warehouse[next_pos]
        if value == WALL:
            return []
        elif value == FLOOR:
            positions.append(next_pos)
            break
        elif value == OBJECT:
            current = next_pos
        else:
            break
    return positions


def move_robot(robot, warehouse, moves):
    for move in moves:
        positions = find_positions(robot, move, warehouse)
        if len(positions) != 0:
            robot, warehouse = update_positions(positions, warehouse)
    return warehouse


def calculate_gps(warehouse):
    gps = []
    for key, value in warehouse.items():
        if value == OBJECT:
            row, col = key
            gps.append(100*row+col)
    return gps


def solve_part_1(robot, warehouse, moves):
    updated_warehouse = move_robot(robot, warehouse, moves)
    return sum(calculate_gps(updated_warehouse))


def solve_part_2(robot, warehouse, moves):
    show(warehouse)
    return 2


if __name__ == '__main__':
    part1_input = parse_day15_input()
    part2_input = parse_and_resize_day15_input()
    print("Answer to part 1: {}".format(solve_part_1(part1_input[0], part1_input[1], part1_input[2])))
    print("Answer to part 2: {}".format(solve_part_2(part2_input[0], part2_input[1], part2_input[2])))
