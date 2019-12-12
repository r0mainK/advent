from itertools import permutations
from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("please pass the path to your input file (and nothing else)")
    sys.exit(1)

p = Path(sys.argv[1])

if not p.exists():
    print("%s does not point to a valid input file" % p)
    sys.exit(1)

moons = {i: {"position": [], "velocity": [0, 0, 0]} for i in range(4)}

with p.open("r", encoding="utf-8") as fin:
    for i, line in enumerate(fin.read().splitlines()):
        moons[i]["position"] = [int(pos.split("=")[1]) for pos in line[1:-1].split(",")]

for _ in range(1000):
    new_moons = moons.copy()
    for moon_1, moon_2 in permutations(moons, 2):
        if moon_1 <= moon_2:
            continue
        for axis in range(3):
            if moons[moon_1]["position"][axis] < moons[moon_2]["position"][axis]:
                new_moons[moon_1]["velocity"][axis] += 1
                new_moons[moon_2]["velocity"][axis] -= 1
            elif moons[moon_1]["position"][axis] > moons[moon_2]["position"][axis]:
                new_moons[moon_1]["velocity"][axis] -= 1
                new_moons[moon_2]["velocity"][axis] += 1
    for moon in moons:
        for axis in range(3):
            new_moons[moon]["position"][axis] += new_moons[moon]["velocity"][axis]
    moons = new_moons.copy()

total_energy = 0

for moon in moons.values():
    total_energy += sum([abs(e) for e in moon["position"]]) * sum(
        [abs(e) for e in moon["velocity"]]
    )

print("total energy in the system after 1000 steps: %d" % total_energy)
