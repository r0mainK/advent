from pathlib import Path


with (Path(__file__).parent / "data" / "03.txt").open() as fin:
    path_1, path_2 = [path.split(",") for path in fin.readlines()]

direction_map = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (1, 1),
    "D": (1, -1),
}
seen_positions = {}
position = [0, 0]
num_steps = 0

for instruction in path_1:
    axis, offset = direction_map[instruction[0]]
    for _ in range(int(instruction[1:])):
        position[axis] += offset
        num_steps += 1
        seen_positions.setdefault(tuple(position), num_steps)

min_steps = float("inf")
position = [0, 0]
num_steps = 0

for instruction in path_2:
    axis, offset = direction_map[instruction[0]]
    for _ in range(int(instruction[1:])):
        position[axis] += offset
        num_steps += 1
        num_previous_steps = seen_positions.get(tuple(position))
        if num_previous_steps is not None:
            min_steps = min(num_steps + num_previous_steps, min_steps)

print(f"fewest combined steps to reach an intersection: {min_steps}")
