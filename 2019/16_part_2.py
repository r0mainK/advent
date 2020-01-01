from pathlib import Path


with (Path(__file__).parent / "data" / "16.txt").open("r", encoding="utf-8") as fin:
    digits = list(map(int, fin.readline())) * 10000

offset = int("".join(map(str, digits[:7])))
digits = digits[offset:][::-1]

for _ in range(100):
    for i in range(1, len(digits)):
        digits[i] = (digits[i] + digits[i - 1]) % 10

print(f"8 digit message: {''.join(map(str, digits[:-9:-1]))}")
