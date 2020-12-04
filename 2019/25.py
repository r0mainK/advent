from pathlib import Path
from typing import List
from typing import Tuple

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


def run_until_command() -> str:
    output = ""
    try:
        while not output.endswith("Command?\n"):
            output += str(chr(next(machine)))
    except BaseException:
        pass
    return output


def parse_output(output: str) -> Tuple[List[str], List[str], bool]:
    instructions = [line[2:] for line in output.splitlines() if line.startswith("-")]
    directions = [d for d in instructions if d in compass]
    if len(instructions) != len(directions):
        return directions, [o for o in instructions if o not in compass][0], "Checkpoint" in output
    return directions, None, "Checkpoint" in output


program = read_int_code(Path(__file__).parent / "data" / "25.txt")
machine = IntCodeMachine(program, lambda: next(instruction))
compass = {"north": "south", "south": "north", "east": "west", "west": "east"}
explored_paths = set()
unexplored_paths = [[direction] for direction in parse_output(run_until_command())[0]]
harmless_objects = {}
current_path = []

while unexplored_paths:
    next_path = unexplored_paths.pop()
    while next_path[: len(current_path)] != current_path:
        instruction = map(ord, f"{compass[current_path.pop()]}\n")
        run_until_command()
    for direction in next_path[len(current_path) :]:
        instruction = map(ord, f"{direction}\n")
        output = run_until_command()
    directions, object_name, checkpoint = parse_output(output)
    current_path = next_path
    explored_paths.add(tuple(current_path))
    for direction in directions:
        if direction == compass[current_path[-1]]:
            continue
        next_path = current_path + [direction]
        if checkpoint:
            exit_path = next_path
            continue
        unexplored_paths.append(next_path.copy())
    if object_name is None:
        continue
    output = ""
    instruction = map(ord, f"take {object_name}\ndrop {object_name}\n")
    while not output.count("\n") == 5:
        output += str(chr(next(machine)))
    if output.endswith("Command?\n\n"):
        output = ""
        while not output.endswith("\n"):
            output += str(chr(next(machine)))
        if output == f"You drop the {object_name}.\n":
            harmless_objects[object_name] = current_path.copy()
    if object_name not in harmless_objects:
        machine.reboot()
        current_path = []
    run_until_command()

instructions = [compass[d] for d in current_path[::-1]]
instructions += [
    instruction
    for object_name, path in harmless_objects.items()
    for instruction in path + [f"take {object_name}"] + [compass[d] for d in path[::-1]]
]
instructions += exit_path[:-1]

for instruction in instructions:
    instruction = map(ord, f"{instruction}\n")
    run_until_command()

objects = sorted(harmless_objects)
previous_gray_code = "0" * len(objects)

for i in range(1, 2 ** len(objects) + 1):
    instruction = map(ord, f"{exit_path[-1]}\n")
    output = run_until_command()
    if "Santa" in output:
        print(output.splitlines()[-1])
        break
    gray_code = f"{i ^( i >> 1):008b}"
    for j, _object_name in enumerate(objects):
        if previous_gray_code[j] != gray_code[j]:
            break
    order = "drop" * (gray_code[j] == "1") + "take" * (gray_code[j] != "1")
    previous_gray_code = gray_code
    instruction = map(ord, f"{order} {_object_name}\n")
    run_until_command()
