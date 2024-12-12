# Initialize lists to hold the columns
column1 = []
column2 = []

# Open the input file and read its contents
with open('2024-12-01/input.txt', 'r') as file:
    for line in file:
        # Split the line into columns based on whitespace
        parts = line.split()
        if len(parts) >= 2:  # Ensure there are at least two columns
            column1.append(parts[0])  # First column
            column2.append(parts[1])  # Second column


# convert to int and order columns
column1_int = [int(x) for x in column1]
column2_int = [int(x) for x in column2]

# count number of times each element in column1 appears in column2
counts = {}
for x in column1_int:
    x_count = column2_int.count(x)
    if x_count > 0:
        counts[x] = column2_int.count(x)

# calculate similiarity score 
similarity_score = 0

for key, value in counts.items():
    sim_score = key * value
    similarity_score += sim_score

print(similarity_score)
