from utils.readinput import read_input


def parse_day05_input():
    #day05_input = read_input('input/day05_sample.txt').split("\n\n")
    day05_input = read_input('input/day05.txt').split("\n\n")
    raw_data = [line.splitlines() for line in day05_input]
    page_rules = {}
    for rule in raw_data[0]:
        key, value = map(int, rule.split('|'))
        if key not in page_rules:
            page_rules[key] = []
        page_rules[key].append(value)

    page_updates = [list(map(int, update.split(','))) for update in raw_data[1]]
    return page_rules, page_updates


def get_middle(pages):
    return pages[len(pages) // 2]


def is_valid_order(page1, page2, page_rules):
    return page1 not in page_rules.get(page2, [])


def check_page_update(page_update, page_rules):
    result = []
    for idx in range(len(page_update) - 1):
        if is_valid_order(page_update[idx], page_update[idx + 1], page_rules):
            result.append(True)
        else:
            result.append(False)
    return all(result)


def sort_page_update(page_update, page_rules):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(len(page_update) - 1):
            if not is_valid_order(page_update[idx], page_update[idx + 1], page_rules):
                page_update[idx], page_update[idx + 1] = page_update[idx + 1], page_update[idx]
                is_sorted = False
                break
    return page_update


def calculate_result(page_updates):
    return sum([get_middle(page_update) for page_update in page_updates])


def solve_part_1(page_rules, page_updates):
    correct_page_updates = []
    for page_update in page_updates:
        if check_page_update(page_update, page_rules):
            correct_page_updates.append(page_update)
    return calculate_result(correct_page_updates)


def solve_part_2(page_rules, page_updates):
    correct_page_updates = []
    for page_update in page_updates:
        if not check_page_update(page_update, page_rules):
            correct_page_updates.append(sort_page_update(page_update, page_rules))
    return calculate_result(correct_page_updates)


if __name__ == '__main__':
    parsed_input = parse_day05_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input[0], parsed_input[1])))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input[0], parsed_input[1])))
