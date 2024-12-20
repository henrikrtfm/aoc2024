from utils.readinput import read_input_as_list
import numpy as np
from collections import deque


SPACE_SIZE = 71
START = (0,0)
END = (SPACE_SIZE-1, SPACE_SIZE-1)
DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def parse_day18_input():
    #day18_input = read_input_as_list('input/day18_sample.txt')
    day18_input = read_input_as_list('input/day18.txt')
    memory_space = np.zeros((SPACE_SIZE, SPACE_SIZE), dtype=int)
    byte_list = []
    for line in day18_input:
        byte = line.split(',')
        byte_list.append((int(byte[1]), int(byte[0])))
    return byte_list, memory_space


def get_neighbors(coordinate, memory_space):
    row, col = coordinate
    rows, cols = memory_space.shape
    neighbors = [(row + dx, col + dy) for dx, dy in DIRECTIONS]
    valid_coordinates = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols]
    return valid_coordinates


def is_safe(next, memory_space):
    if memory_space[next] != 1:
        return True
    else:
        return False


def traverse(memory_space):
    visited = set()
    parent_map = {}
    visited.add(START)
    queue = deque([START])

    while queue:
        current = queue.popleft()
        if current == END:
            path = []
            while current:
                path.append(current)
                current = parent_map.get(current)
            return path[::-1]

        neighbors = get_neighbors(current, memory_space)
        for neighbor in neighbors:
            if neighbor not in visited and is_safe(neighbor, memory_space):
                queue.append(neighbor)
                visited.add(neighbor)
                parent_map[neighbor] = current
    return None


def is_path_possible(memory_space) -> bool:
    if traverse(memory_space) is not None:
        return True
    return False


def solve_part_1(byte_list, memory_space, memory_load):
    for byte in byte_list[:memory_load]:
        memory_space[byte] = 1
    return len(traverse(memory_space))-1


def solve_part_2(byte_list, memory_space):
    low, high = 0, len(byte_list)
    best = 0
    while low <= high:
        mid = (low + high) // 2

        temp_space = memory_space.copy()
        for byte in byte_list[:mid]:
            temp_space[byte] = 1
        if is_path_possible(temp_space):
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return byte_list[best]


if __name__ == '__main__':
    parsed_input = parse_day18_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input[0], parsed_input[1], 2979)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input[0], parsed_input[1])))