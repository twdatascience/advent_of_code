# Day 12 part 1

# set up and define functions
import pandas as pd
from collections import Counter

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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

def set_perimeter(dict, row, col):
    letter = garden.iloc[row, col]

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if new_row < 0 or new_row > len(garden) - 1 or new_col < 0 or new_col > len(garden[0]) - 1:
            dict[(row, col)] += 1
        elif garden.iloc[new_row, new_col] != letter:
            dict[(row, col)] += 1

# read in data and set up dictionaries 

garden = pd.DataFrame([list(letter) for letter in [line.strip() for line in open("2024-12-12/test.txt", "r").readlines()]])

plot_ids = {}
for i in range(len(garden)):
    for j in range(len(garden[i])):
        plot_ids[(i, j)] = None

perimeter_dict = {}
for i in range(len(garden)):
    for j in range(len(garden[i])):
        perimeter_dict[(i, j)] = 0

new_id = 1 
for i in range(len(garden)):
    for j in range(len(garden[i])):
        set_perimeter(perimeter_dict, i, j)
        new_id = set_ids(plot_ids, i, j, new_id)

# count area size and sum cell perimeters

counts = Counter(plot_ids.values())
combined_dict = {}
for id in range(1, new_id):
    cells = [x for x, y in plot_ids.items() if y == id]
    perimeter = 0

    for cell in cells:
        perimeter += perimeter_dict[cell]

    combined_dict[id] = (counts[id] * perimeter)

print(sum(cost for cost in combined_dict.values()))


