from pathlib import Path


with (Path(__file__).parent / "data" / "08.txt").open() as fin:
    instructions = []
    for operation, argument in map(str.split, fin):
        instructions.append((operation, int(argument)))

seen_indexes = set()
accumulator = 0
index = 0
while index not in seen_indexes:
    seen_indexes.add(index)
    operation, argument = instructions[index]
    if operation == "jmp":
        index += argument
        continue
    if operation == "acc":
        accumulator += argument
    index += 1

print(f"{accumulator} is in the accumulator before repeat")
