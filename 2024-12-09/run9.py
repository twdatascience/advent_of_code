# Day 9 Part 1
import sys
import pdb

sys.setrecursionlimit(10**6)
disk_map = open("2024-12-09/input9.txt").read().strip()

# dictionary where key is position and value is block id
A = []
pos = 0
file_id = 0
SPACE = {}
FINAL = {}
for i in range(len(disk_map)):
    if i % 2 == 0:
        for j in range(int(disk_map[i])):
            A.append(file_id)
            FINAL[pos] = (1, file_id)
            pos += 1
        file_id += 1
    else:
        SPACE[i] = int(disk_map[i])
        for j in range(int(disk_map[i])):
            A.append(None)
            pos += 1

for pos, (sz, file_id) in reversed(FINAL.items()):
    for space_i, (space_pos, space_sz) in enumerate(SPACE.items()):
        if space_pos < pos and sz <= space_sz:
            for i in range(sz):
                pdb.set_trace()
                assert FINAL[pos+i] == file_id, f'{FINAL[pos+i]=}'
# print(checksum)