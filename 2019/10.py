from collections import defaultdict
import math
from pathlib import Path


with (Path(__file__).parent / "data" / "10.txt").open("r", encoding="utf-8") as fin:
    asteroids = {
        (i, j)
        for i, line in enumerate(fin.read().splitlines())
        for j, asteroid in enumerate(line)
        if asteroid == "#"
    }

min_asteroid_count = 0
station = None

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
    if min_asteroid_count < len(angle_map):
        min_asteroid_count = len(angle_map)
        station = asteroid
        remaining_asteroids = angle_map

asteroid_count = 0
angles = sorted(remaining_asteroids)
i = 0

while remaining_asteroids:
    angle = angles[i]
    i = (i + 1) % len(angles)
    if angle not in remaining_asteroids:
        continue
    closest_asteroid = min(remaining_asteroids[angle])
    coordinates = remaining_asteroids[angle].pop(closest_asteroid)
    if not remaining_asteroids[angle]:
        remaining_asteroids.pop(angle)
    asteroid_count += 1
    if asteroid_count == 200:
        break


print(f"number of asteroids detectable from location: {min_asteroid_count}")
print(f"{asteroid_count}th asteroid destroyed: {coordinates[1] * 100 + coordinates[0]}")
