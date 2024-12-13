levels = {}

with open('2024-12-02/input.txt', 'r') as f:
    line_index = 0
    for line in f:
        levels[line_index] = [int(x) for x in line.split()]
        line_index += 1

def is_increasing(lst):
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def is_decreasing(lst):
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

def all_elements_differ_by_one_to_three(lst):
    # Check the differences between consecutive elements
    for i in range(len(lst) - 1):
        difference = abs(lst[i] - lst[i + 1])
        if difference < 1 or difference > 3:
            return False
    
    return True

safe_count = 0

for key, value in levels.items():
    if is_increasing(value) or is_decreasing(value):
        if all_elements_differ_by_one_to_three(value):
            safe_count += 1


print(safe_count) 
