from itertools import product
from pathlib import Path

from utils.int_code import IntCodeMachine, read_int_code


program = read_int_code(Path(__file__).parent / "data" / "19.txt")
machine = IntCodeMachine(program, lambda: position.pop(0))
result = 0

for position in product(range(50), range(50)):
    position = list(position)
    result += next(machine)
    machine.reboot()

print(f"number of points affected by the tractor beam: {result}")
