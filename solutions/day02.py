from utils.readinput import read_input_as_list


def parse_day02_input():
    day02_input = read_input_as_list('../input/day02.txt')
    day02_parsed = [list(map(int, line.split())) for line in day02_input]
    return day02_parsed


def is_safe(report):
    ascending = all((report[idx] < report[idx+1]) & (abs(report[idx]-report[idx+1]) <= 3) for idx in range(len(report)-1))
    descending = all((report[idx] > report[idx+1]) & (abs(report[idx]-report[idx+1]) <= 3) for idx in range(len(report)-1))
    return ascending or descending


def can_be_safe(report):
    if is_safe(report):
        return True

    for idx in range(len(report)):
        modified_report = report[:idx] + report[idx + 1:]
        if is_safe(modified_report):
            return True

    return False


def solve_part_1(parsed_reports):
    analyzed_reports = [is_safe(report) for report in parsed_reports]
    return analyzed_reports.count(True)


def solve_part_2(parsed_reports):
    analyzed_reports = [can_be_safe(report) for report in parsed_reports]
    return analyzed_reports.count(True)


if __name__ == '__main__':
    parsed_reports = parse_day02_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_reports)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_reports)))
