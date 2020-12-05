from pathlib import Path


with (Path(__file__).parent / "data" / "02.txt").open() as fin:
    valid_password_count = 0
    for line in fin:
        s, letter, password = line.split()
        m, M = tuple(map(int, s.split("-")))
        letter = letter.replace(":", "")
        valid_password_count += int(m <= sum([letter == e for e in password]) <= M)

print(f"valid password count: {valid_password_count}")
