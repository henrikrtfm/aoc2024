from collections import defaultdict
from utils.readinput import read_input_as_list
import heapq

START = 'S'
END = 'E'
WALL = '#'
FLOOR = '.'
TURN_COST = 1000
WALK_COST = 1
DIRECTIONS = {
    "NORTH": (-1, 0),
    "EAST": (0, 1),
    "WEST": (0, -1),
    "SOUTH": (1, 0)
}
POSSIBLE_DIRECTIONS = {
    "NORTH": ["NORTH", "EAST", "WEST"],
    "EAST": ["EAST", "NORTH", "SOUTH"],
    "WEST": ["WEST", "NORTH", "SOUTH"],
    "SOUTH": ["SOUTH", "EAST", "WEST"]
}


def parse_day16_input():
    #day16_input = read_input_as_list('input/day16_sample.txt')
    day16_input = read_input_as_list('../input/day16.txt')
    maze = {}
    start = None
    end = None
    for row in range(len(day16_input)):
        for col in range(len(day16_input[0])):
            current = day16_input[row][col]
            if current == START:
                start = (row, col)
                maze[(row, col)] = current
            elif current == END:
                end = (row, col)
                maze[(row, col)] = current
            else:
                maze[(row, col)] = current
    return start, end, maze


def get_next_positions(position, direction, raindeer_maze):
    possible_directions = POSSIBLE_DIRECTIONS[direction]
    positions = []
    for direction in possible_directions:
        dx, dy = DIRECTIONS[direction]
        positions.append(((position[0] + dx, position[1] + dy), direction))
    valid_positions = [(position, direction) for position, direction in positions if raindeer_maze[position] != WALL]
    return valid_positions


def traverse_find_best_path(start, end, raindeer_maze):
    visited = set()
    priority_queue = [(0, start, "EAST")]
    heapq.heapify(priority_queue)
    while priority_queue:
        current_weight, current, prev_direction = heapq.heappop(priority_queue)
        if current == end:
            return current_weight
        if (current, prev_direction) in visited:
            continue
        visited.add((current, prev_direction))
        next_positions = get_next_positions(current, prev_direction, raindeer_maze)
        for next_position, new_direction in next_positions:
            new_weight = current_weight + WALK_COST
            if prev_direction and new_direction != prev_direction:
                new_weight += TURN_COST
            heapq.heappush(priority_queue, (new_weight, next_position, new_direction))

    return float('inf')


def traverse_find_seats(start, end, raindeer_maze):
    visited = defaultdict(lambda: float('inf'))
    seats = set()
    best_cost = float('inf')

    priority_queue = [(0, start, "EAST", {start})]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_weight, current, prev_direction, path = heapq.heappop(priority_queue)
        if current_weight > visited[(current, prev_direction)] or current_weight > best_cost:
            continue
        else:
            visited[(current, prev_direction)] = current_weight

        if current == end:
            if current_weight < best_cost:
                best_cost = current_weight
                seats = path
            elif current_weight == best_cost:
                seats.update(path)
            continue

        next_positions = get_next_positions(current, prev_direction, raindeer_maze)
        for next_position, new_direction in next_positions:
            new_weight = current_weight + WALK_COST
            if prev_direction and new_direction != prev_direction:
                new_weight += TURN_COST

            new_path = path.copy()
            new_path.add(next_position)
            heapq.heappush(priority_queue, (new_weight, next_position, new_direction, new_path))

    return len(seats)


def solve_part_1(start, end, raindeer_maze):
    return traverse_find_best_path(start, end, raindeer_maze)


def solve_part_2(start, end, raindeer_maze):
    return traverse_find_seats(start, end, raindeer_maze)


if __name__ == '__main__':
    start, end, raindeer_maze = parse_day16_input()
    print("Answer to part 1: {}".format(solve_part_1(start, end, raindeer_maze)))
    print("Answer to part 2: {}".format(solve_part_2(start, end, raindeer_maze)))
