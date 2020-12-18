from operator import add
from operator import mul
from pathlib import Path


SYMBOL_TO_OP = {"+": add, "*": mul}


def compute(equation):
    if "(" in equation:
        buffer = []
        parentheses = []
        for i, char in enumerate(equation):
            if char == "(":
                buffer.append(i)
            elif char == ")":
                parentheses.append((buffer.pop(), i))
        parentheses.sort(key=lambda e: (e[0], -e[1]), reverse=True)
        while parentheses:
            i, j = parentheses.pop(0)
            result = str(compute(equation[i + 1 : j]))
            equation = equation[:i] + result + equation[j + 1 :]
            delta = i - j + len(result) - 1
            parentheses = [(i2, j2 + (delta * (j2 > j))) for (i2, j2) in parentheses]

    equation = equation.split()
    x = int(equation.pop(0))
    while equation:
        op = SYMBOL_TO_OP[equation.pop(0)]
        x = op(x, int(equation.pop(0)))
    return x


with (Path(__file__).parent / "data" / "18.txt").open() as fin:
    print(f"sum of all results: {sum(map(compute, map(str.strip, fin)))}")
