from collections import defaultdict
from pathlib import Path

from utils.int_code import BareIntCodeMachine, read_int_code


program = read_int_code(Path(__file__).parent / "data" / "23.txt")
network = []

for i in range(50):
    network.append(BareIntCodeMachine(program, lambda: packets[i].pop(0) if packets[i] else -1))

packets = {i: [i] for i in range(50)}
packets[255] = [None, None]
buffer = defaultdict(list)
op_code_history = {i: [] for i in range(50)}
NAT_packet_history = defaultdict(int)

while 2 not in NAT_packet_history.values():
    idle_network = True
    for i, machine in enumerate(network):
        instruction_output = next(machine)
        op_code_history[i].append(machine.op_code)
        op_code_history[i] = op_code_history[i][-10:]
        idle_network &= (
            sorted(op_code_history[i][:5]) == sorted(op_code_history[i][5:]) == [3, 5, 6, 6, 8]
        )
        if instruction_output is None:
            continue
        buffer[i].append(instruction_output)
        if len(buffer[i]) == 3:
            network_adress, x, y = buffer.pop(i)
            if network_adress == 255:
                packets[network_adress] = []
            packets[network_adress] += [x, y]
    idle_network &= sum(map(len, packets.values())) == 2
    if idle_network:
        NAT_packet_history[packets[255][1]] += 1
        packets[0] += packets[255]
        op_code_history[0] = []

print(f"first Y value sent twice by NAT_packet: {packets[255][1]}")
