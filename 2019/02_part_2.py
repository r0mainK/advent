from itertools import product
from pathlib import Path

from utils.int_code import BareIntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "02.txt")
machine = BareIntCodeMachine(program)

for noun, verb in product(range(100), range(100)):
    machine.reboot()
    machine.program[1], machine.program[2] = noun, verb
    for _ in machine:
        pass
    if machine.program[0] == 19690720:
        break

print(f"100 * noun + verb: {100 * noun + verb}")
