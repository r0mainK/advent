from pathlib import Path


with (Path(__file__).parent / "data" / "03.txt").open("r", encoding="utf-8") as fin:
    path_1, path_2 = [path.split(",") for path in fin.readlines()]

direction_map = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (1, 1),
    "D": (1, -1),
}
seen_positions = set()
position = [0, 0]

for instruction in path_1:
    axis, offset = direction_map[instruction[0]]
    for _ in range(int(instruction[1:])):
        position[axis] += offset
        seen_positions.add(tuple(position))

min_distance = float("inf")
position = [0, 0]

for instruction in path_2:
    axis, offset = direction_map[instruction[0]]
    for _ in range(int(instruction[1:])):
        position[axis] += offset
        if tuple(position) in seen_positions:
            min_distance = min(sum(map(abs, position)), min_distance)

print(f"smallest manhattan distance between central port and an intersection: {min_distance}")
