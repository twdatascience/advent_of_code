# Day 8 Part 1
import re
import itertools
import math

# define functions
def find_nodes(point1, point2, max_row, max_col, antinodes_in):
    row1 = point1[0]
    col1 = point1[1]
    row2 = point2[0]
    col2 = point2[1]

    rise = row2 - row1
    run_x = col2 - col1

    gcd = math.gcd(rise, run_x)

    slope_rise = rise // gcd
    slope_run = run_x // gcd

    antinodes_in.add((row1, col1))
    new_row = row1 + slope_rise
    new_col = col1 + slope_run
    while True:
        if new_row > max_row or new_col > max_col or new_row < 0 or new_col < 0:
            break
        antinodes_in.add((new_row, new_col))
        new_row += slope_rise
        new_col += slope_run

    while True:
        new_row -= slope_rise
        new_col -= slope_run
        if new_row > max_row or new_col > max_col or new_row < 0 or new_col < 0:
            break
        antinodes_in.add((new_row, new_col))
    
    return antinodes_in

grid = open("2024-12-08/input8.txt").read().strip().split('\n')


signals = {}

for r_ind in range(len(grid)):
    characters = list(re.sub(r"\.", '', grid[r_ind]))
    for character in characters:
        c_inds = [index for index, char in enumerate(grid[r_ind]) if char == character]
        coords = []
        for ind in c_inds:
            coords.append((r_ind, ind))
        if character not in signals.keys():
            signals[character] = coords
        else:
            signals[character] = signals[character] + coords

antinodes = set()
num_rows = len(grid) - 1
num_cols = len(grid[0]) - 1


for value in signals.values():
    combinations = list(itertools.combinations(value, 2))
    for combination in combinations:
        
        antinodes = find_nodes(point1=combination[0],
                               point2=combination[1],
                               max_row=num_rows,
                               max_col=num_cols,
                               antinodes_in=antinodes)

print(len(antinodes))
        
    
