# Day 6 Part 2
# got help from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2024/6.py
import sys

sys.setrecursionlimit(10**6)
infile = "2024-12-06/input6.txt"
p1 = 0
p2 = 0
D = open(infile).read().strip()

grid = D.split('\n')
row = len(grid)
column = len(grid[0])
for row_start in range(row):
    for column_start in range(column):
        if grid[row_start][column_start] == '^':
            sr, sc = row_start, column_start

row_start, column_start = sr, sc
direction = 0  # 0=up, 1=right, 2=down, 3=left
SEEN = set()
SEEN_RC = set()
while True:
    SEEN_RC.add((row_start, column_start))
    dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
    rr = row_start+dr
    cc = column_start+dc

    if not (0 <= rr < row and 0 <= cc < column):
            p1 = len(SEEN_RC)
            break
    if grid[rr][cc] == '#':
        direction = (direction+1) % 4
    else:
        row_start = rr
        column_start = cc


test_locs = list(SEEN_RC)

for i in range(len(test_locs)):
    o_r, o_c = test_locs[i][0], test_locs[i][1]
    row_start, column_start = sr, sc
    direction = 0  # 0=up, 1=right, 2=down, 3=left
    SEEN = set()
    while True:
        if (row_start, column_start, direction) in SEEN:
            p2 += 1
            break
        SEEN.add((row_start, column_start, direction))
        dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
        rr = row_start+dr
        cc = column_start+dc

        if not (0 <= rr < row and 0 <= cc < column):
            break
        if grid[rr][cc] == '#' or rr == o_r and cc == o_c:
            direction = (direction+1) % 4
        else:
            row_start = rr
            column_start = cc
print(p1)
print(p2)
