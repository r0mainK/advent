from itertools import permutations
from pathlib import Path

from utils.int_code import IntCodeMachine, read_int_code


program = read_int_code(Path(__file__).parent / "data" / "07.txt")
amplifiers = [IntCodeMachine(program, lambda: amplifier_inputs.pop(0)) for _ in range(5)]
max_output_signal = 0

for phase_setting in permutations(range(5)):
    output_signal = 0
    for i, amplifier in enumerate(amplifiers):
        amplifier_inputs = [phase_setting[i], output_signal]
        output_signal = next(amplifier)
        amplifier.reboot()
    max_output_signal = max(output_signal, max_output_signal)

print(f"largest output signal: {max_output_signal}")
