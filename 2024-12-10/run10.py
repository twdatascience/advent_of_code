import sys
import pandas as pd

sys.setrecursionlimit(10**6)

with open('2024-12-10/input10.txt', 'r') as f:
    lines = f.readlines()


def check_path(row, col):
    if row >= 0 and row < len(map_df) and col >= 0 and col < len(map_df.columns):
        return True
    else:
        return False
        
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def find_paths(row_value, col_value, seen = set()):
    if map_df.iloc[row_value, col_value] == 9:
        if not (row_value, col_value) in seen:
            seen.add((row_value, col_value))
            return 1
    # print(row_value, col_value)
    hold = 0
    for dir in directions:
        new_row = row_value + dir[0]
        new_col = col_value + dir[1]
        if check_path(new_row, new_col):
            if map_df.iloc[new_row, new_col] - map_df.iloc[row_value, col_value] == 1:
                hold += find_paths(new_row, new_col, seen)
    return hold



map_df = pd.DataFrame([list(line) for line in lines])
map_df = map_df.drop(map_df.columns[len(map_df.columns)-1], axis = 1)
map_df = map_df.astype(int)

total = 0
for row in range(len(map_df)):
    for col in range(len(map_df.columns)):
        if map_df.iloc[row, col] == 0:
            new = find_paths(row, col, set())
            total += new

print(total)