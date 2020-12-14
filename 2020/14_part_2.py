from copy import deepcopy
from itertools import product
from pathlib import Path


with (Path(__file__).parent / "data" / "14.txt").open() as fin:
    memory = {}
    for line in map(str.strip, fin):
        if line.startswith("mask"):
            mask = line.split()[-1][::-1]
            floating_indexes = [i for i, e in enumerate(mask) if e == "X"]
            continue
        adress, _, value = line.split()
        adress = int(adress[4:-1])
        value = int(value)
        base_digits = []
        for e in mask:
            base_digits.append(adress % 2 if e != "1" else 1)
            adress = adress // 2
        for changes in product([True, False], repeat=len(floating_indexes)):
            digits = deepcopy(base_digits)
            for i, change in zip(floating_indexes, changes):
                if change:
                    digits[i] = 1 - digits[i]
            memory[int("".join(map(str, digits[::-1])), base=2)] = value

print(f"sum of values in memory: {sum(memory.values())}")
