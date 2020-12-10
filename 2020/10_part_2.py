from collections import defaultdict
from pathlib import Path


with (Path(__file__).parent / "data" / "10.txt").open() as fin:
    adapters = list(map(int, map(str.strip, fin)))

adapters.sort()
adapters.append(adapters[-1] + 3)
combinations = defaultdict(int, {0: 1})
for adapter in adapters:
    combinations[adapter] = sum(combinations[adapter - i - 1] for i in range(3))

print(f"total number of distinct ways to arrange the adapters: {combinations[adapters[-1]]}")
