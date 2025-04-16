# Day 4 Part 1
import re
import pandas as pd
import numpy as np

with open("2024-12-04/input4.txt", "r") as f:
    lines = f.readlines()

# create grid data frame of input
df = pd.DataFrame([list(line) for line in lines])
df = df.drop(df.columns[140], axis = 1)

find_values = [r"XMAS", r"SAMX"]

# find all instances in rows
row_count = 0
for ind, row in df.iterrows():
    combined_row = "".join(row)
    for pattern in find_values:
        matches = re.findall(pattern, combined_row)
        row_count += len(matches)

# find all instances in columns
col_count = 0
for column in df.columns:
    combined_column = "".join(df[column])
    for pattern in find_values:
        matches = re.findall(pattern, combined_column)
        col_count += len(matches)

# Function to get all diagonals
def get_all_diagonals(df):
    diagonals = []
    rows, cols = df.shape
    
    # Extract diagonals above and including the main diagonal
    for d in range(cols):
        diag = np.diagonal(df.values, offset=d)
        diagonals.append(diag)
    
    # Extract diagonals below the main diagonal
    for d in range(1, rows):
        diag = np.diagonal(df.values, offset=-d)
        diagonals.append(diag)
    
    # Extract anti-diagonals
    for d in range(-rows + 1, cols):
        anti_diag = np.diagonal(np.fliplr(df.values), offset=d)
        diagonals.append(anti_diag)

    return diagonals


all_diagonals = get_all_diagonals(df)

diag_count = 0
for diag in all_diagonals:
    combined_diag = "".join(diag)
    for pattern in find_values:
        matches = re.findall(pattern, combined_diag)
        diag_count += len(matches)

print(row_count + col_count + diag_count)