# Day 8 Part 1
import re
import itertools
import pdb

# define functions
def find_nodes(point1, point2, max_row, max_col, antinodes_in):
    row1 = point1[0]
    col1 = point1[1]
    row2 = point2[0]
    col2 = point2[1]

    rise = row2 - row1
    run_x = col2 - col1

    test_nodes = []
    for i in range(4):
        if i == 0:
            row = row1 + rise
            col = col1 + run_x
        elif i == 1:
            row = row1 - rise
            col = col1 - run_x
        elif i == 2:
            row = row2 + rise
            col = col2 + run_x
        elif i == 3:
            row = row2 - rise
            col = col2 - run_x
        
        if not (row == row1 and col == col1) and not (row == row2 and col == col2):
            test_nodes.append((row, col))

    for node in test_nodes:
        if not (node[0] > max_row or node[0] < 0 or node[1] > max_col or node[1] < 0):
            antinodes_in.add(node)
    
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
        
    
