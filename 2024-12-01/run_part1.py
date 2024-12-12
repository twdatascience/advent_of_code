# run.py

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

column1_int.sort()
column2_int.sort()

# compare the two lists by element and save diff
diff = [abs(int(x) - int(y)) for x, y in zip(column1_int, column2_int)]

total_sum = sum(diff)

print(total_sum)  # Output the total sum of the differences