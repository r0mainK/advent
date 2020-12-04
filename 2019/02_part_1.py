from pathlib import Path

from utils.int_code import BareIntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "02.txt")
program[1], program[2] = 12, 2
machine = BareIntCodeMachine(program)

for _ in machine:
    pass

print(f"value at position 0: {machine.program[0]}")
