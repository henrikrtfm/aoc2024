from collections import defaultdict, deque
from dataclasses import dataclass

from utils.readinput import read_input

WIRES = defaultdict(lambda: None)
GATES = []


@dataclass
class Gate:
    input1: str
    input2: str
    operation: str
    output: str

    def simulate(self):
        match self.operation:
            case 'AND':
                WIRES[self.output] = WIRES[self.input1] and WIRES[self.input2]
            case 'OR':
                WIRES[self.output] = WIRES[self.input1] or WIRES[self.input2]
            case 'XOR':
                WIRES[self.output] = WIRES[self.input1] ^ WIRES[self.input2]


def parse_day24_input():
    #raw_initial, raw_gates = read_input('../input/day24_sample.txt').split("\n\n")
    raw_initial, raw_gates = read_input('../input/day24.txt').split("\n\n")
    for line in raw_initial.splitlines():
        wire, starting_value = line.split(": ")
        WIRES[wire] = int(starting_value)

    for line in raw_gates.splitlines():
        iw1, op, iw2, _, ow = line.split()
        gate = Gate(input1=iw1, input2=iw2, operation=op, output=ow)
        GATES.append(gate)


def combine_bits():
    z_bits = reversed([str(value) for wire, value in sorted(WIRES.items()) if wire.startswith('z')])
    return ''.join(z_bits)


def solve_part_1():
    gates = deque(GATES.copy())
    while gates:
        gate = gates.popleft()
        if WIRES[gate.input1] is not None and WIRES[gate.input2] is not None:
            gate.simulate()
        else:
            gates.append(gate)

    return int(combine_bits(), 2)


def build_gate_connections(gate_relation):
    gate_connections = []
    for output, (input1, gate, input2) in gate_relation.items():
        gate_connections.append(f"{input1} {gate} {input2} -> {output}")
    return gate_connections


def print_gate_connections(gate_relation, key, depth=0):
    if depth == 3 or key[0] in ("x", "y"):
        return key
    input1, gate, input2 = gate_relation[key]
    return f"({key}=[{print_gate_connections(gate_relation, input1, depth + 1)} {gate} {print_gate_connections(gate_relation, input2, depth + 1)}])"


def part1(data):
    pos = data.index("")
    init_wire_values = data[:pos]
    gate_connections = data[pos + 1:]

    wires = {}

    for line in gate_connections:
        input1, gate, input2, _, output = line.split()
        wires[input1] = None
        wires[input2] = None
        wires[output] = None

    for line in init_wire_values:
        wire, val = line.split(": ")
        wires[wire] = int(val)

    while gate_connections:
        done = []
        for i, line in enumerate(gate_connections):
            input1, gate, input2, _, output = line.split()
            if wires[input1] is not None and wires[input2] is not None:
                if gate == "AND":
                    wires[output] = 1 if wires[input1] + wires[input2] == 2 else 0
                elif gate == "OR":
                    wires[output] = 1 if wires[input1] + wires[input2] > 0 else 0
                elif gate == "XOR":
                    wires[output] = 1 if wires[input1] != wires[input2] else 0
                done.append(i)
        gate_connections = [v for i, v in enumerate(gate_connections) if i not in done]

    z_wires = [v for k, v in
               sorted([val for val in wires.items() if val[0][0] == "z"], key=lambda x: x[0], reverse=True)]
    z_value = int("".join(map(str, z_wires)), 2)

    return z_value


