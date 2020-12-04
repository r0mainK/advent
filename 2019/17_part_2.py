from itertools import combinations
from pathlib import Path

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "17.txt")
machine = IntCodeMachine(program, lambda: 0)
scaffold = set()

x, y = 0, -1
for ascii_code in machine:
    character = str(chr(ascii_code))
    if character == "\n":
        x, y = x + 1, -1
        continue
    y += 1
    if character == ".":
        continue
    scaffold.add((x, y))
    if character in "^v<>":
        robot_position = (x, y)
        i = "^v<>".find(character)
        robot_axis = i // 2
        robot_direction = (i % 2) * 2 - 1

movements = []
done_exploring = False
next_robot_position = list(robot_position)
direction_map = {(0, 1): "L", (0, -1): "R", (1, 1): "R", (1, -1): "L"}
num_steps = -1

while not done_exploring:
    while tuple(next_robot_position) in scaffold:
        num_steps += 1
        robot_position = tuple(next_robot_position)
        next_robot_position[robot_axis] += robot_direction
    if num_steps:
        movements.append(str(num_steps))
    new_axis = 1 - robot_axis
    done_exploring = True
    for new_direction in [1, -1]:
        next_robot_position = list(robot_position)
        next_robot_position[new_axis] += new_direction
        if tuple(next_robot_position) in scaffold:
            done_exploring = False
            movements.append(direction_map[(robot_axis, robot_direction * new_direction)])
            break
    num_steps = 0
    robot_axis, robot_direction = new_axis, new_direction


path = ",".join(movements)
possible_routines = set()
start, end = 0, 1

while start < len(path):
    while end < len(path) and end - start <= 20:
        if path[end] == ",":
            possible_routines.add(path[start:end])
        end += 1
    while start < len(path) and path[start] != ",":
        start += 1
    start += 1
    end = start + 1

for routines in combinations(possible_routines, 3):
    queue = [(path, "")]
    while queue:
        remaining_path, main_routine = queue.pop()
        if not remaining_path:
            break
        for i, routine in enumerate(routines):
            if remaining_path.startswith(routine):
                new_main_routine = ",".join([main_routine, "ABC"[i]]).strip(",")
                if len(new_main_routine) <= 20:
                    new_remaining_path = remaining_path[len(routine) :].strip(",")
                    queue.append((new_remaining_path, new_main_routine))
    if not remaining_path:
        break

program[0] = 2
input_sequence = map(ord, "\n".join([main_routine, "\n".join(routines), "n", ""]))
machine = IntCodeMachine(program, lambda: next(input_sequence))

for _dust in machine:
    pass

print(f"amount of dust the vacuum robot collected: {_dust}")
