# Part 2
import re

with open('2024-12-03/input3.txt', 'r') as f:
    content = f.read()

# split into chunks separating at do()
do_split = re.split(r"do\(\)", content)

do_list = []

# take the first section of each do() chunk separating at don't()
# giving all good do chunks
for i in range(len(do_split)):
    do_list.append(re.split(r"don't\(\)", do_split[i])[0])

# join into one string then calculate the same as part 1
content_sliced = "".join(do_list)

matches = re.findall(r'mul\([0-9]*,[0-9]*\)', content_sliced)

mult_results = []

for match in matches:
    num_pair = re.findall(r'([0-9]*),([0-9]*)', match)
    
    for num1, num2 in num_pair:
        mult_results.append(int(num1) * int(num2))

print(sum(mult_results))