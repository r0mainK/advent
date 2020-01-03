from itertools import product
from pathlib import Path


with (Path(__file__).parent / "data" / "24.txt").open("r", encoding="utf-8") as fin:
    layout = {}
    for i, line in enumerate(fin.read().splitlines()):
        for j, tile in enumerate(line):
            layout[(i, j)] = int(tile == "#")

adjacent_positions = {(i, j): [] for (i, j) in layout}

for i, j, offset in product(range(5), range(5), [-1, 1]):
    if (i + offset, j) in layout:
        adjacent_positions[(i, j)].append((i + offset, j))
    if (i, j + offset) in layout:
        adjacent_positions[(i, j)].append((i, j + offset))

biodiversity_ratings = set()
rating = None

while rating not in biodiversity_ratings:
    biodiversity_ratings.add(rating)
    rating = 0
    next_layout = {}
    for (i, j), tile in layout.items():
        bug_count = sum(layout[position] for position in adjacent_positions[(i, j)])
        next_layout[(i, j)] = tile
        if tile:
            rating += 2 ** (i * len(line) + j)
            if bug_count != 1:
                next_layout[(i, j)] = 0
        elif bug_count in {1, 2}:
            next_layout[(i, j)] = 1
    layout = next_layout

print(f"biodiversity rating for the first layout that appears twice: {rating}")
