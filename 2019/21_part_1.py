from pathlib import Path

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "21.txt")
spring_script = map(
    ord, "\n".join(["NOT A J", "NOT B T", "OR T J", "NOT C T", "OR T J", "AND D J", "WALK", ""])
)

machine = IntCodeMachine(program, lambda: next(spring_script))

for _damage in machine:
    pass

print(f"amount of hull damage: {_damage}")
