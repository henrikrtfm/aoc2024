from utils.readinput import read_input_as_list
from itertools import combinations
import networkx as nx


def parse_day23_input():
    #day23_input = read_input_as_list('../input/day23_sample.txt')
    day23_input = read_input_as_list('../input/day23.txt')
    return day23_input


def solve_part_1(connections) -> int:
    G = nx.Graph()
    for line in connections:
        parts = line.split("-")
        G.add_edge(parts[0], parts[1])

    cliques = [c for c in nx.find_cliques(G) if len(c) >= 3 and any(n[0] == "t" for n in c)]
    sets = set()
    for c in cliques:
        for nodes in combinations(c, 3):
            if any(n[0] == "t" for n in nodes):
                sets.add(tuple(sorted(nodes)))
    count = len(sets)

    return count


def solve_part_2(connections):

    G = nx.Graph()
    for line in connections:
        parts = line.split("-")
        G.add_edge(parts[0], parts[1])

    cliques = nx.find_cliques(G)
    LAN = sorted(sorted(cliques, key=len, reverse=True)[0])

    return ",".join(LAN)


if __name__ == '__main__':
    parsed_input = parse_day23_input()
    print("Answer to part 1: {}".format(solve_part_1(parsed_input)))
    print("Answer to part 2: {}".format(solve_part_2(parsed_input)))
