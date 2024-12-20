from utils.readinput import read_input
from dataclasses import dataclass
import re
import numpy as np


@dataclass
class ClawMachine:
    button_a: (int, int)
    button_b: (int, int)
    prize: (int, int)

    def increase_prize(self, value):
        self.prize = (self.prize[0]+value, self.prize[1]+value)


def parse_values(line):
    match = re.search(r"X[+=](\d+), Y[+=](\d+)", line)
    if match:
        return tuple(map(int, match.groups()))
    return None


def parse_day13_input():
    #day13_input = read_input('input/day13_sample.txt').split("\n\n")
    day13_input = read_input('../input/day13.txt').split("\n\n")
    claw_machines = []

    for block in day13_input:
        button_a = None
        button_b = None
        prize = None
        for line in block.splitlines():
            if line.startswith("Button A:"):
                button_a = parse_values(line)
            if line.startswith("Button B:"):
                button_b = parse_values(line)
            if line.startswith("Prize:"):
                prize = parse_values(line)
        claw_machines.append(ClawMachine(button_a=button_a, button_b=button_b, prize=prize))
    return claw_machines


def solve_claw_machine(claw_machine, tolerance=1e-3):
    coefficients = np.array(((claw_machine.button_a[0], claw_machine.button_b[0]), (claw_machine.button_a[1], claw_machine.button_b[1])))
    constants = np.array(claw_machine.prize)
    solution = np.linalg.solve(coefficients, constants)
    if all(abs(x - round(x)) < tolerance for x in solution):
        return tuple(map(int, map(round, solution)))
    else:
        return None, None


def calculate_tokens(solution):
    return solution[0]*3+solution[1]


def solve_part_1(claw_machines):
    solutions = [solve_claw_machine(claw_machine) for claw_machine in claw_machines]
    return sum([calculate_tokens(solution) for solution in solutions if solution != (None, None)])


def solve_part_2(claw_machines):
    for claw_machine in claw_machines:
        claw_machine.increase_prize(10_000_000_000_000)
    solutions = [solve_claw_machine(claw_machine) for claw_machine in claw_machines]
    return sum([calculate_tokens(solution) for solution in solutions if solution != (None, None)])


if __name__ == '__main__':
    parsed_input = parse_day13_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))
