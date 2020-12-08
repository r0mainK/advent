from pathlib import Path


with (Path(__file__).parent / "data" / "08.txt").open() as fin:
    instructions = []
    possibly_corrupt_indexes = []
    for operation, argument in map(str.split, fin):
        if operation != "acc":
            possibly_corrupt_indexes.append(len(instructions))
        instructions.append((operation, int(argument)))

corrupt_map = {"jmp": "nop", "nop": "jmp"}

for corrupt_index in possibly_corrupt_indexes:
    corrupt_operation, corrupt_argument = instructions[corrupt_index]
    instructions[corrupt_index] = corrupt_map[corrupt_operation], corrupt_argument
    seen_indexes = set()
    accumulator = 0
    index = 0
    while index not in seen_indexes and index < len(instructions):
        seen_indexes.add(index)
        operation, argument = instructions[index]
        if operation == "jmp":
            index += argument
            continue
        if operation == "acc":
            accumulator += argument
        index += 1
    if index == len(instructions):
        break
    instructions[corrupt_index] = corrupt_operation, corrupt_argument

print(f"{accumulator} is in the accumulator after termination")
