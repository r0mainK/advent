from pathlib import Path


with (Path(__file__).parent / "data" / "01.txt").open("r", encoding="utf-8") as fin:
    expense_report = set(map(int, fin))

for i in expense_report:
    s = 2020 - i
    for j in expense_report - {i}:
        k = s - j
        if k in expense_report:
            break
    if k in expense_report:
        break

print(f"Product of ({i}, {j}, {k}): {i*j*k}")
