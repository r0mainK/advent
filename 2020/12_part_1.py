from pathlib import Path


compass = {90: "N", 270: "S", 0: "E", 180: "W"}

with (Path(__file__).parent / "data" / "12.txt").open() as fin:
    ship = [0, 0]
    direction = 0
    for instruction in map(str.strip, fin):
        action, i = instruction[0], int(instruction[1:])
        if action == "F":
            action = compass[direction]
        if action == "N":
            ship[0] += i
        elif action == "S":
            ship[0] -= i
        elif action == "E":
            ship[1] += i
        elif action == "W":
            ship[1] -= i
        elif action == "L":
            direction = (direction + i) % 360
        elif action == "R":
            direction = (direction - i) % 360

print(f"manhattan distance: {sum(map(abs, ship))}")
