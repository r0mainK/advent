from collections import defaultdict
from pathlib import Path

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "13.txt")
machine = IntCodeMachine(program)
screen = defaultdict(int)
position = []
for instruction_output in machine:
    position.append(instruction_output)
    if len(position) == 3:
        screen[tuple(position)] = instruction_output
        position = []
print(f"number of block tiles: {len([tile for tile in screen.values() if tile == 2])}")

print(min(pos[0] for pos in screen))
print(min(pos[1] for pos in screen))
print(max(pos[0] for pos in screen))
print(max(pos[1] for pos in screen))
