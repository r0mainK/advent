from itertools import permutations
from pathlib import Path


with (Path(__file__).parent / "data" / "12.txt").open() as fin:
    moons = {i: {"velocity": [0, 0, 0]} for i in range(4)}
    initial_positions = {}
    for i, line in enumerate(fin.read().splitlines()):
        position = [int(pos.split("=")[1]) for pos in line[1:-1].split(",")]
        initial_positions[i] = position
        moons[i]["position"] = position.copy()

cycle_steps = []
for axis in range(3):
    step = 0
    done = False
    while not done:
        step += 1
        new_moons = moons.copy()
        for moon_1, moon_2 in permutations(moons, 2):
            if moon_1 <= moon_2:
                continue
            if moons[moon_1]["position"][axis] < moons[moon_2]["position"][axis]:
                new_moons[moon_1]["velocity"][axis] += 1
                new_moons[moon_2]["velocity"][axis] -= 1
            elif moons[moon_1]["position"][axis] > moons[moon_2]["position"][axis]:
                new_moons[moon_1]["velocity"][axis] -= 1
                new_moons[moon_2]["velocity"][axis] += 1
        for moon in moons:
            new_moons[moon]["position"][axis] += new_moons[moon]["velocity"][axis]
        moons = new_moons.copy()
        done = True
        for moon in moons:
            if (
                moons[moon]["position"][axis] != initial_positions[moon][axis]
                or moons[moon]["velocity"][axis] != 0
            ):
                done = False
                break
    cycle_steps.append(step)

primes = {}

for prime in range(2, max(cycle_steps) + 1):
    is_prime = True
    for p in primes:
        if prime % p == 0:
            is_prime = False
            break
    if not is_prime:
        continue
    max_multiplicity = 0
    for axis in range(3):
        multiplicity = 0
        while cycle_steps[axis] % prime == 0:
            multiplicity += 1
            cycle_steps[axis] /= prime
        max_multiplicity = max(multiplicity, max_multiplicity)
    primes[prime] = max_multiplicity

num_steps = 1

for prime, multiplicity in primes.items():
    num_steps *= prime ** multiplicity

print(f"number of steps needed to return to initial state: {num_steps}")
