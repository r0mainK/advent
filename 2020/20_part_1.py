from collections import Counter
import math
from pathlib import Path


border_counter = Counter()
id_to_borders = {}

with (Path(__file__).parent / "data" / "20.txt").open() as fin:
    for tile in fin.read().strip().split("\n\n"):
        tile = tile.split("\n")
        tile_id = int(tile[0].replace("Tile", "").replace(":", "").strip())
        up = tile[1].strip()
        down = tile[-1].strip()
        left = "".join(line[0] for line in tile[1:])
        right = "".join(line[-1] for line in map(str.strip, tile[1:]))
        border_counter.update([up, down, left, right])
        border_counter.update([up[::-1], down[::-1], left[::-1], right[::-1]])
        id_to_borders[tile_id] = (up, down, left, right)

corners = []
for tile_id, borders in id_to_borders.items():
    if sum(border_counter[border] for border in borders) == 6:
        corners.append(tile_id)

print(f"product of the four corner tile IDs: {math.prod(corners)}")
