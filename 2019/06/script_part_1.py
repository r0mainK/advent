from collections import defaultdict
from pathlib import Path
import sys

if len(sys.argv) not in [2, 3]:
    print("please pass the path to your input file (optionnaly followed by test for test mode)")
    sys.exit(1)

p = Path(sys.argv[1])

if not p.exists():
    print("%s does not point to a valid input file" % p)
    sys.exit(1)

with p.open("r", encoding="utf-8") as fin:
    direct_orbits = defaultdict(set)
    for e in fin.read().splitlines():
        planet, satellite = e.split(")")
        direct_orbits[planet].add(satellite)

orbit_count = 0
transfer_count = 0
queue = ["COM"]

while queue:
    queue = [satellite for planet in queue for satellite in direct_orbits[planet]]
    transfer_count += 1
    orbit_count += transfer_count * len(queue)

print("total number of orbits: %d" % orbit_count)
