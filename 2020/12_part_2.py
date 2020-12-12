from pathlib import Path


with (Path(__file__).parent / "data" / "12.txt").open() as fin:
    waypoint = [1, 10]
    ship = [0, 0]
    for instruction in map(str.strip, fin):
        action, i = instruction[0], int(instruction[1:])
        if action == "N":
            waypoint[0] += i
        elif action == "S":
            waypoint[0] -= i
        elif action == "E":
            waypoint[1] += i
        elif action == "W":
            waypoint[1] -= i
        elif action == "F":
            ship[0] += i * waypoint[0]
            ship[1] += i * waypoint[1]
        elif i == 180:
            waypoint[0] = -waypoint[0]
            waypoint[1] = -waypoint[1]
        elif (action == "R" and i == 90) or (action == "L" and i == 270):
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        elif (action == "R" and i == 270) or (action == "L" and i == 90):
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]

print(f"manhattan distance: {sum(map(abs, ship))}")
