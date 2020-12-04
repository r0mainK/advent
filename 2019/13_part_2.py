from pathlib import Path

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "13.txt")
program[0] = 2
machine = IntCodeMachine(program, lambda: int(paddle < ball) - int(paddle > ball))
buffer = []

for instruction_output in machine:
    buffer.append(instruction_output)
    if len(buffer) == 3:
        position = buffer[:2]
        buffer = []
        if position == [-1, 0]:
            score = instruction_output
        elif instruction_output == 3:
            paddle = position[0]
        elif instruction_output == 4:
            ball = position[0]

print(f"final score: {score}")
