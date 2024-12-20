from collections import defaultdict

SAMPLE_INPUT = "125 17"
INPUT = "0 89741 316108 7641 756 9 7832357 91"


def parse_day11_input():
    #day11_input = SAMPLE_INPUT.split()
    day11_input = INPUT.split()
    stones_dict = defaultdict(int)
    for stone in day11_input:
        stones_dict[stone] += 1
    return stones_dict


def apply_rules(stone, count):
    results = defaultdict(int)
    if stone == '0':
        results['1'] += count
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        left = stone[:mid]
        right = stone[mid:].lstrip('0') or '0'
        results[left] += count
        results[right] += count
    else:
        new_stone = str(int(stone) * 2024)
        results[new_stone] += count
    return results


def perform_blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        updates = apply_rules(stone, count)
        for key, value in updates.items():
            new_stones[key] += value
    return new_stones


def run(stones, blinks):
    for _ in range(blinks):
        stones = perform_blink(stones)
    return sum(stones.values())


if __name__ == '__main__':
    parsed_input = parse_day11_input()
    print("Answer to part 1: {}".format(run(parsed_input, 25)))
    print("Answer to part 2: {}".format(run(parsed_input, 75)))
