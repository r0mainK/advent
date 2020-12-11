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
max_i = max(i for i, _ in cur_seats)
max_j = max(j for _, j in cur_seats)

adjacent_seats = defaultdict(list)
for (i, j) in cur_seats:
    for d_i, d_j in product([-1, 0, 1], repeat=2):
        if (d_i, d_j) != (0, 0):
            i_2 = i + d_i
            j_2 = j + d_j
            while 0 <= i_2 <= max_i and 0 <= j_2 <= max_j and (i_2, j_2) not in cur_seats:
                i_2 += d_i
                j_2 += d_j
            adjacent_seats[(i, j)].append((i_2, j_2))

prev_seats = None
while cur_seats != prev_seats:
    prev_seats = cur_seats
    cur_seats = {}
    for seat in prev_seats:
        count = sum(prev_seats.get(e, 0) for e in adjacent_seats[seat])
        cur_seats[seat] = prev_seats[seat]
        if prev_seats[seat] == 0 and count == 0:
            cur_seats[seat] = 1
        elif prev_seats[seat] == 1 and count >= 5:
            cur_seats[seat] = 0

print(f"final occupied seat count: {sum(cur_seats.values())}")
