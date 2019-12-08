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
    digits = fin.read()

image_size = 25 * 6
min_zero_count = image_size + 1
result = 0

for i in range(len(digits) // image_size):
    layer = digits[i * image_size : (i + 1) * image_size]
    zero_count = layer.count("0")
    if zero_count < min_zero_count:
        min_zero_count = zero_count
        result = layer.count("1") * layer.count("2")

print("number of 1 digits times number of 2 digits in layer with fewest 0 digits: %d" % result)
