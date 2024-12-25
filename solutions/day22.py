from collections import defaultdict

from utils.readinput import read_input_as_list


def parse_day22_input() -> list[int]:
    #day22_input = list(map(int, read_input_as_list('../input/day22_sample.txt')))
    day22_input = list(map(int, read_input_as_list('../input/day22.txt')))
    return day22_input


def evolve_secret(secret) -> int:
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret


def solve_part_1(starting_secrets) -> int:
    generated_secrets = []
    for secret in starting_secrets:
        for _ in range(2000):
            secret = evolve_secret(secret)
        generated_secrets.append(secret)
    return sum(generated_secrets)


def solve_part_2(starting_secrets) -> int:
    prices = []
    for secret in map(int, starting_secrets):
        price = []
        for _ in range(2000):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((secret // 32) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216
            price.append(secret % 10)
        prices.append(price)

    changes = [[b - a for a, b in zip(p, p[1:])] for p in prices]

    amounts = defaultdict(int)
    for buyer_idx, change in enumerate(changes):
        keys = set()
        for i in range(len(change) - 3):
            key = tuple(change[i : i + 4])
            if key in keys:
                continue
            amounts[key] += prices[buyer_idx][i + 4]
            keys.add(key)
    max_amount = max(amounts.values())

    return max_amount


if __name__ == '__main__':
    parsed_input = parse_day22_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))
