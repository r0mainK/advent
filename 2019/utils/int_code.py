from collections import defaultdict
from copy import deepcopy
import operator
from pathlib import Path
from typing import Callable, DefaultDict, Optional


def read_int_code(path: Path):
    with path.open("r", encoding="utf-8") as fin:
        return defaultdict(int, enumerate(map(int, fin.readline().split(","))))


class BareIntCodeMachine:
    def __init__(
        self, program: DefaultDict[int, int], input_function: Optional[Callable[[], int]] = None,
    ):
        self.memory = deepcopy(program)
        self.reboot()
        self.parameters = {}
        if input_function is None:
            input_function = lambda: None
        self.op_code_map = {
            1: lambda: self._apply(operator.add),
            2: lambda: self._apply(operator.mul),
            3: lambda: self.wrapper(input_function),
            4: self.output,
            5: lambda: self._jump(operator.ne),
            6: lambda: self._jump(operator.eq),
            7: lambda: self._apply(lambda x, y: int(operator.lt(x, y))),
            8: lambda: self._apply(lambda x, y: int(operator.eq(x, y))),
            9: self.update_base,
        }

    def reboot(self):
        self.program = deepcopy(self.memory)
        self.position = 0
        self.base = 0

    def wrapper(self, function: Callable[[], int]):
        self.program[self.parameters[1]] = function()
        self.position += 2

    def _apply(self, function: Callable[[int, int], int]):
        self.program[self.parameters[3]] = function(
            self.program[self.parameters[1]], self.program[self.parameters[2]]
        )
        self.position += 4

    def output(self) -> int:
        self.position += 2
        return self.program[self.parameters[1]]

    def _jump(self, boolean_function: Callable[[int, int], bool]):
        if boolean_function(self.program[self.parameters[1]], 0):
            self.position = self.program[self.parameters[2]]
            return
        self.position += 3

    def update_base(self):
        self.base += self.program[self.parameters[1]]
        self.position += 2

    def parse_instruction(self) -> int:
        instruction = self.program[self.position]
        modes = [instruction // (10 ** (i + 2)) % 10 for i in range(3)]
        for i, mode in enumerate(modes, start=1):
            if mode == 1:
                self.parameters[i] = self.position + i
                continue
            self.parameters[i] = self.program[self.position + i] + self.base * (mode == 2)
        return instruction % 100

    def __iter__(self):
        return self

    def __next__(self):
        self.op_code = self.parse_instruction()
        if self.op_code == 99:
            raise StopIteration
        return self.op_code_map[self.op_code]()


class IntCodeMachine(BareIntCodeMachine):
    def __init__(
        self, program: DefaultDict[int, int], input_function: Optional[Callable[[], int]] = None,
    ):
        super().__init__(program, input_function)

    def __next__(self):
        op_code = self.parse_instruction()
        while op_code != 99:
            instruction_output = self.op_code_map[op_code]()
            if instruction_output is not None:
                return instruction_output
            op_code = self.parse_instruction()
        raise StopIteration
