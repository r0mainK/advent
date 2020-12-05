from pathlib import Path


with (Path(__file__).parent / "data" / "08.txt").open() as fin:
    digits = fin.read()

image_size = 25 * 6
min_zero_count = image_size + 1
result = None

for i in range(len(digits) // image_size):
    layer = digits[i * image_size : (i + 1) * image_size]
    zero_count = layer.count("0")
    if zero_count < min_zero_count:
        min_zero_count = zero_count
        result = layer.count("1") * layer.count("2")

print(f"number of 1 digits times number of 2 digits in layer with fewest 0 digits: {result}")
