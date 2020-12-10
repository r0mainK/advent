from collections import Counter
from pathlib import Path


with (Path(__file__).parent / "data" / "10.txt").open() as fin:
    adapters = list(map(int, map(str.strip, fin)))

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)
jolt_differences = Counter(f - e for e, f in zip(adapters[:-1], adapters[1:]))

print(f"1-jolt differences x 3-jolt differences: {jolt_differences[1] * jolt_differences[3]}")
