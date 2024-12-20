from utils.readinput import read_input_as_list
from collections import defaultdict
import numpy as np
import math


ROWS = 101
COLUMNS = 103
AREA = np.zeros((ROWS, COLUMNS), dtype=int)
MID_ROW = AREA.shape[0] // 2
MID_COLUMN = AREA.shape[1] // 2


def parse_day14_input():
    #day14_input = read_input_as_list('input/day14_sample.txt')
    day14_input = read_input_as_list('../input/day14.txt')
    robots = defaultdict(list)
    for line in day14_input:
        position = tuple(map(int, line.split()[0].split("=")[1].split(',')))
        velocity = tuple(map(int, line.split()[1].split("=")[1].split(',')))
        robots[position].append(velocity)
    return robots


def update_robot_position(position, velocity):
    new_col = (position[0]+velocity[0]) % AREA.shape[0]
    new_row = (position[1]+velocity[1]) % AREA.shape[1]
    return new_col, new_row


def move(robots):
    updated_robots = defaultdict(list)
    for position, velocities in robots.items():
        for velocity in velocities:
            new_position = update_robot_position(position, velocity)
            updated_robots[new_position].append(velocity)
    return updated_robots


def divide_into_quadrants(robots):
    quadrants = {
        "top_left": 0,
        "top_right": 0,
        "bottom_left": 0,
        "bottom_right": 0,
    }

    for position, velocities in robots.items():
        row, col = position
        if row < MID_ROW and col < MID_COLUMN:
            quadrants["top_left"] += len(velocities)
        elif row < MID_ROW and col > MID_COLUMN:
            quadrants["top_right"] += len(velocities)
        elif row > MID_ROW and col < MID_COLUMN:
            quadrants["bottom_left"] += len(velocities)
        elif row > MID_ROW and col > MID_COLUMN:
            quadrants["bottom_right"] += len(velocities)

    return quadrants


def solve_part_1(robots, ticks):
    current_robots = robots.copy()
    for tick in range(ticks):
        current_robots = move(current_robots)
    quadrants = divide_into_quadrants(current_robots)
    return math.prod(quadrants.values())


def solve_part_2(robots):
    ticks = 0
    christmas_tree = False
    current_robots = robots.copy()
    while not christmas_tree:
        current_robots = move(current_robots)
        ticks += 1
        if all(len(value) == 1 for value in current_robots.values()):
            return ticks

    return ticks


if __name__ == '__main__':
    robots = parse_day14_input()
    print("Answer to part 1: {}".format(solve_part_1(robots, 100)))
    print("Answer to part 2: {}".format(solve_part_2(robots)))
