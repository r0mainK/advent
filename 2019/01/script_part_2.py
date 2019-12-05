from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("please pass the path to your input file (and nothing else)")
    sys.exit(1)

p = Path(sys.argv[1])

if not p.exists():
    print("%s does not point to a valid input file" % p)
    sys.exit(1)

with p.open("r", encoding="utf-8") as fin:
    total_fuel = 0
    for line in fin.read().splitlines():
        fuel = round(int(line) // 3) - 2
        while fuel > 0:
            total_fuel += fuel
            fuel = round(fuel // 3) - 2

print("total fuel: %d" % total_fuel)
