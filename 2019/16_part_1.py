from pathlib import Path


with (Path(__file__).parent / "data" / "16.txt").open() as fin:
    digits = list(map(int, fin.readline()))

pattern = [0, 1, 0, -1]

for _ in range(100):
    old_digits, digits = digits, []
    for i in range(1, len(old_digits) + 1):
        digit = sum(pattern[(j // i) % 4] * digit for j, digit in enumerate(old_digits, start=1))
        digits.append(abs(digit) % 10)

print(f"first 8 digits in output list after 100 phases: {''.join(map(str, digits[:8]))}")
