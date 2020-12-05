from pathlib import Path


def binary_split(seq: str, M: int) -> int:
    m = 0
    for char in seq:
        if char in "FL":
            M = (m + M) // 2
            continue
        m = (m + M) // 2 + 1
    return m


with (Path(__file__).parent / "data" / "05.txt").open("r", encoding="utf-8") as fin:
    seat_ids = set()
    for line in map(str.strip, fin):
        row = binary_split(line[:7], 127)
        col = binary_split(line[7:], 7)
        seat_ids.add(row * 8 + col)


for seat_id in range(min(seat_ids), max(seat_ids)):
    if seat_id not in seat_ids:
        print(f"your seat id: {seat_id}")
        break
