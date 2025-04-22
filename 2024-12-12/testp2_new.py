import pdb
# set up and define functions
import pandas as pd
from collections import Counter

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_sides = {
    (0, 1): 0,   # right
    (0, -1): 1,  # left
    (1, 0): 2,   # down
    (-1, 0): 3   # up
}

# dict for each cell = id, location
# dict for each id = id, area
# dict for each id = id, sides
#  

def set_ids(dict, row, col, set_id, is_root = True):
    if dict[(row, col)] == None:
        letter = garden.iloc[row, col]

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            if new_row < 0 or new_row > len(garden) - 1 or new_col < 0 or new_col > len(garden[0]) - 1:
                continue
            elif garden.iloc[new_row, new_col] == letter and dict[(new_row, new_col)] != None:
                dict[(row, col)] = dict[(new_row, new_col)]

        if dict[(row, col)] == None:
            dict[(row, col)] = set_id

        for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if new_row < 0 or new_row > len(garden) - 1 or new_col < 0 or new_col > len(garden[0]) - 1:
                    continue
                elif garden.iloc[new_row, new_col] == letter:
                    set_ids(dict, new_row, new_col, set_id, False)
        
        if is_root:
            set_id += 1

    return set_id

def set_sides(dict, row, col):
    letter = garden.iloc[row, col]

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]
        side = dir_sides[direction]

        if new_row < 0 or new_row > len(garden) - 1 or new_col < 0 or new_col > len(garden[0]) - 1:
            hold = dict[(row, col)]
            hold[side] = True
            dict[(row, col)] = hold
        elif garden.iloc[new_row, new_col] != letter:
            hold = dict[(row, col)]
            hold[side] = True
            dict[(row, col)] = hold


# 80
garden1 = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test1.txt", "r").readlines()]])
# 236
# garden2 = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test2.txt", "r").readlines()]])
# 368
# garden3 = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test3.txt", "r").readlines()]])
# 1206
# garden4 = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test.txt", "r").readlines()]])


garden = garden1
plot_ids = {}
for i in range(len(garden)):
    for j in range(len(garden[i])):
        plot_ids[(i, j)] = None

side_dict = {}
for i in range(len(garden)):
    for j in range(len(garden[i])):
        side_dict[(i, j)] = [None, None, None, None]

# side_dict = (row, col) [right side, left side, bottom, top]
# list = is it a side?

new_id = 1 
for i in range(len(garden)):
    for j in range(len(garden[i])):
        set_sides(side_dict, i, j)
        new_id = set_ids(plot_ids, i, j, new_id)

# make dict of ids with corresponding cells
id_areas = {}
for key, value in plot_ids.items():
    if value not in id_areas:
        id_areas[value] = []
    id_areas[value].append(key)



pdb.set_trace()