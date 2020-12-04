from collections import defaultdict
from pathlib import Path

from utils.int_code import BareIntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "23.txt")
network = []

for i in range(50):
    network.append(BareIntCodeMachine(program, lambda: packets[i].pop(0) if packets[i] else -1))

packets = {i: [i] for i in range(50)}
buffer = defaultdict(list)
network_adress = None

while network_adress != 255:
    for i, machine in enumerate(network):
        instruction_output = next(machine)
        if instruction_output is None:
            continue
        buffer[i].append(instruction_output)
        if len(buffer[i]) == 3:
            network_adress, x, y = buffer.pop(i)
            if network_adress == 255:
                break
            packets[network_adress] += [x, y]

print(f"Y value of the first packet sent to address 255: {y}")
