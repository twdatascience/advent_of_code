# Day 9 Part 1
import sys
import pdb

sys.setrecursionlimit(10**6)
disk_map = open("2024-12-09/input9.txt").read().strip()



# def get_last(dict_in, prev_ind):
#     get_value = dict_in[prev_ind]
#     del dict_in[prev_ind]
#     if get_value == ".":
#         return get_last(dict_in, prev_ind-1)
#     else:
#         prev_ind -= 1
#         return get_value, prev_ind, dict_in


# dictionary where key is position and value is block id
disk = {}
disk_ind = 0
block_id = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        for j in range(int(disk_map[i])):
            disk[disk_ind] = block_id
            disk_ind += 1
        block_id += 1
    else:
        for j in range(int(disk_map[i])):
            disk[disk_ind] = "."
            disk_ind += 1

# for 

# compact_disk = {}
# prev_ind = len(disk.keys()) -1 
# for i in range(len(disk.keys())):
#     if i > len(disk):
#         break
#     value = disk[i]
#     if value == ".":
#         last_value, prev_ind, dict_in = get_last(disk, prev_ind)
#         compact_disk[i] = last_value
#     else:
#         compact_disk[i] = value

# checksum = 0
# for key, value in compact_disk.items():
#     checksum += key*value

pdb.set_trace()
# print(checksum)