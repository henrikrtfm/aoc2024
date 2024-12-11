from utils.readinput import read_input


def parse_day09_input():
    #day09_input = '2333133121414131402'
    day09_input = read_input('input/day09.txt')
    block_representation = []
    file_id = 0
    for i, char in enumerate(day09_input):
        size = int(char)
        if i % 2 == 0:
            block_representation.extend([file_id] * size)
            file_id += 1
        else:
            block_representation.extend(['.'] * size)

    return block_representation


def compact_disc(disk):
    last_free_space_idx = 0

    for idx in range(len(disk) - 1, -1, -1):
        if disk[idx] == '.':
            continue

        while last_free_space_idx < len(disk) and disk[last_free_space_idx] != '.':
            last_free_space_idx += 1

        if last_free_space_idx < idx:
            disk[last_free_space_idx], disk[idx] = disk[idx], '.'
            last_free_space_idx += 1

    return disk


def find_free_space_block(disk, size):
    start_idx = 0
    while start_idx < len(disk):
        if disk[start_idx] == '.':
            free_space_size = 0
            while start_idx + free_space_size < len(disk) and disk[start_idx + free_space_size] == '.':
                free_space_size += 1
            if free_space_size >= size:
                return start_idx, free_space_size
            start_idx += free_space_size
        else:
            start_idx += 1
    return None, None


def compact_disc_blocks(disk):
    compacted = disk[:]
    idx = len(compacted) - 1

    while idx >= 0:
        if compacted[idx] == '.':
            idx -= 1
            continue

        file_id = compacted[idx]
        block_end = idx
        block_size = 0

        while block_end >= 0 and compacted[block_end] == file_id:
            block_size += 1
            block_end -= 1
        block_start = block_end + 1


        free_start, free_size = find_free_space_block(compacted, block_size)
        if free_start is not None and free_start < block_start:
            compacted[free_start:free_start + block_size] = [file_id] * block_size
            compacted[block_start:block_start + block_size] = ['.'] * block_size

        idx = block_end

    return compacted


def calculate_checksum(disk):
    return sum(idx * int(block) for idx, block in enumerate(disk) if block != '.')


def solve_part_1(block_representation):
    compacted_disc = compact_disc(block_representation)
    return calculate_checksum(compacted_disc)


def solve_part_2(block_representation):
    compacted_disc = compact_disc_blocks(block_representation)
    return calculate_checksum(compacted_disc)


if __name__ == '__main__':
    parsed_input = parse_day09_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))