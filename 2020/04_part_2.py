from collections import defaultdict
from pathlib import Path
import re
from typing import DefaultDict


hair_color_pattern = re.compile(r"^#[0-9a-f]{6}$")


def check_digit_field(value: str, m: int, M: int) -> bool:
    return value.isdigit() and m <= int(value) <= M


def check_height(height: str) -> bool:
    return (height.endswith("cm") and check_digit_field(height[:-2], 150, 193)) or (
        height.endswith("in") and check_digit_field(height[:-2], 59, 76)
    )


def check_pid(pid: str) -> bool:
    return pid.isdigit() and len(pid) == 9


def validate(passport: DefaultDict[str, str]) -> int:
    return int(
        check_digit_field(passport["byr"], 1920, 2002)
        and check_digit_field(passport["iyr"], 2010, 2020)
        and check_digit_field(passport["eyr"], 2020, 2030)
        and check_height(passport["hgt"])
        and bool(hair_color_pattern.match(passport["hcl"]))
        and passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        and check_pid(passport["pid"])
    )


with (Path(__file__).parent / "data" / "04.txt").open() as fin:
    count = 0
    cur_passport = defaultdict(str)
    for line in map(str.strip, fin):
        if not line and cur_passport:
            count += validate(cur_passport)
            cur_passport = defaultdict(str)
            continue
        for e in line.split():
            field, value = e.split(":")
            cur_passport[field] = value
    count += validate(cur_passport)

print(f"valid passports count: {count}")
