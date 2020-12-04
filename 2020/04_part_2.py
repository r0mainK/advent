from pathlib import Path
import re


hair_color_pattern = re.compile(r"^#[0-9a-f]{6}$")


def check_digit_field(value, min_value, max_value):
    return value is not None and value.isdigit() and min_value <= int(value) <= max_value


def check_height(height):
    return height is not None and (
        (height.endswith("cm") and check_digit_field(height[:-2], 150, 193))
        or (height.endswith("in") and check_digit_field(height[:-2], 59, 76))
    )


def check_pid(pid):
    return pid is not None and pid.isdigit() and len(pid) == 9


def validate(passport):
    return int(
        check_digit_field(passport.get("byr"), 1920, 2002)
        and check_digit_field(passport.get("iyr"), 2010, 2020)
        and check_digit_field(passport.get("eyr"), 2020, 2030)
        and check_height(passport.get("hgt"))
        and bool(hair_color_pattern.match(passport.get("hcl", "")))
        and passport.get("ecl") in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        and check_pid(passport.get("pid"))
    )


with (Path(__file__).parent / "data" / "04.txt").open("r", encoding="utf-8") as fin:
    count = 0
    cur_passport = {}
    for line in map(str.strip, fin.readlines()):
        if not line and cur_passport:
            count += validate(cur_passport)
            cur_passport = {}
            continue
        for e in line.split():
            field, value = e.split(":")
            cur_passport[field] = value
    count += validate(cur_passport)

print(f"valid passports count: {count}")
