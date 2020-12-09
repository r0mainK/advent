from itertools import combinations
from pathlib import Path


with (Path(__file__).parent / "data" / "09.txt").open() as fin:
    xmas_data = list(map(int, fin))

for i, n in enumerate(xmas_data[25:]):
    if n not in map(sum, combinations(xmas_data[i : i + 25], 2)):
        invalid_n = n
        break

print(f"invalid number: {invalid_n}")

cur_sum = xmas_data[0]
i = 0
j = 1

while cur_sum != invalid_n:
    cur_sum += xmas_data[j]
    while cur_sum > invalid_n:
        cur_sum -= xmas_data[i]
        i += 1
    j += 1

print(f"encryption weakness: {min(xmas_data[i : j]) + max(xmas_data[i: j])}")
