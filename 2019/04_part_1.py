from pathlib import Path


with (Path(__file__).parent / "data" / "04.txt").open() as fin:
    start, end = fin.read().split("-")

position = ([i < j for i, j in zip(start[:-1], start[1:])] + [False]).index(False) + 1
digits = start[:position] + start[position - 1] * (len(start) - position)
end = int(end)
password_count = 0

while int(digits) < end + 1:
    password_count += len(set(digits)) < 6
    digits = str(int(digits) + 1)
    position = [i != "0" for i in digits[::-1]].index(True) + 1
    digits = digits[:-position] + digits[-position] * (position)

print(f"number of different passwords: {password_count}")
