from pathlib import Path


with (Path(__file__).parent / "data" / "03.txt").open("r", encoding="utf-8") as fin:
    tree_count = 0
    i = 0
    for line in map(str.strip, fin.readlines()):
        tree_count += int(line[i] == "#")
        i = (i + 3) % len(line)

print(f"tree count: {tree_count}")
