from collections import defaultdict
import math
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
    asteroids = {
        (i, j)
        for i, line in enumerate(fin.read().splitlines())
        for j, asteroid in enumerate(line)
        if asteroid == "#"
    }

best_asteroid_count = 0
best_location = None

for location in asteroids:
    angle_map = defaultdict(dict)
    for asteroid in asteroids:
        if asteroid == location:
            continue
        vector = (location[0] - asteroid[0], location[1] - asteroid[1])
        norm = math.sqrt(sum(map(lambda x: x ** 2, vector)))
        angle = math.acos(vector[0] / norm)
        if asteroid[1] < location[1]:
            angle = 2 * math.pi - angle
        angle = round(angle, 3)
        angle_map[angle][norm] = asteroid
    if best_asteroid_count < len(angle_map):
        best_asteroid_count = len(angle_map)
        best_location = asteroid
        remaining_asteroids = angle_map

coordinates = None
destroyed_count = 0

while remaining_asteroids and coordinates is None:
    remaining_angles = sorted(remaining_asteroids)
    for angle in remaining_angles:
        closest_asteroid = min(remaining_asteroids[angle])
        destroyed_asteroid = remaining_asteroids[angle].pop(closest_asteroid)
        if not remaining_asteroids[angle]:
            remaining_asteroids.pop(angle)
        destroyed_count += 1
        if destroyed_count == 200:
            coordinates = destroyed_asteroid
            break

print("number of asteroids detectable from location: %d" % best_asteroid_count)
print("200th asteroid destroyed: %d" % (coordinates[1] * 100 + coordinates[0]))
