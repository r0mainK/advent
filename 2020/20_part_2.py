from collections import defaultdict
from itertools import product
import math
from pathlib import Path
import re
from typing import List
from typing import Tuple


class Tile:
    def __init__(self, tile: List[str]) -> None:
        self.tile = tile
        self.last_rotated = True

    def transform(self) -> None:
        self.tile = [line[::-1] for line in self.tile]
        self.last_rotated = not self.last_rotated
        if self.last_rotated:
            self.tile = [
                "".join(line[i] for line in self.tile[::-1]) for i in range(len(self.tile))
            ]

    def borders(self) -> Tuple[List[str], List[str], List[str], List[str]]:
        return (
            self.tile[0],
            self.tile[-1],
            "".join(line[0] for line in self.tile),
            "".join(line[-1] for line in self.tile),
        )

    def tile_no_borders(self) -> List[List[str]]:
        return [list(line[1:-1]) for line in self.tile[1:-1]]


id_to_tiles = {}
border_to_ids = defaultdict(set)
id_to_borders = {}

with (Path(__file__).parent / "data" / "20.txt").open() as fin:
    for tile in fin.read().strip().split("\n\n"):
        tile = list(map(str.strip, tile.split("\n")))
        tile_id = int(tile[0].replace("Tile", "").replace(":", "").strip())
        tile = Tile(tile[1:])
        borders = tile.borders()
        for border in borders:
            border_to_ids[border].add(tile_id)
            border_to_ids[border[::-1]].add(tile_id)
        id_to_tiles[tile_id] = tile

image = {}
used_tiles = set()
for tile_id, tile in id_to_tiles.items():
    up, down, left, right = tile.borders()
    border_count = sum(len(border_to_ids[border]) for border in [up, down, left, right])
    if border_count == 6:
        while len(border_to_ids[up]) != 1 or len(border_to_ids[left]) != 1:
            tile.transform()
            up, down, left, right = tile.borders()
        image[(0, 0)] = tile_id
        last_down = down
        last_right = right

n_tiles = int(math.sqrt(len(id_to_tiles)))
for i in range(1, n_tiles):
    tile_ids = list(border_to_ids[last_down])
    tile_id = tile_ids[0] if tile_ids[0] != image[(i - 1, 0)] else tile_ids[1]
    tile = id_to_tiles[tile_id]
    up, down, left, right = tile.borders()
    while up != last_down or len(border_to_ids[left]) != 1:
        tile.transform()
        up, down, left, right = tile.borders()
    image[(i, 0)] = tile_id
    last_down = down

for j in range(1, n_tiles):
    tile_ids = list(border_to_ids[last_right])
    tile_id = tile_ids[0] if tile_ids[0] != image[(0, j - 1)] else tile_ids[1]
    tile = id_to_tiles[tile_id]
    up, down, left, right = tile.borders()
    while left != last_right or len(border_to_ids[up]) != 1:
        tile.transform()
        up, down, left, right = tile.borders()
    image[(0, j)] = tile_id
    last_right = right

for i, j in product(range(1, n_tiles), repeat=2):
    last_down_id = border_to_ids[image[(i - 1, j)]]
    last_right_id = border_to_ids[image[(i, j - 1)]]
    _, last_down, _, _ = id_to_tiles[image[(i - 1, j)]].borders()
    _, _, _, last_right = id_to_tiles[image[(i, j - 1)]].borders()
    tile_id = list(border_to_ids[last_right].intersection(border_to_ids[last_down]))[0]
    tile = id_to_tiles[tile_id]
    up, down, left, right = tile.borders()
    while left != last_right or up != last_down:
        tile.transform()
        up, down, left, right = tile.borders()
    image[(i, j)] = tile_id


real_image = []
for i in range(n_tiles):
    row = [[] for _ in up[1:-1]]
    for j in range(n_tiles):
        part = id_to_tiles[image[(i, j)]].tile_no_borders()

        for k, line in enumerate(part):
            row[k].extend(line)
    real_image.extend(row)

real_image = Tile(["".join(line) for line in real_image])

sea_monster_count = 0


sml = len("                  # ")
pat_1 = re.compile("                  # ".replace(" ", "."))
pat_2 = re.compile("#    ##    ##    ###".replace(" ", "."))
pat_3 = re.compile(" #  #  #  #  #  #   ".replace(" ", "."))


while not sea_monster_count:
    tile = real_image.tile
    for i in range(len(tile) - 3):
        for j in range(len(tile) - sml):
            if (
                pat_1.match(tile[i][j : j + sml])
                and pat_2.match(tile[i + 1][j : j + sml])
                and pat_3.match(tile[i + 2][j : j + sml])
            ):
                sea_monster_count += 1

    real_image.transform()

print(sea_monster_count)
print(sum(line.count("#") for line in tile) - sea_monster_count * 15)
