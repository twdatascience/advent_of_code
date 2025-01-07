# Day 9 Part 2
class disk_obj():
    def __init__(self, id, pos_start, mem_type, size):
        self.id = id
        self.pos_start = pos_start
        self.type = mem_type
        self.size = size

    def val(self):
        if self.type == "free" or self.size == 0:
            return 0

        val = 0
        for i in range(self.size):
            val += self.id * (self.pos_start + i)
        return (val)

disk_map = open("2024-12-09/input9.txt").read().strip()

ind, id, pos, disk = 0, 0, 0, []
for map_val in map(int, disk_map):
    if ind % 2 == 0:
        block_type = "used"
    else:
        block_type = "free"
    
    disk += [disk_obj(id, pos, block_type, map_val)]
    pos += map_val
    
    if ind % 2 == 0:
        id += 1
    ind += 1


for backward in disk[::-2]:
    # make sure loops are advancing
    if backward.id % 100 == 0:
        print(backward.id)
    for forward in disk:
        if forward.pos_start <= backward.pos_start:
            if forward.type == "free" and backward.type == "used" and forward.size >= backward.size:
                backward.pos_start = forward.pos_start
                forward.size = forward.size - backward.size
                forward.pos_start = forward.pos_start + backward.size
                if forward.size == 0:
                    forward.type = "used"

print(sum(m.val() for m in disk))