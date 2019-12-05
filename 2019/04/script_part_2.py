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
    start, end = fin.read().split("-")

position = 1
while start[position - 1] < start[position] and position < len(start):
    position += 1
integer = start[:position] + start[position - 1] * (len(start) - position)
password_count = 0
end = int(end)

while int(integer) < end + 1:
    for c in set(integer):
        if integer.count(c) == 2:
            password_count += 1
            break
    integer = str(int(integer) + 1)
    position = 1
    while integer[-position] == "0":
        position += 1
    integer = integer[:-position] + integer[-position] * (position)

print("number of different passwords: %d" % password_count)
