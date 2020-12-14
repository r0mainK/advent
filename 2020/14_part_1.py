from pathlib import Path


with (Path(__file__).parent / "data" / "14.txt").open() as fin:
    memory = {}
    for line in map(str.strip, fin):
        if line.startswith("mask"):
            mask = line.split()[-1][::-1]
            continue
        adress, _, value = line.split()
        value = int(value)
        digits = []
        for e in mask:
            digits.append(str(value % 2) if e == "X" else e)
            value = value // 2
        memory[int(adress[4:-1])] = int("".join(digits[::-1]), base=2)

print(f"sum of values in memory: {sum(memory.values())}")
