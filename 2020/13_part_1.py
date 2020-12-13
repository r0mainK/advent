import math
from pathlib import Path


with (Path(__file__).parent / "data" / "13.txt").open() as fin:
    earliest_timestamp = int(next(fin).strip())
    best_bus_id = None
    best_timedelta = None
    for bus_id in fin.read().strip().split(","):
        if bus_id == "x":
            continue
        bus_id = int(bus_id)
        timedelta = math.ceil(earliest_timestamp / bus_id) * bus_id - earliest_timestamp
        if best_timedelta is None or timedelta < best_timedelta:
            best_timedelta = timedelta
            best_bus_id = bus_id

print(f"bus id x waiting time = {best_bus_id * best_timedelta}")
