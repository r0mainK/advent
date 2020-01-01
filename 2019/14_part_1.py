from collections import defaultdict
import math
from pathlib import Path


with (Path(__file__).parent / "data" / "14.txt").open("r", encoding="utf-8") as fin:
    reaction_inputs = {}
    reaction_outputs = {}
    for reaction in fin.read().splitlines():
        inputs, output = reaction.split("=>")
        reaction_input = {}
        for e in inputs.split(","):
            input_quantity, input_chemical = e.strip().split(" ")
            reaction_input[input_chemical] = int(input_quantity)
        output_quantity, output_chemical = output.strip().split(" ")
        reaction_inputs[output_chemical] = reaction_input
        reaction_outputs[output_chemical] = int(output_quantity)

chemical_queue = ["FUEL"]
parents = defaultdict(set)

while chemical_queue:
    chemical = chemical_queue.pop(0)
    for input_chemical in reaction_inputs[chemical]:
        if input_chemical == "ORE":
            continue
        if input_chemical not in parents:
            chemical_queue.append(input_chemical)
        parents[input_chemical].add(chemical)

chemical_queue = ["FUEL"]
chemicals = defaultdict(int)
chemicals["FUEL"] = 1
seen_chemicals = set()

while chemical_queue:
    chemical = chemical_queue.pop(0)
    seen_chemicals.add(chemical)
    required_quantity = chemicals[chemical]
    output_quantity = reaction_outputs[chemical]
    num_reactions = math.ceil(required_quantity / output_quantity)
    for input_chemical, input_quantity in reaction_inputs[chemical].items():
        chemicals[input_chemical] += input_quantity * num_reactions
        if input_chemical != "ORE" and not parents[input_chemical] - seen_chemicals:
            chemical_queue.append(input_chemical)

print(f"minimum amount of ORE required to produce exactly 1 fuel: {chemicals['ORE']}")
