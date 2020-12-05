from pathlib import Path


with (Path(__file__).parent / "data" / "01.txt").open() as fin:
    expense_report = set(map(int, fin))

for i in expense_report:
    j = 2020 - i
    if j in expense_report:
        break

print(f"Product of ({i}, {j}): {i*j}")
