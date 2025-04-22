# Day 12 part 2
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

# change perimeter to count sides
# change dict values to four piece tuples 
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

# read in data and set up dictionaries 

# 80
garden1 = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test1.txt", "r").readlines()]])
# 236
garden2 = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test2.txt", "r").readlines()]])
# 368
garden3 = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test3.txt", "r").readlines()]])
# 1206
garden4 = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test.txt", "r").readlines()]])


garden = garden1
plot_ids = {}
for i in range(len(garden)):
    for j in range(len(garden[i])):
        plot_ids[(i, j)] = None

side_dict = {}
for i in range(len(garden)):
    for j in range(len(garden[i])):
        side_dict[(i, j)] = [None, None, None, None]

new_id = 1 
for i in range(len(garden)):
    for j in range(len(garden[i])):
        set_sides(side_dict, i, j)
        new_id = set_ids(plot_ids, i, j, new_id)

# get sides for each area



# count area size and sum cell perimeters

def find_side(area):
    hold_dict = {}
    hold_ind = 0
    for cell in area:
        sides = side_dict[cell]
        for ind in range(len(sides)):
            if sides[ind]:
                if (cell, ind) not in hold_dict.values():
                    hold_dict[hold_ind] = set([(cell, ind)])
                    hold_ind += 1 
                else:
                    continue
                if ind == 0 or ind == 1: # 0: right 1: left 2: down 3 up
                    for i in [-1, 1]:
                        new_col = cell[1] + i
                        if new_col < 0 or new_col > len(garden[0]) - 1:
                            continue
                        else:
                            new_cell = (cell[0], new_col)
                if ind == 2 or ind == 3:
                    for i in [-1, 1]:
                        new_row = cell[0] + i
                        if new_row < 0 or new_row > len(garden) - 1:
                            continue
                        else:
                            new_cell = (new_row, cell[1])
                
                if side_dict[new_cell][ind]:
                        if (new_cell, ind) not in hold_dict.values():
                            key = [key for key, value in hold_dict.items() if (cell, ind) in value][0]
                            # pdb.set_trace()
                            hold_dict[key].add((new_cell, ind))
    pdb.set_trace()
    return len(hold_dict)

counts = Counter(plot_ids.values())
combined_dict = {}
for id in range(1, new_id):
    cells = [x for x, y in plot_ids.items() if y == id]
    combined_dict[id] = (len(cells), find_side(cells))

print(combined_dict)

# pdb.set_trace()

# print(sum(cost for cost in combined_dict.values()))

