from utils.readinput import read_input


def parse_day25_input() -> (list[list[int]],list[list[int]]):
    #day25_input = read_input('../input/day25_sample.txt').split("\n\n")
    day25_input = read_input('../input/day25.txt').split("\n\n")
    key_schematics = []
    lock_schematics = []
    for schematic in day25_input:
        schematic_rows = schematic.splitlines()
        if schematic_rows[0] == '#####':
            columns = zip(*schematic_rows[1:])
            key_schematics.append([column.count('#') for column in columns])
        else:
            columns = zip(*schematic_rows[:-1])
            lock_schematics.append([column.count('#') for column in columns])

    return key_schematics, lock_schematics


def analyze_lock_key_schematic(key, lock) -> bool:
    key_lock_pairs = list(zip(key, lock))
    key_lock_overlaps = [sum(pair) for pair in key_lock_pairs]
    return all(key_lock_overlap <= 5 for key_lock_overlap in key_lock_overlaps)


def solve_part_1(key_schematics, lock_schematics):
    fit = 0
    for key_schematic in key_schematics:
        for lock_schematic in lock_schematics:
            if analyze_lock_key_schematic(key_schematic, lock_schematic):
                fit += 1
    return fit


def solve_part_2(parsed_input):
    return 2


if __name__ == '__main__':
    parsed_input = parse_day25_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input[0], parsed_input[1])))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))
