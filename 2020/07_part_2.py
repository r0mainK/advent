from collections import defaultdict
from pathlib import Path


with (Path(__file__).parent / "data" / "07.txt").open() as fin:
    bag_to_containings = defaultdict(list)
    for line in fin:
        if line.endswith("no other bags.\n"):
            continue
        container, containings = line.split("contain")
        container = container.replace("bags", "").strip()
        for containing in containings.split(","):
            containing = containing.split()
            n = int(containing[0])
            containing = " ".join(containing[1:-1])
            bag_to_containings[container].append((containing, n))

total = 0
queue = [("shiny gold", 1)]
while queue:
    bag_color, n = queue.pop()
    total += n
    for (bag_color_2, n_2) in bag_to_containings[bag_color]:
        queue.append((bag_color_2, n_2 * n))

print(f"{total-1} individual bags are required inside your single shiny gold bag")
