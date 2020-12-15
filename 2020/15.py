from pathlib import Path


with (Path(__file__).parent / "data" / "15.txt").open() as fin:
    memory = {}
    for i, cur in enumerate(map(int, fin.read().strip().split(",")), start=1):
        memory[cur] = i

del memory[cur]

for nth in [2020, 30000000]:
    while i != nth:
        memory[cur], cur = i, i - memory.get(cur, i)
        i += 1
    print(f"{nth}th number spoken: {cur}")
