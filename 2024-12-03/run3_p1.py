# Part 1
import re

with open('2024-12-03/input3.txt', 'r') as f:
    content = f.read()

matches = re.findall(r'mul\([0-9]*,[0-9]*\)', content)

# initialize list to hold results
mult_results = []

# loop through matches to pull out num1 and num2
for match in matches:
    num_pair = re.findall(r'([0-9]*),([0-9]*)', match)
    
    for num1, num2 in num_pair:
        mult_results.append(int(num1) * int(num2))

print(sum(mult_results))