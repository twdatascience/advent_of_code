# Part 1
import re
import pdb

with open('2024-12-03/input3.txt', 'r') as f:
    content = f.read()

# regex is hard use slicing to get chunks
# matches = re.findall(r"(.*?)don't.*?(do.*?)don't", content)
# (.*?)don't.*?
 


# do_locs = [d.start() for d in re.finditer(r'do\(\)', content, re.IGNORECASE)]
# dont_locs = [d.start() for d in re.finditer(r"don't\(\)", content, re.IGNORECASE)]

# # real_do_locs = [loc for loc in do_locs if loc not in dont_locs]
# real_do_locs = do_locs.copy()
# real_do_locs.insert(0, 0)

# do_chunks = []

# slice_inds = {}
# dict_inds = 0

# for i in range(len(real_do_locs)):
#     hold = real_do_locs[i]
#     greater_elements = [k for k in dont_locs if k > hold]
#     if greater_elements:
#         smallest_greater = min(greater_elements)
#         slice_inds[dict_inds] = [hold, smallest_greater]
#         dict_inds += 1



# for key, value in slice_inds.items():
#     do_chunks.append(content[value[0]:value[1]])

# content_sliced = "".join(do_chunks)

# matches = re.findall(r'mul\([0-9]*,[0-9]*\)', content_sliced)

# mult_results = []

# for match in matches:
#     num_pair = re.findall(r'([0-9]*),([0-9]*)', match)
    
#     for num1, num2 in num_pair:
#         mult_results.append(int(num1) * int(num2))
# pdb.set_trace()
# print(sum(mult_results))


# try something new
do_split = re.split(r"do\(\)", content)

do_list = []

for i in range(len(do_split)):
    do_list.append(re.split(r"don't\(\)", do_split[i])[0])

content_sliced = "".join(do_list)

matches = re.findall(r'mul\([0-9]*,[0-9]*\)', content_sliced)

mult_results = []

for match in matches:
    num_pair = re.findall(r'([0-9]*),([0-9]*)', match)
    
    for num1, num2 in num_pair:
        mult_results.append(int(num1) * int(num2))

print(sum(mult_results))