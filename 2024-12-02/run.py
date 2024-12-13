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
# Initialize a counter for the number of reports that are now considered safe
now_safe = 0

# Initialize a list to keep track of indices of reports that are now safe
now_safe_ind = []

# Create a copy of the levels list to work with, preserving the original data
levels_test = levels.copy()

# Iterate through each index of the unsafe reports
for ind in unsafe_ind:
    
    # Remove the report at the current index from the copied levels list
    report = levels_test.pop(ind)
    
    # Initialize a flag to track if a change has been made to the report's safety status
    change_safe = False
    
    # Continue checking until a change in safety status is confirmed
    while change_safe == False:
        # Iterate through each element in the report to test removing it
        for i in range(len(report)):
            # Create a copy of the report to test removing the current element
            test_report = list(report)
            # Remove the element at the current index from the test report
            test_report.pop(i)
            
            # Check if the modified report is either increasing or decreasing
            if is_increasing(test_report) or is_decreasing(test_report):
                # Check if all adjacent levels in the modified report differ by 1 to 3
                if all_elements_differ_by_one_to_three(test_report):
                    # If the current index is not already marked as safe
                    if ind not in now_safe_ind:
                        # Mark the index as safe
                        now_safe_ind.append(ind)
                        # Increment the count of safe reports
                        now_safe += 1
                        # Set the change_safe flag to True to exit the loop
                        change_safe = True
        
        # Set change_safe to True to exit the while loop if no changes were made
        change_safe = True

# Print the total number of reports that are now safe, along with the previous safe count
print(now_safe, safe_count, now_safe + safe_count)

    