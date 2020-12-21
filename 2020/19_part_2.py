from pathlib import Path
import re


def create_pattern(i):
    if i in characters:
        return characters[i]
    return (
        "(?:" + "|".join("".join(create_pattern(j) for j in subrule) for subrule in rules[i]) + ")"
    )


with (Path(__file__).parent / "data" / "19.txt").open() as fin:
    data = fin.read().split("\n\n")

characters = {}
rules = {}
for line in map(str.strip, data[0].split("\n")):
    i, rule = line.split(":")
    i = int(i.strip())
    if '"' in rule:
        characters[i] = rule.strip().replace('"', "")
        continue
    rules[i] = [list(map(int, subrule.split())) for subrule in rule.split("|")]

pattern_1 = create_pattern(42)
pattern_2 = create_pattern(31)
pattern = re.compile(f"^((?:{pattern_1})+)((?:{pattern_2})+)$")
pattern_1 = re.compile(pattern_1)
pattern_2 = re.compile(pattern_2)
updated_count = 0
for ((block_1, block_2),) in filter(len, map(pattern.findall, data[1].split())):
    updated_count += len(pattern_1.findall(block_1)) > len(pattern_2.findall(block_2))

print(f"count of messages matching updated rule 0: {updated_count}")
