from pathlib import Path

from utils.int_code import IntCodeMachine, read_int_code


program = read_int_code(Path(__file__).parent / "data" / "09.txt")
machine = IntCodeMachine(program, lambda: 1)
print(f"diagnostic code: {next(machine)}")
