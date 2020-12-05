from collections import defaultdict
from pathlib import Path


with (Path(__file__).parent / "data" / "24.txt").open() as fin:
    layout = defaultdict(int)
    for i, line in enumerate(fin.read().splitlines()):
        for j, tile in enumerate(line):
            if i == j == 2:
                continue
            layout[(0, (i, j))] = int(tile == "#")

adjacent_positions_map = {}

for _, (i, j) in layout:
    adjacent_positions = set()
    for offset in {1, -1}:
        if i + offset in range(5):
            adjacent_positions.add((0, (i + offset, j)))
        if j + offset in range(5):
            adjacent_positions.add((0, (i, j + offset)))
    if (0, (2, 2)) in adjacent_positions:
        adjacent_positions.remove((0, (2, 2)))
        for target, value in zip([1, 3], [0, 4]):
            if i == target:
                adjacent_positions = adjacent_positions.union((1, (value, k)) for k in range(5))
            if j == target:
                adjacent_positions = adjacent_positions.union((1, (k, value)) for k in range(5))
    for target, value in zip([0, 4], [1, 3]):
        if i == target:
            adjacent_positions.add((-1, (value, 2)))
        if j == target:
            adjacent_positions.add((-1, (2, value)))
    adjacent_positions_map[(i, j)] = adjacent_positions

for i in range(1, 201):
    next_layout = layout.copy()
    for level in range(-i, i + 1):
        for position, adjacent_positions in adjacent_positions_map.items():
            bug_count = sum(
                layout[level + offset, (i, j)] for offset, (i, j) in adjacent_positions
            )
            if layout[level, position] and bug_count != 1:
                next_layout[level, position] = 0
            elif not layout[level, position] and bug_count in {1, 2}:
                next_layout[level, position] = 1
    layout = next_layout

print("bugs present after 200 minutes: " f"{sum(layout.values())}")
