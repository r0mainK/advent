from itertools import permutations
from pathlib import Path

from utils.int_code import IntCodeMachine
from utils.int_code import read_int_code


program = read_int_code(Path(__file__).parent / "data" / "07.txt")
amplifiers = []

for i in range(5):
    amplifiers.append(IntCodeMachine(program, lambda: amplifier_inputs[i].pop(0)))

max_output_signal = 0

for phase_setting in permutations(range(5, 10)):
    amplifier_inputs = {i: [phase] for i, phase in enumerate(phase_setting)}
    output_signal = 0
    done = False
    while not done:
        for i, amplifier in enumerate(amplifiers):
            try:
                amplifier_inputs[i].append(output_signal)
                output_signal = next(amplifier)
            except StopIteration:
                amplifier.reboot()
                done = True
    max_output_signal = max(output_signal, max_output_signal)

print(f"largest output signal: {max_output_signal}")
