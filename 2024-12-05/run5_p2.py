# Day 5 Part 1

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

# track bad updates
mid_count = 0
bad_list = []
for update in updates:
    update = [int(x) for x in update.split(",")]
    if test_instructs(update):
        mid_count += get_middle(update)
    else:
        bad_list.append(update)

# new function to find instructions that flag bad
def fix_bad(pages):
    for value in dict_insts.values():
        if value[0] in pages and value[1] in pages:
            if pages.index(value[0]) < pages.index(value[1]):
                continue
            else:
                hold = pages.pop(pages.index(value[0]))
                pages.insert(pages.index(value[1]), hold)
                # make recursive to fix all bads
                fix_bad(pages)
    return pages
    
bad_sum = 0
for bad in bad_list:
    bad_sum += get_middle(fix_bad(bad))

print(bad_sum)