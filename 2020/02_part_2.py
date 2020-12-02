from pathlib import Path


with (Path(__file__).parent / "data" / "02.txt").open("r", encoding="utf-8") as fin:
    valid_password_count = 0
    for line in fin.readlines():
        s, letter, password = line.split()
        i, j = tuple(map(int, s.split("-")))
        letter = letter.replace(":", "")
        valid_password_count += int((password[i - 1] == letter) ^ (password[j - 1] == letter) == 1)

print(f"valid password count: {valid_password_count}")
