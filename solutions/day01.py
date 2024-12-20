from utils.readinput import read_input_as_list
import itertools


def parse_day01_input():
    todays_input = read_input_as_list('../input/day01.txt')
    split_list = [x.split() for x in todays_input]
    instructions_1 = []
    instructions_2 = []
    for row in split_list:
        instructions_1.append(int(row[0]))
        instructions_2.append(int(row[-1]))

    return instructions_1, instructions_2


def solve_part_1(parsed_input):
    sorted_instructions = list(itertools.zip_longest(sorted(parsed_input[0]), sorted(parsed_input[-1])))
    distances = [abs(pair[0]-pair[1]) for pair in sorted_instructions]
    return sum(distances)


def solve_part_2(parsed_input):
    similarity = [x*parsed_input[1].count(x) for x in parsed_input[0]]
    return sum(similarity)


if __name__ == '__main__':
    parsed_input = parse_day01_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))
