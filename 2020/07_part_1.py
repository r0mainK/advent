from collections import defaultdict
from pathlib import Path


with (Path(__file__).parent / "data" / "07.txt").open() as fin:
    bag_to_container = defaultdict(list)
    for line in fin:
        if line.endswith("no other bags.\n"):
            continue
        container, containings = line.split("contain")
        container = container.replace("bags", "").strip()
        for containing in containings.split(","):
            containing = " ".join(containing.split()[1:-1])
            bag_to_container[containing].append(container)


seen_bag_colors = set(["shiny gold"])
queue = bag_to_container["shiny gold"]
while queue:
    bag_color = queue.pop()
    if bag_color not in seen_bag_colors:
        seen_bag_colors.add(bag_color)
        queue += bag_to_container[bag_color]

print(f"{len(seen_bag_colors) - 1} can eventually contain at least one shiny gold bag")
