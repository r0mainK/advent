from collections import defaultdict
from pathlib import Path

from utils.int_code import IntCodeMachine, read_int_code


program = read_int_code(Path(__file__).parent / "data" / "11.txt")
machine = IntCodeMachine(program, lambda: panels[tuple(position)])
panels = defaultdict(int)
position = [0, 0]
direction = 0
direction_map = {
    0: (0, -1),
    1: (1, 1),
    2: (0, 1),
    3: (1, -1),
}
paint = False

for instruction_output in machine:
    paint = not paint
    if paint:
        panels[tuple(position)] = instruction_output
        continue
    direction = (direction + instruction_output * 2 - 1) % 4
    axis, shift = direction_map[direction]
    position[axis] += shift

print(f"number of panels painted at least once: {len(panels)}")
