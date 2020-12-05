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
    highest_seat_id = -1
    for line in map(str.strip, fin):
        row = binary_split(line[:7], 127)
        col = binary_split(line[7:], 7)
        highest_seat_id = max(highest_seat_id, row * 8 + col)

print(f"highest seat id: {highest_seat_id}")
