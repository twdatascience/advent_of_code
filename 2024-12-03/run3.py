# Part 1
import re

with open('2024-12-03/input3.txt', 'r') as f:
    content = f.read()

matches = re.findall(r'mul\([0-9]*,[0-9]*\)', content)

mult_results = []
for match in matches:
    num_pair = re.findall(r'([0-9]*),([0-9]*)', match)
    
    for num1, num2 in num_pair:
        mult_results.append(int(num1) * int(num2))

print(sum(mult_results))