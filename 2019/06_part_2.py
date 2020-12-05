from pathlib import Path


with (Path(__file__).parent / "data" / "06.txt").open() as fin:
    reverse_orbits = {}
    for line in fin.read().splitlines():
        planet, satellite = line.split(")")
        reverse_orbits[satellite] = planet

planet_to_you = {}
planet = "YOU"

while planet != "COM":
    planet = reverse_orbits[planet]
    planet_to_you[planet] = len(planet_to_you)

planet_to_santa = 0
planet = reverse_orbits["SAN"]

while planet not in planet_to_you:
    planet = reverse_orbits[planet]
    planet_to_santa += 1

print(f"minimum number of orbital transfers: {planet_to_you[planet] + planet_to_santa}")
