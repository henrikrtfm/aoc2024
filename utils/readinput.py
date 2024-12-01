def read_input(filename):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    return read_data


def read_input_as_list(filename):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read().splitlines()
    return read_data
