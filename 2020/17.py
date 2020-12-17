from collections import defaultdict
from itertools import product
from pathlib import Path
from typing import DefaultDict
from typing import Iterator
from typing import Tuple


def neighbors(point: Tuple) -> Iterator[Tuple]:
    for delta in product(range(-1, 2), repeat=len(point)):
        if set(delta) == {0}:
            continue
        yield tuple(c + delta[i] for i, c in enumerate(point))


def simulate(cubes: DefaultDict[Tuple, int]) -> int:
    point_to_neighbors = {point: list(neighbors(point)) for point in cubes}
    for _ in range(6):
        next_cubes = defaultdict(int)
        next_points = set(neighbor for point in cubes for neighbor in point_to_neighbors[point])
        point_to_neighbors.update(
            {point: list(neighbors(point)) for point in next_points if point not in cubes}
        )
        next_cubes = defaultdict(int, {point: 0 for point in next_points})
        for point in next_points:
            count = sum(cubes[neighbor] for neighbor in point_to_neighbors[point])
            if (cubes[point] and count in {2, 3}) or (not cubes[point] and count == 3):
                next_cubes[point] = 1
        cubes = next_cubes
    return sum(cubes.values())


with (Path(__file__).parent / "data" / "17.txt").open() as fin:
    cubes = {}
    for i, line in enumerate(map(str.strip, fin)):
        for j, e in enumerate(line):
            cubes[(i, j)] = int(e == "#")
    cubes_3d = defaultdict(int, {(i, j, 0): state for (i, j), state in cubes.items()})
    print(f"{simulate(cubes_3d)} active cubes after the sixth cycle in 3-dimensional space")
    cubes_4d = defaultdict(int, {(i, j, 0, 0): state for (i, j), state in cubes.items()})
    print(f"{simulate(cubes_4d)} active cubes after the sixth cycle in 4-dimensional space")
