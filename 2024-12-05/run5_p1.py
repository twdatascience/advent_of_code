# Day 5 Part 1
import pdb

with open("2024-12-05/input5.txt", "r") as f:
    lines = f.readlines()

instructions = []
updates = []
current_set = instructions

for line in lines:
    line = line.strip()
    if line == "":
        current_set = updates
        continue
    current_set.append(line)


dict_insts = {}
for i in range(len(instructions)):
    dict_insts[i] = [int(x) for x in instructions[i].split("|")]


def test_instructs(pages):
    # pages = [int(x) for x in pages.split(",")]
    for value in dict_insts.values():
        if value[0] in pages and value[1] in pages:
            if pages.index(value[0]) < pages.index(value[1]):
                continue
            else:
                # print(f"{pages}\n{value[0]}|{value[1]}") # for testing
                return False
    
    return True

def get_middle(lst):
    length = len(lst)
    middle = length // 2
    return lst[middle]


mid_count = 0

for update in updates:
    update = [int(x) for x in update.split(",")]
    if test_instructs(update):
        mid_count += get_middle(update)

print(mid_count)