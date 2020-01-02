from pathlib import Path

deck_size = 119315717514047
num_shuffles = 101741582076661
slope, intercept = 1, 0
# Use modular arithmetic to transform the whole shuffle to a linear transformation of the position
with (Path(__file__).parent / "data" / "22.txt").open("r", encoding="utf-8") as fin:
    for instruction in fin.read().splitlines():
        instruction = instruction.split(" ")
        if instruction[-1] == "stack":
            slope = -slope % deck_size
            intercept = (deck_size - 1 - intercept) % deck_size
        elif instruction[0] == "cut":
            intercept = (intercept - int(instruction[-1])) % deck_size
        else:
            slope = (slope * int(instruction[-1])) % deck_size
            intercept = (intercept * int(instruction[-1])) % deck_size
# Same with the composition of each shuffle
fermat_inverse = lambda i: pow(i, deck_size - 2, deck_size)
global_slope = pow(slope, num_shuffles, deck_size)
global_intercept = (intercept * (global_slope - 1) * fermat_inverse(slope - 1)) % deck_size
# Finally compute the inverse of the linear transformation
card = ((2020 - global_intercept) * fermat_inverse(global_slope)) % deck_size
print(f"card at position 2020: {card}")
