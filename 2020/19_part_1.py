from pathlib import Path
import re


def create_pattern(i):
    if i in characters:
        return characters[i]
    return (
        "(" + "|".join("".join(create_pattern(j) for j in subrule) for subrule in rules[i]) + ")"
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

pattern = re.compile(f"^{create_pattern(0)}$")
print(
    "count of messages matching rule 0: "
    f"{sum(pattern.match(message) is not None for message in data[1].split())}"
)
