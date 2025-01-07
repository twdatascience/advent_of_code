import pdb

class disk():
    def __init__(self, id, pos_start, size):
        self.id = id
        self.pos_start = pos_start
        self.size = size

    def val(self):
        val = 0
        for i in range(self.size):
            val += self.id * (self.pos + i)
        return (val)




disk_map = open("2024-12-09/input9.txt").read().strip()

id, pos, mem = 0, 0, []
for map_val in map(int, disk_map):
    mem += [disk(id, pos, map_val)]
    id += 1
    pos += map_val

for used in mem[::-2]:
    pdb.set_trace()
    for free in mem[1::2]:
        if free.id <= used.id:
            free.id = used.id
            free.pos_start += 1
            free.size -= 1


print(sum(m.val() for m in mem[::2]))
