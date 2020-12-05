from pathlib import Path


card = 2019
deck_size = 10007

with (Path(__file__).parent / "data" / "22.txt").open() as fin:
    for instruction in fin.read().splitlines():
        instruction = instruction.split(" ")
        if instruction[-1] == "stack":
            card = deck_size - card - 1
        elif instruction[0] == "cut":
            card = (card - int(instruction[-1])) % deck_size
        else:
            card = (card * int(instruction[-1])) % deck_size

print(f"position of card 2019: {card}")
