from collections import defaultdict
from heapq import heappop
from heapq import heappush
from itertools import product
from pathlib import Path


def find_reachable_keys(base_position):
    position_queue = [(base_position, (), 0)]
    seen_positions = set()
    base_to_key = {}
    while position_queue:
        position, required_keys, depth = position_queue.pop(0)
        if position in seen_positions:
            continue
        seen_positions.add(position)
        if position in key_positions and position != base_position:
            base_to_key[key_positions[position]] = (depth, frozenset(required_keys))
        for axis, offset in product([0, 1], [-1, 1]):
            next_position = list(position)
            next_position[axis] += offset
            next_position = tuple(next_position)
            if next_position not in tunnels:
                continue
            position_queue.append(
                (next_position, required_keys + door_positions[next_position], depth + 1)
            )
    return base_to_key


with (Path(__file__).parent / "data" / "18.txt").open() as fin:
    vault = fin.read().splitlines()

key_positions = {}
door_positions = defaultdict(tuple)
possible_keys = {str(chr(i)) for i in range(97, 123)}
tunnels = set()

for x, line in enumerate(vault):
    for y, character in enumerate(line):
        if character == "#":
            continue
        if character == "@":
            start_position = (x, y)
        if character in possible_keys:
            key_positions[(x, y)] = character
        elif character.lower() in possible_keys:
            door_positions[(x, y)] = (character.lower(),)
        tunnels.add((x, y))

tunnels.remove(start_position)

for axis, offset in product([0, 1], [-1, 1]):
    adjacent_position = list(start_position)
    adjacent_position[axis] += offset
    tunnels.remove(tuple(adjacent_position))

key_to_keys = {}

for droid, (x_offset, y_offset) in enumerate(product([1, -1], [1, -1]), start=1):
    droid_position = list(start_position)
    droid_position[0] += x_offset
    droid_position[1] += y_offset
    droid_position = tuple(droid_position)
    tunnels.add(droid_position)
    key_to_keys["@" + str(droid)] = find_reachable_keys(droid_position)

for position, key in key_positions.items():
    key_to_keys[key] = find_reachable_keys(position)

node_heap = [(0, (("@1", "@2", "@3", "@4"), frozenset()))]
node_distances = {}

while node_heap:
    distance, node = heappop(node_heap)
    if node in node_distances:
        continue
    node_distances[node] = distance
    keys, collected_keys = node
    collected_keys = collected_keys | frozenset(keys)
    if len(collected_keys) == len(key_positions) + 4:
        break
    for i, key in enumerate(keys):
        for next_key, (added_distance, required_keys) in key_to_keys[key].items():
            if next_key not in collected_keys and not required_keys - collected_keys:
                next_keys = list(keys)
                next_keys[i] = next_key
                next_keys = tuple(next_keys)
                heappush(node_heap, (distance + added_distance, (next_keys, collected_keys)))

print(f"minimum amount of steps to collect all keys: {distance}")
