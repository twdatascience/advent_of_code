# Part 1
# 
# # Initialize a dictionary to store the levels from each report
levels = {}

# Open the input file containing the reports
with open('2024-12-02/input.txt', 'r') as f:
    # Initialize a line index to keep track of report numbers
    line_index = 0  
    # Iterate through each line in the file
    for line in f:
        # Split the line into individual numbers, convert them to integers, and store them in the levels dictionary
        levels[line_index] = [int(x) for x in line.split()]
        # Increment the line index for the next report
        line_index += 1  

# Function to check if a list of numbers is strictly increasing
def is_increasing(lst):
    # Return True if all elements are in increasing order
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

# Function to check if a list of numbers is strictly decreasing
def is_decreasing(lst):
    # Return True if all elements are in decreasing order
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

# Function to check if all adjacent elements in the list differ by at least 1 and at most 3
def all_elements_differ_by_one_to_three(lst):
    # Check the differences between consecutive elements
    for i in range(len(lst) - 1):
        # Calculate the absolute difference between adjacent elements
        difference = abs(lst[i] - lst[i + 1])  
        # If the difference is less than 1 or greater than 3, return False
        if difference < 1 or difference > 3:
            return False
    # All differences are within the acceptable range
    return True  

# Initialize a counter for safe reports
safe_count = 0

# Iterate through each report in the levels dictionary
for key, value in levels.items():
    # Check if the report is either increasing or decreasing
    if is_increasing(value) or is_decreasing(value):
        # Check if all adjacent levels differ by 1 to 3
        if all_elements_differ_by_one_to_three(value):
            # Increment the safe report counter
            safe_count += 1  

# Print the total number of safe reports
print("Part1: ", safe_count)

# Part 2
#
# Add a tracker for unsafe reports
unsafe_ind = []
# reset safe_count
safe_count = 0
# Iterate through each report in the levels dictionary
for key, value in levels.items():
    # Check if the report is either increasing or decreasing
    if is_increasing(value) or is_decreasing(value):
        # Check if all adjacent levels differ by 1 to 3
        if all_elements_differ_by_one_to_three(value):
            # Increment the safe report counter
            safe_count += 1
        else:
            unsafe_ind.append(key)
    else:
        unsafe_ind.append(key)

# brute force
now_safe = 0
now_safe_ind = []

levels_test = levels.copy()

for ind in unsafe_ind:
    print("Testing index ", ind, "out of ", len(unsafe_ind))
    report = levels_test.pop(ind)
    change_safe = False
    while change_safe == False:
        for i in range(len(report)):
            test_report = list(report)
            test_report.pop(i)
            if is_increasing(test_report) or is_decreasing(test_report):
                if all_elements_differ_by_one_to_three(test_report):
                    if ind not in now_safe_ind:
                        now_safe_ind.append(ind)
                        now_safe +=1
                        change_safe = True
        
        change_safe = True

print(now_safe, safe_count, now_safe + safe_count)

    