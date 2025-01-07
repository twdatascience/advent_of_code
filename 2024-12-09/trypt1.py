import pdb

class disk_obj():
    def __init__(self, id, pos_start, mem_type):
        self.id = id
        self.pos_start = pos_start
        self.type = mem_type

    def val(self):
        if self.type == "free":
            return 0
        val = self.id * self.pos_start
        return (val)

disk_map = open("2024-12-09/input9.txt").read().strip()

ind, id, pos, disk = 0, 0, 0, []
for map_val in map(int, disk_map):
    if ind % 2 == 0:
        block_type = "used"
    else:
        block_type = "free"
    
    for i in range(map_val):
        disk += [disk_obj(id, pos, block_type)]
        pos += 1
    
    if ind % 2 == 0:
        id += 1
    ind += 1


for backward in disk[::-1]:
    # make sure loops are advancing
    if backward.id % 100 == 0:
        print(backward.id)
    for forward in disk:
        if forward.pos_start <= backward.pos_start:
            if forward.type == "free" and backward.type == "used":
                forward.id = backward.id
                forward.type = "used"
                backward.type = "free"

print(sum(m.val() for m in disk))


