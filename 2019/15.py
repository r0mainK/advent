from pathlib import Path
from typing import Iterator
from typing import Tuple

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


def get_adjacent(position: Tuple[int, int]) -> Iterator[Tuple[Tuple[int, int], int]]:
    for direction in direction_map:
        axis, offset = direction_map[direction]
        next_position = list(position)
        next_position[axis] += offset
        yield (tuple(next_position), direction)


program = read_int_code(Path(__file__).parent / "data" / "15.txt")
machine = IntCodeMachine(program, lambda: directions[-1])
direction_map = {1: [0, -1], 2: [0, 1], 3: [1, 1], 4: [1, -1]}
directions = []
initial_position = position = (0, 0)
explored_positions = set([initial_position])
unexplored_positions = [
    (position, direction, 1) for position, direction in get_adjacent(initial_position)
]
walls = set()

while unexplored_positions:
    next_position, direction, depth = unexplored_positions.pop()
    while len(directions) != depth - 1:
        directions[-1] = directions[-1] + 2 * (directions[-1] % 2) - 1
        next(machine)
        directions.pop()
    directions.append(direction)
    instruction_output = next(machine)
    explored_positions.add(next_position)
    if instruction_output == 0:
        directions.pop()
        walls.add(next_position)
        next_position = position
    elif instruction_output == 2:
        oxygen_system = next_position
    position = next_position
    for next_position, direction in get_adjacent(position):
        if next_position not in explored_positions:
            unexplored_positions.append((next_position, direction, len(directions) + 1))

queue = [(oxygen_system, 0)]
seen_positions = set()

while len(queue):
    position, depth = queue.pop(0)
    seen_positions.add(position)
    if position == initial_position:
        print(f"fewest number of movement commands required: {depth}")
    for next_position, _ in get_adjacent(position):
        if next_position not in seen_positions and next_position not in walls:
            queue.append((next_position, depth + 1))

print(f"minutes until the area is filled with oxygen: {depth}")
