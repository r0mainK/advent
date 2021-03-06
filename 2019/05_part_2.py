from pathlib import Path

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "05.txt")
machine = IntCodeMachine(program, lambda: 5)
print(f"diagnostic code: {next(machine)}")
