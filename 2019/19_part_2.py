from pathlib import Path

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "19.txt")
machine = IntCodeMachine(program, lambda: position.pop(0))
beam = set()
min_x, max_x, y = 1, 0, 50

while not ((min_x, y) in beam and (min_x + 99, y - 99) in beam):
    y += 1
    min_x -= 1
    in_beam = False
    while not in_beam:
        min_x += 1
        position = [min_x, y]
        in_beam = next(machine)
        machine.reboot()
    max_x = max(min_x, max_x - 1)
    while in_beam:
        max_x += 1
        position = [max_x, y]
        in_beam = next(machine)
        machine.reboot()
    beam = beam.union((x, y) for x in range(min_x, max_x))

print(f"result: {min_x * 10000 + y - 99}")
