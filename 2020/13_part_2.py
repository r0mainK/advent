import math
from pathlib import Path


with (Path(__file__).parent / "data" / "13.txt").open() as fin:
    next(fin)
    timestamp = 0
    step = 1
    for offset, bus_id in enumerate(fin.read().strip().split(",")):
        if bus_id == "x":
            continue
        bus_id = int(bus_id)
        while (timestamp + offset) % bus_id != 0:
            timestamp += step
        step = step * bus_id // math.gcd(step, bus_id)

print(f"earliest timestamp: {timestamp}")
