import operator
from pathlib import Path
import sys
from typing import Callable


def get_parameter_pointer(parameter_index: int):
    if len(instruction) < 2 + parameter_index or instruction[-(2 + parameter_index)] == "0":
        parameter_pointers[parameter_index] = program[instruction_pointer + parameter_index]
        return
    parameter_pointers[parameter_index] = instruction_pointer + parameter_index


def apply_op(op: Callable[[int, int], int]):
    program[parameter_pointers[3]] = op(
        program[parameter_pointers[1]], program[parameter_pointers[2]]
    )


def acquire_system_id():
    program[parameter_pointers[1]] = int(input("enter system ID: "))


def print_diagnostic():
    print("diagnostic code: %d" % program[parameter_pointers[1]])


def jump_op(op: Callable[[int, int], bool]) -> int:
    if op(program[parameter_pointers[1]], 0):
        return program[parameter_pointers[2]]


if len(sys.argv) != 2:
    print("please pass the path to your input file (and nothing else)")
    sys.exit(1)

p = Path(sys.argv[1])

if not p.exists():
    print("%s does not point to a valid input file" % p)
    sys.exit(1)

with p.open("r", encoding="utf-8") as fin:
    line = fin.read().replace("\n", "")
    program = [int(e) for e in line.split(",")]

instruction_pointer = 0
parameter_pointers = {}
op_code_map = {
    "1": (4, lambda: apply_op(operator.add)),
    "2": (4, lambda: apply_op(operator.mul)),
    "3": (2, acquire_system_id),
    "4": (2, print_diagnostic),
    "5": (3, lambda: jump_op(operator.ne)),
    "6": (3, lambda: jump_op(operator.eq)),
    "7": (4, lambda: apply_op(lambda x, y: int(operator.lt(x, y)))),
    "8": (4, lambda: apply_op(lambda x, y: int(operator.eq(x, y)))),
}

while program[instruction_pointer] != 99:
    instruction = str(program[instruction_pointer])
    pointer_delta, op = op_code_map[instruction[-1]]
    for i in range(1, pointer_delta):
        get_parameter_pointer(i)
    new_instruction_pointer = op()
    if new_instruction_pointer is None:
        new_instruction_pointer = instruction_pointer + pointer_delta
    instruction_pointer = new_instruction_pointer
