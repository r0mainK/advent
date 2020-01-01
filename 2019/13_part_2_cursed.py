from collections import defaultdict
import curses
from pathlib import Path

from utils.int_code import IntCodeMachine, read_int_code


program = read_int_code(Path(__file__).parent / "data" / "13.txt")
program[0] = 2
machine = IntCodeMachine(program, lambda: int(paddle < ball) - int(paddle > ball))
buffer = []
stdscr = curses.initscr()
curses.noecho()
curses.start_color()
stdscr.clear()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
pixel_map = {0: " ", 1: " ", 2: " ", 3: "-", 4: "@"}
MIN_X = (curses.COLS - 44) // 2
MAX_X = MIN_X + 45
MIN_Y = (curses.LINES - 23) // 2
MAX_Y = MIN_Y + 24
screen = defaultdict(int)
score = 0

for instruction_output in machine:
    buffer.append(instruction_output)
    if len(buffer) == 3:
        position = buffer[:2]
        buffer = []
        if position == [-1, 0]:
            score = instruction_output
            continue
        elif instruction_output == 3:
            paddle = position[0]
        elif instruction_output == 4:
            ball = position[0]
        screen[tuple(position)] = instruction_output
        for j, y in enumerate(range(MIN_Y, MAX_Y)):
            for i, x in enumerate(range(MIN_X, MAX_X)):
                pixel = pixel_map[screen[(i, j)]]
                stdscr.addstr(y, x, pixel, curses.color_pair(screen[(i, j)] + 1))
        score_string = f"SCORE: {score}"
        stdscr.addstr(MAX_Y, (curses.COLS - len(score_string)) // 2, score_string, 4)
        stdscr.refresh()

stdscr.getkey()
curses.echo()
curses.endwin()
