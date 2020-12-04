from pathlib import Path


with (Path(__file__).parent / "data" / "04.txt").open("r", encoding="utf-8") as fin:
    count = 0
    cur_passport_fields = set()
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for line in map(str.strip, fin.readlines()):
        if not line and cur_passport_fields:
            count += int(len(required_fields - cur_passport_fields) == 0)
            cur_passport_fields = set()
            continue
        for e in line.split():
            cur_passport_fields.add(e.split(":")[0])
    count += int(len(required_fields - cur_passport_fields) == 0)

print(f"valid passports count: {count}")
