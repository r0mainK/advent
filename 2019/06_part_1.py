from collections import defaultdict
from pathlib import Path


with (Path(__file__).parent / "data" / "06.txt").open("r", encoding="utf-8") as fin:
    direct_orbits = defaultdict(set)
    for line in fin.read().splitlines():
        planet, satellite = line.split(")")
        direct_orbits[planet].add(satellite)

orbit_count = 0
depth = 0
planets = ["COM"]

while planets:
    planets = [satellite for planet in planets for satellite in direct_orbits[planet]]
    depth += 1
    orbit_count += depth * len(planets)

print(f"total number of orbits: {orbit_count}")
