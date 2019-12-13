from collections import defaultdict
import operator
from pathlib import Path
import sys
from typing import Callable, Optional


def update_pointers(pointer_delta: int):
    def decorator(op: Callable):
        def wrapper(*args) -> Optional[int]:
            for i in range(1, pointer_delta):
                if len(instruction) < 2 + i or instruction[-(2 + i)] == "0":
                    pointers["parameter_%d" % i] = program[pointers["instruction"] + i]
                elif instruction[-(2 + i)] == "2":
                    pointers["parameter_%d" % i] = (
                        program[pointers["instruction"] + i] + pointers["base"]
                    )
                else:
                    pointers["parameter_%d" % i] = pointers["instruction"] + i
            instruction_output = op(*args)
            if instruction[-1] in {"5", "6"} and instruction_output is not None:
                pointers["instruction"] = instruction_output
                return
            pointers["instruction"] += pointer_delta
            return instruction_output

        return wrapper

    return decorator


@update_pointers(pointer_delta=4)
def apply_op(op: Callable[[int, int], int]):
    program[pointers["parameter_3"]] = op(
        program[pointers["parameter_1"]], program[pointers["parameter_2"]]
    )


@update_pointers(pointer_delta=2)
def output_tile() -> int:
    return program[pointers["parameter_1"]]


@update_pointers(pointer_delta=3)
def jump_op(op: Callable[[int, int], bool]) -> Optional[int]:
    if op(program[pointers["parameter_1"]], 0):
        return program[pointers["parameter_2"]]


@update_pointers(pointer_delta=2)
def update_base():
    pointers["base"] += program[pointers["parameter_1"]]


# if len(sys.argv) != 2:
#     print("please pass the path to your input file (and nothing else)")
#     sys.exit(1)

p = Path(__file__).parent / "data.txt"  # Path(sys.argv[1])

if not p.exists():
    print("%s does not point to a valid input file" % p)
    sys.exit(1)

with p.open("r", encoding="utf-8") as fin:
    line = fin.read().replace("\n", "")
    program = defaultdict(int)
    for i, e in enumerate(line.split(",")):
        program[i] = int(e)

op_code_map = {
    "1": lambda: apply_op(operator.add),
    "2": lambda: apply_op(operator.mul),
    "4": output_tile,
    "5": lambda: jump_op(operator.ne),
    "6": lambda: jump_op(operator.eq),
    "7": lambda: apply_op(lambda x, y: int(operator.lt(x, y))),
    "8": lambda: apply_op(lambda x, y: int(operator.eq(x, y))),
    "9": update_base,
}
pointers = {
    "instruction": 0,
    "base": 0,
    "parameter_1": 0,
    "parameter_2": 0,
    "parameter_3": 0,
}
screen = defaultdict(int)
position = []

while program[pointers["instruction"]] != 99:
    instruction = str(program[pointers["instruction"]])
    instruction_output = op_code_map[instruction[-1]]()
    if instruction_output is None:
        continue
    if len(position) == 2:
        screen[tuple(position)] = instruction_output
        position = []
    else:
        position.append(instruction_output)

print("number of block tiles: %d" % len([tile for tile in screen.values() if tile == 2]))
