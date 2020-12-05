from functools import reduce
from operator import mul
from pathlib import Path


with (Path(__file__).parent / "data" / "03.txt").open() as fin:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    positions = [(0, 0) for _ in slopes]
    tree_counts = [0 for _ in slopes]
    for cur_j, line in enumerate(map(str.strip, fin)):
        for slope_ind, ((slope_i, slope_j), (i, j)) in enumerate(zip(slopes, positions)):
            if j != cur_j:
                continue
            tree_counts[slope_ind] += int(line[i] == "#")
            positions[slope_ind] = ((i + slope_i) % len(line), j + slope_j)

print(f"total tree count: {reduce(mul, tree_counts)}")
