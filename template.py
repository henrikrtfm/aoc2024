from utils.readinput import read_input_as_list
from collections import defaultdict


def parse_dayXX_input():
    todays_input = read_input_as_list('input/dayXX_sample.txt')
    #todays_input = read_input_as_list('input/dayXX.txt')
    return todays_input


def solve_part_1(parsed_input):
    return 1


def solve_part_2(parsed_input):
    return 2


if __name__ == '__main__':
    parsed_input = parse_dayXX_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))
