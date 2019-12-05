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
    path_1 = fin.readline().replace("\n", "").split(",")
    path_2 = fin.readline().replace("\n", "").split(",")

instructions_map = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (1, 1),
    "D": (1, -1),
}

current_position = [0, 0]
possible_intersections = set()

for instruction in path_1:
    axis, step_direction = instructions_map[instruction[0]]
    for _ in range(int("".join(instruction[1:]))):
        current_position[axis] += step_direction
        possible_intersections.add(tuple(current_position))

current_position = [0, 0]
smallest_distance = float("inf")

for instruction in path_2:
    axis, step_direction = instructions_map[instruction[0]]
    for _ in range(int("".join(instruction[1:]))):
        current_position[axis] += step_direction
        if tuple(current_position) in possible_intersections:
            smallest_distance = min(
                abs(current_position[0]) + abs(current_position[1]), smallest_distance
            )

print(
    "smallest manhattan distance between central port and an intersection: %d" % smallest_distance
)
