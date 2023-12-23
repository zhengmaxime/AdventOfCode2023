INPUT_FILE = 'input_test3'
INPUT_FILE = 'input'

import sys
sys.setrecursionlimit(15000)

input_lines = open(INPUT_FILE).readlines()

grid = [ x.strip() for x in input_lines ]

W = len(grid[0])
H = len(grid)

visited = [ [0] * W for _ in grid ]
steps_grid = [ [0] * W for _ in grid ]

def find_start():
    for i, _ in enumerate(grid):
        for j, c in enumerate(grid[i]):
            if c == 'S':
                return j, i

s_x, s_y = find_start()

def printm(grid):
    for r in grid:
        print(r, sep='')
    print()

#printm(grid)

def rec(y, x, steps, orig):
    if orig != "start":
        if y < 0 or x < 0 or x >= W or y >= H:
            return
        if grid[y][x] == '.':
            return
        if orig == 'up' and grid[y][x] not in ['|', 'L', 'J']:
            return
        if orig == 'down' and grid[y][x] not in ['|', '7', 'F']:
            return
        if orig == 'left' and grid[y][x] not in ['-', 'J', '7']:
            return
        if orig == 'right' and grid[y][x] not in ['-', 'L', 'F']:
            return
        if visited[y][x] == 1:
            return
    visited[y][x] = 1
    if 0 == steps_grid[y][x]:
        steps_grid[y][x] = steps
    else:
        steps_grid[y][x] = min(steps, steps_grid[y][x])
    steps += 1
    s = grid[y][x]
    if s in ['S', '|', '7', 'F']:
        rec(y + 1, x, steps, "up")
    if s in ['S', '|', 'L', 'J']:
        rec(y - 1, x, steps, "down")
    if s in ['S', '-', 'L', 'F']:
        rec(y, x + 1, steps, "left")
    if s in ['S', '-', '7', 'J']:
        rec(y, x - 1, steps, "right")
    visited[y][x] = 0
    return

rec(s_y, s_x, 0, "start")

def get_max(grid):
    return max([max(x) for x in grid])

#printm(steps_grid)
print(get_max(steps_grid))
