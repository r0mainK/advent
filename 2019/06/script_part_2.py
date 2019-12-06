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
    reverse_orbits = {}
    for e in fin.read().splitlines():
        planet, satellite = e.split(")")
        reverse_orbits[satellite] = planet

transfers_you = {}
planet = "YOU"

while planet != "COM":
    transfers_you[planet] = len(transfers_you)
    planet = reverse_orbits[planet]

transfers_count_santa = 0
planet = "SAN"

while planet not in transfers_you:
    planet = reverse_orbits[planet]
    transfers_count_santa += 1

print("minimum number of orbital transfers: %d" % (transfers_you[planet] + transfers_count_santa))
