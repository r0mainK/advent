from collections import defaultdict
from pathlib import Path

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "11.txt")
machine = IntCodeMachine(program, lambda: panels[tuple(position)])
panels = defaultdict(int)
panels[(0, 0)] = 1
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


min_x = min(pos[0] for pos in panels)
min_y = min(pos[1] for pos in panels)
max_x = max(pos[0] for pos in panels)
max_y = max(pos[1] for pos in panels)
pixel_map = {0: " ", 1: "#"}

for x in range(min_x, max_x + 1):
    line = ""
    for y in range(min_y, max_y + 1):
        line += pixel_map[panels[(x, y)]]
    print(line)
