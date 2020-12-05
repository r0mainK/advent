from itertools import permutations
from itertools import product
from pathlib import Path


with (Path(__file__).parent / "data" / "20.txt").open() as fin:
    maze = fin.read().splitlines()
    maze = [line + " " for line in maze] + [" " * len(maze[0])]

passages = set()
seen_portals = {}
portals = {}
outer_edge = set()

for i, line in enumerate(maze[:-1]):
    for j, char in enumerate(line[:-1]):
        if char in {"#", " "}:
            continue
        if char == ".":
            passages.add((i, j))
            continue
        for offset_i, offset_j in permutations(range(2)):
            if not maze[(i + offset_i)][j + offset_j].isalpha():
                continue
            portal_name = char + maze[(i + offset_i)][j + offset_j]
            if maze[(i + offset_i * 2)][j + offset_j * 2] == ".":
                portal_position = (i + offset_i * 2, j + offset_j * 2)
            else:
                portal_position = (i - offset_i, j - offset_j)
            if portal_name in seen_portals:
                portals[portal_position] = seen_portals[portal_name]
                portals[seen_portals[portal_name]] = portal_position
            seen_portals[portal_name] = portal_position
            if i in {0, len(maze) - 3} or j in {0, len(line) - 3}:
                outer_edge.add(portal_position)

maze_entry = seen_portals["AA"]
maze_exit = seen_portals["ZZ"]
outer_edge -= {maze_entry, maze_exit}
queue = [(maze_entry, 0, 0)]
seen_positions = set()

while queue:
    position, level, depth = queue.pop(0)
    if position == maze_exit and level == 0:
        break
    seen_positions.add((position, level))
    if position in outer_edge:
        if (portals[position], level - 1) not in seen_positions and level > 0:
            queue.append((portals[position], level - 1, depth + 1))
    elif position in portals and (portals[position], level + 1) not in seen_positions:
        queue.append((portals[position], level + 1, depth + 1))
    for axis, offset in product([0, 1], [-1, 1]):
        next_position = list(position)
        next_position[axis] += offset
        next_position = tuple(next_position)
        if next_position in passages and (next_position, level) not in seen_positions:
            queue.append((next_position, level, depth + 1))

print(f"steps to exit the maze: {depth}")
