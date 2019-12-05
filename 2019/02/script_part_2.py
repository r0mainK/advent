from copy import deepcopy
import operator
from pathlib import Path
import sys

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

result = 19690720
noun, verb = -1, -1
op_code_map = {1: operator.add, 2: operator.mul}

while verb != 100:
    noun = (noun + 1) % 100
    verb += int(noun == 0)
    program = deepcopy(memory)
    program[1] = noun
    program[2] = verb
    instruction_pointer = 0
    while program[instruction_pointer] != 99:
        op_code, pointer_1, pointer_2, pointer_3 = program[
            instruction_pointer : instruction_pointer + 4
        ]
        program[pointer_3] = op_code_map[op_code](program[pointer_1], program[pointer_2])
        instruction_pointer += 4
    if result == program[0]:
        print("100*noun+verb:  %d" % (100 * noun + verb))
        break

if verb == 100:
    print("did not find any (noun, verb) pair that produced desired output")
    sys.exit(1)
