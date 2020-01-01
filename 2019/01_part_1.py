from pathlib import Path


with (Path(__file__).parent / "data" / "01.txt").open("r", encoding="utf-8") as fin:
    total_fuel = 0
    for line in fin.read().splitlines():
        total_fuel += round(int(line) // 3) - 2

print(f"total fuel: {total_fuel}")
