from copy import deepcopy
import itertools
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


def acquire_input():
    program[parameter_pointers[1]] = next(amplifier_inputs)


def output_signal() -> int:
    return program[parameter_pointers[1]]


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
    memory = [int(e) for e in line.split(",")]

op_code_map = {
    "1": (4, lambda: apply_op(operator.add)),
    "2": (4, lambda: apply_op(operator.mul)),
    "3": (2, acquire_input),
    "4": (2, output_signal),
    "5": (3, lambda: jump_op(operator.ne)),
    "6": (3, lambda: jump_op(operator.eq)),
    "7": (4, lambda: apply_op(lambda x, y: int(operator.lt(x, y)))),
    "8": (4, lambda: apply_op(lambda x, y: int(operator.eq(x, y)))),
}
largest_output_signal = 0
parameter_pointers = {}

for phase_setting in itertools.permutations(range(5)):
    amplifier_signal = 0
    for amplifier in range(5):
        instruction_pointer = 0
        program = deepcopy(memory)
        amplifier_inputs = [phase_setting[amplifier], amplifier_signal].__iter__()
        while program[instruction_pointer] != 99:
            instruction = str(program[instruction_pointer])
            op_code = instruction[-1]
            pointer_delta, op = op_code_map[op_code]
            for i in range(1, pointer_delta):
                get_parameter_pointer(i)
            instruction_output = op()
            if instruction_output is not None:
                if op_code in ["5", "6"]:
                    instruction_pointer = instruction_output
                    continue
                amplifier_signal = instruction_output
            instruction_pointer += pointer_delta
    largest_output_signal = max(largest_output_signal, amplifier_signal)

print("largest output signal: %d" % largest_output_signal)
