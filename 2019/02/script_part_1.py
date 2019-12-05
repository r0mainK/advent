import operator
from pathlib import Path
import sys

if len(sys.argv) not in [2, 3]:
    print("please pass the path to your input file (optionnaly followed by test for test mode)")
    sys.exit(1)

p = Path(sys.argv[1])

if not p.exists():
    print("%s does not point to a valid input file" % p)
    sys.exit(1)

with p.open("r", encoding="utf-8") as fin:
    line = fin.read().replace("\n", "")
    program = [int(e) for e in line.split(",")]

test_mode = False
if not len(sys.argv) == 3:
    print("replacing value at position 1 with value 12 and value at position 2 with value 2")
    program[1] = 12
    program[2] = 2
elif sys.argv[2] == "test":
    print("running in test mode")
    test_mode = True
else:
    print("second value must be test if supplied")
    sys.exit(1)

instruction_pointer = 0
op_code_map = {1: operator.add, 2: operator.mul}

while program[instruction_pointer] != 99:
    op_code, pointer_1, pointer_2, pointer_3 = program[
        instruction_pointer : instruction_pointer + 4
    ]
    program[pointer_3] = op_code_map[op_code](program[pointer_1], program[pointer_2])
    instruction_pointer += 4

if test_mode:
    print("program state:", program)
else:
    print("value at position 0: %d" % program[0])