def solve_part_2(data):
    pos = data.index("")
    init_wire_values = data[:pos]
    gate_connections = data[pos + 1 :]

    x_bin = "".join([line.split(": ")[1] for line in init_wire_values if line.startswith("x")])[::-1]
    y_bin = "".join([line.split(": ")[1] for line in init_wire_values if line.startswith("y")])[::-1]
    z = int(x_bin, 2) + int(y_bin, 2)
    z_bin = bin(z)[2:][::-1]

    gate_relation = {}
    for line in gate_connections:
        input1, gate, input2, _, output = line.split()
        gate_relation[output] = (input1, gate, input2)

    # for i in range(46):
    #     print(self.print_gate_connections(gate_relation, f"z{i:02}"))

    """
    Check the gate type based on the depth level:

    - The gate at depth level 0 must be XOR only.
    - At depth level 1, the gate can be either XOR or OR.
    - If the gate at level 1 is XOR, the inputs should be x-wire and y-wire.
    - If the gate at level 1 is OR, the gates at level 2 must be AND.

    The format should follow these guidelines:

    level 0: XOR
    (a XOR b)
     ^^^^^^^

    level 1 (type 1): XOR, a1 and a2 are x-wire and y-wire
    ((a1 XOR a2) XOR b)
      ^^^^^^^^^

    level 1 (type 2): OR + level 2: AND
    ((a1 XOR a2) XOR ((b11 AND b12) OR (b21 AND b22)))
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       ^^^^^^^^^^^      ^^^^^^^^^^^
    """

    is_valid = False
    swap_candidate = []
    result = []

    while not is_valid:
        curr_gate_connections = build_gate_connections(gate_relation)
        z_test = bin(part1(data[: pos + 1] + curr_gate_connections))[2:][::-1]

        if z_bin == z_test:
            is_valid = True
            break

        for i in range(len(z_bin)):
            if z_bin[i] != z_test[i] or len(swap_candidate) == 1:
                key1 = f"z{i:02}"
                if z_bin[i] != z_test[i]:
                    print("unmatch bit:", key1)
                else:
                    print("look for possible unmatch:", key1)

                input1, gate, input2 = gate_relation[key1]
                connections = print_gate_connections(gate_relation, key1)
                print(connections)

                if gate == "XOR":
                    if input1[0] in ("x", "y") and input2[0] in ("x", "y"):
                        continue

                    l_lv1_input1, l_lv1_gate1, l_lv1_input2 = gate_relation[input1]
                    r_lv1_input1, r_lv1_gate1, r_lv1_input2 = gate_relation[input2]

                    if l_lv1_gate1 == "XOR" and l_lv1_input1[0] in ("x", "y"):
                        if r_lv1_gate1 != "OR":
                            swap_candidate.append(input2)
                        else:
                            _, r_lv1_input1_lv2_gate1, _ = gate_relation[r_lv1_input1]
                            if r_lv1_input1_lv2_gate1 != "AND":
                                swap_candidate.append(r_lv1_input1)
                            _, r_lv1_input2_lv2_gate1, _ = gate_relation[r_lv1_input2]
                            if r_lv1_input2_lv2_gate1 != "AND":
                                swap_candidate.append(r_lv1_input2)
                    else:
                        if l_lv1_gate1 != "OR":
                            swap_candidate.append(input1)
                        else:
                            _, l_lv1_input1_lv2_gate1, _ = gate_relation[l_lv1_input1]
                            if l_lv1_input1_lv2_gate1 != "AND":
                                swap_candidate.append(l_lv1_input1)
                            _, l_lv1_input2_lv2_gate1, _ = gate_relation[l_lv1_input2]
                            if l_lv1_input2_lv2_gate1 != "AND":
                                swap_candidate.append(l_lv1_input2)
                else:
                    swap_candidate.append(key1)

                print("invalid format, need swap:", swap_candidate[-1], end="\n\n")

                if len(swap_candidate) == 2:
                    break

        gate_relation[swap_candidate[0]], gate_relation[swap_candidate[1]] = gate_relation[swap_candidate[1]], \
        gate_relation[swap_candidate[0]]
        result.extend(swap_candidate)
        swap_candidate = []

    return ",".join(sorted(result))


if __name__ == '__main__':
    parse_day24_input()
    data = read_input('../input/day24.txt').splitlines()
    print("Answer to part 1: {}".format(solve_part_1()))
    print("Answer to part 2: {}".format(solve_part_2(data)))
