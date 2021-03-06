from collections import defaultdict
from itertools import product
from pathlib import Path


with (Path(__file__).parent / "data" / "11.txt").open() as fin:
    cur_seats = {
        (i, j): 0
        for i, line in enumerate(map(str.strip, fin))
        for j, seat in enumerate(line)
        if seat == "L"
    }

adjacent_seats = defaultdict(list)
for (i, j) in cur_seats:
    for d_i, d_j in product([-1, 0, 1], repeat=2):
        if (d_i, d_j) != (0, 0):
            adjacent_seats[(i, j)].append((i + d_i, j + d_j))

prev_seats = None
while cur_seats != prev_seats:
    prev_seats = cur_seats
    cur_seats = {}
    for seat in prev_seats:
        count = sum(prev_seats.get(e, 0) for e in adjacent_seats[seat])
        cur_seats[seat] = prev_seats[seat]
        if prev_seats[seat] == 0 and count == 0:
            cur_seats[seat] = 1
        elif prev_seats[seat] == 1 and count >= 4:
            cur_seats[seat] = 0

print(f"final occupied seat count: {sum(cur_seats.values())}")
