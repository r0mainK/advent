from collections import defaultdict
from pathlib import Path


with (Path(__file__).parent / "data" / "16.txt").open() as fin:
    data = fin.read().split("\n\n")

rules = {}
for line in data[0].split("\n"):
    name, vs = line.split(":")
    v1, v2 = map(str.strip, vs.split("or"))
    rules[name] = tuple(map(int, v1.split("-"))), tuple(map(int, v2.split("-")))

rule_order_constraints = {i: set(rules) for i in range(len(rules))}
error_rate = 0
for ticket in (map(int, line.split(",")) for line in data[2].strip().split("\n")[1:]):
    ticket_constraints = defaultdict(set)
    valid_ticket = True
    for i, v in enumerate(ticket):
        for name, ((m1, M1), (m2, M2)) in rules.items():
            if not (m1 <= v <= M1 or m2 <= v <= M2):
                ticket_constraints[i].add(name)
        if len(ticket_constraints[i]) == len(rules):
            error_rate += v
            valid_ticket = False
    if valid_ticket:
        for i, constraints in ticket_constraints.items():
            rule_order_constraints[i] -= constraints

print(f"ticket scanning error rate: {error_rate}")

rule_order = [None for _ in rules]
for i in sorted(rule_order_constraints, key=rule_order_constraints.get):
    rule_order[i] = list(rule_order_constraints[i] - set(rule_order))[0]

product = 1
for i, v in enumerate(data[1].split("\n")[1].split(",")):
    if rule_order[i].startswith("departure"):
        product *= int(v)

print(f"product of fields starting by 'departure': {product}")
