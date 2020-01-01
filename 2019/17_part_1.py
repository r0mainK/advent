from itertools import product
from pathlib import Path

from utils.int_code import IntCodeMachine, read_int_code


program = read_int_code(Path(__file__).parent / "data" / "17.txt")
machine = IntCodeMachine(program, lambda: 0)
scaffold = set()
x, y = 0, 0

for ascii_code in machine:
    character = str(chr(ascii_code))
    if character == "\n":
        x, y = x + 1, 0
        continue
    if character == "#":
        scaffold.add((x, y))
    y += 1

result = 0

for position in scaffold:
    is_intersection = True
    for axis, offset in product([0, 1], [1, -1]):
        adjacent_position = list(position)
        adjacent_position[axis] += offset
        if tuple(adjacent_position) not in scaffold:
            is_intersection = False
            break
    if is_intersection:
        result += position[0] * position[1]

print(f"sum of the alignment parameters of all scaffold intersections: {result}")
