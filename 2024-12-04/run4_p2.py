# Day 4 Part 2
import re
import pandas as pd
import numpy as np
import pdb

with open("2024-12-04/input4.txt", "r") as f:
    lines = f.readlines()


df = pd.DataFrame([list(line) for line in lines])
df = df.drop(df.columns[140], axis = 1)


# Function to extract 3x3 chunks
def extract_chunks(df):
    chunks = []
    rows, cols = df.shape
    
    # Iterate over the DataFrame in steps of 1
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            # Ensure we don't go out of bounds
            if i + 3 <= rows and j + 3 <= cols:
                chunk = df.iloc[i:i+3, j:j+3]
                chunks.append(chunk)
    
    return chunks


def test_xmas(chunk):
    find_values = {"MAS", "SAM"}
    diag = "".join(np.diagonal(chunk.values))
    anti_diag = "".join(np.diagonal(np.fliplr(chunk.values)))
    if diag in find_values and anti_diag in find_values:
        return True
    
chunks = extract_chunks(df)
xmas_count = 0

for chunk in chunks:
    if test_xmas(chunk):
        xmas_count += 1

print(xmas_count)